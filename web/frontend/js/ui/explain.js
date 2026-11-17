// Painel "Explicar": fórmula do fator com valores substituídos, texto didático (markdown + KaTeX) e sensibilidade
import { S } from '../app.js';
import { api } from '../api.js';
import { fmtNum } from '../results.js';
import { sensChart } from '../draw/charts.js';

let drawer, docsIndex = null;
export function init() {
  drawer = document.getElementById('drawer');
  document.addEventListener('explain', (e) => open(e.detail));
  document.addEventListener('show-doc', (e) => showDoc(e.detail));
  document.addEventListener('render-aprender', renderAprender);
}
function katexRender(el) { if (window.renderMathInElement) window.renderMathInElement(el, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }, { left: '\\(', right: '\\)', display: false }], throwOnError: false }); }
function md(txt) { const html = window.marked ? window.marked.parse(txt || '') : (txt || ''); return html.replace(/src="Figuras\//g, 'src="/api/figuras/'); }

async function open({ fator, roda, malha }) {
  drawer.classList.add('show');
  drawer.innerHTML = `<div class="dhead"><h2>Explicação</h2><button class="btn sm" id="d-close">Fechar</button></div><div class="dbody"><div class="empty">Carregando…</div></div>`;
  drawer.querySelector('#d-close').addEventListener('click', () => drawer.classList.remove('show'));
  try {
    const ex = await api.explicar({ projeto: S.proj, malha, fator, roda });
    const body = drawer.querySelector('.dbody'); body.innerHTML = '';
    drawer.querySelector('h2').textContent = ex.titulo || fator;
    const left = document.createElement('div');
    if (ex.resumo) left.innerHTML += `<p class="doc">${ex.resumo}</p>`;
    if (ex.formula) left.innerHTML += `<div class="formula">$$${ex.formula}$$</div>`;
    if (ex.variaveis && ex.variaveis.length) {
      const v = document.createElement('div'); v.className = 'vars';
      ex.variaveis.forEach(x => { v.innerHTML += `<span class="sym">$${x.simbolo}$</span><span class="d">${x.nome}</span><span class="v">${typeof x.valor === 'number' ? fmtNum(x.valor, 4) : x.valor}${x.unidade ? ' ' + x.unidade : ''}</span>`; });
      left.appendChild(v);
    }
    if (ex.resultado) left.innerHTML += `<div class="formula"><b>${ex.resultado}</b></div>`;
    if (ex.notas && ex.notas.length) left.innerHTML += '<ul class="doc small">' + ex.notas.map(n => `<li>${n}</li>`).join('') + '</ul>';
    // sensibilidade
    if (ex.sensibilidade && ex.sensibilidade.length) {
      const sbox = document.createElement('div'); sbox.className = 'sens';
      sbox.innerHTML = `<div class="ctl"><b>Sensibilidade</b> variar <select class="s-par">${ex.sensibilidade.map(p => `<option value="${p.key}">${p.label}</option>`).join('')}</select> · ver <select class="s-y"><option value="fator">${ex.titulo_curto || fator}</option><option value="S_H">S_H</option><option value="S_F">S_F</option></select><span class="muted small s-msg"></span></div><svg></svg>`;
      left.appendChild(sbox);
      const run = async () => {
        const par = sbox.querySelector('.s-par').value, y = sbox.querySelector('.s-y').value;
        sbox.querySelector('.s-msg').textContent = 'calculando…';
        try { const r = await api.sensibilidade({ projeto: S.proj, malha, parametro: par, fator, roda }); sensChart(sbox.querySelector('svg'), r, y); sbox.querySelector('.s-msg').textContent = r.nota || ''; }
        catch (e) { sbox.querySelector('.s-msg').textContent = e.message; }
      };
      sbox.querySelector('.s-par').addEventListener('change', run); sbox.querySelector('.s-y').addEventListener('change', run); run();
    }
    body.appendChild(left);
    const right = document.createElement('div'); right.className = 'doc';
    right.innerHTML = ex.doc ? md(ex.doc) : '<div class="empty">Sem texto didático para este item.</div>';
    body.appendChild(right);
    katexRender(body);
  } catch (e) { drawer.querySelector('.dbody').innerHTML = `<div class="alert erro"><span class="ic">✕</span><span>${e.message}</span></div>`; }
}
let aprenderPronto = null;
async function showDoc(chave) {
  const p = document.querySelector('[data-p="aprender"]');
  await renderAprender();
  await aprenderPronto;                                   // o índice pode ainda estar carregando (renderAprender roda também na troca de aba)
  const a = p.querySelector(`[data-doc="${chave}"]`);
  if (!a) { document.dispatchEvent(new CustomEvent('toast-msg', { detail: `Tema "${chave}" não encontrado no Aprender.` })); return; }
  a.click(); a.scrollIntoView({ block: 'center' });
}
async function renderAprender() {
  const p = document.querySelector('[data-p="aprender"]');
  if (p.dataset.ready) return aprenderPronto; p.dataset.ready = '1';
  let fim; aprenderPronto = new Promise(r => { fim = r; });
  p.innerHTML = '<div class="toolbar"><b>Aprender</b><span class="muted small">textos do caderno de dimensionamento (Mazzo, DIN, ISO 6336)</span><div class="search" style="margin-left:auto;width:240px"><span class="muted">⌕</span><input placeholder="buscar tema…"></div></div><div class="body" style="display:grid;grid-template-columns:260px 1fr"><div class="idx" style="border-right:1px solid var(--line);overflow:auto"></div><div class="doc txt" style="overflow:auto;padding:16px 22px"><div class="empty" style="margin:20px">Escolha um tema à esquerda.</div></div></div>';
  try { docsIndex = docsIndex || await api.docsIndex(); } catch (e) { p.querySelector('.idx').innerHTML = `<div class="alert erro" style="margin:10px">${e.message}</div>`; fim(); return; }
  const idx = p.querySelector('.idx'), txt = p.querySelector('.txt');
  const draw = (f) => { idx.innerHTML = ''; for (const d of docsIndex) { if (f && !d.titulo.toLowerCase().includes(f)) continue; const a = document.createElement('div'); a.className = 'node'; a.dataset.doc = d.chave; a.innerHTML = `<span class="lbl">${d.titulo}</span>`; a.addEventListener('click', async () => { idx.querySelectorAll('.node').forEach(n => n.classList.toggle('on', n === a)); const r = await api.docs(d.chave); txt.innerHTML = md(r.markdown); katexRender(txt); txt.scrollTop = 0; }); idx.appendChild(a); } };
  p.querySelector('input').addEventListener('input', (e) => draw(e.target.value.trim().toLowerCase())); draw('');
  fim();
}
