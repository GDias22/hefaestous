// Gráfico de sensibilidade (linha com ponto atual e faixa mínima)
const NS = 'http://www.w3.org/2000/svg';
const el = (t, a = {}, p = null, txt = null) => { const e = document.createElementNS(NS, t); for (const k in a) if (a[k] != null) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; if (p) p.appendChild(e); return e; };

/** r = {x:[], label_x, unidade_x, atual_x, series:{fator:[], S_H:[], S_F:[]}, minimo:{S_H, S_F}, rotulo_fator} */
export function sensChart(svg, r, y) {
  svg.innerHTML = '';
  const W = svg.clientWidth || 440, H = svg.clientHeight || 220; svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
  const m = { l: 48, r: 14, t: 26, b: 34 };
  const xs = r.x, ys = r.series[y]; if (!xs || !ys) return;
  const pts = xs.map((x, i) => [x, ys[i]]).filter(p => p[1] != null && Number.isFinite(p[1]));
  if (!pts.length) { el('text', { x: W / 2, y: H / 2, class: 'sch-label', 'text-anchor': 'middle' }, svg, 'sem pontos válidos'); return; }
  const minX = Math.min(...pts.map(p => p[0])), maxX = Math.max(...pts.map(p => p[0]));
  let minY = Math.min(...pts.map(p => p[1])), maxY = Math.max(...pts.map(p => p[1]));
  const lim = r.minimo && r.minimo[y]; if (lim != null) { minY = Math.min(minY, lim); maxY = Math.max(maxY, lim); }
  const pad = (maxY - minY) * 0.12 || 0.1; minY -= pad; maxY += pad;
  const sx = (x) => m.l + (x - minX) / ((maxX - minX) || 1) * (W - m.l - m.r), sy = (v) => H - m.b - (v - minY) / ((maxY - minY) || 1) * (H - m.t - m.b);
  // grid
  const g = el('g', { class: 'grid' }, svg);
  for (let i = 0; i <= 4; i++) { const v = minY + (maxY - minY) * i / 4; el('line', { x1: m.l, x2: W - m.r, y1: sy(v), y2: sy(v) }, g); el('text', { x: m.l - 6, y: sy(v) + 3, class: 'sch-label', 'text-anchor': 'end' }, svg, v.toFixed(2)); }
  for (let i = 0; i <= 4; i++) { const x = minX + (maxX - minX) * i / 4; el('text', { x: sx(x), y: H - m.b + 14, class: 'sch-label', 'text-anchor': 'middle' }, svg, Number(x.toPrecision(3)).toString()); }
  el('text', { x: (m.l + W - m.r) / 2, y: H - 4, class: 'sch-label', 'text-anchor': 'middle' }, svg, `${r.label_x}${r.unidade_x ? ' [' + r.unidade_x + ']' : ''}`);
  el('text', { x: 10, y: 12, class: 'sch-label' }, svg, y === 'fator' ? (r.rotulo_fator || 'fator') : y);
  // faixa abaixo do mínimo
  if (lim != null) { el('rect', { x: m.l, y: sy(lim), width: W - m.l - m.r, height: Math.max(0, H - m.b - sy(lim)), fill: '#b8282c', opacity: .07 }, svg); el('line', { x1: m.l, x2: W - m.r, y1: sy(lim), y2: sy(lim), stroke: '#b8282c', 'stroke-dasharray': '4 3' }, svg); el('text', { x: W - m.r - 4, y: sy(lim) - 4, class: 'sch-label', 'text-anchor': 'end', fill: '#b8282c' }, svg, `mínimo ${lim}`); }
  // linha
  el('path', { d: pts.map((p, i) => `${i ? 'L' : 'M'}${sx(p[0]).toFixed(1)} ${sy(p[1]).toFixed(1)}`).join(' '), fill: 'none', stroke: '#003882', 'stroke-width': 2 }, svg);
  // ponto atual
  if (r.atual_x != null) {
    const i = pts.reduce((b, p, k) => (Math.abs(p[0] - r.atual_x) < Math.abs(pts[b][0] - r.atual_x) ? k : b), 0);
    const cy = r.atual_y && r.atual_y[y] != null ? r.atual_y[y] : pts[i][1];
    el('circle', { cx: sx(r.atual_x), cy: sy(cy), r: 5, fill: '#b8282c', stroke: '#fff', 'stroke-width': 2 }, svg);
    el('text', { x: sx(r.atual_x) + 8, y: sy(cy) - 8, class: 'sch-value', fill: '#b8282c' }, svg, `atual: ${Number(cy).toFixed(3)}`);
  }
}
