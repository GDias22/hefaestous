// Passo 3 — Busca de dentes: busca de números de dentes como etapa do projeto (não é mais um modal).
// Centro: tabela de candidatos + esboço do candidato escolhido + "Usar este candidato".  Inspetor: parâmetros da busca.
// Estado (parâmetros, resultado, linha escolhida, filtros) fica em S.bz e sobrevive a sair/voltar do passo.
import { S, commit, select, toast } from '../app.js';
import { api } from '../api.js';
import { field, block, adv } from './fields.js';
import { fmtNum } from '../results.js';
import { COR } from '../model/rodas.js';
import { fixoDe } from './arquitetura.js';

const NS = 'http://www.w3.org/2000/svg';
const el = (t, a = {}, p = null, txt = null) => { const e = document.createElementNS(NS, t); for (const k in a) if (a[k] != null) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; if (p) p.appendChild(e); return e; };
const SHOW = ['idx', 'Zs', 'Zbp', 'Zsp', 'Zr', 'i_real', 'a_ext', 'sum_x_ext', 'sum_x_int', 'x_sun', 'x_sp', 'eps_alpha_ext', 'eps_alpha_int', 'D_envolvente_planetas', 'D_ext_anelar', 'folga_planetas', 'defasagem'];
const MEMBRO = { sol: 0, 'porta-planetas': 1, anelar: 2 };
const ORDENS = { erro: 'erro de redução', anelar: 'menor anelar', envolvente: 'menor envolvente dos planetas', soma: 'menor soma de dentes' };

let pane = null, pollT = null, host = {};
export function init() { document.addEventListener('open-busca', () => select('dentes')); document.addEventListener('open-busca-trem', () => select('dentes')); }

const isTrem = () => S.proj.tipo === 'trem';
const st = () => (isTrem() ? S.bz.trem : S.bz.pla);
const tolI = () => (S.proj.entrada.tol_i != null ? S.proj.entrada.tol_i : 0.5);
function iAlvo() { const a = S.proj.entrada.i_alvo; if (a) return a; const t = S.res && S.res.transmissao; return t ? Math.round(Math.abs(t.i_total) * 100) / 100 : 10; }

// ---------------------------------------------------------------- parâmetros (derivados do projeto na 1ª vez; editáveis aqui)
function paramsPla() {
  const pl = S.proj.planetario, b = S.bz.pla; b.params = b.params || {};
  const d = { alpha_n_ext: pl.malha_ext.alpha_n ?? 20, alpha_n_int: pl.malha_int.alpha_n ?? 20, m_n_ext: pl.malha_ext.m_n ?? 1, m_n_int: pl.malha_int.m_n ?? 1, beta_ext: pl.malha_ext.beta ?? 0, beta_int: pl.malha_int.beta ?? 0,
    Upright_Diameter: pl.anelar.D_ext ? pl.anelar.D_ext + 2 : 120, Sr_ring: 10, tol_dist_centros: 3, eps_alpha_min: 1.4, sum_x_max: 0.5, d_alpha_wt: 5, max_resultados: 300,
    Z_max_sun: 50, Z_max_big: 100, Z_max_small: 100, Z_max_ring: 150, tol_m_n_ext: 0, tol_m_n_int: 0, tol_beta_ext: 0, tol_beta_int: 0 };
  for (const k in d) if (b.params[k] === undefined) b.params[k] = d[k];
  return b.params;
}
function paramsTrem() {
  const p = S.proj, b = S.bz.trem; b.params = b.params || {};
  const d = { alpha_n: p.estagios[0]?.malha.alpha_n ?? 20, beta: p.estagios[0]?.malha.beta ?? 0, z1_max: 30, z2_max: 150, hunting: true, distribuicao: 'equilibrada', i_max_estagio: 8 };
  for (const k in d) if (b.params[k] === undefined) b.params[k] = d[k];
  return b.params;
}
function lerDoProjeto() { const b = st(); b.params = null; (isTrem() ? paramsTrem : paramsPla)(); toast('Parâmetros lidos do projeto atual.'); renderInspectorAgain(); }

// ---------------------------------------------------------------- inspetor
let inspRoot = null;
function renderInspectorAgain() { if (inspRoot && S.sel.kind === 'dentes') { inspRoot.innerHTML = ''; renderInspector(inspRoot); } }
export function renderInspector(root) {
  inspRoot = root; const p = S.proj, M = (k) => S.meta.params[k];
  const t = S.res && S.res.transmissao;
  const pr = block('Vem do projeto');
  const rows = [];
  if (isTrem()) rows.push(['Arquitetura', `trem · ${p.estagios.length} estágio(s)`]);
  else { const pl = p.planetario; rows.push(['Arquitetura', `planetário ${pl.tipo.toLowerCase()} · ${pl.N_cp} planetas`], ['Entrada → saída', `${pl.entrada} → ${pl.saida} (fixo: ${fixoDe(pl)})`]); }
  rows.push(['Redução alvo', `${fmtNum(iAlvo(), 3)} ± ${fmtNum(tolI(), 2)}`], ['Redução atual', t ? fmtNum(Math.abs(t.i_total), 3) : '—']);
  pr.innerHTML += '<div class="kvs">' + rows.map(([k, v]) => `<span class="k">${k}</span><span class="v">${v}</span><span></span>`).join('') + '</div>';
  const go = document.createElement('div'); go.style.cssText = 'display:flex;gap:6px;margin-top:8px';
  const b1 = document.createElement('button'); b1.className = 'btn xs'; b1.textContent = 'Alterar arquitetura'; b1.addEventListener('click', () => select('arquitetura'));
  const b2 = document.createElement('button'); b2.className = 'btn xs'; b2.textContent = 'Alterar redução (Entrada)'; b2.addEventListener('click', () => select('entrada'));
  const b3 = document.createElement('button'); b3.className = 'btn xs ghost'; b3.textContent = 'Reler do projeto'; b3.title = 'Refaz os parâmetros abaixo a partir dos módulos e ângulos atuais do projeto'; b3.addEventListener('click', lerDoProjeto);
  go.append(b1, b2, b3); pr.appendChild(go); root.appendChild(pr);
  if (isTrem()) {
    const params = paramsTrem(); const b = block('Parâmetros da busca');
    const F = (k, o) => b.appendChild(field(k, Object.assign({ root: params, key: k }, o)));
    const ne = document.createElement('div'); ne.className = 'fld'; ne.dataset.path = 'estagios.length';
    ne.innerHTML = `<label><span class="t">Número de estágios</span></label><div class="ctl" style="gap:8px"><b class="mono" style="flex:1;text-align:right">${p.estagios.length}</b><button class="btn xs">alterar</button></div>`;
    ne.querySelector('button').addEventListener('click', () => select('arquitetura')); ne.title = 'Definido na Arquitetura; a busca distribui a redução entre estes estágios.';
    b.appendChild(ne);
    F('distribuicao', { type: 'choice', choices: ['equilibrada', 'decrescente'], label: 'Distribuição', help: 'Equilibrada: mesma relação em todos os estágios. Decrescente: primeiro estágio (mais rápido, menor torque) com relação maior, como é usual em redutores.' });
    F('alpha_n', { type: 'number', min: 14.5, max: 30, label: 'Ângulo de pressão α_n', unit: '°', help: 'Define o número mínimo de dentes sem undercut (z_min = 2/sin²α).' });
    F('beta', { type: 'number', min: 0, max: 40, label: 'Ângulo de hélice β', unit: '°', help: 'Reduz o z_min pelo número de dentes virtuais.' });
    F('z1_max', { type: 'int', min: 8, max: 80, label: 'z₁ máximo', help: 'Maior número de dentes do pinhão a considerar.' });
    F('z2_max', { type: 'int', min: 20, max: 400, label: 'z₂ máximo', help: 'Maior número de dentes da coroa (limita o diâmetro).' });
    F('hunting', { type: 'bool', label: 'Exigir hunting (z₁, z₂ primos)', help: 'Dentes sem fator comum distribuem o desgaste: cada dente do pinhão encontra todos os da coroa.' });
    root.appendChild(b);
  } else {
    const params = paramsPla();
    const grupos = [['Malhas', ['alpha_n_ext', 'alpha_n_int', 'm_n_ext', 'm_n_int', 'beta_ext', 'beta_int'], true], ['Envelope', ['Upright_Diameter', 'Sr_ring', 'tol_dist_centros'], true], ['Filtros e limites', ['eps_alpha_min', 'sum_x_max', 'd_alpha_wt', 'max_resultados', 'Z_max_sun', 'Z_max_big', 'Z_max_small', 'Z_max_ring'], false], ['Variações (avançado)', ['tol_m_n_ext', 'tol_m_n_int', 'tol_beta_ext', 'tol_beta_int'], false]];
    const comp = p.planetario.tipo === 'Composto';
    for (const [t1, ks, open] of grupos) {
      const fl = ks.filter(k => M(k) && !(!comp && /_int$|small/.test(k) && k !== 'sum_x_max')).map(k => field(k, { root: params, meta: M(k), key: k }));
      root.appendChild(block(null)).appendChild(adv(t1, fl, open));
    }
  }
  const run = document.createElement('button'); run.className = 'btn primary'; run.style.cssText = 'margin:12px 16px'; run.textContent = 'Buscar candidatos'; run.addEventListener('click', buscar); root.appendChild(run);
}

// ---------------------------------------------------------------- execução
async function buscar() {
  const b = st();
  if (b.rodando) return;
  b.res = null; b.sel = null; b.erro = null; b.prog = { p: 0, txt: 'iniciando…' };
  try {
    if (isTrem()) {
      const prm = paramsTrem(); const i = iAlvo(); b.rodando = true; refresh();
      const body = { i_alvo: i, tol_rel: Math.max(0.001, tolI() / i), ...prm, n_estagios: S.proj.estagios.length, max_resultados: 300 };   // nº de estágios vem sempre do projeto
      const r = await api.buscaTrem(body); b.res = r; b.entradas = { ...body }; b.rodando = false; b.sel = r.n ? 0 : null; refresh();
    } else {
      const pl = S.proj.planetario, prm = paramsPla();
      const params = { ...prm, reduction: iAlvo(), tol_reduction: tolI(), Planetary_Type: pl.tipo === 'Composto' ? 1 : 0, torq_Input: MEMBRO[pl.entrada], torq_Output: MEMBRO[pl.saida], N_Cp: pl.N_cp };
      const j = await api.cinJobStart({ params }); b.job = j.job_id; b.rodando = true; b.paramsUsados = params; refresh();
      clearInterval(pollT); pollT = setInterval(tick, 600);
    }
  } catch (e) { b.rodando = false; b.erro = e.message; refresh(); toast(e.message, true); }
}
async function tick() {
  const b = S.bz.pla;
  try {
    const j = await api.cinJob(b.job);
    b.prog = { p: j.progresso, txt: `${j.progresso.toFixed(0)} % · ${j.encontrados} candidatos · ${j.tempo_s} s` };
    if (['concluido', 'cancelado', 'erro'].includes(j.status)) {
      clearInterval(pollT); pollT = null; b.rodando = false;
      if (j.status === 'erro') b.erro = (j.erro || 'erro').split('\n')[0];
      else { b.res = await api.cinJobResult(b.job, 2000); b.sel = null; b.cancelado = j.status === 'cancelado'; selecionarPrimeiro(); }
    }
  } catch (e) { clearInterval(pollT); pollT = null; b.rodando = false; b.erro = e.message; }
  refresh();
}
function refresh() { if (pane && pane.classList.contains('on') && S.sel.kind === 'dentes') renderPane(pane); else if (pane && pane.classList.contains('on')) renderPane(pane); }

// ---------------------------------------------------------------- lista filtrada
function candidatosFiltrados() {
  const b = st(); if (!b.res) return [];
  let l = isTrem() ? b.res.candidatos.slice() : b.res.candidatos.slice();
  if (!isTrem()) {
    const red = (b.paramsUsados || {}).reduction ?? iAlvo(), tol = (b.paramsUsados || {}).tol_reduction ?? tolI(), comp = b.res.tipo === 'Composto';
    if (b.nodef !== false) l = l.filter(c => c.defasagem !== 'SIM');
    if (b.caderno) l = l.filter(c => comp ? (c.i_real >= red && c.i_real <= red + tol / 4) : (c.i_real >= red - tol / 2 && c.i_real <= red + tol / 4));
    const o = b.ordem || 'erro';
    const chave = { erro: c => Math.abs(c.i_real - red), anelar: c => c.D_ext_anelar, envolvente: c => c.D_envolvente_planetas, soma: c => c.Zs + c.Zbp + c.Zsp + Math.abs(c.Zr) }[o];
    l.sort((a, c) => chave(a) - chave(c) || a.idx - c.idx);
  } else {
    const o = b.ordem || 'erro';
    if (o === 'soma') l.sort((a, c) => a.soma_z - c.soma_z || Math.abs(a.erro_rel) - Math.abs(c.erro_rel));
  }
  return l;
}
function selecionarPrimeiro() { const l = candidatosFiltrados(); const b = st(); b.sel = l.length ? l[0].idx : null; }
function candSel() { const b = st(); if (!b.res || b.sel == null) return null; return b.res.candidatos.find(c => c.idx === b.sel) || null; }

// ---------------------------------------------------------------- painel central
export function renderPane(p) {
  pane = p; if (!S.proj) return;
  if (isTrem() && S.bz.trem.res && S.bz.trem.res.candidatos.length && S.bz.trem.res.candidatos[0].estagios.length !== S.proj.estagios.length) { S.bz.trem.res = null; S.bz.trem.sel = null; }   // nº de estágios mudou: resultado velho
  const b = st(); const keepScroll = p.querySelector('.tbl-wrap')?.scrollTop || 0;
  p.innerHTML = '';
  const tb = document.createElement('div'); tb.className = 'toolbar'; p.appendChild(tb);
  const head = document.createElement('b'); head.textContent = isTrem() ? 'Busca de dentes — trem de engrenagens' : `Busca de dentes — planetário ${S.proj.planetario.tipo.toLowerCase()}`; tb.appendChild(head);
  const alvo = document.createElement('span'); alvo.className = 'muted small'; alvo.innerHTML = `redução alvo <b class="mono">${fmtNum(iAlvo(), 3)}</b> ± ${fmtNum(tolI(), 2)}`; tb.appendChild(alvo);
  const run = document.createElement('button'); run.className = 'btn sm primary'; run.textContent = b.rodando ? 'Buscando…' : 'Buscar candidatos'; run.disabled = !!b.rodando; run.addEventListener('click', buscar); tb.appendChild(run);
  if (!isTrem() && b.rodando) { const c = document.createElement('button'); c.className = 'btn sm'; c.textContent = 'Cancelar'; c.addEventListener('click', () => b.job && api.cinJobCancel(b.job).catch(() => {})); tb.appendChild(c); }
  const lista = candidatosFiltrados();
  if (b.res) {
    const lbl = (txt, chk, fn) => { const l = document.createElement('label'); l.innerHTML = `<input type="checkbox" ${chk ? 'checked' : ''}> ${txt}`; l.querySelector('input').addEventListener('change', (e) => { fn(e.target.checked); selecionarPrimeiro(); renderPane(p); }); tb.appendChild(l); };
    if (!isTrem()) {
      lbl('sem defasagem', b.nodef !== false, v => { b.nodef = v; });
      lbl(`faixa do caderno ${S.proj.planetario.tipo === 'Composto' ? '[i, i+tol/4]' : '[i−tol/2, i+tol/4]'}`, !!b.caderno, v => { b.caderno = v; });
    }
    const sel = document.createElement('select'); sel.innerHTML = Object.entries(ORDENS).filter(([k]) => !isTrem() || k === 'erro' || k === 'soma').map(([k, v]) => `<option value="${k}" ${((b.ordem || 'erro') === k) ? 'selected' : ''}>ordenar: ${v}</option>`).join('');
    sel.addEventListener('change', () => { b.ordem = sel.value; selecionarPrimeiro(); renderPane(p); }); tb.appendChild(sel);
    const n = document.createElement('span'); n.className = 'muted small'; n.style.marginLeft = 'auto'; n.textContent = `${lista.length} de ${b.res.n} candidatos${b.res.limite_atingido ? ' (limite atingido)' : ''}`; tb.appendChild(n);
  }
  const body = document.createElement('div'); body.className = 'body dentes-body'; p.appendChild(body);
  if (b.rodando) {
    const e = document.createElement('div'); e.className = 'empty'; e.style.margin = '20px';
    e.innerHTML = `<progress max="100" value="${b.prog ? b.prog.p : 0}" style="width:60%"></progress><div class="p-txt">${b.prog ? b.prog.txt : 'iniciando…'}</div>`; body.appendChild(e); return;
  }
  if (b.erro) { body.innerHTML = `<div class="alert erro" style="margin:16px"><span class="ic">✕</span><span>${b.erro}</span></div>`; return; }
  if (!b.res) { body.innerHTML = `<div class="empty" style="margin:20px"><b>3 · Dentes</b><br>Defina a arquitetura e a redução alvo, ajuste os parâmetros na direita e clique em "Buscar candidatos".<br><span class="small">${isTrem() ? 'A busca distribui a redução entre os estágios (z mínimo sem undercut, hunting).' : 'A busca varre sol, planetas e anelar: montagem com N planetas, hunting, folga entre planetas, interferência e recobrimento — as mesmas verificações do Dim_cinematico.'}</span></div>`; return; }
  if (!b.res.n) { body.innerHTML = '<div class="empty" style="margin:20px">Nenhuma combinação dentro da tolerância. Afrouxe a tolerância (Entrada), o envelope ou os limites de z.</div>'; return; }
  if (!lista.length) { body.innerHTML = '<div class="empty" style="margin:20px">Nenhum candidato passa nos filtros marcados. Desmarque "faixa do caderno" ou "sem defasagem" para ver todos.</div>'; return; }
  const left = document.createElement('div'); left.className = 'tbl-wrap'; body.appendChild(left);
  const right = document.createElement('div'); right.className = 'prev'; body.appendChild(right);
  host = { left, right };
  desenharTabela(left, lista); left.scrollTop = keepScroll; desenharPreview(right);
}
function desenharTabela(wrap, lista) {
  const b = st(); const t = document.createElement('table'); t.className = 'res sel-rows';
  let cols;
  if (isTrem()) {
    const ne = b.res.candidatos[0].estagios.length;
    t.innerHTML = `<thead><tr><th>#</th>${Array.from({ length: ne }, (_, k) => `<th>Estágio ${k + 1} (z₁/z₂ · i)</th>`).join('')}<th>i total</th><th>erro</th><th>Σz</th></tr></thead>`;
  } else {
    const labels = Object.fromEntries(b.res.colunas); cols = SHOW;
    t.innerHTML = `<thead><tr>${cols.map(k => `<th>${labels[k] || k}</th>`).join('')}</tr></thead>`;
  }
  const tb = document.createElement('tbody');
  lista.slice(0, 300).forEach(c => {
    const tr = document.createElement('tr'); tr.dataset.idx = c.idx; if (c.idx === b.sel) tr.className = 'on';
    tr.innerHTML = isTrem() ? `<td class="num">${c.idx}</td>${c.estagios.map(e => `<td class="num">${e.z1}/${e.z2} · ${e.i.toFixed(3)}</td>`).join('')}<td class="num">${c.i_total.toFixed(4)}</td><td class="num">${(c.erro_rel * 100).toFixed(2)} %</td><td class="num">${c.soma_z}</td>`
      : cols.map(k => `<td class="num">${typeof c[k] === 'number' ? fmtNum(c[k], 3) : c[k]}</td>`).join('');
    tr.addEventListener('click', () => { b.sel = c.idx; tb.querySelectorAll('tr').forEach(x => x.classList.toggle('on', +x.dataset.idx === c.idx)); desenharPreview(host.right); });
    tr.addEventListener('dblclick', () => usar(c));
    tb.appendChild(tr);
  });
  t.appendChild(tb); wrap.appendChild(t);
}

// ---------------------------------------------------------------- esboço do candidato (porta da célula 26 do Dim_cinematico)
function desenharPreview(box) {
  box.innerHTML = ''; const c = candSel(); if (!c) { box.innerHTML = '<div class="empty" style="margin:16px">Selecione um candidato na tabela para ver o esboço.</div>'; return; }
  const head = document.createElement('div'); head.className = 'prev-h';
  head.innerHTML = isTrem() ? `<b>Candidato #${c.idx}</b><span class="muted small">i = ${c.i_total.toFixed(4)} · erro ${(c.erro_rel * 100).toFixed(2)} %</span>`
    : `<b>Candidato #${c.idx}</b><span class="muted small">z ${c.Zs}/${c.Zbp}${S.proj.planetario.tipo === 'Composto' ? '/' + c.Zsp : ''}/${Math.abs(c.Zr)} · i = ${c.i_real.toFixed(4)}</span>`;
  box.appendChild(head);
  const svg = el('svg', { class: 'prev-svg' }); box.appendChild(svg);
  if (isTrem()) previewTrem(svg, c); else previewPla(svg, c);
  const info = document.createElement('div'); info.className = 'kvs prev-kv';
  const rows = isTrem() ? c.estagios.map((e, k) => [`Estágio ${k + 1}`, `${e.z1}/${e.z2} · i ${e.i.toFixed(3)}`]) : [
    ['Redução real', fmtNum(c.i_real, 4)], ['a externa / interna', `${fmtNum(c.a_ext, 3)} / ${fmtNum(Math.abs(c.a_int), 3)} mm`], ['Σx ext / int', `${fmtNum(c.sum_x_ext, 3)} / ${fmtNum(c.sum_x_int, 3)}`],
    ['ε_α ext / int', `${fmtNum(c.eps_alpha_ext, 3)} / ${fmtNum(c.eps_alpha_int, 3)}`], ['Ø envolvente dos planetas', `${fmtNum(c.D_envolvente_planetas, 2)} mm`], ['Ø externo da anelar', `${fmtNum(c.D_ext_anelar, 2)} mm`], ['Folga entre planetas', `${fmtNum(c.folga_planetas, 3)} mm`], ['Defasagem', c.defasagem]];
  info.innerHTML = rows.map(([k, v]) => `<span class="k">${k}</span><span class="v">${v}</span><span></span>`).join(''); box.appendChild(info);
  const bt = document.createElement('button'); bt.className = 'btn primary'; bt.textContent = 'Usar este candidato'; bt.addEventListener('click', () => usar(c)); bt.style.margin = '8px 0 12px'; box.appendChild(bt);
}
function previewPla(svg, c) {
  const pl = S.proj.planetario, N = pl.N_cp, comp = pl.tipo === 'Composto'; const A = Math.abs;
  const up = (S.bz.pla.paramsUsados || {}).Upright_Diameter || (pl.anelar.D_ext ? pl.anelar.D_ext + 2 : 120);
  const R = Math.max(up, c.D_ext_anelar) / 2 * 1.06; svg.setAttribute('viewBox', `${-R} ${-R} ${2 * R} ${2 * R}`);
  const circ = (r, o = {}, cx = 0, cy = 0, g = svg, tip = null) => { const e = el('circle', { cx, cy, r, fill: 'none', ...o }, g); if (tip) el('title', {}, e, tip); return e; };
  circ(up / 2, { stroke: '#4b5560', 'stroke-width': .6, 'stroke-dasharray': '1 3' }, 0, 0, svg, `Caixa (Ø interno máx. da manga) ${fmtNum(up, 1)} mm`);
  const gr = el('g', {}, svg);
  circ(c.D_ext_anelar / 2, { stroke: COR.anelar, 'stroke-width': .8, 'stroke-dasharray': '5 2 1 2' }, 0, 0, gr, `Anelar — Ø externo ${fmtNum(c.D_ext_anelar, 2)} mm`);
  circ(A(c.df_r) / 2, { stroke: COR.anelar, 'stroke-width': 1 }, 0, 0, gr); circ(A(c.da_r) / 2, { stroke: COR.anelar, 'stroke-width': .6, 'stroke-dasharray': '3 2' }, 0, 0, gr); circ(A(c.dw_r) / 2, { stroke: COR.anelar, 'stroke-width': .6, opacity: .6, 'stroke-dasharray': '6 4' }, 0, 0, gr, `Anelar — d_w ${fmtNum(A(c.dw_r), 2)} mm`);
  const gs = el('g', {}, svg); circ(c.da_sun / 2, { stroke: COR.sol, 'stroke-width': 1, fill: '#fbecec' }, 0, 0, gs, `Sol — d_a ${fmtNum(c.da_sun, 2)} mm`); circ(c.dw_sun / 2, { stroke: COR.sol, 'stroke-width': .6, 'stroke-dasharray': '6 4' }, 0, 0, gs);
  const rc = A(c.a_ext);
  for (let k = 0; k < N; k++) {
    const an = -Math.PI / 2 + k * 2 * Math.PI / N, x = rc * Math.cos(an), y = rc * Math.sin(an); const g = el('g', {}, svg);
    circ(c.da_bp / 2, { stroke: COR.planeta_maior, 'stroke-width': 1, fill: '#e8eef8', 'fill-opacity': .85 }, x, y, g, `Planeta ${comp ? 'maior ' : ''}— d_a ${fmtNum(c.da_bp, 2)} mm`);
    circ(c.dw_bp / 2, { stroke: COR.planeta_maior, 'stroke-width': .6, 'stroke-dasharray': '6 4' }, x, y, g);
    if (comp) { circ(c.da_sp / 2, { stroke: COR.planeta_menor, 'stroke-width': 1, 'stroke-dasharray': '4 2', fill: '#dff3f7', 'fill-opacity': .9 }, x, y, g, `Planeta menor — d_a ${fmtNum(c.da_sp, 2)} mm`); }
    circ(.8, { stroke: '#4b5560' }, x, y, g);
  }
  circ(rc, { stroke: '#95999e', 'stroke-width': .5, 'stroke-dasharray': '2 3' });
  // rótulos
  const fs = R / 20; const tx = (x, y, t, col) => el('text', { x, y, 'font-size': fs, fill: col, 'text-anchor': 'middle', 'font-family': 'Inter Tight, Inter, sans-serif', 'font-weight': 600 }, svg, t);
  tx(0, fs * .35, `S z${c.Zs}`, COR.sol); tx(0, -rc, `${comp ? 'PM' : 'P'} z${c.Zbp}`, COR.planeta_maior); if (comp) tx(0, -rc + fs * 1.15, `Pm z${c.Zsp}`, COR.planeta_menor);
  tx(0, -(A(c.df_r) / 2 + fs * .4), `Anelar z${A(c.Zr)}`, COR.anelar);
}
function previewTrem(svg, c) {
  const p = S.proj, prm = S.bz.trem.params || {}; const beta = prm.beta || 0;
  const dref = (k, z) => { const mn = (p.estagios[k] && p.estagios[k].malha.m_n) || 2; return mn * z / Math.cos(beta * Math.PI / 180); };
  let cx = 0, cy = 0, ang = 0; const els = []; let minx = 1e9, maxx = -1e9, miny = 1e9, maxy = -1e9;
  const ext = (x, y, r) => { minx = Math.min(minx, x - r); maxx = Math.max(maxx, x + r); miny = Math.min(miny, y - r); maxy = Math.max(maxy, y + r); };
  c.estagios.forEach((e, k) => {
    const d1 = dref(k, e.z1), d2 = dref(k, e.z2), a = (d1 + d2) / 2; const x2 = cx + a * Math.cos(ang), y2 = cy + a * Math.sin(ang);
    els.push({ x: cx, y: cy, r: d1 / 2, cor: k === 0 ? COR.pinhao : COR.coroa, dash: k > 0, t: `P${k + 1} z${e.z1}` }); els.push({ x: x2, y: y2, r: d2 / 2, cor: COR.coroa, t: `C${k + 1} z${e.z2}` });
    ext(cx, cy, d1 / 2); ext(x2, y2, d2 / 2); cx = x2; cy = y2; ang = k % 2 === 0 ? Math.PI / 4 : -Math.PI / 4;
  });
  const pad = 6, W = maxx - minx + 2 * pad, H = maxy - miny + 2 * pad; svg.setAttribute('viewBox', `${minx - pad} ${miny - pad} ${W} ${H}`);
  const fs = Math.max(W, H) / 24;
  els.forEach(o => { const g = el('g', {}, svg); el('circle', { cx: o.x, cy: o.y, r: o.r, fill: o.cor + '14', stroke: o.cor, 'stroke-width': Math.max(W, H) / 400, 'stroke-dasharray': o.dash ? '4 2' : null }, g); el('text', { x: o.x, y: o.y + fs * .35, 'font-size': fs, 'text-anchor': 'middle', fill: o.cor, 'font-weight': 600, 'font-family': 'Inter Tight, Inter, sans-serif' }, g, o.t); });
}

// ---------------------------------------------------------------- aplicar ao projeto
function usar(c) {
  const b = st();
  if (isTrem()) {
    const p = S.proj, n = c.estagios.length, prm = b.params || {};
    while (p.estagios.length < n) { const last = p.estagios[p.estagios.length - 1]; p.estagios.push(JSON.parse(JSON.stringify(last))); }
    p.estagios.length = n;
    c.estagios.forEach((e, k) => { const est = p.estagios[k]; est.nome = est.nome && !/^Estágio \d+$/.test(est.nome) ? est.nome : `Estágio ${k + 1}`; est.malha = { ...est.malha, Z_pinhao: e.z1, Z_coroa: Math.sign(est.malha.Z_coroa || 1) * e.z2, a: null, alpha_n: prm.alpha_n ?? est.malha.alpha_n, beta: prm.beta ?? est.malha.beta }; });
    S.flags.dentes = true; commit('busca de dentes (trem)'); select('estagio', 0, 'pinhao'); toast(`Trem de ${n} estágios aplicado: i = ${c.i_total.toFixed(3)}`);
  } else {
    const pl = S.proj.planetario, res = b.res, comp = pl.tipo === 'Composto';
    pl.sol.z = c.Zs; pl.planeta_maior.z = c.Zbp; if (comp) pl.planeta_menor.z = c.Zsp; pl.anelar.z = Math.abs(c.Zr);
    pl.malha_ext = { ...pl.malha_ext, m_n: c.m_n_ext, beta: c.beta_ext, a: c.a_ext, x_pinhao: c.x_sun, alpha_n: res.entradas.alpha_n_ext, tipo: 'Otimização' };
    pl.malha_int = { ...pl.malha_int, m_n: c.m_n_int, beta: c.beta_int, a: -Math.abs(c.a_int), x_pinhao: c.x_sp, alpha_n: comp ? res.entradas.alpha_n_int : res.entradas.alpha_n_ext, tipo: 'Otimização' };
    pl.anelar.D_ext = Math.round(c.D_ext_anelar * 100) / 100;
    S.flags.dentes = true; commit('busca de dentes'); select('sol'); toast(`Candidato z = ${c.Zs}/${c.Zbp}/${c.Zsp}/${Math.abs(c.Zr)} aplicado ao projeto`);
  }
}
