// Passo 5 — Layout de eixos e mancais: desenho à escala de cada eixo (arraste a roda ao longo do eixo) + campos no inspetor.
// O backend (projeto/layout.py) deduz s, o arranjo físico 1–7 e K' pela posição das rodas; com o layout ATIVO eles
// sobrescrevem d_sh, L, s e arranjo das rodas no cálculo.
import { S, on, commit, select, toast } from '../app.js';
import { api } from '../api.js';
import { field, block } from './fields.js';
import { wheels, wheelByKey } from '../model/rodas.js';
import { fmtNum } from '../results.js';

const NS = 'http://www.w3.org/2000/svg';
const el = (t, a = {}, p = null, txt = null) => { const e = document.createElementNS(NS, t); for (const k in a) if (a[k] != null) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; if (p) p.appendChild(e); return e; };
const f1 = (v) => Number(v).toLocaleString('pt-BR', { maximumFractionDigits: 1 });

let pane = null, insp = null, busy = false, selKey = null;
export function init() {
  on(ev => {
    if (ev.type === 'select' && S.sel.kind === 'layout') garantir();
    if (['result', 'load'].includes(ev.type)) { if (pane && pane.classList.contains('on')) renderPane(pane); readouts(); }
    if (ev.type === 'change' && ['tipo do planetário', 'adicionar estágio', 'remover estágio', 'interno', 'busca de dentes', 'busca de dentes (trem)'].includes(ev.label)) { /* o resolvedor reposiciona as rodas; o painel redesenha no 'result' */ }
  });
}
const lay = () => S.proj && S.proj.layout;
const res = () => S.res && S.res.layout;

/** Layout guardado no projeto (necessário para os campos); criado a partir dos campos atuais das rodas. */
async function garantir(force = false) {
  if (busy || !S.proj) return;
  if (!force && lay() && lay().eixos && Object.keys(lay().eixos).length) return;
  busy = true;
  try {
    const { busca, buscaT, ...projeto } = S.proj;
    const novo = await api.layoutPadrao({ projeto });
    S.proj.layout = { ...novo, ativo: force && lay() ? !!lay().ativo : false };
    commit('layout'); renderInsp();
  } catch (e) { toast('Layout: ' + e.message, true); } finally { busy = false; }
}

// ------------------------------------------------------------------ desenho
export function renderPane(p) {
  pane = p; if (!S.proj) return;
  const keepTop = p.querySelector('.body')?.scrollTop || 0;
  p.innerHTML = '';
  const tb = document.createElement('div'); tb.className = 'toolbar';
  const ativo = !!(lay() && lay().ativo);
  tb.innerHTML = `<b>5 · Layout de eixos e mancais</b><span class="muted small">arraste a roda ou dê duplo clique numa cota (a, l) para digitar o valor</span>
    <span class="lay-badge ${ativo ? 'on' : ''}">${ativo ? 'layout ATIVO nos cálculos' : 'layout inativo (apenas visualização)'}</span>`;
  p.appendChild(tb);
  const body = document.createElement('div'); body.className = 'body lay-body'; p.appendChild(body);
  const r = res();
  if (!r || !r.eixos.length) { body.innerHTML = '<div class="empty" style="margin:20px">Aguardando cálculo…</div>'; return; }
  r.eixos.forEach(e => body.appendChild(desenhoEixo(e)));
  const n = document.createElement('p'); n.className = 'small muted lay-note';
  n.innerHTML = 'Convenções: <b>l</b> = vão entre os centros dos mancais; <b>a</b> = distância do centro da roda ao mancal esquerdo; <b>s</b> = distância do centro da roda ao meio do vão (arranjos 1–5) ou entre as rodas (6–7). Arranjo e K′ seguem a figura de Mazzo / ISO 6336-1 (método C).';
  body.appendChild(n);
  body.scrollTop = keepTop;
}

function desenhoEixo(e) {
  const box = document.createElement('div'); box.className = 'lay-eixo' + (e.invalido ? ' bad' : '');
  const head = document.createElement('div'); head.className = 'lay-h';
  head.innerHTML = `<b>${e.nome}</b><span class="muted small">Ø ${f1(e.d_sh)} · l = ${f1(e.L)} mm${e.montagem ? ` · planeta ${e.montagem === 'agulhas' ? 'sobre rolamentos de agulhas' : 'solidário ao eixo (eixo biapoiado)'}` : ''}</span>`;
  box.appendChild(head);
  const W = 1000, padX = 56;
  const vars = (w) => { const m = S.res.malhas && S.res.malhas[w.malha] && S.res.malhas[w.malha].geometria; const v = m && m.vars; return v ? { da: Math.abs(v[`d_a_${w.lado}`]), df: Math.abs(v[`d_f_${w.lado}`]) } : null; };
  const ws = e.rodas.map(r => { const w = wheelByKey(r.key) || { cor: '#7c8792' }; const v = w.malha != null ? vars(w) : null; return { ...r, cor: w.cor, da: (v && v.da) || r.d_ref * 1.1, df: (v && v.df) || r.d_ref * 0.9 }; });
  const xmin = Math.min(0, ...ws.map(r => r.a - r.b / 2)) - 28, xmax = Math.max(e.L, ...ws.map(r => r.a + r.b / 2)) + 28;
  const hmax = Math.max(...ws.map(r => r.da), e.d_sh + 18);
  let sc = (W - 2 * padX) / (xmax - xmin); sc = Math.min(sc, 300 / hmax);
  const nl = ws.length, TOP = 24 + 16 * nl;                          // uma faixa de rótulo por roda no topo
  const LH = 30;                                                      // espaço vertical entre linhas de cota (o texto fica acima da própria linha)
  const cy = TOP + hmax * sc / 2, H = cy + hmax * sc / 2 + 70 + LH * (nl + 1);
  const svg = el('svg', { viewBox: `0 0 ${W} ${H}`, class: 'lay-svg', preserveAspectRatio: 'xMidYMin meet' }); box.appendChild(svg);
  const X = (mm) => padX + (mm - xmin) * sc;
  // linha de centro e meio do vão
  el('line', { x1: X(xmin + 6), x2: X(xmax - 6), y1: cy, y2: cy, class: 'sch-axis' }, svg);
  el('line', { x1: X(e.L / 2), x2: X(e.L / 2), y1: cy - hmax * sc / 2 - 6, y2: cy + hmax * sc / 2 + 16, stroke: '#95999e', 'stroke-dasharray': '2 4' }, svg);
  el('text', { x: X(e.L / 2) + 4, y: cy + hmax * sc / 2 + 28, class: 'sch-label' }, svg, 'meio do vão');
  // eixo
  const dsh = e.d_sh * sc;
  el('rect', { x: X(xmin + 6), y: cy - dsh / 2, width: (xmax - xmin - 12) * sc, height: dsh, class: 'sch-shaft' }, svg);
  // torque
  if (e.torque === 'esq' || e.torque === 'dir') {
    const l = e.torque === 'esq'; const x0 = l ? X(xmin + 6) : X(xmax - 6);
    el('path', { d: `M ${x0 + (l ? -34 : 34)} ${cy} h ${l ? 28 : -28} m ${l ? -7 : 7} -5 l ${l ? 7 : -7} 5 l ${l ? -7 : 7} 5`, stroke: '#b8282c', 'stroke-width': 1.8, fill: 'none' }, svg);
    el('text', { x: x0 + (l ? -36 : 36), y: cy - 8, 'text-anchor': l ? 'end' : 'start', class: 'sch-label', style: 'fill:#b8282c;font-weight:700' }, svg, 'T');
  }
  // mancais
  const bw = 14, bh = dsh + 26;
  [[0, e.tipo === 'pino' ? 'apoio A' : 'mancal A'], [e.L, e.tipo === 'pino' ? 'apoio B' : 'mancal B']].forEach(([x, nome]) => {
    el('rect', { x: X(x) - bw / 2, y: cy - bh / 2, width: bw, height: bh, rx: 2, fill: '#fff', stroke: '#1f252b', 'stroke-width': 1.6 }, svg);
    el('path', { d: `M ${X(x) - 11} ${cy + bh / 2 + 10} h 22 l -11 -10 z`, fill: '#e9ecef', stroke: '#1f252b' }, svg);
    el('text', { x: X(x), y: cy + bh / 2 + 24, 'text-anchor': 'middle', class: 'sch-label' }, svg, nome);
  });
  // rodas (arrastáveis)
  ws.forEach(r => {
    const g = el('g', { class: 'lay-wheel sch-hit' + (r.key === selKey ? ' sel' : ''), 'data-w': r.key }, svg);
    const x = X(r.a - r.b / 2), w = r.b * sc, hd = r.da * sc, hf = r.df * sc;
    const err = (r.avisos || []).some(a => a.nivel === 'erro');
    el('rect', { x, y: cy - hf / 2, width: w, height: hf, fill: r.cor + '14', stroke: r.cor, 'stroke-width': 1 }, g);
    [-1, 1].forEach(sg => el('rect', { x, y: sg < 0 ? cy - hd / 2 : cy + hf / 2, width: w, height: Math.max(2, (hd - hf) / 2), fill: r.cor + '44', stroke: err ? '#b8282c' : r.cor, 'stroke-width': r.key === selKey ? 2.4 : 1.4 }, g));
    if (e.tipo === 'pino' && e.montagem === 'agulhas' && r.d_furo) {                      // rolamento de agulhas (entre o pino e o furo do planeta)
      const hb = r.d_furo * sc;
      [-1, 1].forEach(sg => el('rect', { x: x + 2, y: sg < 0 ? cy - hb / 2 : cy + dsh / 2, width: w - 4, height: Math.max(1.5, (hb - dsh) / 2), fill: 'url(#agulhas)', stroke: '#4b5560', 'stroke-width': .8 }, g));
    }
    el('rect', { x: x - 3, y: cy - hd / 2 - 4, width: w + 6, height: hd + 8, fill: 'transparent' }, g);   // área de captura
    const i = ws.indexOf(r), ty = 16 + 16 * i;                      // faixa própria no topo; guia vertical até a roda
    el('line', { x1: X(r.a), x2: X(r.a), y1: ty + 3, y2: cy - hd / 2 - 2, stroke: r.cor, 'stroke-dasharray': '2 3', 'stroke-width': .8 }, g);
    el('text', { x: X(r.a), y: ty, 'text-anchor': 'middle', class: 'sch-wl', style: `fill:${r.cor};font-size:12px` }, g, `${r.nome} · arranjo ${r.arranjo}`);
    el('circle', { cx: X(r.a), cy: cy, r: 3, fill: r.cor }, g);
  });
  // cotas: uma linha por roda (a, editável) e a linha do vão (l, editável); s é calculado (cinza). Duplo clique no texto edita.
  const y1 = cy + hmax * sc / 2 + 60;
  const dim = (xa, xb, y, txt, col, edit) => {
    el('line', { x1: X(xa), x2: X(xb), y1: y, y2: y, stroke: col, 'stroke-width': 1 }, svg);
    [xa, xb].forEach(x => el('line', { x1: X(x), x2: X(x), y1: y - 4, y2: y + 4, stroke: col }, svg));
    const g = el('g', { class: 'lay-cota' + (edit ? ' edit' : '') }, svg);
    const t = el('text', { x: (X(xa) + X(xb)) / 2, y: y - 7, 'text-anchor': 'middle', class: 'sch-value lay-cota-t', style: `fill:${col}` }, g, txt);
    if (edit) {
      const bb = { x: (X(xa) + X(xb)) / 2 - 62, y: y - 21, w: 124, h: 18 };
      el('rect', { x: bb.x, y: bb.y, width: bb.w, height: bb.h, fill: 'transparent', class: 'lay-cota-hit' }, g);
      g.appendChild(t);                                               // texto acima da área de captura
      el('title', {}, g, 'Duplo clique para digitar o valor');
      g.addEventListener('dblclick', (ev) => { ev.stopPropagation(); editarCota(box, g, edit); });
    }
  };
  ws.forEach((r, i) => {
    const y = y1 + LH * i;
    el('line', { x1: X(r.a), x2: X(r.a), y1: cy + r.da * sc / 2 + 2, y2: y, stroke: r.cor, 'stroke-dasharray': '2 3', 'stroke-width': .8 }, svg);
    dim(0, r.a, y, `a = ${f1(r.a)} mm`, r.cor, { eixo: e.id, key: r.key, campo: 'a', valor: r.a, unidade: 'mm' });
    if (r.s > 0.05) el('text', { x: X(r.a) + 8, y: y - 7, class: 'sch-label lay-cota-t', style: 'fill:#7c8792' }, svg, `s = ${f1(r.s)} mm`);
  });
  dim(0, e.L, y1 + LH * ws.length + 4, `l = ${f1(e.L)} mm`, '#1f252b', { eixo: e.id, campo: 'L', valor: e.L, unidade: 'mm' });
  // padrão de hachura das agulhas
  const defs = el('defs', {}, svg); const pat = el('pattern', { id: 'agulhas', width: 4, height: 4, patternUnits: 'userSpaceOnUse' }, defs); el('path', { d: 'M0 4 L4 0', stroke: '#4b5560', 'stroke-width': .7 }, pat);
  // arrastar
  svg.querySelectorAll('.lay-wheel').forEach(g => arrastar(svg, g, e, X, sc, xmin));
  // avisos do eixo
  const av = [...(e.avisos || []), ...ws.flatMap(r => (r.avisos || []).map(a => ({ ...a, texto: `${r.nome}: ${a.texto}` })))];
  if (av.length) { const d = document.createElement('div'); d.className = 'alerts lay-av'; av.forEach(a => { const x = document.createElement('div'); x.className = 'alert ' + (a.nivel === 'erro' ? 'erro' : a.nivel === 'info' ? 'ok' : 'aviso'); x.innerHTML = `<span class="ic">${a.nivel === 'erro' ? '✕' : a.nivel === 'info' ? 'i' : '!'}</span><span>${a.texto}</span>`; d.appendChild(x); }); box.appendChild(d); }
  return box;
}

/** Campo de texto sobre a cota (duplo clique). Enter confirma, Esc cancela, clicar fora confirma. */
function editarCota(box, g, ed) {
  if (box.querySelector('.lay-cota-in')) return;
  const t = g.querySelector('text'), rb = t.getBoundingClientRect(), bb = box.getBoundingClientRect();
  const inp = document.createElement('input'); inp.type = 'number'; inp.step = 'any'; inp.className = 'lay-cota-in'; inp.value = String(Math.round(ed.valor * 100) / 100);
  inp.style.left = `${rb.left - bb.left + rb.width / 2 - 48}px`; inp.style.top = `${rb.top - bb.top + rb.height / 2 - 14}px`;
  const un = document.createElement('span'); un.className = 'lay-cota-un'; un.textContent = ed.unidade;
  const w = document.createElement('div'); w.className = 'lay-cota-box'; w.style.left = inp.style.left; w.style.top = inp.style.top; w.append(inp, un);
  let fim = false;
  const fechar = () => { fim = true; w.remove(); };
  const ok = () => {
    if (fim) return; const v = parseFloat(String(inp.value).replace(',', '.'));
    fechar();
    if (!isFinite(v) || (ed.campo === 'L' && v <= 0)) { toast(ed.campo === 'L' ? 'O vão entre mancais deve ser positivo.' : 'Valor inválido.', true); return; }
    if (Math.abs(v - ed.valor) < 1e-9) return;
    const cfg = lay().eixos[ed.eixo];
    if (ed.campo === 'L') cfg.L = v; else cfg.rodas[ed.key].a = v;
    if (ed.key) selKey = ed.key;
    commit('layout'); renderInsp();
  };
  inp.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); ok(); } else if (e.key === 'Escape') { e.preventDefault(); fechar(); } e.stopPropagation(); });
  inp.addEventListener('blur', ok);
  box.appendChild(w); inp.focus(); inp.select();
}

function arrastar(svg, g, e, X, sc, xmin) {
  const key = g.dataset.w; let drag = null;
  const ponto = (ev) => { const pt = svg.createSVGPoint(); pt.x = ev.clientX; pt.y = ev.clientY; return pt.matrixTransform(svg.getScreenCTM().inverse()); };
  const mmDe = (ev) => xmin + (ponto(ev).x - (X(xmin))) / sc;
  g.addEventListener('pointerdown', (ev) => { g.setPointerCapture(ev.pointerId); const r = e.rodas.find(x => x.key === key); drag = { mm0: mmDe(ev), a0: r.a, moveu: false }; ev.preventDefault(); });
  g.addEventListener('pointermove', (ev) => {
    if (!drag) return;
    let a = drag.a0 + (mmDe(ev) - drag.mm0); a = Math.round(Math.max(-0.6 * e.L, Math.min(1.6 * e.L, a)) * 2) / 2;
    if (Math.abs(a - drag.a0) > 0.4) drag.moveu = true;
    drag.a = a; g.setAttribute('transform', `translate(${(a - drag.a0) * sc},0)`);
    pos(key, a);
  });
  g.addEventListener('pointerup', (ev) => {
    if (!drag) return; g.releasePointerCapture(ev.pointerId); const d = drag; drag = null;
    if (!d.moveu) { selecionar(key); return; }
    setA(e.id, key, d.a); selKey = key;
  });
}
function pos(key, a) { const i = insp && insp.querySelector(`.fld[data-path$="rodas.${key}.a"] input`); if (i) i.value = String(a); }
function setA(eid, key, a) {
  const c = lay().eixos[eid].rodas[key]; c.a = a; commit('layout'); renderInsp();
}
function selecionar(key) { selKey = key; marcar(); if (pane) renderPane(pane); }

// ------------------------------------------------------------------ inspetor
function normalizar() {            // campos de escolha precisam de valor textual ('auto' em vez de null)
  const L = lay(); if (!L || !L.eixos) return;
  for (const e of Object.values(L.eixos)) for (const r of Object.values(e.rodas || {})) { if (r.arranjo == null || r.arranjo === '') r.arranjo = 'auto'; else r.arranjo = String(r.arranjo); if (!r.fixacao) r.fixacao = 'auto'; }
}
export function renderInspector(root) { insp = root; normalizar(); renderInsp(); }
function renderInsp() {
  if (!insp || S.sel.kind !== 'layout') return;
  insp.innerHTML = '';
  normalizar(); const L = lay();
  if (!L || !L.eixos || !Object.keys(L.eixos).length) { insp.innerHTML = '<div class="block"><div class="empty">Preparando o layout a partir das rodas…</div></div>'; garantir(); return; }
  const b = block('Layout de eixos e mancais');
  b.appendChild(field('layout.ativo', { type: 'bool', label: 'Usar o layout nos cálculos', key: 'ativo', help: 'Ativo: d_sh, l, s e o arranjo físico (1–7) de cada roda vêm daqui e substituem os campos "Corpo, eixo e mancais" das rodas (que ficam ocultos). Inativo: o desenho é só visualização e os campos das rodas valem.', onChange: () => { setTimeout(() => { renderInsp(); }, 0); } }));
  const nt = document.createElement('p'); nt.className = 'small muted'; nt.style.margin = '6px 0';
  nt.textContent = 'Informe, por eixo, o diâmetro, o vão entre mancais e a posição de cada roda; o programa deduz s, o arranjo e K′. A anelar não entra (é da carcaça).';
  b.appendChild(nt);
  const bt = document.createElement('button'); bt.className = 'btn xs'; bt.textContent = 'Recarregar dos campos das rodas'; bt.title = 'Refaz o layout a partir de d_sh, L e largura atuais das rodas (perde as posições editadas)';
  bt.addEventListener('click', () => { if (confirm('Refazer o layout a partir dos campos atuais das rodas? As posições editadas serão perdidas.')) garantir(true); });
  b.appendChild(bt); insp.appendChild(b);
  const eixos = (res() && res().eixos) || [];
  for (const e of eixos) {
    const cfg = L.eixos[e.id]; if (!cfg) continue;
    const blk = block(e.nome);
    blk.appendChild(field(`layout.eixos.${e.id}.d_sh`, { type: 'number', min: 0.1, unit: 'mm', label: e.tipo === 'pino' ? 'Diâmetro do pino d_sh' : 'Diâmetro do eixo d_sh', key: 'd_sh', docKey: 'eixo', fig: 'eixo.png', help: 'Diâmetro do eixo sob as rodas (ou do pino do porta-planetas). Entra na deflexão f_sh (K_Hβ), no jogo entre flancos e na razão d/d_sh que escolhe o K′.' }));
    blk.appendChild(field(`layout.eixos.${e.id}.L`, { type: 'number', min: 1, unit: 'mm', label: 'Vão entre mancais l', key: 'L', help: 'Distância entre os centros dos dois mancais (ou apoios) do eixo, no plano axial.' }));
    blk.appendChild(field(`layout.eixos.${e.id}.torque`, { type: 'choice', choices: ['esq', 'dir', 'indef'], labels: { esq: 'pela esquerda (mancal A)', dir: 'pela direita (mancal B)', indef: 'não se aplica / intermediário' }, label: e.tipo === 'pino' ? 'Lado do carregamento' : 'Torque entra por', key: 'torque', help: 'Lado do eixo por onde o torque entra. Diferencia o arranjo 3 (roda do mesmo lado do torque) do 4 (lado oposto) quando a roda está descentrada.' }));
    if (e.tipo === 'pino') blk.appendChild(field(`layout.eixos.${e.id}.montagem`, { type: 'choice', choices: ['agulhas', 'solidaria'], labels: { agulhas: 'rolamentos de agulhas dentro do planeta', solidaria: 'planeta solidário ao eixo (eixo biapoiado)' }, label: 'Montagem do planeta', key: 'montagem', help: 'Agulhas: o planeta gira sobre o pino por rolamentos no furo (informe o Ø do furo). Solidária: planeta e eixo são uma peça (sem furo) e o eixo gira biapoiado nos mancais.' }));
    for (const r of e.rodas) {
      const w = wheelByKey(r.key) || { cor: '#7c8792' };
      const d = document.createElement('details'); d.className = 'wheelbox' + (r.key === selKey ? ' on' : ''); d.style.setProperty('--wc', w.cor); d.dataset.wkey = r.key; d.open = true;
      d.innerHTML = `<summary><i class="chip" style="background:${w.cor}"></i><b>${r.nome}</b><span class="muted small">b ${f1(r.b)} · Ø ${f1(r.d_ref)}</span><span class="sel-tag">selecionada</span></summary>`;
      const inner = document.createElement('div'); inner.className = 'wb'; d.appendChild(inner);
      const p0 = `layout.eixos.${e.id}.rodas.${r.key}`;
      inner.appendChild(field(`${p0}.a`, { type: 'number', unit: 'mm', label: 'Centro da roda a partir do mancal A', key: 'a', help: 'Distância do meio da largura da roda ao centro do mancal esquerdo. Fora de 0…l = roda em balanço. Também pode arrastar a roda no desenho.' }));
      inner.appendChild(field(`${p0}.fixacao`, { type: 'choice', choices: ['auto', 'integrada_prensada', 'chaveta'], labels: { auto: 'automática (pela razão d/d_sh ≥ 1,15)', integrada_prensada: 'integrada ao eixo ou prensada', chaveta: 'com chaveta ou estrias' }, label: 'Fixação da roda ao eixo', key: 'fixacao', fig: 'arranjos.png', help: 'Define o ramo do K′ da figura: roda integrada/prensada usa o valor de d/d_sh ≥ 1,15; com chaveta/estrias usa o de d/d_sh < 1,15. Automática reproduz a regra do código original.' }));
      inner.appendChild(field(`${p0}.arranjo`, { type: 'choice', choices: ['auto', '1', '2', '3', '4', '5', '6', '7'], labels: { auto: 'automático (pela posição)' }, label: 'Arranjo físico (Mazzo)', key: 'arranjo', fig: 'arranjos.png', help: 'Automático: deduzido pela posição das rodas e pelo lado do torque. Escolha 1–7 só para forçar um arranjo diferente do deduzido.' }));
      if (e.tipo === 'pino' && e.montagem === 'agulhas') inner.appendChild(field(`${p0}.d_furo`, { type: 'number', min: 0, unit: 'mm', label: 'Ø do furo do planeta (rolamento)', key: 'd_furo', help: 'Diâmetro interno da roda (externo do rolamento de agulhas). Usado como d_i na espessura de aro e na inércia do K_v. Ignorado se o planeta for solidário ao eixo.' }));
      const ro = document.createElement('div'); ro.className = 'lay-out small'; ro.dataset.rk = r.key; inner.appendChild(ro);
      d.addEventListener('focusin', () => { if (selKey !== r.key) { selKey = r.key; marcar(); if (pane) renderPane(pane); } });
      blk.appendChild(d);
    }
    const av = document.createElement('div'); av.className = 'lay-eixo-av'; av.dataset.ek = e.id; blk.appendChild(av);
    insp.appendChild(blk);
  }
  readouts();
}
function marcar() { if (!insp) return; insp.querySelectorAll('details.wheelbox').forEach(d => d.classList.toggle('on', d.dataset.wkey === selKey)); }
/** Atualiza os valores calculados (arranjo, s, K′, avisos) sem recriar os campos — não tira o foco de quem está digitando. */
function readouts() {
  if (!insp || S.sel.kind !== 'layout' || !res()) return;
  for (const e of res().eixos) {
    for (const r of e.rodas) {
      const o = insp.querySelector(`.lay-out[data-rk="${r.key}"]`); if (!o) continue;
      const man = r.arranjo_manual != null;
      o.innerHTML = `<div class="kvs"><span class="k">Arranjo usado${man ? ' (manual)' : ''}</span><span class="v">${r.arranjo}${man ? ` · auto ${r.arranjo_auto}` : ''}</span><span></span>
        <span class="k">s · s/l</span><span class="v">${fmtNum(r.s, 2)} mm · ${fmtNum(r.s_l, 3)}</span><span></span>
        <span class="k">K′ (${r.ramo})</span><span class="v">${fmtNum(r.k_linha, 2)}</span><span></span>
        <span class="k">d_ref / d_sh</span><span class="v">${fmtNum(r.razao_d, 2)}</span><span></span></div>` +
        (r.avisos || []).map(a => `<div class="alert ${a.nivel === 'erro' ? 'erro' : a.nivel === 'info' ? 'ok' : 'aviso'}" style="margin-top:4px"><span class="ic">${a.nivel === 'erro' ? '✕' : a.nivel === 'info' ? 'i' : '!'}</span><span>${a.texto}</span></div>`).join('');
    }
    const av = insp.querySelector(`.lay-eixo-av[data-ek="${e.id}"]`);
    if (av) av.innerHTML = (e.avisos || []).map(a => `<div class="alert ${a.nivel === 'erro' ? 'erro' : 'aviso'}" style="margin-top:6px"><span class="ic">${a.nivel === 'erro' ? '✕' : '!'}</span><span>${a.texto}</span></div>`).join('');
  }
}

/** Chaves (d_sh, L, sh, Arranjo, k_linha, di) que o layout ativo impõe à roda `wkey` ([] quando inativo/não coberta). */
export function camposImpostos(wkey) {
  if (!(lay() && lay().ativo) || !res()) return [];
  for (const e of res().eixos) for (const r of e.rodas) if (r.key === wkey && r.override) {
    const ks = Object.keys(r.override); if (ks.includes('Arranjo') || ks.includes('k_linha')) { ks.push('Arranjo', 'k_linha'); } return ks;
  }
  return [];
}
