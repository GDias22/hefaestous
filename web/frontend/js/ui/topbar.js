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
  verificarAtualizacao();
}

/** Padrão Argus: consulta o repositório de produção ao abrir; se há versão maior, mostra a faixa "Nova versão" no topo com
 *  "Atualizar agora" (baixa, troca os arquivos e reabre sozinho) e "Depois" (esconde até a próxima abertura). Offline: silencioso. */
async function verificarAtualizacao() {
  const box = document.getElementById('upd'); if (!box) return;
  let r; try { r = await api.updateCheck(); } catch { return; }
  if (!r || !r.disponivel) return;
  if (sessionStorage.getItem('engr.upd.depois') === r.remota) return;
  box.querySelector('.upd-txt').innerHTML = `Nova versão <b>v${r.remota}</b> disponível (você usa v${r.atual})${r.pode_aplicar ? '' : ` · <a href="${r.pagina}" target="_blank" rel="noopener">baixar</a>`}`;
  const b = document.getElementById('upd-aplicar');
  if (!r.pode_aplicar) b.classList.add('hidden');
  b.addEventListener('click', async () => {
    if (!confirm(`Atualizar o HEFAESTOUS para a v${r.remota}?\n\nProjetos não gravados em .fem serão perdidos. O programa vai fechar e reabrir sozinho em alguns segundos.`)) return;
    b.disabled = true; b.textContent = 'Baixando…';
    try {
      const a = await api.updateApply();
      box.querySelector('.upd-txt').textContent = a.mensagem; b.classList.add('hidden'); document.getElementById('upd-depois').classList.add('hidden');
      document.body.style.pointerEvents = 'none'; document.body.style.opacity = '.6';
    } catch (e) { b.disabled = false; b.textContent = 'Atualizar agora'; toast(e.message, true, 9000); }
  });
  document.getElementById('upd-depois').addEventListener('click', () => { sessionStorage.setItem('engr.upd.depois', r.remota); box.classList.add('hidden'); });
  box.classList.remove('hidden');
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
