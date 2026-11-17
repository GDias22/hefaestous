// Fluxo do projeto (stepper): 1 Arquitetura → 2 Entrada → 3 Busca de dentes → 4 Rodas → 5 Layout → 6 Operação → 7 Análise → Saída
import { S, on, select, commit } from '../app.js';
import { wheels, minSeg, keyOfSel } from '../model/rodas.js';

const ICONS = {
  arq: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="7" height="7" rx="1.5"/><rect x="14" y="4" width="7" height="7" rx="1.5"/><rect x="8.5" y="14" width="7" height="7" rx="1.5"/><path d="M6.5 11v1.5h11V11M12 12.5V14"/></svg>',
  motor: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="7" width="13" height="10" rx="2"/><path d="M16 10h3l2 2-2 2h-3M6 7V5M10 7V5"/></svg>',
  search: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg>',
  axis: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12h20"/><rect x="8" y="5" width="3" height="14" rx="1"/><path d="M16 8v8M5 9v6M19 9v6"/></svg>',
  gear: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/></svg>',
  ring: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/></svg>',
  carrier: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="2"/><circle cx="12" cy="4.5" r="2"/><circle cx="18.5" cy="15.8" r="2"/><circle cx="5.5" cy="15.8" r="2"/><path d="M12 6.5v3.5M13.7 13l3.1 1.8M10.3 13l-3.1 1.8"/></svg>',
  cog: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h10M4 18h7"/></svg>',
  check: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 12l5 5L20 6"/></svg>',
  out: '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 12h12M12 6l6 6-6 6"/></svg>',
};
let root;
export function init() { root = document.getElementById('tree'); on(ev => { if (['load', 'result', 'select', 'change'].includes(ev.type)) render(); }); }

function statusOf(w) {
  const m = S.res && S.res.malhas && S.res.malhas[w.malha];
  if (!m || m.erro) return 'bad';
  if (!m.cards) return 'na';
  const mal = [m].concat(w.extra ? [S.res.malhas[w.extra.malha]] : []).filter(Boolean);
  const st = mal.flatMap(x => (x.cards || []).map(c => c.status));
  return st.includes('ruim') ? 'bad' : st.includes('atencao') ? 'warn' : st.length ? 'ok' : 'na';
}
function node({ kind, idx = 0, roda = null, icon, label, sub, status, child, num, cor, active }) {
  const d = document.createElement('div');
  const on_ = active !== undefined ? active : (S.sel.kind === kind && S.sel.idx === idx && (roda == null || S.sel.roda === roda));
  d.className = 'node' + (child ? ' child' : '') + (on_ ? ' on' : '');
  d.dataset.kind = kind; d.dataset.idx = idx; if (roda) d.dataset.roda = roda;
  d.innerHTML = `${num != null ? `<span class="num">${num}</span>` : ''}${cor ? `<i class="chip" style="background:${cor}"></i>` : (ICONS[icon] || '')}<span class="lbl">${label}${sub ? `<span class="sub">${sub}</span>` : ''}</span>${status ? `<span class="st ${status}"></span>` : ''}`;
  // mousedown (e não click): ao sair de um campo em edição o 'change' redesenha a árvore antes do click terminar e o clique se perderia
  d.addEventListener('mousedown', (e) => { if (e.button === 0) select(kind, idx, roda, 'tree'); });
  return d;
}
const step = (n, txt, go = null) => { const h = document.createElement('div'); h.className = 'stepno' + (go ? ' link' : ''); h.innerHTML = `<span>${n}</span>${txt}`; if (go) { h.title = 'Abrir a primeira roda'; h.addEventListener('mousedown', (e) => { if (e.button === 0) go(); }); } return h; };

function render() {
  if (!root || !S.proj) return;
  root.innerHTML = '';
  const p = S.proj, t = S.res && S.res.transmissao, pl = p.planetario;
  const fmt = (v, nd = 0) => (v == null ? '—' : Number(v).toLocaleString('pt-BR', { maximumFractionDigits: nd }));
  const arqSub = p.tipo === 'trem' ? `trem · ${p.estagios.length} estágio${p.estagios.length > 1 ? 's' : ''}` : `${pl.tipo.toLowerCase()} · ${pl.N_cp} planetas${pl.modo === 'diferencial' ? ' · diferencial' : ''}`;
  root.appendChild(node({ kind: 'arquitetura', icon: 'arq', num: 1, label: 'Arquitetura', sub: arqSub }));
  root.appendChild(node({ kind: 'entrada', icon: 'motor', num: 2, label: 'Entrada', sub: `${fmt(p.entrada.n)} rpm · ${fmt(p.entrada.T, 1)} N·m` }));
  root.appendChild(node({ kind: 'dentes', icon: 'search', num: 3, label: 'Busca de dentes', sub: t ? `i ${fmt(t.i_total, 3)}` : '' }));
  const ws = wheels(p);
  root.appendChild(step(4, 'Rodas', ws.length ? () => select(ws[0].kind, ws[0].idx, ws[0].roda, 'tree') : null));
  if (p.tipo === 'trem') {
    p.estagios.forEach((e, i) => {
      const h = document.createElement('div'); h.className = 'grp'; h.textContent = e.nome || `Estágio ${i + 1}`; root.appendChild(h);
      ws.filter(w => w.idx === i).forEach(w => root.appendChild(node({ kind: w.kind, idx: w.idx, roda: w.roda, cor: w.cor, child: true, label: w.base, sub: `z ${w.z}`, status: statusOf(w) })));
    });
  } else {
    ws.forEach(w => root.appendChild(node({ kind: w.kind, idx: 0, cor: w.cor, child: true, label: w.label, sub: `z ${w.z}${w.kind === 'planeta_maior' || w.kind === 'planeta_menor' ? ` · ×${pl.N_cp}` : ''}`, status: statusOf(w) })));
    root.appendChild(node({ kind: 'carrier', icon: 'carrier', child: true, label: 'Porta-planetas', sub: t && t.cinematica ? `${fmt(t.cinematica.n_c)} rpm` : '' }));
  }
  root.appendChild(node({ kind: 'layout', icon: 'axis', num: 5, label: 'Layout (eixos e mancais)', sub: (p.layout && p.layout.ativo) ? 'ativo' : 'inativo' }));
  root.appendChild(node({ kind: 'operacao', icon: 'cog', num: 6, label: 'Operação e materiais', sub: `${fmt(p.operacao && p.operacao.Vr)} h` }));
  root.appendChild(node({ kind: 'analise', icon: 'check', num: 7, label: 'Análise ISO 6336', sub: p.metodos ? `Y_F ${p.metodos.metodo_YF} · ${p.metodos.curva_vida}` : '' }));
  const out = p.tipo === 'trem' ? (t && t.eixos ? t.eixos[t.eixos.length - 1] : null) : (t && t.cinematica ? { n: t.cinematica.n_membros[t.cinematica.saida], T: t.cinematica.T_membros[t.cinematica.saida] } : null);
  const dev = (t && p.entrada.i_alvo) ? 100 * (Math.abs(t.i_total) - p.entrada.i_alvo) / p.entrada.i_alvo : null;
  root.appendChild(node({ kind: 'saida', icon: 'out', label: 'Saída', sub: out ? `${fmt(out.n)} rpm · ${fmt(out.T, 1)} N·m · i ${fmt(t.i_total, 2)}${dev != null ? ` (${dev >= 0 ? '+' : ''}${fmt(dev, 1)} %)` : ''}` : '' }));
}
