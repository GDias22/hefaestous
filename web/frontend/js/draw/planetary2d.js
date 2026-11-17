// Esquema do planetário: vista frontal à escala. Cada roda (sol, planeta maior, planeta menor, anelar) é um alvo de clique
// próprio, com cor fixa, rótulo permanente, tooltip ao passar o mouse e realce da roda selecionada (as demais atenuam).
import { COR } from '../model/rodas.js';
import { showTip, hideTip } from './tip.js';

const NS = 'http://www.w3.org/2000/svg';
const el = (t, a = {}, p = null, txt = null) => { const e = document.createElementNS(NS, t); for (const k in a) if (a[k] != null) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; if (p) p.appendChild(e); return e; };
const f1 = (v) => Number(v).toLocaleString('pt-BR', { maximumFractionDigits: 1 });
const f2 = (v) => Number(v).toLocaleString('pt-BR', { maximumFractionDigits: 2 });

/** ext/inte: {apelido, vars}; cin: cinemática; N planetas; sel: key da roda selecionada ('sol'|'planeta_maior'|'planeta_menor'|'anelar'|null);
 *  seg: {key: {SH,SF}} (mínimos por roda); onSelect(key). */
export function drawPlanetary(svg, ext, inte, cin, N, sel, onSelect, seg = {}) {
  svg.innerHTML = '';
  const W = svg.clientWidth || 900, H = svg.clientHeight || 520;
  const ve = ext.vars, vi = inte.vars; const A = Math.abs;
  const composto = vi.Tipo_planetario !== 'Simples';
  const Rext = Math.max(A(vi.di_coroa || 0) / 2, A(vi.d_a_coroa) / 2 * 1.08, A(vi.d_f_coroa) / 2 * 1.06);
  const padL = 214; const sc = Math.min((W - padL - 30) / (2 * Rext), (H - 70) / (2 * Rext));
  const cx = padL + (W - padL) / 2, cy = H / 2 + 14;
  const g = el('g', { transform: `translate(${cx},${cy})` }, svg);
  el('text', { x: 14, y: 22, class: 'sch-title' }, svg, `Planetário ${composto ? 'composto' : 'simples'} — vista frontal (à escala) · clique numa roda para editá-la`);
  const dim = (k) => (sel && sel !== k ? ' dim' : '');
  const grupo = (k, rotulo, info) => {
    const h = el('g', { class: 'sch-hit wheel' + (sel === k ? ' sel' : '') + dim(k), 'data-w': k }, g);
    h.addEventListener('click', (e) => { e.stopPropagation(); onSelect && onSelect(k); });
    h.addEventListener('mousemove', (e) => showTip(e, tipHtml(k, rotulo, info)));
    h.addEventListener('mouseleave', hideTip);
    return h;
  };
  const tipHtml = (k, rotulo, info) => { const s = seg[k] || {}; const cor = COR[k]; return `<b style="color:${cor}">${rotulo}</b><br>${info}${s.SH != null ? `<br>S<sub>H</sub> mín ${f2(s.SH)} · S<sub>F</sub> mín ${f2(s.SF)}` : ''}<br><span class="muted">clique para editar</span>`; };
  const label = (x, y, txt, col, anchor = 'middle') => { const t = el('text', { x, y, class: 'sch-wl', 'text-anchor': anchor, fill: col }, g, txt); t.setAttribute('paint-order', 'stroke'); return t; };

  // ---- anelar (aro externo + coroa interna)
  const ga = grupo('anelar', 'Anelar', `z ${A(vi.Z_coroa)} · m<sub>n</sub> ${vi.m_n} · d<sub>w</sub> ${f2(A(vi.dw_coroa))} mm · b ${f1(vi.b_coroa)} mm`);
  const rAro = A(vi.di_coroa || 0) / 2 * sc || A(vi.d_a_coroa) / 2 * sc * 1.08;
  el('circle', { r: rAro, class: 'wfill', fill: '#f3f5f1', stroke: COR.anelar, 'stroke-width': 1.4 }, ga);
  el('circle', { r: A(vi.d_f_coroa) / 2 * sc, fill: '#fff', stroke: COR.anelar, 'stroke-width': 1.2 }, ga);
  el('circle', { r: A(vi.d_a_coroa) / 2 * sc, fill: 'none', stroke: COR.anelar, 'stroke-width': 1.2, 'stroke-dasharray': '3 3' }, ga);
  el('circle', { r: A(vi.dw_coroa) / 2 * sc, fill: 'none', stroke: COR.anelar, 'stroke-width': .8, 'stroke-dasharray': '6 4', opacity: .7 }, ga);
  label(0, -(rAro + 6), `Anelar · z ${A(vi.Z_coroa)}`, COR.anelar);

  // ---- planetas (maior e menor com alvos separados; o menor fica por cima)
  const rc = A(ve.a) * sc;
  const gb = grupo('planeta_maior', composto ? 'Planeta maior' : 'Planeta', `z ${ve.Z_coroa} · m<sub>n</sub> ${ve.m_n} · d<sub>w</sub> ${f2(A(ve.dw_coroa))} mm · b ${f1(ve.b_coroa)} mm · ×${N}`);
  const gm = composto ? grupo('planeta_menor', 'Planeta menor', `z ${vi.Z_pinhao} · m<sub>n</sub> ${vi.m_n} · d<sub>w</sub> ${f2(A(vi.dw_pinhao))} mm · b ${f1(vi.b_pinhao)} mm · ×${N}`) : null;
  for (let k = 0; k < N; k++) {
    const an = -Math.PI / 2 + k * 2 * Math.PI / N; const px = rc * Math.cos(an), py = rc * Math.sin(an);
    el('circle', { cx: px, cy: py, r: A(ve.d_a_coroa) / 2 * sc, class: 'wfill', fill: '#e8eef8', stroke: COR.planeta_maior, 'stroke-width': 1.4 }, gb);
    el('circle', { cx: px, cy: py, r: A(ve.dw_coroa) / 2 * sc, fill: 'none', stroke: COR.planeta_maior, 'stroke-width': .8, 'stroke-dasharray': '6 4', opacity: .7 }, gb);
    if (gm) {
      el('circle', { cx: px, cy: py, r: A(vi.d_a_pinhao) / 2 * sc, class: 'wfill', fill: '#d9f0f5', stroke: COR.planeta_menor, 'stroke-width': 1.6, 'stroke-dasharray': '4 3' }, gm);
      el('circle', { cx: px, cy: py, r: A(vi.dw_pinhao) / 2 * sc, fill: 'none', stroke: COR.planeta_menor, 'stroke-width': .8, 'stroke-dasharray': '6 4', opacity: .7 }, gm);
    }
    el('circle', { cx: px, cy: py, r: Math.max(2, A(ve.d_sh_coroa || 0) / 2 * sc), fill: '#fff', stroke: '#7c8792', 'pointer-events': 'none' }, g);
    // rótulos curtos no centro de cada planeta (o menor, mais abaixo): identificam a roda sem poluir o contorno
    const lh = Math.max(11, A(ve.d_a_coroa) / 2 * sc * 0.16);
    label(px, py - (gm ? 4 : -4), `${composto ? 'PM' : 'P'} z ${ve.Z_coroa}`, COR.planeta_maior);
    if (gm) label(px, py + lh + 2, `Pm z ${vi.Z_pinhao}`, COR.planeta_menor);
  }
  el('circle', { r: rc, fill: 'none', stroke: '#95999e', 'stroke-dasharray': '2 5', opacity: .6, 'pointer-events': 'none' }, g);

  // ---- sol
  const gs = grupo('sol', 'Sol', `z ${ve.Z_pinhao} · m<sub>n</sub> ${ve.m_n} · d<sub>w</sub> ${f2(A(ve.dw_pinhao))} mm · b ${f1(ve.b_pinhao)} mm`);
  el('circle', { r: A(ve.d_a_pinhao) / 2 * sc, class: 'wfill', fill: '#fbecec', stroke: COR.sol, 'stroke-width': 1.4 }, gs);
  el('circle', { r: A(ve.dw_pinhao) / 2 * sc, fill: 'none', stroke: COR.sol, 'stroke-width': .8, 'stroke-dasharray': '6 4', opacity: .7 }, gs);
  el('circle', { r: Math.max(2, A(ve.d_sh_pinhao || 0) / 2 * sc), fill: '#fff', stroke: '#7c8792', 'pointer-events': 'none' }, gs);
  label(0, 4, `Sol z ${ve.Z_pinhao}`, COR.sol);

  // ---- legenda clicável à esquerda + dados de cinemática
  const L = -cx + 14; let y = -cy + 52;
  const leg = (k, nome, txt) => { const r = el('g', { class: 'sch-hit legrow' + (sel === k ? ' sel' : '') + dim(k) }, g); r.addEventListener('click', () => onSelect && onSelect(k)); el('rect', { x: L - 4, y: y - 12, width: 192, height: 18, fill: 'transparent' }, r); el('circle', { cx: L + 5, cy: y - 3, r: 5, fill: COR[k] }, r); el('text', { x: L + 16, y, class: 'sch-label' }, r, `${nome}: ${txt}`); y += 20; };
  leg('sol', 'Sol', `z ${ve.Z_pinhao} · m ${ve.m_n}`);
  leg('planeta_maior', composto ? 'Planeta maior' : 'Planeta', `z ${ve.Z_coroa} · ×${N}`);
  if (composto) leg('planeta_menor', 'Planeta menor', `z ${vi.Z_pinhao} · m ${vi.m_n}`);
  leg('anelar', 'Anelar', `z ${A(vi.Z_coroa)} · m ${vi.m_n}`);
  y += 10;
  const row = (lab, val, col) => { el('text', { x: L, y, class: 'sch-label', style: `fill:${col}` }, g, lab); el('text', { x: L, y: y + 14, class: 'sch-value' }, g, val); y += 34; };
  if (cin) {
    row(`Entrada (${cin.entrada})`, `${f1(cin.n_membros[cin.entrada])} rpm · ${f1(cin.T_membros[cin.entrada])} N·m`, '#b8282c');
    row(`Saída (${cin.saida})`, `${f1(cin.n_membros[cin.saida])} rpm · ${f1(cin.T_membros[cin.saida])} N·m`, '#003882');
    if (cin.modo === 'diferencial') row(`Livre (${cin.membro_livre})`, `${f1(cin.n_membros[cin.membro_livre])} rpm · ${f1(cin.T_membros[cin.membro_livre])} N·m`, '#0e8aa6');
    else row(`Fixo (${cin.membro_fixo})`, `reação ${f1(cin.T_membros[cin.membro_fixo])} N·m`, '#1f7a34');
    row('Relação i', `${Number(cin.i).toFixed(3)}`, '#1f252b');
    row('Planeta (abs. / rel.)', `${f1(cin.n_pla)} / ${f1(cin.n_pla_rel)} rpm`, '#1f252b');
  }
}
