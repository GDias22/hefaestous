// Esquema do trem de engrenagens à escala: vista lateral (eixos horizontais; rodas como seções com cubo) e n/T/P por eixo.
// Cada roda (pinhão e coroa de cada estágio) é um alvo de clique próprio, com rótulo, tooltip e realce da selecionada.
import { COR, keyTrem } from '../model/rodas.js';
import { showTip, hideTip } from './tip.js';
const NS = 'http://www.w3.org/2000/svg';
const el = (t, a = {}, p = null, txt = null) => { const e = document.createElementNS(NS, t); for (const k in a) if (a[k] != null) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; if (p) p.appendChild(e); return e; };
const f1 = (v) => Number(v).toLocaleString('pt-BR', { maximumFractionDigits: 1 });
const f2 = (v) => Number(v).toLocaleString('pt-BR', { maximumFractionDigits: 2 });

/** Seção lateral de uma roda externa: coroa dentada (entre d_f e d_a) + alma + cubo. cy = eixo. */
function roda(g, x, cy, b, ra, rf, rhub, o) {
  const w = b;
  const grp = el('g', { class: 'sch-hit wheel' + (o.sel ? ' sel' : '') + (o.dim ? ' dim' : ''), 'data-w': o.key }, g);
  el('rect', { x, y: cy - rf, width: w, height: 2 * rf, class: 'sch-shaft', rx: 1 }, grp);
  el('rect', { x, y: cy - ra, width: w, height: Math.max(1.5, ra - rf), class: 'wfill', fill: o.cor + '22', stroke: o.cor, 'stroke-width': o.sel ? 2.2 : 1.4 }, grp);
  el('rect', { x, y: cy + rf, width: w, height: Math.max(1.5, ra - rf), class: 'wfill', fill: o.cor + '22', stroke: o.cor, 'stroke-width': o.sel ? 2.2 : 1.4 }, grp);
  if (rhub > 0 && rhub < rf * 0.9) el('rect', { x, y: cy - rhub, width: w, height: 2 * rhub, fill: 'none', stroke: '#95999e', 'stroke-width': .8, 'stroke-dasharray': '3 2' }, grp);
  grp.addEventListener('click', (e) => { e.stopPropagation(); o.onSelect(o.key); });
  grp.addEventListener('mousemove', (e) => showTip(e, o.tip)); grp.addEventListener('mouseleave', hideTip);
  return grp;
}

/** malhas: [{apelido, vars}], eixos: [{nome,n,T,P_kW,i_estagio}], sel: key da roda (`estagio:i:pinhao|coroa`) ou null,
 *  onSelect(key), seg: {key: {SH,SF}} */
export function drawTrain(svg, malhas, eixos, sel, onSelect, seg = {}) {
  svg.innerHTML = '';
  const W = svg.clientWidth || 900, H = svg.clientHeight || 520;
  const n = malhas.length;
  if (!n) { el('text', { x: W / 2, y: H / 2, class: 'sch-label', 'text-anchor': 'middle' }, svg, 'Adicione um estágio'); return; }
  const gap = 22;                                       // folga axial entre estágios (mm, em escala)
  const totalB = malhas.reduce((s, m) => s + Math.max(m.vars.b_pinhao, m.vars.b_coroa), 0) + gap * (n + 1);
  const maxR0 = Math.abs(malhas[0].vars.d_a_pinhao) / 2;
  let span = maxR0;
  malhas.forEach(m => { const v = m.vars; span += v.Z_coroa < 0 ? 0 : Math.abs(v.a); });
  span += Math.max(...malhas.map(m => Math.abs(m.vars.Z_coroa < 0 ? (m.vars.di_coroa || m.vars.d_a_coroa) : m.vars.d_a_coroa) / 2));
  const padL = 200, padR = 30, padT = 44, padB = 44;
  const sc = Math.min((W - padL - padR) / totalB, (H - padT - padB) / span);
  el('text', { x: 14, y: 22, class: 'sch-title' }, svg, 'Trem de engrenagens — vista lateral (à escala)');
  const g = el('g', { transform: `translate(${padL},${padT})` }, svg);
  let x = gap * sc, y = maxR0 * sc;
  const eixoY = [y];
  malhas.forEach((m, k) => {
    const v = m.vars; const interna = v.Z_coroa < 0;
    const bp = v.b_pinhao * sc, bc = v.b_coroa * sc, bmax = Math.max(bp, bc);
    const ra1 = Math.abs(v.d_a_pinhao) / 2 * sc, rf1 = Math.abs(v.d_f_pinhao) / 2 * sc, rh1 = Math.abs(v.d_sh_pinhao || 0) / 2 * sc;
    const ra2 = Math.abs(v.d_a_coroa) / 2 * sc, rf2 = Math.abs(v.d_f_coroa) / 2 * sc, rh2 = Math.abs(v.d_sh_coroa || 0) / 2 * sc;
    const a = Math.abs(v.a) * sc;
    const y1 = y, y2 = interna ? y + a : y + a;      // coroa no eixo abaixo (interna: eixo da anelar deslocado de a)
    const xc = x + (bmax - bp) / 2, xcc = x + (bmax - bc) / 2;
    const Rext = Math.max((v.di_coroa ? Math.abs(v.di_coroa) / 2 : Math.max(Math.abs(v.d_a_coroa), Math.abs(v.d_f_coroa)) / 2 * 1.12) * sc, Math.max(ra2, rf2) + 2);   // raio externo do aro (≥ cabeça)
    const gs = el('g', {}, g);
    const kp = keyTrem(k, 'pinhao'), kc = keyTrem(k, 'coroa');
    const mk = (key, nome, z, mn, dw, b, cor) => ({ key, cor, sel: sel === key, dim: sel && sel !== key, onSelect: onSelect || (() => {}),
      tip: `<b style="color:${cor}">${nome}</b><br>z ${z} · m<sub>n</sub> ${mn} · d<sub>w</sub> ${f2(Math.abs(dw))} mm · b ${f1(b)} mm${(seg[key] || {}).SH != null ? `<br>S<sub>H</sub> mín ${f2(seg[key].SH)} · S<sub>F</sub> mín ${f2(seg[key].SF)}` : ''}<br><span class="muted">clique para editar</span>` });
    const op = mk(kp, `Pinhão ${k + 1}`, Math.abs(v.Z_pinhao), v.m_n, v.dw_pinhao, v.b_pinhao, COR.pinhao);
    const oc = mk(kc, `${interna ? 'Anelar' : 'Coroa'} ${k + 1}`, Math.abs(v.Z_coroa), v.m_n, v.dw_coroa, v.b_coroa, interna ? COR.interna : COR.coroa);
    if (interna) {
      // anelar: coroa dentada do lado de dentro, aro do lado de fora; seção acima e abaixo do eixo da anelar
      const ga = el('g', { class: 'sch-hit wheel' + (oc.sel ? ' sel' : '') + (oc.dim ? ' dim' : ''), 'data-w': kc }, gs);
      const rin = Math.min(ra2, rf2), rout = Math.max(ra2, rf2);        // anelar: d_a < d_f; a faixa de dentes fica entre os dois raios
      const wst = { fill: oc.cor + '22', stroke: oc.cor, 'stroke-width': oc.sel ? 2.2 : 1.4, class: 'wfill' };
      el('rect', { x: xcc, y: y2 - Rext, width: bc, height: Math.max(0, Rext - rout), class: 'sch-shaft' }, ga);
      el('rect', { x: xcc, y: y2 - rout, width: bc, height: Math.max(1.5, rout - rin), ...wst }, ga);
      el('rect', { x: xcc, y: y2 + rin, width: bc, height: Math.max(1.5, rout - rin), ...wst }, ga);
      el('rect', { x: xcc, y: y2 + rout, width: bc, height: Math.max(0, Rext - rout), class: 'sch-shaft' }, ga);
      ga.addEventListener('click', (e) => { e.stopPropagation(); oc.onSelect(kc); }); ga.addEventListener('mousemove', (e) => showTip(e, oc.tip)); ga.addEventListener('mouseleave', hideTip);
      roda(gs, xc, y1, bp, ra1, rf1, rh1, op);
    } else {
      roda(gs, xcc, y2, bc, ra2, rf2, rh2, oc);
      roda(gs, xc, y1, bp, ra1, rf1, rh1, op);
    }
    // rótulos permanentes das rodas (ao lado da seção)
    el('text', { x: xc + bp / 2, y: y1 - ra1 - 6, class: 'sch-wl', 'text-anchor': 'middle', style: `fill:${COR.pinhao}` }, g, `P${k + 1} · z ${Math.abs(v.Z_pinhao)} · m ${v.m_n}${v.beta ? ' · β ' + v.beta + '°' : ''}`);
    el('text', { x: xcc + bc / 2, y: interna ? y2 - Rext - 6 : y2 + ra2 + 14, class: 'sch-wl', 'text-anchor': 'middle', style: `fill:${oc.cor}` }, g, `${interna ? 'A' : 'C'}${k + 1} · z ${Math.abs(v.Z_coroa)}`);
    // linha de contato (ponto primitivo)
    const yp = y1 + Math.abs(v.dw_pinhao) / 2 * sc * (interna ? -1 : 1);
    el('line', { x1: x - 4, x2: x + bmax + 4, y1: yp, y2: yp, stroke: '#b8282c', 'stroke-width': 1, 'stroke-dasharray': '3 2', 'pointer-events': 'none' }, gs);
    // rótulos
    const yl = Math.max(y1 + ra1, y2 + (interna ? (v.di_coroa ? Math.abs(v.di_coroa) / 2 : ra2 * 1.12) * sc : ra2));
    el('text', { x: x + bmax / 2, y: yl + (interna ? 16 : 30), class: 'sch-label', 'text-anchor': 'middle' }, gs, `${m.apelido || 'Estágio ' + (k + 1)} · i = ${f2(Math.abs(v.Z_coroa / v.Z_pinhao))}${interna ? ' (interna)' : ''}`);
    y = y2; eixoY.push(y);
    x += bmax + gap * sc;
  });
  // eixos (linhas de centro atravessando) e dados por eixo
  const xEnd = x;
  eixoY.forEach((yy, k) => {
    el('line', { x1: -10, x2: xEnd, y1: yy, y2: yy, class: 'sch-axis' }, g);
    const e = eixos[k]; if (!e) return;
    el('text', { x: -padL + 12, y: yy - 14, class: 'sch-label' }, g, e.nome);
    el('text', { x: -padL + 12, y: yy + 2, class: 'sch-value' }, g, `${f1(e.n)} rpm${e.n < 0 ? ' (inverso)' : ''}`);
    el('text', { x: -padL + 12, y: yy + 15, class: 'sch-value' }, g, `${f1(e.T)} N·m · ${f2(e.P_kW)} kW`);
  });
  // seta de entrada
  el('path', { d: `M -46 ${eixoY[0]} l 30 0 m -7 -5 l 7 5 l -7 5`, stroke: '#b8282c', 'stroke-width': 1.6, fill: 'none' }, g);
}
