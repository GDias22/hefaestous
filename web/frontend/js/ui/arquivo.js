// Arquivo de projeto do app: `.fem` (JSON legível). Salvar grava o projeto completo + foto dos resultados; Abrir recarrega
// tudo para continuar editando (inclusive projetos gravados em versões antigas do modelo, que o servidor migra).
// Usa o File System Access API (Chrome/Edge) para "Salvar" regravar no mesmo arquivo; sem ele, baixa o arquivo.
import { S, on, aplicarProjeto, novoProjeto, toast, emit } from '../app.js';
import { api } from '../api.js';
import { openModal, closeModal } from './modal.js';

const EXT = '.fem';
const TIPOS = [{ description: 'Projeto FEM (.fem)', accept: { 'application/json': ['.fem'] } }];
const temFS = () => typeof window.showSaveFilePicker === 'function' && typeof window.showOpenFilePicker === 'function';
const nomeArquivo = () => `${(S.proj.nome || 'projeto').replace(/[\\/:*?"<>|]+/g, '_').trim() || 'projeto'}${EXT}`;
const projetoLimpo = () => { const { busca, buscaT, ...p } = S.proj; return p; };   // 'busca*' é estado temporário

export function init() {
  on(ev => { if (['change', 'result', 'load', 'saved'].includes(ev.type)) rotulos(); });
  // arrastar um .fem para a janela abre o projeto
  window.addEventListener('dragover', (e) => { if ([...(e.dataTransfer?.items || [])].some(i => i.kind === 'file')) e.preventDefault(); });
  window.addEventListener('drop', async (e) => {
    const f = [...(e.dataTransfer?.files || [])].find(x => x.name.toLowerCase().endsWith(EXT)); if (!f) return;
    e.preventDefault(); if (!confirmarPerda()) return; await abrirArquivo(f, null);
  });
  window.addEventListener('beforeunload', (e) => { if (S.dirty) { e.preventDefault(); e.returnValue = ''; } });
}
function rotulos() {
  const b = document.getElementById('b-salvar'); if (b) { b.textContent = S.dirty ? 'Salvar •' : 'Salvar'; b.title = 'Salvar projeto (.fem) — Ctrl+S · Salvar como: Ctrl+Shift+S'; }
  const a = document.getElementById('proj-arquivo'); if (a) a.textContent = S.arquivo ? `${S.arquivo}${S.dirty ? ' •' : ''}` : (S.dirty ? 'não salvo •' : '');
}
export const confirmarPerda = () => !S.dirty || confirm('Há alterações não salvas no projeto atual. Descartá-las?');

// ------------------------------------------------------------------ salvar
async function gravar(handle, texto) { const w = await handle.createWritable(); await w.write(texto); await w.close(); }
function baixar(nome, texto) {
  const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([texto], { type: 'application/json' })); a.download = nome; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
/** Salva o projeto em .fem. `comoNovo`: sempre pergunta onde. Devolve true se gravou. */
export async function salvarFem({ comoNovo = false } = {}) {
  if (!S.proj) return false;
  let arq;
  try { arq = await api.femEmpacotar({ projeto: projetoLimpo() }); }
  catch (e) { toast('Não foi possível salvar: ' + e.message, true, 8000); return false; }
  const texto = JSON.stringify(arq, null, 2);
  try {
    if (temFS()) {
      let h = !comoNovo && S.fileHandle ? S.fileHandle : null;
      if (!h) h = await window.showSaveFilePicker({ suggestedName: nomeArquivo(), types: TIPOS });
      await gravar(h, texto); S.fileHandle = h; S.arquivo = h.name;
    } else { const n = nomeArquivo(); baixar(n, texto); S.arquivo = n; }
  } catch (e) {
    if (e && e.name === 'AbortError') return false;                 // usuário cancelou o diálogo
    toast('Falha ao gravar o arquivo: ' + (e.message || e), true, 8000); return false;
  }
  S.dirty = false; rotulos(); emit({ type: 'saved' }); toast(`Salvo em ${S.arquivo}`);
  return true;
}

// ------------------------------------------------------------------ abrir
async function abrirArquivo(file, handle) {
  let conteudo;
  try { conteudo = JSON.parse(await file.text()); }
  catch { toast(`"${file.name}" não é um arquivo .fem válido (o conteúdo não é JSON).`, true, 8000); return false; }
  try {
    const r = await api.femLer({ conteudo });
    aplicarProjeto(r.projeto, { arquivo: file.name, handle, dentes: true, label: 'abrir .fem' });
    toast(`"${file.name}" aberto${r.migrado ? ' (formato antigo atualizado)' : ''}${r.salvo_em ? ` · salvo em ${String(r.salvo_em).replace('T', ' ')}` : ''}`, false, 6000);
    return true;
  } catch (e) { toast(`Não foi possível abrir "${file.name}": ${e.message}`, true, 9000); return false; }
}
export async function abrirFem() {
  if (!confirmarPerda()) return;
  if (temFS()) {
    try { const [h] = await window.showOpenFilePicker({ types: TIPOS, multiple: false }); await abrirArquivo(await h.getFile(), h); }
    catch (e) { if (!e || e.name !== 'AbortError') toast('Falha ao abrir: ' + (e.message || e), true); }
    return;
  }
  const inp = document.createElement('input'); inp.type = 'file'; inp.accept = EXT + ',application/json';
  inp.addEventListener('change', async () => { if (inp.files[0]) await abrirArquivo(inp.files[0], null); });
  inp.click();
}
export { novoProjeto, closeModal, openModal };
