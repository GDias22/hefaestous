// Resultados do item selecionado: medidores S_H/S_F, avisos clicáveis, fatores em barras com "Por quê?"
import { S, on, select } from '../app.js';
import { fmtNum } from '../results.js';
import { wheelOf, ladoCard, wheels } from '../model/rodas.js';
const wheelsDaMalha = (i) => wheels().find(w => w.malha === i && w.lado === 'pinhao') || wheels().find(w => w.malha === i);

let root;
export function init() { root = document.getElementById('results'); on(ev => { if (['result', 'select', 'load'].includes(ev.type)) render(); }); }

function gauge(c, malhaIdx, mine = false) {
  const d = document.createElement('div'); d.className = 'gauge ' + (c.status || 'na') + (mine ? ' mine' : '');
  const v = c.valor, mn = c.minimo, mx = Math.max(mn * 2.2, (v || 0) * 1.15, 0.1);
  const pct = v == null ? 0 : Math.min(100, (v / mx) * 100), mpct = Math.min(100, (mn / mx) * 100);
  d.innerHTML = `<div class="f"><span>${c.fator === 'S_H' ? 'S<sub>H</sub> pitting' : 'S<sub>F</sub> flexão'} · ${c.roda}</span></div>
    <div class="v">${v == null ? '—' : fmtNum(v, 3)}</div>
    <div class="bar"><i style="width:${pct}%"></i><b style="left:${mpct}%"></b></div>
    <div class="m"><span>mín. ${fmtNum(mn, 2)}</span><span>${c.status === 'ok' ? 'atende' : c.status === 'atencao' ? 'margem < 10 %' : c.status === 'ruim' ? 'não atende' : ''}</span></div>
    <button class="why" title="Como este valor foi obtido">por quê?</button>`;
  d.querySelector('.why').addEventListener('click', () => document.dispatchEvent(new CustomEvent('explain', { detail: { fator: c.fator, roda: c.roda, malha: malhaIdx } })));
  return d;
}
function fatoresBar(m, malhaIdx) {
  const t = m.tensoes; if (!t) return null;
  const want = [['Kv', 'K_v'], ['K_Hbeta', 'K_Hβ'], ['K_Halpha', 'K_Hα'], ['Z_H', 'Z_H'], ['Z_epsilon', 'Z_ε'], ['Z_B', 'Z_B'], ['Z_L', 'Z_L'], ['Z_V', 'Z_V'], ['Z_R', 'Z_R'], ['Y_F', 'Y_F'], ['Y_S', 'Y_S'], ['Y_beta', 'Y_β'], ['Y_B', 'Y_B'], ['Y_dRelT', 'Y_δrelT'], ['Y_RRelT', 'Y_RrelT'], ['Y_NT', 'Y_NT'], ['Z_NT', 'Z_NT']];
  const flat = {}; t.secoes.forEach(s => s.linhas.forEach(l => { flat[l.k] = l; }));
  const box = document.createElement('div'); box.className = 'kvs';
  for (const [k, lab] of want) {
    const l = flat[k]; if (!l) continue;
    const vals = l.pc ? l.pc : [l.v];
    const txt = l.pc ? `${fmtNum(l.pc[0], 3)} / ${fmtNum(l.pc[1], 3)}` : fmtNum(l.v, 3);
    const row = document.createElement('span'); row.className = 'k'; row.textContent = lab; row.title = l.label;
    const v = document.createElement('span'); v.className = 'v'; v.textContent = txt;
    const w = document.createElement('button'); w.className = 'why'; w.textContent = '?'; w.title = 'Por quê?';
    w.addEventListener('click', () => document.dispatchEvent(new CustomEvent('explain', { detail: { fator: k, malha: malhaIdx } })));
    const bar = document.createElement('span'); bar.className = 'bar'; const ref = Math.max(...vals.filter(x => x != null), 0); const scale = k.startsWith('K') ? 2.5 : 3;
    bar.innerHTML = `<i style="width:${Math.min(100, ref / scale * 100)}%"></i>`;
    box.appendChild(row); box.appendChild(v); box.appendChild(w); box.appendChild(bar);
  }
  return box;
}
function avisos(m) {
  const list = (m.avisos || []).filter(a => a && a.nivel !== 'ok');
  const box = document.createElement('div'); box.className = 'alerts';
  if (!list.length) { box.innerHTML = '<div class="alert ok"><span class="ic">✓</span><span>Sem avisos nesta malha.</span></div>'; return box; }
  for (const a of list) {
    const d = document.createElement('div'); d.className = 'alert ' + (a.nivel || 'aviso');
    d.innerHTML = `<span class="ic">!</span><span>${a.texto.replace(/^AVISO\s*:\s*/i, '')}</span>`; box.appendChild(d);
  }
  return box;
}
/** Painel de erro de uma malha: o que houve, em que campo agir e botão para ir até ele. */
const ROTULO = { x_pinhao: 'Deslocamento de perfil x₁', a: 'Distância entre centros a', Z_pinhao: 'Dentes do pinhão', Z_coroa: 'Dentes da coroa', m_n: 'Módulo', alpha_n: 'Ângulo de pressão', beta: 'Ângulo de hélice', Arranjo: 'Arranjo físico' };
function rotuloCampo(path) {
  const k = path.split('.').pop().replace(/_(pinhao|coroa)$/, '');
  const p = S.meta && S.meta.params && (S.meta.params[path.split('.').pop()] || S.meta.params[k + '_pinhao']);
  return ROTULO[path.split('.').pop()] || (p && p.label) || path;
}
function painelErro(m, titulo) {
  const b = document.createElement('div'); b.className = 'block';
  const campos = Object.entries(m.erro_campos || {});
  b.innerHTML = `<h3><span>${titulo}</span><span class="cnt">sem resultado</span></h3>`;
  const card = document.createElement('div'); card.className = 'errcard';
  card.innerHTML = '<div class="errh"><span class="ic">✕</span><b>Estes valores não geram uma engrenagem possível</b></div>';
  if (!campos.length) { const t = document.createElement('p'); t.textContent = m.erro; card.appendChild(t); }
  campos.forEach(([path, msg]) => {
    const it = document.createElement('div'); it.className = 'erritem';
    it.innerHTML = `<div class="errcampo">Ajuste: <b>${rotuloCampo(path)}</b></div><p>${msg}</p>`;
    const go = document.createElement('button'); go.className = 'btn xs blue'; go.textContent = 'Ir para o campo'; go.addEventListener('click', () => irPara(path));
    it.appendChild(go); card.appendChild(it);
  });
  const dica = document.createElement('div'); dica.className = 'errdica small muted';
  dica.innerHTML = 'Dica: enquanto houver erro, os resultados de resistência ficam indisponíveis. Corrija o campo indicado e o cálculo volta sozinho.';
  card.appendChild(dica); b.appendChild(card); return b;
}
function blocoMalha(m, malhaIdx, titulo, lado = null) {
  const wrap = document.createElement('div');
  if (!m) return wrap;
  if (m.erro) { wrap.appendChild(painelErro(m, titulo)); return wrap; }
  const b1 = document.createElement('div'); b1.className = 'block'; b1.innerHTML = `<h3><span>${titulo} — seguranças</span>${lado != null ? '<span class="cnt">roda selecionada em destaque</span>' : ''}</h3>`;
  if (m.cards) { const g = document.createElement('div'); g.className = 'gauges'; m.cards.forEach(c => g.appendChild(gauge(c, malhaIdx, lado != null && c.roda === ladoCard(lado)))); b1.appendChild(g); }
  else b1.innerHTML += '<div class="empty">Seguranças indisponíveis (corrija as entradas).</div>';
  wrap.appendChild(b1);
  const b2 = document.createElement('div'); b2.className = 'block'; b2.innerHTML = `<h3><span>Avisos</span><span class="cnt">${(m.avisos || []).filter(a => a.nivel !== 'ok').length}</span></h3>`; b2.appendChild(avisos(m)); wrap.appendChild(b2);
  const fb = fatoresBar(m, malhaIdx);
  if (fb) { const b3 = document.createElement('div'); b3.className = 'block'; b3.innerHTML = '<h3><span>Fatores ISO 6336</span><span class="cnt">pinhão / coroa</span></h3>'; b3.appendChild(fb); wrap.appendChild(b3); }
  const g = m.geometria; if (g) {
    const b4 = document.createElement('div'); b4.className = 'block'; b4.innerHTML = '<h3><span>Geometria principal</span></h3>';
    const v = g.vars; const kv = document.createElement('div'); kv.className = 'kvs';
    const rows = [['Diâmetro primitivo d_w', [v.dw_pinhao, v.dw_coroa], 'mm'], ['Diâmetro de cabeça d_a', [v.d_a_pinhao, v.d_a_coroa], 'mm'], ['Diâmetro de pé d_f', [v.d_f_pinhao, v.d_f_coroa], 'mm'], ['Deslocamento de perfil x', [v.x_pinhao, v.x_coroa], ''], ['Recobrimento ε_α / ε_β', [v.epsilon_alpha, v.epsilon_beta], ''], ['Força tangencial F_t', [v.Ft], 'N'], ['Velocidade tangencial v_t', [v.v_t], 'm/s'], ['Distância entre centros a', [v.a], 'mm']];
    rows.forEach(([lab, vals, u]) => { kv.innerHTML += `<span class="k">${lab}</span><span class="v">${vals.map(x => fmtNum(x, 3)).join(' / ')}</span><span class="muted small">${u}</span>`; });
    b4.appendChild(kv); wrap.appendChild(b4);
  }
  return wrap;
}
function render() {
  if (!root) return;
  root.innerHTML = '';
  if (!S.res) { root.innerHTML = '<div class="block"><div class="empty">Aguardando cálculo…</div></div>'; return; }
  const { kind, idx } = S.sel;
  if (S.res.erros && S.res.erros[''] ) { const b = document.createElement('div'); b.className = 'block'; b.innerHTML = `<div class="alert erro"><span class="ic">✕</span><span>${S.res.erros['']}</span></div>`; root.appendChild(b); }
  const w = wheelOf(S.sel);
  if (w) {
    const nome = S.proj.tipo === 'trem' ? `${w.estagio} (${w.base})` : (w.malha === 0 ? 'Malha externa' : 'Malha interna');
    root.appendChild(blocoMalha(S.res.malhas[w.malha], w.malha, nome, w.lado));
    if (w.extra) root.appendChild(blocoMalha(S.res.malhas[w.extra.malha], w.extra.malha, 'Malha interna', w.extra.lado));
  }
  else {
    // visão geral: pior segurança e resumo por malha
    const b = document.createElement('div'); b.className = 'block'; b.innerHTML = '<h3><span>Visão geral</span></h3>';
    const r = S.res.resumo;
    if (r && r.pior) {
      const ordem = (c) => (c.fator === 'S_H' ? 0 : 2) + (c.roda === 'pinhão' ? 0 : 1);       // S_H pinhão, S_H coroa, S_F pinhão, S_F coroa
      S.res.malhas.forEach((m, i) => {
        if (!m.cards || !m.cards.length) return;
        const titulo = S.proj.tipo === 'trem' ? m.apelido : (i === 0 ? 'Malha externa (sol × planeta' + (S.proj.planetario.tipo === 'Composto' ? ' maior)' : ')') : 'Malha interna (' + (S.proj.planetario.tipo === 'Composto' ? 'planeta menor' : 'planeta') + ' × anelar)');
        const sec = document.createElement('div'); sec.className = 'ov-sec';
        const h = document.createElement('div'); h.className = 'ov-h'; h.innerHTML = `<b>${titulo}</b><span class="muted small">pinhão = ${S.proj.tipo === 'trem' ? 'roda motora' : (i === 0 ? 'sol' : 'planeta')} · coroa = ${S.proj.tipo === 'trem' ? 'roda movida' : (i === 0 ? 'planeta' : 'anelar')}</span>`;
        h.addEventListener('click', () => { const w = wheelsDaMalha(i); if (w) select(w.kind, w.idx, w.roda, 'results'); });
        sec.appendChild(h);
        const g = document.createElement('div'); g.className = 'gauges';
        m.cards.slice().sort((x, y) => ordem(x) - ordem(y)).forEach(c => g.appendChild(gauge(c, i)));
        sec.appendChild(g); b.appendChild(sec);
      });
      const s = document.createElement('div'); s.className = 'small muted'; s.style.marginTop = '8px'; s.textContent = r.todos_atendem ? 'Todas as seguranças atendem aos mínimos.' : 'Há seguranças abaixo do mínimo: clique no título da malha (ou numa roda) para ver detalhes e avisos.'; b.appendChild(s);
    } else b.innerHTML += '<div class="empty">Sem resultados de resistência (verifique os erros nos campos).</div>';
    root.appendChild(b);
    const errs = Object.entries(S.res.erros || {}).filter(([k]) => k);
    if (errs.length) { const e = document.createElement('div'); e.className = 'block'; e.innerHTML = `<h3><span>Problemas nas entradas</span><span class="cnt">${errs.length}</span></h3>`; const al = document.createElement('div'); al.className = 'alerts'; errs.forEach(([k, msg]) => { const d = document.createElement('div'); d.className = 'alert erro link'; d.innerHTML = `<span class="ic">✕</span><span><b class="mono small">${k}</b><br>${msg}</span>`; d.addEventListener('click', () => irPara(k)); al.appendChild(d); }); e.appendChild(al); root.appendChild(e); }
  }
}
document.addEventListener('ir-para-campo', (e) => irPara(e.detail));
function irPara(path) {
  const m = path.match(/^estagios\[(\d+)\]/); if (m) select('estagio', +m[1], /\.coroa\b/.test(path) ? 'coroa' : 'pinhao');
  else if (path.startsWith('planetario.sol') || path.startsWith('planetario.malha_ext')) select('sol'); else if (path.startsWith('planetario.planeta_maior')) select('planeta_maior'); else if (path.startsWith('planetario.planeta_menor') || path.startsWith('planetario.malha_int')) select(S.proj.planetario.tipo === 'Composto' ? 'planeta_menor' : 'planeta_maior'); else if (path.startsWith('planetario.anelar')) select('anelar'); else if (path.startsWith('planetario')) select('arquitetura');
  else if (path.startsWith('operacao')) select('operacao'); else if (path.startsWith('metodos')) select('analise'); else if (path.startsWith('entrada')) select('entrada');
  setTimeout(() => { const f = document.querySelector(`#inspector .fld[data-path="${path}"]`); if (f) { f.closest('details')?.setAttribute('open', ''); f.scrollIntoView({ block: 'center' }); f.classList.add('hl'); setTimeout(() => f.classList.remove('hl'), 1800); } }, 80);
}
