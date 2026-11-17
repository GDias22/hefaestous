import { S, commit, novoProjeto, salvarSessao, toast } from '../app.js';
import { api } from '../api.js';
import { openModal } from './modal.js';
import { salvarFem, abrirFem, confirmarPerda } from './arquivo.js';

export function init() {
  const nome = document.getElementById('proj-nome');
  nome.addEventListener('change', () => { S.proj.nome = nome.value.trim() || 'Projeto'; commit('nome'); });
  document.querySelectorAll('#seg-modo button').forEach(b => b.addEventListener('click', () => {
    document.querySelectorAll('#seg-modo button').forEach(x => x.classList.toggle('on', x === b));
    S.modo = b.dataset.v; document.dispatchEvent(new CustomEvent('modo', { detail: S.modo }));
  }));
  document.getElementById('b-novo').addEventListener('click', async () => { if (confirmarPerda()) await novoProjeto(S.proj.tipo, S.proj.nome); });
  document.getElementById('b-salvar').addEventListener('click', () => salvarFem());
  document.getElementById('b-salvar-como').addEventListener('click', () => salvarFem({ comoNovo: true }));
  document.getElementById('b-abrir').addEventListener('click', abrirFem);
  document.getElementById('b-relatorio').addEventListener('click', relatorio);
  document.getElementById('b-export').addEventListener('click', exportar);
}

/** Relatório e exportações xlsx/json são gerados no servidor a partir de uma sessão interna (não é o arquivo do usuário). */
async function garantirSessao() {
  if (!S.session_id || S.sessDirty) await salvarSessao();
  return S.session_id;
}
async function relatorio() {
  const w = window.open('', '_blank');
  if (!w) { toast('Permita pop-ups para abrir o relatório.', true); return; }
  w.document.write('<p style="font-family:sans-serif;padding:2rem">Gerando relatório…</p>');
  try {
    const sid = await garantirSessao();
    const svgs = {};
    const esq = document.querySelector('[data-p="esquema"] svg.draw'); if (esq) svgs.esquema = esq.outerHTML;
    document.querySelectorAll('[data-p="dente"] svg.draw[data-key]').forEach(s => { svgs[s.dataset.key] = s.outerHTML; });
    const r = await fetch(`/api/relatorio/${sid}.html`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ svgs }) });
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    const html = await r.text(); w.document.open(); w.document.write(html); w.document.close();
  } catch (e) { w.close(); toast('Relatório: ' + e.message, true); }
}
async function exportar() {
  try {
    const sid = await garantirSessao();
    const body = document.createElement('div'); body.style.cssText = 'display:flex;gap:8px;flex-wrap:wrap';
    body.innerHTML = `<button class="btn blue" id="exp-fem">Projeto (.fem) — para reabrir e editar</button>
      <a class="btn" href="/api/export/${sid}.json" download>JSON (entradas + resultados)</a>
      <a class="btn" href="/api/export/${sid}.xlsx" download>XLSX (planilha)</a>`;
    body.querySelector('#exp-fem').addEventListener('click', () => salvarFem({ comoNovo: true }));
    openModal('Exportar', body);
  } catch { /* toast já emitido */ }
}
