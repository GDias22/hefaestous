// Passo 1 — Arquitetura: família (trem / planetário simples / composto), N planetas, membros de entrada e saída.
// Painel central = escolha visual + diagrama + fórmula de i; campos = inspetor (renderInspector).
import { S, on, commit, novoProjeto, select, toast } from '../app.js';
import { field, block, adv } from './fields.js';
import { ensurePlanetas, COR } from '../model/rodas.js';

const NS = 'http://www.w3.org/2000/svg';
let pane = null;
export function init() { on(ev => { if (['load', 'result', 'change'].includes(ev.type) && pane && pane.classList.contains('on')) renderPane(pane); }); }

const MEM = { sol: 0, 'porta-planetas': 1, anelar: 2 };
const NOME = { sol: 'Sol', 'porta-planetas': 'Porta-planetas', anelar: 'Anelar' };
// i = n_entrada / n_saída para cada par (entrada, saída) — mesma tabela de speed_ratio() do Dim_cinematico.ipynb
const F_SIMPLES = { '0-2': 'z_r/z_s', '0-1': '(z_s+z_r)/z_s', '2-0': 'z_s/z_r', '2-1': '(z_s+z_r)/z_r', '1-0': 'z_s/(z_s+z_r)', '1-2': 'z_r/(z_s+z_r)' };
const F_COMPOSTO = { '0-2': '\\dfrac{z_{bp}\\,z_r}{z_{sp}\\,z_s}', '0-1': '\\dfrac{z_{sp}z_s+z_{bp}z_r}{z_s\\,z_{sp}}', '2-0': '\\dfrac{z_{sp}\\,z_s}{z_{bp}\\,z_r}', '2-1': '\\dfrac{z_{sp}z_s+z_{bp}z_r}{z_{bp}\\,z_r}', '1-0': '\\dfrac{z_{sp}\\,z_s}{z_{sp}z_s+z_r z_{bp}}', '1-2': '\\dfrac{z_{bp}\\,z_r}{z_{bp}z_r+z_{sp}z_s}' };
const el = (t, a = {}, p = null, txt = null) => { const e = document.createElementNS(NS, t); for (const k in a) if (a[k] != null) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; if (p) p.appendChild(e); return e; };
const f = (v, n = 3) => (v == null || !isFinite(v) ? '—' : Number(v).toLocaleString('pt-BR', { maximumFractionDigits: n }));

export function fixoDe(pl) { return ['sol', 'porta-planetas', 'anelar'].find(m => m !== pl.entrada && m !== pl.saida); }
const difer = (pl) => pl.modo === 'diferencial';
/** Aviso didático sobre a anelar no K_v (fator dinâmico), em função do que gira. */
export function avisoRing(pl, cin) {
  const fixo = fixoDe(pl), ring = cin ? cin.ring : (fixo === 'anelar' && !difer(pl) ? 'Fixo' : 'Rotativo');
  const txt = ring === 'Fixo'
    ? `<b>Anelar presa à carcaça (Ring = Fixo):</b> no fator dinâmico K_v a anelar entra com massa infinita — só as inércias do sol e dos ${pl.N_cp} planetas definem as frequências de ressonância n_E1 (malha externa) e n_E2 (malha interna). É o caso da ISO 6336-1 para planetário com anelar fixa.`
    : `<b>Anelar girando (Ring = Rotativo):</b> o conjunto é tratado como um trem com roda intermediária (ISO 6336-1 §6, "engrenagem intermediária"): a inércia da anelar entra no sistema e as duas frequências de ressonância saem das raízes do sistema de 2 graus de liberdade (B e C na fórmula do caderno). Isso muda n_E, a zona de operação e K_v das duas malhas.`;
  const nota = ring === 'Fixo' ? '' : ' <span class="muted">A estrutura segue a norma; a calibração numérica de n_E com a anelar girando ainda não foi validada contra uma referência externa (o caso KISSsoft "alef" mostra desvios em n_E e nas rigidezes).</span>';
  return `<div class="alert ${ring === 'Fixo' ? 'ok' : 'aviso'} ring-aviso"><span class="ic">${ring === 'Fixo' ? 'i' : '!'}</span><span>${txt}${nota}</span></div>`;
}

/** Planetário simples exige z_r = z_s + 2 z_p e módulo/ângulo iguais nas duas malhas. */
function ajustarSimples(pl) {
  const zs = Number(pl.sol.z) || 15; let zp = Math.round(((Number(pl.anelar.z) || 69) - zs) / 2); if (zp < 6) zp = 6;
  pl.planeta_maior.z = zp; pl.anelar.z = zs + 2 * zp;
  pl.malha_ext = { ...pl.malha_ext, a: null, x_pinhao: 0.0, tipo: 'Otimização' };
  pl.malha_int = { ...pl.malha_int, m_n: pl.malha_ext.m_n, alpha_n: pl.malha_ext.alpha_n, beta: pl.malha_ext.beta, a: null, x_pinhao: 0.0, tipo: 'Otimização' };
}
export async function escolherFamilia(op) {      // 'trem' | 'Simples' | 'Composto'
  const p = S.proj; const atual = p.tipo === 'trem' ? 'trem' : p.planetario.tipo;
  if (op === atual) return;
  if ((op === 'trem') !== (p.tipo === 'trem')) {
    if (!confirm(`Trocar para ${op === 'trem' ? 'trem de engrenagens' : 'planetário'}? O projeto atual será substituído por um modelo padrão (o atual fica no histórico de desfazer).`)) return;
    const nome = p.nome; await novoProjeto(op === 'trem' ? 'trem' : 'planetario', nome);
    if (op === 'trem') return;
  }
  const pl = S.proj.planetario; if (pl.tipo === op) return;
  const cp = (o) => JSON.parse(JSON.stringify(o));
  const CAMPOS = ['sol', 'planeta_maior', 'planeta_menor', 'anelar', 'malha_ext', 'malha_int'];
  if (op === 'Simples') {                         // guarda o composto para restaurá-lo se o usuário voltar
    S.stash = S.stash || {}; S.stash.Composto = Object.fromEntries(CAMPOS.map(k => [k, cp(pl[k])]));
    pl.tipo = op; ajustarSimples(pl);
  } else {
    pl.tipo = op;
    const sv = S.stash && S.stash.Composto;
    if (sv) { CAMPOS.forEach(k => { pl[k] = cp(sv[k]); }); S.stash.Composto = null; } else ensurePlanetas(pl);
  }
  commit('tipo do planetário'); select('arquitetura');
  if (op === 'Simples') toast('Simples: z_anelar = z_sol + 2·z_planeta e mesmo módulo nas duas malhas; use "Busca de dentes" para buscar combinações.', false, 6000);
}

// ---------------------------------------------------------------- painel central
export function renderPane(p) {
  pane = p; if (!S.proj) return;
  const pr = S.proj, pl = pr.planetario, t = S.res && S.res.transmissao;
  const atual = pr.tipo === 'trem' ? 'trem' : pl.tipo;
  p.innerHTML = '';
  const body = document.createElement('div'); body.className = 'body arq'; p.appendChild(body);
  const h = document.createElement('div'); h.className = 'arq-h';
  h.innerHTML = '<h2>1 · Arquitetura da transmissão</h2><p class="muted">Escolha o tipo de transmissão antes de tudo: ele define quais rodas existem, como a potência flui e quais condições de montagem valem.</p>';
  body.appendChild(h);
  const cards = document.createElement('div'); cards.className = 'arq-cards'; body.appendChild(cards);
  [['trem', 'Trem de engrenagens', 'N estágios pinhão × coroa em série (par externo ou interno). Cada estágio herda n e T do anterior.', null],
   ['Simples', 'Planetário simples (tipo A)', 'Sol, planetas, anelar e porta-planetas. O planeta engrena com o sol e com a anelar (mesmo módulo).', 'Simple_Epicyclic.png'],
   ['Composto', 'Planetário composto (tipo B)', 'Planeta duplo: o maior engrena com o sol e o menor com a anelar. Duas rodas configuráveis, módulos independentes.', 'Compound_Epicyclic.png']].forEach(([k, t1, d, fig]) => {
    const c = document.createElement('div'); c.className = 'arq-card' + (k === atual ? ' on' : ''); c.dataset.op = k;
    c.innerHTML = `${fig ? `<img src="/api/figuras/${fig}" alt="">` : '<div class="arq-ico">' + trenIcone() + '</div>'}<b>${t1}</b><span>${d}</span>`;
    c.addEventListener('mousedown', (e) => { if (e.button === 0) escolherFamilia(k); }); cards.appendChild(c);   // mousedown: o 'change' de um campo em edição redesenha o painel antes do click
  });
  const dg = document.createElement('div'); dg.className = 'arq-diag'; body.appendChild(dg);
  if (pr.tipo === 'trem') desenharTrem(dg, pr, t); else desenharPlanetario(dg, pl, t);
  if (window.renderMathInElement) window.renderMathInElement(dg, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false });
}
/** Corte lateral de um trem de 2 estágios, na mesma linguagem das figuras de corte dos planetários: eixos, mancais, rodas dentadas e fluxo de potência. */
function trenIcone() {
  const C1 = '#b8282c', C2 = '#003882', K = '#1f252b', G = '#e9ecef';
  const Y1 = 30, Y2 = 84;                                   // linha de centro do eixo 1 (entrada) e do eixo 2 (intermediário)
  const dentes = (x, w, y, r0, r1, cor) => [0.18, 0.39, 0.61, 0.82].map(f => `<line x1="${x + w * f}" x2="${x + w * f}" y1="${y + r0}" y2="${y + r1}" stroke="${cor}" stroke-width=".7"/>`).join('');
  // roda em corte: alma (cinza) + coroa dentada (cor), simétrica em relação ao eixo; ra = raio de cabeça, rf = raio de pé
  const roda = (x, w, cy, ra, rf, cor) =>
    `<rect x="${x}" y="${cy - rf}" width="${w}" height="${2 * rf}" fill="#f4f6f9" stroke="${K}" stroke-width=".8"/>` +
    [-1, 1].map(sg => `<rect x="${x}" y="${sg < 0 ? cy - ra : cy + rf}" width="${w}" height="${ra - rf}" fill="${cor}30" stroke="${cor}" stroke-width="1.3"/>` + dentes(x, w, cy, sg * rf, sg * ra, cor)).join('');
  const mancal = (x, cy) => `<rect x="${x - 3.5}" y="${cy - 11}" width="7" height="22" rx="1.5" fill="#fff" stroke="${K}" stroke-width="1.1"/><path d="M${x - 7} ${cy + 18} h14 l-7 -7 z" fill="${G}" stroke="${K}" stroke-width=".9"/>`;
  const seta = (x, y, d) => `<path d="M${x} ${y} h${14 * d} m${-4 * d} -3.5 l${4 * d} 3.5 l${-4 * d} 3.5" fill="none" stroke="${C1}" stroke-width="1.6"/>`;
  const t = (x, y, txt, cor = '#4b5560', w = 600, a = 'middle') => `<text x="${x}" y="${y}" text-anchor="${a}" font-size="8" fill="${cor}" font-weight="${w}">${txt}</text>`;
  return `<svg viewBox="0 0 270 150" role="img" aria-label="Trem de dois estágios em corte lateral">
    <rect x="28" y="${Y1 - 3.5}" width="132" height="7" fill="${G}" stroke="${K}" stroke-width=".9"/>
    <rect x="62" y="${Y2 - 3.5}" width="180" height="7" fill="${G}" stroke="${K}" stroke-width=".9"/>
    ${mancal(44, Y1)}${mancal(146, Y1)}${mancal(72, Y2)}${mancal(230, Y2)}
    ${roda(90, 16, Y1, 13, 9, C1)}${roda(90, 16, Y2, 28, 24, C2)}
    ${roda(158, 20, Y2, 13, 9, C1)}
    ${seta(8, Y1, 1)}${seta(262, Y2, -1)}
    ${t(98, Y1 - 19, 'pinhão 1', C1)}${t(98, Y2 + 44, 'coroa 1', C2)}${t(168, Y2 - 19, 'pinhão 2', C1)}${t(168, Y2 + 24, 'coroa 2', C2)}
    ${t(8, 14, 'entrada (n, T)', '#4b5560', 600, 'start')}${t(262, Y2 - 12, 'saída', '#4b5560', 600, 'end')}
    ${t(44, Y1 + 34, 'mancal', '#4b5560', 500)}
    ${t(135, 143, 'cada estágio: i = z₂/z₁ · rotação cai, torque sobe', '#4b5560', 500)}
  </svg>`;
}
function desenharTrem(host, pr, t) {
  const n = pr.estagios.length, BW = 156, GAP = 40, STEP = BW + GAP;
  host.innerHTML = `<h3>Fluxo de potência</h3>`;
  const svg = el('svg', { viewBox: `0 0 ${20 + (n + 2) * STEP - GAP} 90`, class: 'arq-svg', style: `max-width:${Math.min(980, 120 + (n + 2) * 200)}px` }, host);
  const box = (x, label, sub, col) => { el('rect', { x, y: 14, width: BW, height: 62, rx: 8, fill: '#fff', stroke: col, 'stroke-width': 2 }, svg); el('text', { x: x + BW / 2, y: 38, 'text-anchor': 'middle', class: 'sch-title' }, svg, label); el('text', { x: x + BW / 2, y: 58, 'text-anchor': 'middle', class: 'sch-value' }, svg, sub); };
  const arrow = (x) => el('path', { d: `M ${x + 4} 45 h ${GAP - 12} m -7 -5 l 7 5 l -7 5`, stroke: '#7c8792', 'stroke-width': 1.6, fill: 'none' }, svg);
  const e = t && t.eixos;
  box(10, 'Entrada', e ? `${f(e[0].n, 0)} rpm · ${f(e[0].T, 1)} N·m` : '', COR.pinhao);
  pr.estagios.forEach((s, i) => { const x = 10 + (i + 1) * STEP; arrow(x - GAP); const m = s.malha || {}; box(x, s.nome || `Estágio ${i + 1}`, `z ${Math.abs(m.Z_pinhao)}/${Math.abs(m.Z_coroa)}${m.Z_coroa < 0 ? ' · interna' : ''}`, m.Z_coroa < 0 ? COR.interna : COR.coroa); });
  const xs = 10 + (n + 1) * STEP; arrow(xs - GAP); box(xs, 'Saída', e ? `${f(e[e.length - 1].n, 0)} rpm · ${f(e[e.length - 1].T, 1)} N·m` : '', COR.coroa);
  const i = document.createElement('p'); i.className = 'muted'; i.style.marginTop = '10px';
  i.innerHTML = `Em série, <i>i</i><sub>total</sub> = Π <i>i</i><sub>k</sub>, com <i>i</i> = z₂/z₁ por estágio.`;
  host.appendChild(i);
  const alvo = document.createElement('div'); alvo.className = 'arq-alvo'; alvoReducao(alvo, 'arquitetura'); host.appendChild(alvo);
}

/** Define quem recebe (entrada) e quem entrega (saída) o torque; o terceiro membro fica fixo (ou livre, no diferencial). Trocar
 *  um papel para um membro que já tinha o outro papel troca os dois (nunca deixa entrada = saída). */
export function definirPapel(pl, membro, papel, voltar = 'entrada') {
  const outro = papel === 'entrada' ? 'saida' : 'entrada';
  if (pl[papel] === membro) return;
  if (pl[outro] === membro) pl[outro] = pl[papel];
  pl[papel] = membro;
  commit(`membro de ${papel}`); select(voltar);
}
function desenharPlanetario(host, pl, t) {
  host.innerHTML = '<h3>Fluxo de torque — quem recebe e quem entrega</h3>';
  cartaoFluxo(host, 'arquitetura');
  const alvo = document.createElement('div'); alvo.className = 'arq-alvo'; alvoReducao(alvo, 'arquitetura'); host.appendChild(alvo);
}
/** Redução alvo e tolerância (entrada.i_alvo / tol_i), editáveis no painel central; comparadas com a redução atual. */
export function alvoReducao(host, voltar = 'arquitetura') {
  const e = S.proj.entrada, t = S.res && S.res.transmissao, cur = t ? Math.abs(t.i_total) : null;
  const dev = (e.i_alvo && cur != null) ? 100 * (cur - e.i_alvo) / e.i_alvo : null;
  const ok = dev != null && Math.abs(cur - e.i_alvo) <= (e.tol_i ?? 0.5);
  host.innerHTML = `<h3>Redução alvo</h3><div class="arq-alvo-row">
    <label>Redução desejada <i>i</i><sub>alvo</sub> <input class="i-alvo" type="number" step="0.01" min="1.01" value="${e.i_alvo ?? ''}" placeholder="ex.: 11,5"></label>
    <label>Tolerância ± <input class="tol-i" type="number" step="0.05" min="0" value="${e.tol_i ?? 0.5}"></label>
    <span class="arq-cmp ${dev == null ? '' : ok ? 'ok' : 'bad'}">atual <b class="mono">${cur != null ? f(cur, 4) : '—'}</b>${dev != null ? ` · desvio <b class="mono">${dev >= 0 ? '+' : ''}${f(dev, 2)} %</b> ${ok ? '✓ dentro da tolerância' : '✕ fora da tolerância'}` : ''}</span></div>
    <p class="muted small">A redução alvo alimenta a busca de dentes (etapa 3)${S.proj.tipo === 'trem' ? ' e é a redução total dos estágios em série' : ''}.</p>`;
  const upd = (k, el) => { const v = el.value === '' ? null : Number(el.value); if (v === e[k] || (v != null && !isFinite(v))) return; e[k] = v; commit('redução alvo'); select(voltar); };
  host.querySelector('.i-alvo').addEventListener('change', (ev) => upd('i_alvo', ev.target));
  host.querySelector('.tol-i').addEventListener('change', (ev) => upd('tol_i', ev.target));
}

/** Campos do modo de operação (membro fixo / diferencial) e da rotação do membro livre. */
export function camposModo(root, voltar = 'arquitetura') {
  const pl = S.proj.planetario, fixo = fixoDe(pl);
  root.appendChild(field('planetario.modo', { type: 'choice', choices: ['fixo', 'diferencial'], labels: { fixo: 'membro fixo (3º membro preso à carcaça)', diferencial: 'diferencial (3º membro gira, rotação imposta)' }, label: 'Modo de operação', key: 'modo', docKey: 'planetario', help: 'Fixo: o terceiro membro (nem entrada nem saída) é preso à carcaça e a relação i é fixa. Diferencial: o terceiro membro também gira, com rotação imposta por outro acionamento (2 graus de liberdade, como num diferencial ou somador de velocidades); i passa a depender dessa rotação. A anelar entra como "Rotativo" no K_v sempre que gira.', onChange: () => setTimeout(() => select(voltar), 0) }));
  if (difer(pl)) root.appendChild(field('planetario.n_livre', { type: 'number', unit: 'rpm', label: `Rotação do membro livre (${NOME[fixo]})`, key: 'n_livre', docKey: 'planetario', help: 'Rotação absoluta imposta ao terceiro membro, com sinal (sol positivo). Zero equivale ao modo de membro fixo.' }));
}
/** Cartão de fluxo de torque (etapa "Entrada e saída"): ENTRADA ▾ → SAÍDA ▾ · terceiro membro, relação i e aviso do Ring. */
export function cartaoFluxo(root, voltar = 'arquitetura') {
  const pl = S.proj.planetario, t = S.res && S.res.transmissao, cin = t && t.cinematica, fixo = fixoDe(pl);
  const ti = MEM[pl.entrada], to = MEM[pl.saida];
  const card = document.createElement('div'); card.className = 'arq-fluxo arq-membros';
  const seletor = (papel, atual, col) => {
    const ops = ['sol', 'porta-planetas', 'anelar'].map(m => `<option value="${m}"${m === atual ? ' selected' : ''}>${NOME[m]}</option>`).join('');
    return `<div class="arq-m ${papel}" data-m="${atual}" style="border-color:${col}"><span class="rot" style="color:${col}">${papel === 'entrada' ? 'ENTRADA · torque do motor' : 'SAÍDA · torque para a carga'}</span>` +
      `<select class="sel-${papel}" title="${papel === 'entrada' ? 'Membro que recebe o torque do motor' : 'Membro que entrega o torque à carga'}">${ops}</select>` +
      `<span class="rpm">${cin ? `${f(cin.n_membros[atual], 0)} rpm · ${f(cin.T_membros[atual], 1)} N·m` : '&nbsp;'}</span></div>`;
  };
  const fcol = difer(pl) ? '#0e8aa6' : '#7c8792';
  card.innerHTML = seletor('entrada', pl.entrada, COR.sol) + '<span class="arq-seta">→</span>' + seletor('saida', pl.saida, COR.coroa) +
    `<div class="arq-m terceiro" data-m="${fixo}" style="border-color:${fcol}"><span class="rot" style="color:${fcol}">${difer(pl) ? 'LIVRE · rotação imposta' : 'FIXO · preso à carcaça'}</span><b>${NOME[fixo]}</b><span class="rpm">${cin ? `${f(cin.n_membros[fixo], 0)} rpm · ${f(cin.T_membros[fixo], 1)} N·m` : '&nbsp;'}</span></div>`;
  card.querySelector('.sel-entrada').addEventListener('change', (e) => definirPapel(pl, e.target.value, 'entrada', voltar));
  card.querySelector('.sel-saida').addEventListener('change', (e) => definirPapel(pl, e.target.value, 'saida', voltar));
  root.appendChild(card);
  const mid = document.createElement('p'); mid.className = 'muted small'; mid.style.margin = '6px 0 0';
  mid.textContent = difer(pl) ? `O terceiro membro (${NOME[fixo]}) gira com a rotação imposta de ${f(pl.n_livre, 0)} rpm.` : 'O terceiro membro, nem entrada nem saída, fica preso à carcaça. Escolher para a saída o membro que era a entrada troca os dois.';
  root.appendChild(mid);
  const fm = pl.tipo === 'Composto' ? F_COMPOSTO[`${ti}-${to}`] : F_SIMPLES[`${ti}-${to}`];
  const d = document.createElement('div'); d.className = 'arq-formula';
  d.innerHTML = ti === to ? '<div class="alert erro"><span class="ic">✕</span><span>Entrada e saída devem ser membros diferentes.</span></div>'
    : difer(pl)
      ? `<div class="muted small">Modo <b>diferencial</b> (2 graus de liberdade): <b>${NOME[pl.entrada]}</b> entra, <b>${NOME[fixo]}</b> gira a ${f(pl.n_livre, 0)} rpm (imposto), <b>${NOME[pl.saida]}</b> sai. Equação de Willis:</div>$$ n_{sol}-n_{c} = -k\\,(n_{anel}-n_{c}),\\qquad k=\\frac{z_r\\,z_{bp}}{z_s\\,z_{sp}} $$<div class="muted small">A relação i = n_entrada/n_saída deixa de ser fixa: depende da rotação do membro livre. Os torques seguem a estática (T_c = (1+k)·T_s, T_anel = k·T_s).</div><div class="muted">Relação atual i: <b class="mono">${cin ? f(cin.i, 4) : '—'}</b> · ${pl.N_cp} planetas</div>`
      : `<div class="muted small">Relação de velocidades para <b>${NOME[pl.entrada]}</b> → <b>${NOME[pl.saida]}</b> (membro fixo: <b>${NOME[fixo]}</b>), AGMA 6123:</div>$$ i=\\frac{n_{\\text{entrada}}}{n_{\\text{saída}}}=${fm} $$
       <div class="muted">Valor atual: <b class="mono">${cin ? f(cin.i, 4) : '—'}</b>${S.proj.entrada.i_alvo ? ` · alvo <b class="mono">${f(S.proj.entrada.i_alvo, 3)}</b> (±${f(S.proj.entrada.tol_i ?? 0.5, 2)})` : ''} · ${pl.N_cp} planetas</div>`;
  root.appendChild(d);
  const ra = document.createElement('div'); ra.className = 'arq-ring'; ra.innerHTML = avisoRing(pl, cin); root.appendChild(ra);
  if (window.renderMathInElement) window.renderMathInElement(d, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false });
}

// ---------------------------------------------------------------- inspetor
export function renderInspector(root) {
  const p = S.proj, M = (k) => S.meta.params[k];
  if (p.tipo === 'planetario') {
    const pl = p.planetario, fixo = fixoDe(pl);
    const b = block('Planetário');
    b.appendChild(field('planetario.N_cp', { meta: M('N_cp'), key: 'N_cp' }));
    b.appendChild(field('planetario.entrada', { type: 'choice', choices: ['sol', 'porta-planetas', 'anelar'], label: 'Membro de ENTRADA (recebe o torque do motor)', help: 'Quem recebe o torque do motor. O terceiro membro (nem entrada nem saída) fica fixo à carcaça.', key: 'entrada', docKey: 'planetario' }));
    b.appendChild(field('planetario.saida', { type: 'choice', choices: ['sol', 'porta-planetas', 'anelar'], label: 'Membro de SAÍDA (entrega o torque à roda)', help: 'Quem entrega o torque modificado à carga.', key: 'saida', docKey: 'planetario' }));
    camposModo(b, 'arquitetura');
    const info = document.createElement('div'); info.className = 'small muted'; info.style.margin = '6px 0';
    info.innerHTML = pl.entrada === pl.saida ? '<span style="color:var(--bad)">Entrada e saída devem ser diferentes.</span>' : (difer(pl) ? `Membro livre: <b>${NOME[fixo]}</b> a ${f(pl.n_livre, 0)} rpm` : `Membro fixo (deduzido): <b>${NOME[fixo]}</b>`);
    b.appendChild(info);
    b.appendChild(adv('Avançado', [field('planetario.Ky', { meta: M('Ky'), key: 'Ky' })]));
    root.appendChild(b);
  } else {
    const b = block('Estágios', p.estagios.length);
    p.estagios.forEach((e, i) => {
      const row = document.createElement('div'); row.className = 'fld'; row.dataset.path = `estagios[${i}]`;
      const m = e.malha || {}; const interna = m.Z_coroa < 0;
      row.innerHTML = `<label><span class="t">${e.nome || `Estágio ${i + 1}`} · z ${Math.abs(m.Z_pinhao)}/${Math.abs(m.Z_coroa)}</span></label><div class="ctl" style="gap:8px"><label class="small" style="display:flex;gap:4px;align-items:center"><input type="checkbox" ${interna ? 'checked' : ''} style="width:auto"> interna</label><button class="btn xs">✕</button></div>`;
      row.querySelector('input').addEventListener('change', (ev) => {
        const z = Math.abs(m.Z_coroa); m.Z_coroa = ev.target.checked ? -z : z; if (m.a != null) m.a = ev.target.checked ? -Math.abs(m.a) : Math.abs(m.a);
        commit('interno'); select('arquitetura');
      });
      row.querySelector('button').addEventListener('click', () => { if (p.estagios.length > 1 && confirm(`Remover ${e.nome || 'estágio ' + (i + 1)}?`)) { p.estagios.splice(i, 1); commit('remover estágio'); select('arquitetura'); } });
      b.appendChild(row);
    });
    const add = document.createElement('button'); add.className = 'btn sm blue'; add.textContent = '+ adicionar estágio'; add.style.marginTop = '8px';
    add.addEventListener('click', () => { const last = p.estagios[p.estagios.length - 1]; const novo = JSON.parse(JSON.stringify(last)); novo.nome = `Estágio ${p.estagios.length + 1}`; p.estagios.push(novo); commit('adicionar estágio'); select('arquitetura'); });
    b.appendChild(add);
    const nt = document.createElement('p'); nt.className = 'small muted'; nt.style.marginTop = '8px'; nt.textContent = 'O estágio i recebe n e T do estágio i−1 (n/|u|, T·|u|·η). Os números de dentes vêm do passo "Busca de dentes".';
    b.appendChild(nt); root.appendChild(b);
  }
}
