// Desenhos 2D em SVG: esboço do planetário montado e perfil do dente (com zoom/pan)
const NS = 'http://www.w3.org/2000/svg';
const C = { sol: '#b8282c', bp: '#003882', sp: '#2a7fd4', anel: '#2e7d32', caixa: '#646566', aux: '#95999e', final: '#003882', pre: '#c77700', circ: '#95999e' };

function el(tag, attrs = {}, parent = null) {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (parent) parent.appendChild(e);
  return e;
}

export function makeSvg(w, h, viewBox) {
  const svg = el('svg', { viewBox, width: '100%', preserveAspectRatio: 'xMidYMid meet' });
  svg.style.aspectRatio = `${w} / ${h}`;
  enablePanZoom(svg, viewBox);
  return svg;
}

function enablePanZoom(svg, vb0) {
  let vb = vb0.split(' ').map(Number); let drag = null;
  const apply = () => svg.setAttribute('viewBox', vb.join(' '));
  svg.addEventListener('wheel', (e) => {
    e.preventDefault();
    const r = svg.getBoundingClientRect(); const mx = vb[0] + (e.clientX - r.left) / r.width * vb[2]; const my = vb[1] + (e.clientY - r.top) / r.height * vb[3];
    const f = e.deltaY > 0 ? 1.15 : 1 / 1.15;
    vb = [mx - (mx - vb[0]) * f, my - (my - vb[1]) * f, vb[2] * f, vb[3] * f]; apply();
  }, { passive: false });
  // listeners globais só durante o arraste (removidos no mouseup) — nada fica pendurado em window
  const move = (e) => { if (!drag) return; const r = svg.getBoundingClientRect(); vb[0] = drag.vb[0] - (e.clientX - drag.x) / r.width * vb[2]; vb[1] = drag.vb[1] - (e.clientY - drag.y) / r.height * vb[3]; apply(); };
  const up = () => { drag = null; svg.style.cursor = 'grab'; window.removeEventListener('mousemove', move); window.removeEventListener('mouseup', up); };
  svg.addEventListener('mousedown', (e) => { e.preventDefault(); drag = { x: e.clientX, y: e.clientY, vb: [...vb] }; svg.style.cursor = 'grabbing'; window.addEventListener('mousemove', move); window.addEventListener('mouseup', up); });
  svg.addEventListener('dblclick', () => { vb = vb0.split(' ').map(Number); apply(); });
}

/** Esboço do planetário: círculos primitivos/cabeça do sol, planetas (N), anelar, aro e caixa. */
export function drawPlanetary(p) {
  const R = Math.max(p.D_caixa || 0, p.D_ext_r || 0, p.d_r || 0) / 2 * 1.08;
  const svg = makeSvg(600, 600, `${-R} ${-R} ${2 * R} ${2 * R}`);
  const g = el('g', { fill: 'none', 'stroke-width': R / 300 }, svg);
  el('circle', { r: p.d_sun / 2, stroke: C.sol }, g);
  if (p.da_sun) el('circle', { r: p.da_sun / 2, stroke: C.sol, 'stroke-dasharray': `${R / 60} ${R / 90}`, opacity: .6 }, g);
  const rc = p.a_ext || (p.d_sun + p.d_bp) / 2;
  for (let i = 0; i < p.N; i++) {
    const ang = i * 2 * Math.PI / p.N; const x = rc * Math.cos(ang), y = rc * Math.sin(ang);
    el('circle', { cx: x, cy: y, r: p.d_bp / 2, stroke: C.bp }, g);
    if (p.da_bp) el('circle', { cx: x, cy: y, r: p.da_bp / 2, stroke: C.bp, 'stroke-dasharray': `${R / 60} ${R / 90}`, opacity: .6 }, g);
    if (p.d_sp && Math.abs(p.d_sp - p.d_bp) > 1e-6) el('circle', { cx: x, cy: y, r: p.d_sp / 2, stroke: C.sp, 'stroke-dasharray': `${R / 40} ${R / 80}` }, g);
    el('circle', { cx: x, cy: y, r: R / 120, fill: C.bp, stroke: 'none' }, g);
  }
  el('circle', { r: rc, stroke: C.aux, 'stroke-dasharray': `${R / 100} ${R / 50}`, opacity: .7 }, g);
  el('circle', { r: p.d_r / 2, stroke: C.anel }, g);
  if (p.df_r) el('circle', { r: p.df_r / 2, stroke: C.anel, 'stroke-dasharray': `${R / 60} ${R / 90}`, opacity: .6 }, g);
  if (p.D_ext_r) el('circle', { r: p.D_ext_r / 2, stroke: C.anel, 'stroke-width': R / 150 }, g);
  if (p.D_caixa) el('circle', { r: p.D_caixa / 2, stroke: C.caixa, 'stroke-dasharray': `${R / 30} ${R / 60}` }, g);
  // cotas simples
  const txt = (x, y, s, col) => { const t = el('text', { x, y, fill: col, 'font-size': R / 22, 'font-family': 'Inter, sans-serif', 'text-anchor': 'middle' }, svg); t.textContent = s; };
  txt(0, -p.d_sun / 2 - R / 30, `sol d_w ${p.d_sun.toFixed(2)}`, C.sol);
  txt(0, p.d_r / 2 + R / 18, `anelar d_w ${p.d_r.toFixed(2)}`, C.anel);
  if (p.D_ext_r) txt(0, -p.D_ext_r / 2 + R / 18, `Ø ext. anelar ${p.D_ext_r.toFixed(1)}`, C.anel);
  const wrap = document.createElement('div'); wrap.style.position = 'relative'; wrap.appendChild(svg);
  const leg = document.createElement('div'); leg.className = 'legend';
  leg.innerHTML = `<span><i style="border-color:${C.sol}"></i>sol</span><span><i style="border-color:${C.bp}"></i>planeta maior</span>${p.d_sp && Math.abs(p.d_sp - p.d_bp) > 1e-6 ? `<span><i style="border-color:${C.sp}"></i>planeta menor</span>` : ''}<span><i style="border-color:${C.anel}"></i>anelar / aro</span><span><i style="border-color:${C.caixa}"></i>manga</span><span class="muted">rolagem = zoom · arrastar = mover · 2 cliques = reset</span>`;
  wrap.appendChild(leg);
  return wrap;
}

/** Perfil do dente: res = resposta de /api/perfil/2d  {final:{x,y}, pre:{x,y}|null, circulos:{d, d_b, d_a, d_f, d_Nf, d_Na, d_Ff}, interna, z, setor} */
export function drawToothProfile(res, { modo = 'dente', mostrarPre = true } = {}) {
  const pts = res.final; const pre = res.pre;
  const all = [...pts.x, ...(pre ? pre.x : [])]; const ally = [...pts.y, ...(pre ? pre.y : [])];
  let minx = Math.min(...all), maxx = Math.max(...all), miny = Math.min(...ally), maxy = Math.max(...ally);
  if (modo === 'roda') { const R = Math.max(Math.abs(res.circulos.d_a), Math.abs(res.circulos.d_f), res.circulos.D_ext || 0) / 2; minx = -R; maxx = R; miny = -R; maxy = R; }
  const pad = (maxx - minx) * 0.08 + 1e-6;
  const w = maxx - minx + 2 * pad, h = maxy - miny + 2 * pad;
  const svg = makeSvg(700, 700 * h / w, `${minx - pad} ${-(maxy + pad)} ${w} ${h}`);
  const sw = w / 500;
  const path = (xs, ys, col, dash) => el('path', { d: xs.map((x, i) => `${i ? 'L' : 'M'}${x.toFixed(5)} ${(-ys[i]).toFixed(5)}`).join(' '), fill: 'none', stroke: col, 'stroke-width': sw * 1.6, ...(dash ? { 'stroke-dasharray': `${sw * 6} ${sw * 4}` } : {}) }, svg);
  const circ = (d, col, dash, label) => {
    if (!d) return; const r = Math.abs(d) / 2;
    el('circle', { r, stroke: col, fill: 'none', 'stroke-width': sw * 0.8, 'stroke-dasharray': dash ? `${sw * 4} ${sw * 4}` : null, opacity: .8 }, svg);
    if (label && modo === 'dente') { const t = el('text', { x: minx + pad * 0.2, y: -(r) - sw * 3, fill: col, 'font-size': sw * 10, 'font-family': 'Inter, sans-serif' }, svg); t.textContent = `${label} ${Math.abs(d).toFixed(3)}`; }
  };
  const c = res.circulos;
  circ(c.d_f, C.circ, true, 'd_f'); circ(c.d_Ff, '#c77700', true, 'd_Ff'); circ(c.d_b, '#95999e', false, 'd_b'); circ(c.d, '#353c43', true, 'd');
  circ(c.d_Nf, '#2e7d32', true, 'd_Nf'); circ(c.d_Na, '#2e7d32', true, 'd_Na'); circ(c.d_a, C.circ, true, 'd_a');
  if (modo === 'roda' && res.roda) {
    path(res.roda.x, res.roda.y, C.final);
    if (res.roda_pre && mostrarPre) path(res.roda_pre.x, res.roda_pre.y, C.pre, true);
  } else {
    if (pre && mostrarPre) path(pre.x, pre.y, C.pre, true);
    path(pts.x, pts.y, C.final);
  }
  const wrap = document.createElement('div'); wrap.style.position = 'relative'; wrap.appendChild(svg);
  const leg = document.createElement('div'); leg.className = 'legend';
  leg.innerHTML = `<span><i style="border-color:${C.final}"></i>perfil final (retificado)</span>${pre && mostrarPre ? `<span><i style="border-color:${C.pre};border-top-style:dashed"></i>pré-usinagem (protuberância)</span>` : ''}<span><i style="border-color:${C.circ};border-top-style:dashed"></i>d_a, d_f</span><span><i style="border-color:#2e7d32;border-top-style:dashed"></i>d_Na, d_Nf (úteis)</span><span><i style="border-color:#c77700;border-top-style:dashed"></i>d_Ff (início da evolvente)</span>`;
  wrap.appendChild(leg);
  return wrap;
}
