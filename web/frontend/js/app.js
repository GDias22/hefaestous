// Estado do projeto, cálculo ao vivo (debounce), autosave, undo/redo, roteamento entre módulos de UI
import { api } from './api.js';
import * as Tree from './ui/sidebar.js';
import * as Inspector from './ui/inspector.js';
import * as Canvas from './ui/canvas.js';
import * as Results from './ui/results.js';
import * as Explain from './ui/explain.js';
import * as Guide from './ui/guide.js';
import * as Topbar from './ui/topbar.js';
import * as Busca from './ui/busca.js';
import * as Arq from './ui/arquitetura.js';
import * as Layout from './ui/layout.js';
import * as Arquivo from './ui/arquivo.js';
import { isWheelKind, ensurePlanetas } from './model/rodas.js';

export const S = {
  proj: null,            // objeto do projeto (JSON)
  res: null,             // último resultado de /api/projeto/calcular
  sel: { kind: 'arquitetura', idx: 0, roda: null },   // passo/roda selecionado: arquitetura | entrada | dentes | layout | estagio(+roda) | sol | planeta_maior | planeta_menor | anelar | carrier | operacao | analise | saida
  wheel: null,           // última roda selecionada (as abas de perfil/3D seguem esta, mesmo quando o passo atual não é uma roda)
  flags: { dentes: false },
  stash: null,           // composto guardado ao alternar para Simples
  bz: { pla: {}, trem: {} },   // estado da busca de dentes (resultados, linha escolhida, filtros) — fica em memória
  session_id: null,
  meta: null, presets: null, vocab: null,
  modo: 'livre',
  dirty: false,          // alterações ainda não gravadas no arquivo .fem
  sessDirty: true,       // alterações ainda não enviadas à sessão interna (usada só por relatório/exportações)
  arquivo: null,         // nome do .fem aberto/salvo
  fileHandle: null,      // handle do File System Access API (regravar no mesmo arquivo)
  busy: false,
};
const listeners = new Set();
export function on(fn) { listeners.add(fn); return () => listeners.delete(fn); }
export function emit(ev) { for (const fn of listeners) fn(ev); }

// ---------- utilidades de caminho ("estagios[0].malha.m_n") ----------
export function getPath(obj, path) {
  return path.split(/\.|\[|\]/).filter(Boolean).reduce((o, k) => (o == null ? undefined : o[k]), obj);
}
export function setPath(obj, path, value) {
  const parts = path.split(/\.|\[|\]/).filter(Boolean);
  let o = obj;
  for (let i = 0; i < parts.length - 1; i++) {
    const k = parts[i];
    if (o[k] == null || typeof o[k] !== 'object') o[k] = /^\d+$/.test(parts[i + 1]) ? [] : {};
    o = o[k];
  }
  o[parts[parts.length - 1]] = value;
}

// ---------- undo/redo ----------
const hist = { past: [], future: [] };
function snapshot() { return JSON.stringify(S.proj); }
export function commit(label) {
  hist.past.push(snapshot()); if (hist.past.length > 60) hist.past.shift(); hist.future = [];
  S.dirty = true; S.sessDirty = true; schedule(); emit({ type: 'change', label });
}
export function undo() { if (!hist.past.length) return; hist.future.push(snapshot()); S.proj = JSON.parse(hist.past.pop()); afterLoad('undo'); }
export function redo() { if (!hist.future.length) return; hist.past.push(snapshot()); S.proj = JSON.parse(hist.future.pop()); afterLoad('redo'); }

// ---------- cálculo ao vivo ----------
let timer = null, inflight = null, pending = false;
export function schedule(ms = 160) { clearTimeout(timer); timer = setTimeout(calc, ms); }
export async function calc() {
  if (inflight) { pending = true; return; }
  setStatus('busy', 'calculando…');
  const { busca, buscaT, ...projeto } = S.proj;   // 'busca*' é estado temporário dos modais, não faz parte do projeto
  const body = { projeto, com_tensoes: true };
  inflight = api.projetoCalcular(body);
  try {
    const r = await inflight;
    S.res = r;
    setStatus(r.ok ? 'ok' : 'err', r.ok ? 'atualizado' : `${Object.keys(r.erros).length} problema(s) nas entradas`);
    emit({ type: 'result' });
    localStorage.setItem('engr.projeto', JSON.stringify(S.proj));
  } catch (e) {
    setStatus('err', 'erro no servidor'); toast(e.message, true);
  } finally {
    inflight = null;
    if (pending) { pending = false; calc(); }
  }
}
export function setStatus(kind, txt) {
  const el = document.getElementById('status'); el.className = 'status ' + (kind === 'busy' ? 'busy' : kind === 'err' ? 'err' : '');
  el.querySelector('.txt').textContent = txt;
}
export function toast(msg, err = false, ms = 3500) {
  const t = document.getElementById('toast'); t.textContent = msg; t.className = 'toast show' + (err ? ' err' : '');
  clearTimeout(t._tm); t._tm = setTimeout(() => t.classList.remove('show'), ms);
}

// ---------- seleção ----------
export function select(kind, idx = 0, roda = null, src = null) {
  S.sel = { kind, idx, roda };
  if (isWheelKind(kind)) S.wheel = { kind, idx, roda };
  emit({ type: 'select', src });
}

// ---------- projeto ----------
const clone = (o) => JSON.parse(JSON.stringify(o));
/** Formato antigo (um `planeta` com z_ext/z_int e overrides ext/int) -> planeta_maior + planeta_menor. */
export function migrarProjeto(p) {
  const pl = p && p.planetario; if (!pl) return p;
  if (pl.planeta) {
    const pla = clone(pl.planeta); const ext = pla.ext || {}, inte = pla.int || {}; const ze = pla.z_ext, zi = pla.z_int;
    delete pla.ext; delete pla.int; delete pla.z_ext; delete pla.z_int;
    if (!pl.planeta_maior) pl.planeta_maior = { ...clone(pla), ...clone(ext), z: ze };
    if (!pl.planeta_menor) pl.planeta_menor = { ...clone(pla), ...clone(inte), z: zi != null ? zi : ze };
    delete pl.planeta;
  }
  ensurePlanetas(pl);
  if (!pl.modo) pl.modo = 'fixo';
  if (pl.n_livre == null) pl.n_livre = 0.0;
  return p;
}
/** Troca o projeto inteiro (novo, aberto de .fem ou da sessão): zera histórico, seleção e estado temporário. */
export function aplicarProjeto(proj, { arquivo = null, handle = null, dentes = true, label = 'abrir' } = {}) {
  S.proj = migrarProjeto(proj); S.session_id = null; S.arquivo = arquivo; S.fileHandle = handle; S.dirty = false; S.sessDirty = true; hist.past = []; hist.future = [];
  S.flags = { dentes }; S.stash = null; S.bz = { pla: {}, trem: {} }; S.wheel = null; S.sel = { kind: 'arquitetura', idx: 0, roda: null };
  afterLoad(label);
}
export async function novoProjeto(tipo, nome = null) {
  S.proj = migrarProjeto(await api.projetoPadrao(tipo)); if (nome) S.proj.nome = nome; S.session_id = null; S.arquivo = null; S.fileHandle = null; S.dirty = false; S.sessDirty = true; hist.past = []; hist.future = [];
  S.flags = { dentes: false }; S.stash = null; S.bz = { pla: {}, trem: {} }; S.wheel = null; S.sel = { kind: 'arquitetura', idx: 0, roda: null };
  afterLoad('novo');
}
export function afterLoad(label) {
  document.getElementById('proj-nome').value = S.proj.nome || '';
  emit({ type: 'load', label }); schedule(0);
}
/** Sessão interna no servidor (necessária ao relatório e às exportações xlsx/json). Não é o arquivo do usuário: ver ui/arquivo.js. */
export async function salvarSessao() {
  try {
    const { busca, buscaT, ...projeto } = S.proj;
    const r = await api.projetoSalvar({ projeto, session_id: S.session_id });
    S.session_id = r.session_id; S.sessDirty = false;
    return r.session_id;
  } catch (e) { toast('Sessão: ' + e.message, true); throw e; }
}
export async function carregar(id) {
  const r = await api.projetoCarregar(id); aplicarProjeto(r.projeto, { label: 'carregar' }); S.session_id = id; S.sessDirty = false;
  toast(`Projeto "${r.titulo}" carregado (sessão do servidor)`);
}

// ---------- batimento: o servidor iniciado pelo HEFAESTOUS.exe se encerra quando a última aba fecha ----------
function iniciarBatimento() {
  const bate = () => { api.vidaPing().catch(() => {}); };
  bate(); setInterval(bate, 5000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) bate(); });
  window.addEventListener('pagehide', () => {
    try { navigator.sendBeacon('/api/vida/adeus'); } catch { /* ignore */ }
  });
}

// ---------- boot ----------
async function boot() {
  iniciarBatimento();
  try {
    const [meta, presets, vocab] = await Promise.all([api.meta(), api.presets(), api.projetoVocabulario()]);
    S.meta = meta; S.presets = presets; S.vocab = vocab;
  } catch (e) { toast('Falha ao carregar metadados: ' + e.message, true, 10000); return; }
  Topbar.init(); Tree.init(); Arq.init(); Layout.init(); Arquivo.init(); Inspector.init(); Canvas.init(); Results.init(); Explain.init(); Guide.init(); Busca.init();
  const saved = localStorage.getItem('engr.projeto');
  const hash = location.hash.replace('#', '');
  if (hash.startsWith('p=')) { try { await carregar(hash.slice(2)); return; } catch { /* cai no padrão */ } }
  if (saved) { try { S.proj = migrarProjeto(JSON.parse(saved)); S.flags = { dentes: true }; S.sel = { kind: 'arquitetura', idx: 0, roda: null }; afterLoad('local'); return; } catch { /* ignore */ } }
  await novoProjeto('trem');
  Guide.maybeTour();
}
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') { e.preventDefault(); Arquivo.salvarFem({ comoNovo: e.shiftKey }); }
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z' && !e.shiftKey && !/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); undo(); }
  if ((e.ctrlKey || e.metaKey) && (e.key.toLowerCase() === 'y' || (e.key.toLowerCase() === 'z' && e.shiftKey)) && !/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); redo(); }
});
boot();
