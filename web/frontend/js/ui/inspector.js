// Inspetor: edita o item selecionado (essenciais na frente, avançado por tema), com erros inline vindos do backend
import { S, on, getPath, setPath, commit, select } from '../app.js';
import { field, subobject, applyErrors, block, adv } from './fields.js';
import * as Arq from './arquitetura.js';
import * as Busca from './busca.js';
import * as Layout from './layout.js';
import { wheelByKey, keyOfSel, selInfo, wheels, COR } from '../model/rodas.js';

let root, title, sub;
export function init() {
  root = document.getElementById('inspector'); title = document.getElementById('insp-title'); sub = document.getElementById('insp-sub');
  on(ev => {
    if (ev.type === 'select') { if (ev.src === 'inspector') marcarRoda(); else render(); }
    else if (ev.type === 'load') render();
    else if (ev.type === 'result') { applyErrors(root, (S.res && S.res.erros) || {}); if (['carrier', 'saida', 'arquitetura'].includes(S.sel.kind) && !root.contains(document.activeElement)) render(); }   // painéis só de leitura (cinemática) acompanham o novo resultado
    else if (ev.type === 'change' && ['remover estágio', 'adicionar estágio', 'tipo do planetário', 'interno'].includes(ev.label)) render();
  });
}
const M = (k) => S.meta.params[k];
// metadata de campo de roda (sem sufixo): usa a versão _pinhao do metadata
const MR = (b) => { const pair = S.vocab.roda[b]; return pair ? M(pair[0]) : null; };

const docOf = { m_n: 'modulo', alpha_n: 'angulo_pressao', beta: 'angulo_helice', a: 'distancia_centros', x_pinhao: 'desloc_perfil', Z_pinhao: 'numero_dentes', Z_coroa: 'numero_dentes',
  b: 'largura', IQ: 'qualidade', op_acabamento: 'qualidade', Ra_flanco: 'qualidade', afastamento: 'espessura', tol: 'espessura', f_chanfro: 'chanfro', crwon_s: 'K_Hbeta', di: 'aro', d_sh: 'eixo', Arranjo: 'arranjo', Vr: 'vida', T_op: 'temperatura', S_Hmin: 'seguranca', S_Fmin: 'seguranca' };

/** Campo de roda: path = `${base}.${campo}`, metadata da versão _pinhao. */
function rf(base, campo, extra = {}) {
  const meta = MR(campo); if (!meta) return null;
  const m = Object.assign({}, meta, extra); m.label = m.label.replace(/ do pinhão| da coroa| pinhão| coroa/g, '').replace(/ b₁| b₂| d_i| b_s| d_sh| l| s$/g, (s) => s);
  return field(`${base}.${campo}`, { meta: m, key: campo, docKey: docOf[campo] });
}
function roda(base, nome, { material = true, ferramenta = true, interna = false, wkey = null, cor = '#7c8792', z = null } = {}) {
  const ess = [rf(base, 'b', { label: 'Largura do dente b', unit: 'mm' }), rf(base, 'IQ', { label: 'Qualidade ISO 1328' }), rf(base, 'op_acabamento', { label: 'Acabamento' })].filter(Boolean);
  const subs = [];
  if (material) subs.push(subobject(`${base}.material`, 'material', 'Material'));
  if (ferramenta) subs.push(subobject(`${base}.ferramenta`, 'ferramenta', 'Ferramenta'));
  const g = {
    'Acabamento e rugosidade': ['Ra_flanco', 'Ra_pe', 'S_M'],
    'Tolerâncias DIN 3967': ['afastamento', 'tol', 'ASNE_min', 'ASNE_max'],
    'Modificações do dente': ['f_chanfro', 'crwon_s', 'crwon_i', 'f_b'],
    'Corpo, eixo e mancais': ['Arranjo', 'k_linha', 'di', 'bs', 'd_sh', 'L', 'sh'],
    'Controle dimensional': ['k_otimi', 'Dim_sobre_pinos'],
  };
  const advs = Object.entries(g).map(([t, ks]) => adv(t, ks.map(k => rf(base, k, k === 'di' && interna ? { label: 'Diâmetro externo do aro (negativo)', help: 'Para a anelar, informe o diâmetro EXTERNO do aro com sinal negativo (ex.: −115). Define a espessura de aro para Y_B e a inércia em K_v.' } : {})).filter(Boolean)));
  const wrap = document.createElement('details'); wrap.className = 'wheelbox'; wrap.style.setProperty('--wc', cor); if (wkey) wrap.dataset.wkey = wkey;
  wrap.open = !wkey || keyOfSel(S.sel) === wkey;
  const sm = document.createElement('summary'); sm.innerHTML = `<i class="chip" style="background:${cor}"></i><b>${nome}</b>${z != null ? `<span class="muted small">z ${z}</span>` : ''}<span class="sel-tag">editando</span>`; wrap.appendChild(sm);
  const inner = document.createElement('div'); inner.className = 'wb'; wrap.appendChild(inner);
  ess.forEach(e => inner.appendChild(e)); subs.forEach(s => inner.appendChild(s)); advs.forEach(a => inner.appendChild(a));
  const imp = wkey ? Layout.camposImpostos(wkey) : [];
  if (imp.length) {                     // layout ativo: d_sh, L, s, arranjo (e furo do planeta) vêm do passo Layout
    const KMAP = { d_sh: 'd_sh', L: 'L', sh: 'sh', Arranjo: 'Arranjo', k_linha: 'k_linha', di: 'di' };
    inner.querySelectorAll('.fld').forEach(f => { const campo = (f.dataset.path || '').split('.').pop(); if (imp.includes(KMAP[campo])) { f.classList.add('locked'); f.querySelectorAll('input,select').forEach(i => { i.disabled = true; }); f.title = 'Definido no passo Layout (eixos e mancais)'; } });
    const n = document.createElement('div'); n.className = 'alert ok link'; n.style.margin = '6px 0';
    n.innerHTML = '<span class="ic">i</span><span>Eixo, vão entre mancais, s e arranjo vêm do <b>Layout</b> (campos cinza). Clique para editar.</span>';
    n.addEventListener('click', () => select('layout')); inner.insertBefore(n, inner.firstChild);
  }
  if (wkey) {
    const pick = () => { const w = wheelByKey(wkey); if (w && keyOfSel(S.sel) !== wkey) select(w.kind, w.idx, w.roda, 'inspector'); };
    wrap.addEventListener('focusin', pick); sm.addEventListener('click', () => setTimeout(() => { if (wrap.open) pick(); }, 0));
  }
  return wrap;
}
/** Abre só o bloco da roda selecionada e destaca-o (chamado quando a seleção vem do esquema/inspetor sem recriar o inspetor). */
function marcarRoda() {
  const k = keyOfSel(S.sel);
  root.querySelectorAll('details.wheelbox').forEach(d => { const on_ = d.dataset.wkey === k; d.classList.toggle('on', on_); if (on_) d.open = true; });
  const i = selInfo(); title.innerHTML = i.cor ? `<i class="chip" style="background:${i.cor}"></i>${i.titulo}` : i.titulo;
}
function malha(base, { interna = null, zEditavel = true, aAuto = true } = {}) {
  const items = [];
  const z1 = M('Z_pinhao'), z2 = M('Z_coroa');
  items.push(field(`${base}.m_n`, { meta: M('m_n'), docKey: 'modulo' }));
  if (zEditavel) {
    items.push(field(`${base}.Z_pinhao`, { meta: Object.assign({}, z1, { label: 'Dentes do pinhão z₁' }), docKey: 'numero_dentes' }));
    const fz2 = field(`${base}.Z_coroa`, { meta: Object.assign({}, z2, { label: 'Dentes da coroa z₂', help: z2.help }), docKey: 'numero_dentes', onChange: (v) => { const a = getPath(S.proj, `${base}.a`); if (a != null && v != null && Math.sign(a) !== Math.sign(v)) setPath(S.proj, `${base}.a`, -a); } });
    items.push(fz2);
    const interno = document.createElement('div'); interno.className = 'fld';
    const cur = getPath(S.proj, `${base}.Z_coroa`);
    interno.innerHTML = `<label><span class="t">Engrenagem interna (anelar)</span></label><div class="ctl"><input type="checkbox" ${cur < 0 ? 'checked' : ''}></div>`;
    interno.querySelector('input').addEventListener('change', (e) => { const z = getPath(S.proj, `${base}.Z_coroa`); setPath(S.proj, `${base}.Z_coroa`, e.target.checked ? -Math.abs(z) : Math.abs(z)); const a = getPath(S.proj, `${base}.a`); if (a != null) setPath(S.proj, `${base}.a`, e.target.checked ? -Math.abs(a) : Math.abs(a)); commit('interno'); render(); });
    items.push(interno);
  }
  items.push(field(`${base}.a`, { meta: Object.assign({}, M('a'), { nullable: true }), auto: aAuto ? 'padrão (sem Σx)' : undefined, docKey: 'distancia_centros' }));
  items.push(field(`${base}.alpha_n`, { meta: M('alpha_n'), docKey: 'angulo_pressao' }));
  items.push(field(`${base}.beta`, { meta: M('beta'), docKey: 'angulo_helice' }));
  items.push(field(`${base}.x_pinhao`, { meta: Object.assign({}, M('x_pinhao'), { nullable: true }), auto: 'automático (DIN)', docKey: 'desloc_perfil', onChange: (v) => { setPath(S.proj, `${base}.tipo`, v == null ? 'Inicial' : 'Otimização'); } }));
  return items;
}

function setTitle(t, sb) { const i = selInfo(); title.innerHTML = i.cor ? `<i class="chip" style="background:${i.cor}"></i>${t}` : t; sub.textContent = sb || ''; }

function render() {
  if (!root || !S.proj) return;
  root.innerHTML = '';
  const { kind, idx } = S.sel; const p = S.proj; const E = (k) => M(k);
  const pl = p.planetario;
  if (kind === 'arquitetura') {
    setTitle('1 · Arquitetura', p.tipo === 'trem' ? 'trem de engrenagens' : `planetário ${pl.tipo.toLowerCase()}`);
    Arq.renderInspector(root);
  } else if (kind === 'dentes') {
    setTitle('3 · Dentes', 'busca de números de dentes');
    Busca.renderInspector(root);
  } else if (kind === 'layout') {
    setTitle('5 · Layout', 'eixos, mancais e arranjo físico');
    Layout.renderInspector(root);
  } else if (kind === 'entrada') {
    setTitle('2 · Entrada', 'carga e aplicação');
    const b = block('Carga de entrada');
    b.appendChild(field('entrada.n', { meta: Object.assign({}, E('n_t'), { label: 'Rotação de entrada n', help: 'Rotação do eixo de entrada (motor) no ponto de maior torque. Para o trem, é a rotação do pinhão do estágio 1; para o planetário, a do membro de entrada escolhido.' }), key: 'n' }));
    b.appendChild(field('entrada.T', { meta: Object.assign({}, E('T'), { label: 'Torque de entrada T', help: 'Torque no eixo de entrada. Cada estágio recebe o torque do anterior multiplicado pela relação e pelo rendimento.' }), key: 'T' }));
    b.appendChild(field('entrada.irregularidade_motora', { meta: E('irregularidade_motora'), docKey: 'aplicacao' }));
    b.appendChild(field('entrada.irregularidade_movida', { meta: E('irregularidade_movida'), docKey: 'aplicacao' }));
    b.appendChild(adv('Avançado', [field('entrada.Ka_imposto', { meta: E('Ka_imposto') })]));
    root.appendChild(b);
    const pot = document.createElement('div'); pot.className = 'block'; const P = Math.abs(p.entrada.n * p.entrada.T) * 2 * Math.PI / 60000;
    pot.innerHTML = `<h3><span>Potência de entrada</span></h3><div class="mono" style="font-size:20px;font-weight:700">${P.toFixed(2)} kW</div><div class="small muted">P = T·ω = T·2π·n/60</div>`; root.appendChild(pot);
    const r = document.createElement('div'); r.className = 'block small muted'; r.innerHTML = `Redução alvo <b class="mono">${p.entrada.i_alvo != null ? Number(p.entrada.i_alvo).toFixed(3) : '—'}</b> (±${Number(p.entrada.tol_i ?? 0.5).toFixed(2)}) — definida na <a href="#" class="ir-arq">Arquitetura</a>; a comparação com a redução obtida está em <a href="#" class="ir-saida">Saída</a>.`;
    r.querySelector('.ir-arq').addEventListener('click', (e) => { e.preventDefault(); select('arquitetura'); }); r.querySelector('.ir-saida').addEventListener('click', (e) => { e.preventDefault(); select('saida'); }); root.appendChild(r);
  } else if (kind === 'saida') {
    setTitle('Saída', 'resultado da cinemática × redução desejada');
    const t = S.res && S.res.transmissao; const e = p.entrada;
    const cur = t ? Math.abs(t.i_total) : null; const dev = (e.i_alvo && cur != null) ? 100 * (cur - e.i_alvo) / e.i_alvo : null; const okTol = dev != null && Math.abs(cur - e.i_alvo) <= (e.tol_i ?? 0.5);
    const c = block('Redução: desejada × obtida');
    c.innerHTML += `<div class="kvs cmp-red"><span class="k">Redução desejada (alvo)</span><span class="v">${e.i_alvo != null ? Number(e.i_alvo).toFixed(4) : '—'}</span><span class="muted small">± ${Number(e.tol_i ?? 0.5).toFixed(2)}</span>
      <span class="k">Redução obtida (total)</span><span class="v">${cur != null ? cur.toFixed(4) : '—'}</span><span class="muted small">${p.tipo === 'trem' ? 'Π i_k' : 'cinemática'}</span>
      <span class="k">Desvio</span><span class="v desvio ${dev == null ? '' : okTol ? 'ok' : 'bad'}">${dev != null ? (dev >= 0 ? '+' : '') + dev.toFixed(2) + ' %' : '—'}</span><span class="muted small">${dev != null ? (okTol ? 'dentro da tolerância' : 'fora da tolerância') : (e.i_alvo == null ? 'defina o alvo na Arquitetura' : '')}</span></div>`;
    root.appendChild(c);
    const b = block(p.tipo === 'trem' ? 'Eixos' : 'Membros');
    if (t) {
      const tb = document.createElement('table'); tb.className = 'res'; tb.innerHTML = '<thead><tr><th>Eixo</th><th>n [rpm]</th><th>T [N·m]</th><th>P [kW]</th></tr></thead>';
      const body = document.createElement('tbody'); t.eixos.forEach(x => { const tr = document.createElement('tr'); tr.innerHTML = `<td>${x.nome}</td><td class="num">${x.n.toFixed(1)}</td><td class="num">${x.T.toFixed(2)}</td><td class="num">${x.P_kW.toFixed(3)}</td>`; body.appendChild(tr); }); tb.appendChild(body); b.appendChild(tb);
      const i = document.createElement('div'); i.className = 'small muted'; i.style.marginTop = '6px'; i.innerHTML = `Redução total i = <b class="mono">${t.i_total.toFixed(4)}</b>${t.eta_total != null && p.tipo === 'trem' ? ` · rendimento total η = <b class="mono">${t.eta_total.toFixed(4)}</b>` : ''}${t.i_total < 0 ? ' · sinal negativo: a saída gira em sentido oposto à entrada' : ''}`; b.appendChild(i);
    } else b.innerHTML += '<div class="empty">Calcule para ver a saída.</div>';
    root.appendChild(b);
  } else if (kind === 'estagio') {
    const e = p.estagios[idx]; if (!e) { select('arquitetura'); return; }
    const interna = e.malha.Z_coroa < 0;
    setTitle(`${e.nome || `Estágio ${idx + 1}`} › ${S.sel.roda === 'coroa' ? (interna ? 'Anelar' : 'Coroa') : 'Pinhão'}`, `estágio ${idx + 1} de ${p.estagios.length}`);
    const b0 = block(null);
    b0.appendChild(field(`estagios[${idx}].nome`, { type: 'text', label: 'Nome do estágio', help: 'Nome do estágio no esquema e no relatório.', key: 'nome' }));
    b0.appendChild(field(`estagios[${idx}].eta`, { type: 'number', label: 'Rendimento η', min: 0.5, max: 1, step: 0.005, default: 0.98, help: 'Rendimento do estágio (perdas de engrenamento e mancais). Reduz o torque entregue ao estágio seguinte: T_out = T_in·|u|·η. Típico 0,97–0,99 por estágio.', key: 'eta', docKey: 'forcas' }));
    root.appendChild(b0);
    const b1 = block('Malha (pinhão × coroa)'); malha(`estagios[${idx}].malha`).forEach(f => b1.appendChild(f)); root.appendChild(b1);
    const wp = wheelByKey(`estagio:${idx}:pinhao`), wc = wheelByKey(`estagio:${idx}:coroa`);
    const b2 = block(null);
    b2.appendChild(roda(`estagios[${idx}].pinhao`, 'Pinhão', { wkey: wp.key, cor: wp.cor, z: wp.z }));
    b2.appendChild(roda(`estagios[${idx}].coroa`, interna ? 'Anelar (coroa interna)' : 'Coroa', { interna, wkey: wc.key, cor: wc.cor, z: wc.z }));
    root.appendChild(b2);
    const b3 = block(null); b3.appendChild(adv('Análise ISO 6336 deste estágio', [
      field(`estagios[${idx}].analise.k`, { meta: Object.assign({}, E('k1'), { label: 'Rodas no eixo do pinhão k' }), key: 'k' }),
      field(`estagios[${idx}].analise.Ck`, { meta: Object.assign({}, E('Ck1'), { label: 'Recuo de cabeça C_a' }), key: 'Ck' }),
      field(`estagios[${idx}].analise.K_Hbeta_imposto`, { meta: Object.assign({}, E('K_Hbeta_imposto1'), { label: 'K_Hβ imposto' }), key: 'K_Hbeta_imposto' }),
    ])); root.appendChild(b3);
  } else if (['sol', 'planeta_maior', 'planeta_menor', 'anelar', 'carrier'].includes(kind)) {
    const comp = pl.tipo === 'Composto';
    const nomes = { sol: 'Sol', planeta_maior: comp ? 'Planeta maior' : 'Planeta', planeta_menor: 'Planeta menor', anelar: 'Anelar', carrier: 'Porta-planetas' };
    const w = wheelByKey(kind);
    setTitle(`4 · ${nomes[kind]}`, `planetário ${pl.tipo.toLowerCase()} · ${pl.N_cp} planetas`);
    if (kind === 'sol') {
      const b = block('Sol');
      b.appendChild(field('planetario.sol.z', { type: 'int', min: 6, label: 'Dentes do sol z_s', help: 'Número de dentes do sol (externo).', key: 'z', docKey: 'numero_dentes' }));
      b.appendChild(roda('planetario.sol', 'Roda do sol', { wkey: 'sol', cor: w.cor, z: w.z })); root.appendChild(b);
      const m = block('Malha externa (sol × planeta' + (comp ? ' maior)' : ')')); malha('planetario.malha_ext', { zEditavel: false }).forEach(f => m.appendChild(f)); root.appendChild(m);
    } else if (kind === 'planeta_maior') {
      const b = block(comp ? 'Planeta maior — engrena com o sol' : 'Planeta (engrena com sol e anelar)');
      b.appendChild(field('planetario.planeta_maior.z', { type: 'int', min: 6, label: comp ? 'Dentes do planeta maior z_bp' : 'Dentes do planeta z_p', help: comp ? 'Planeta maior: engrena com o sol (malha externa). Fica no mesmo eixo do planeta menor.' : 'Planeta único: engrena com o sol e com a anelar.', key: 'z', docKey: 'numero_dentes', fig: comp ? 'Compound_Epicyclic.png' : 'Simple_Epicyclic.png' }));
      b.appendChild(roda('planetario.planeta_maior', comp ? 'Roda do planeta maior' : 'Roda do planeta', { wkey: 'planeta_maior', cor: w.cor, z: w.z })); root.appendChild(b);
      const m = block(comp ? 'Malha externa (sol × planeta maior)' : 'Malha externa (sol × planeta)'); malha('planetario.malha_ext', { zEditavel: false }).forEach(f => m.appendChild(f)); root.appendChild(m);
      if (!comp) { const n = document.createElement('div'); n.className = 'block'; n.innerHTML = '<p class="small muted">No planetário simples o mesmo planeta engrena com o sol e com a anelar (módulo e ângulo de pressão iguais). A malha interna usa estes dados.</p>'; root.appendChild(n); }
    } else if (kind === 'planeta_menor') {
      if (!comp) { const b = block(null); b.innerHTML = '<div class="alert aviso"><span class="ic">!</span><span>O planetário simples não tem planeta menor. Selecione "Composto" na Arquitetura para configurá-lo.</span></div>'; root.appendChild(b); }
      else {
        const b = block('Planeta menor — engrena com a anelar');
        b.appendChild(field('planetario.planeta_menor.z', { type: 'int', min: 6, label: 'Dentes do planeta menor z_sp', help: 'Planeta menor: engrena com a anelar (malha interna). Solidário ao planeta maior (mesmo eixo, mesma rotação).', key: 'z', docKey: 'numero_dentes', fig: 'Compound_Epicyclic.png' }));
        b.appendChild(roda('planetario.planeta_menor', 'Roda do planeta menor', { wkey: 'planeta_menor', cor: w.cor, z: w.z })); root.appendChild(b);
        const m = block('Malha interna (planeta menor × anelar)'); malha('planetario.malha_int', { zEditavel: false }).forEach(f => m.appendChild(f)); root.appendChild(m);
      }
    } else if (kind === 'anelar') {
      const b = block('Anelar');
      b.appendChild(field('planetario.anelar.z', { type: 'int', min: 10, label: 'Dentes da anelar z_r', help: 'Número de dentes da coroa interna (informe positivo; o programa aplica a convenção DIN de sinal negativo).', key: 'z', docKey: 'numero_dentes' }));
      b.appendChild(field('planetario.anelar.D_ext', { type: 'number', min: 0, unit: 'mm', label: 'Diâmetro externo do aro', help: 'Diâmetro externo da anelar (carcaça). Define a espessura de aro s_R usada em Y_B e deve caber no envelope da máquina.', key: 'D_ext', docKey: 'aro' }));
      b.appendChild(roda('planetario.anelar', 'Roda da anelar', { interna: true, wkey: 'anelar', cor: w.cor, z: w.z })); root.appendChild(b);
      const m = block('Malha interna (' + (comp ? 'planeta menor' : 'planeta') + ' × anelar)');
      if (!comp) { const n = document.createElement('p'); n.className = 'small muted'; n.textContent = 'Simples: módulo e ângulo seguem a malha externa (mesmo planeta).'; m.appendChild(n); }
      malha('planetario.malha_int', { zEditavel: false }).forEach(f => m.appendChild(f)); root.appendChild(m);
    } else {
      const b = block('Porta-planetas'); const t = S.res && S.res.transmissao && S.res.transmissao.cinematica;
      if (t) {
        const k = document.createElement('div'); k.className = 'kvs';
        const rows = [['Rotação do porta-planetas', t.n_c, 'rpm'], ['Rotação da anelar', t.n_anel, 'rpm'], ['Rotação absoluta do planeta', t.n_pla, 'rpm'], ['Rotação relativa do sol', t.n_sol_rel, 'rpm'], ['Rotação relativa do planeta', t.n_pla_rel, 'rpm'], ['Torque no sol (malha externa)', t.T_malha_ext, 'N·m'], ['Torque na malha interna', t.T_malha_int, 'N·m'], ['Torque na anelar', t.T_anel, 'N·m'], ['Torque no porta-planetas', t.T_carrier, 'N·m'], ['Relação i', t.i, ''], t.modo === 'diferencial' ? ['Membro livre (rotação imposta)', t.membro_livre, ''] : ['Membro fixo', t.membro_fixo, ''], ['Anelar no K_v (Ring)', t.ring === 'Fixo' ? 'Fixo — presa à carcaça' : 'Rotativo — girando', '']];
        rows.forEach(([a, v, u]) => { k.innerHTML += `<span class="k">${a}</span><span class="v">${typeof v === 'number' ? v.toFixed(2) : v}</span><span class="muted small">${u}</span>`; });
        b.appendChild(k);
      } else b.innerHTML += '<div class="empty">Calcule para ver a cinemática.</div>';
      const an = adv('Análise ISO 6336 (K_Hβ, C_a, k por malha)', [
        field('planetario.analise_ext.k', { meta: Object.assign({}, E('k1'), { label: 'k (malha externa)' }), key: 'k' }), field('planetario.analise_int.k', { meta: Object.assign({}, E('k2'), { label: 'k (malha interna)' }), key: 'k' }),
        field('planetario.analise_ext.K_Hbeta_imposto', { meta: Object.assign({}, E('K_Hbeta_imposto1'), { label: 'K_Hβ imposto (externa)' }), key: 'K_Hbeta_imposto' }), field('planetario.analise_int.K_Hbeta_imposto', { meta: Object.assign({}, E('K_Hbeta_imposto2'), { label: 'K_Hβ imposto (interna)' }), key: 'K_Hbeta_imposto' }),
        field('planetario.analise_ext.Ck', { meta: Object.assign({}, E('Ck1'), { label: 'C_a (externa)' }), key: 'Ck' }), field('planetario.analise_int.Ck', { meta: Object.assign({}, E('Ck2'), { label: 'C_a (interna)' }), key: 'Ck' }),
      ]); b.appendChild(an); root.appendChild(b);
    }
  } else if (kind === 'operacao') {
    setTitle('6 · Operação e materiais', 'condições comuns a toda a transmissão');
    const b = block('Vida e segurança');
    ['Vr', 'S_Hmin', 'S_Fmin'].forEach(k => b.appendChild(field(`operacao.${k}`, { meta: E(k), key: k, docKey: docOf[k] })));
    b.appendChild(adv('Alvos máximos', ['S_Hmax', 'S_Fmax'].map(k => field(`operacao.${k}`, { meta: Object.assign({}, E(k), { advanced: false }), key: k }))));
    root.appendChild(b);
    const c = block('Lubrificação e temperatura');
    c.appendChild(subobject('operacao.lubrificante', 'lubrificante', 'Lubrificante'));
    ['T_op', 'imersao'].forEach(k => c.appendChild(field(`operacao.${k}`, { meta: E(k), key: k, docKey: docOf[k] })));
    c.appendChild(adv('Dilatação e jogo', ['T_Rmd', 'T_Cmd', 'C_Cdil', 'ISO', 'F_B_rolamento'].map(k => field(`operacao.${k}`, { meta: Object.assign({}, E(k), { advanced: false }), key: k }))));
    root.appendChild(c);
    const d = block('Relatório'); d.appendChild(field('operacao.Proj', { meta: E('Proj'), key: 'Proj' })); root.appendChild(d);
  } else if (kind === 'analise') {
    setTitle('7 · Análise ISO 6336', 'métodos de cálculo');
    const b = block('Métodos');
    ['metodo_YF', 'curva_vida', 'metodo_x'].forEach(k => b.appendChild(field(`metodos.${k}`, { meta: E(k), key: k })));
    b.appendChild(adv('Avançado', ['metodo_YF_interno', 'M_BS', 'Lambda'].map(k => field(`metodos.${k}`, { meta: Object.assign({}, E(k), { advanced: false }), key: k }))));
    root.appendChild(b);
  }
  marcarRoda();
  applyErrors(root, (S.res && S.res.erros) || {});
}
