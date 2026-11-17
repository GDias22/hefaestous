// Centro: abas Esquema / Dente / Roda 2D / 3D / Tabelas / Aprender
import { S, on, select, toast } from '../app.js';
import { api } from '../api.js';
import { drawTrain } from '../draw/train2d.js';
import { drawPlanetary } from '../draw/planetary2d.js';
import { drawToothProfile } from '../gear2d.js';
import { renderSections, fmtNum } from '../results.js';
import * as Arq from './arquitetura.js';
import * as Busca from './busca.js';
import * as Layout from './layout.js';
import { wheels, curWheel, keyOfSel, minSeg, wheelByKey } from '../model/rodas.js';

// Árvore = ETAPAS (o que se edita; muda o inspetor). Abas = VISTAS (o que o centro mostra). São independentes: clicar numa aba
// NÃO muda a etapa/seleção. Arquitetura e Busca de dentes só existem como painel (sem aba): abrem pela árvore e, ao escolher uma
// roda a partir deles, o centro volta ao Esquema. Layout tem painel e aba. O trilho à esquerda das abas mostra a etapa atual.
const PASSO_PANE = ['arquitetura', 'dentes', 'layout'];
let tab = 'arquitetura'; const panes = {}; let viewer = null; const perfilCache = {};
export function init() {
  document.querySelectorAll('#tabs button').forEach(b => { b.addEventListener('click', () => setTab(b.dataset.t)); });
  document.querySelectorAll('#canvas .pane').forEach(p => { panes[p.dataset.p] = p; });
  on(ev => {
    if (ev.type === 'select') irParaAba();
    if (ev.type === 'result' || ev.type === 'select' || ev.type === 'load' || (ev.type === 'change' && ['tipo do planetário', 'adicionar estágio', 'remover estágio', 'interno'].includes(ev.label))) { if (ev.type === 'result') Object.keys(perfilCache).forEach(k => delete perfilCache[k]); render(); }
  });
  window.addEventListener('resize', () => { if (tab === 'esquema') renderEsquema(); });
  document.addEventListener('open-doc', (e) => { setTab('aprender'); document.dispatchEvent(new CustomEvent('show-doc', { detail: e.detail })); });
}
/** Passo com painel próprio mostra esse painel; sair dele para uma roda (ou outro passo) volta às vistas, no esquema. */
function irParaAba() {
  const k = S.sel.kind;
  if (PASSO_PANE.includes(k)) { if (tab !== k) setTab(k); return; }
  if (PASSO_PANE.includes(tab)) setTab('esquema');
}
/** Rótulo da roda em foco nas vistas Dente / Roda 2D / 3D (a roda se escolhe na ÁRVORE, à esquerda — não há seletor na vista). */
function whoRoda(host) {
  const w = curWheel(); if (!host) return;
  host.innerHTML = w ? `<i class="chip" style="background:${w.cor}"></i><b>${w.estagio ? w.estagio + ' › ' : ''}${w.base}</b><span class="muted small">· z ${w.z}</span>` : '';
}
export function setTab(t) {
  tab = t;
  document.querySelectorAll('#tabs button').forEach(b => b.classList.toggle('on', b.dataset.t === t));
  Object.entries(panes).forEach(([k, p]) => p.classList.toggle('on', k === t));
  render();
}

function malhaIdx() { const w = curWheel(); return w ? w.malha : 0; }
function malhaOk(i) { const m = S.res && S.res.malhas && S.res.malhas[i]; return m && !m.erro ? m : null; }

function render() {
  if (tab === 'arquitetura') { Arq.renderPane(panes.arquitetura); return; }
  if (tab === 'dentes') { Busca.renderPane(panes.dentes); return; }
  if (tab === 'layout') { Layout.renderPane(panes.layout); return; }
  if (!S.res) return;
  if (tab === 'esquema') renderEsquema();
  else if (tab === 'dente' || tab === 'roda') renderPerfil(tab);
  else if (tab === 'cad') renderCad();
  else if (tab === 'tabelas') renderTabelas();
  else if (tab === 'aprender') document.dispatchEvent(new CustomEvent('render-aprender'));
}

// ---------------- Esquema ----------------
function escolherRoda(key) { const w = wheelByKey(key); if (w) select(w.kind, w.idx, w.roda, 'esquema'); }
function segPorRoda() { const o = {}; wheels().forEach(w => { o[w.key] = minSeg(w); }); return o; }
/** Esquema indisponível por erro de entrada: diz o que está errado e leva ao campo (o painel da direita mostra o mesmo, com detalhes). */
function erroNoCentro(p, svg) {
  let box = p.querySelector('.erro-centro'); if (!box) { box = document.createElement('div'); box.className = 'erro-centro'; p.appendChild(box); }
  const erros = Object.entries((S.res && S.res.erros) || {}).filter(([k]) => k);
  box.innerHTML = '<h3>O esquema não pode ser desenhado</h3><p class="muted">Alguma roda não tem geometria possível com os valores atuais. Corrija o item abaixo e o desenho volta sozinho.</p>';
  erros.forEach(([k, msg]) => { const d = document.createElement('div'); d.className = 'alert erro link'; d.innerHTML = `<span class="ic">✕</span><span>${msg}</span>`; d.addEventListener('click', () => document.dispatchEvent(new CustomEvent('ir-para-campo', { detail: k }))); box.appendChild(d); });
  if (!erros.length) box.innerHTML += '<div class="alert erro"><span class="ic">✕</span><span>Verifique os campos destacados em vermelho no painel da direita.</span></div>';
}
function renderEsquema() {
  const p = panes.esquema; if (!S.res) return;
  let svg = p.querySelector('svg.draw');
  if (!svg) { p.innerHTML = ''; svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); svg.setAttribute('class', 'draw'); p.appendChild(svg); const h = document.createElement('div'); h.className = 'canvas-hint'; h.textContent = 'passe o mouse para ver os dados · clique para selecionar e editar a roda'; p.appendChild(h); }
  if (S.res.transmissao && S.res.transmissao.tipo !== S.proj.tipo) return;      // resultado antigo de outro tipo de projeto: espera o recálculo
  const malhas = S.res.malhas.filter(m => m && !m.erro).map(m => ({ apelido: m.apelido, vars: m.geometria.vars }));
  if (S.proj.tipo === 'trem') {
    if (!malhas.length || malhas.length !== S.res.malhas.length) { svg.innerHTML = ''; erroNoCentro(p, svg); return; }
    p.querySelector('.erro-centro')?.remove();
    drawTrain(svg, malhas, S.res.transmissao.eixos, keyOfSel(S.sel) && wheelByKey(keyOfSel(S.sel)) ? keyOfSel(S.sel) : null, escolherRoda, segPorRoda());
  } else {
    if (malhas.length < 2) { svg.innerHTML = ''; return; }
    drawPlanetary(svg, malhas[0], malhas[1], S.res.transmissao.cinematica, S.proj.planetario.N_cp, wheelByKey(keyOfSel(S.sel)) ? S.sel.kind : null, escolherRoda, segPorRoda());
  }
}

// ---------------- Dente / Roda ----------------
function toolbarRoda(p, onChange, extra = '') {
  let tb = p.querySelector('.toolbar');
  if (tb) return tb;
  tb = document.createElement('div'); tb.className = 'toolbar';
  tb.innerHTML = `<span class="r-who" title="Roda mostrada nesta vista (escolha na árvore à esquerda)"></span>
    <label><input type="checkbox" class="r-pre" checked> pré-usinagem (protuberância)</label>${extra}<span class="muted small r-info" style="margin-left:auto"></span>`;
  tb.querySelector('.r-pre').addEventListener('change', onChange);
  p.appendChild(tb); const body = document.createElement('div'); body.className = 'body'; p.appendChild(body);
  return tb;
}
async function renderPerfil(modo) {
  const p = panes[modo]; const i = malhaIdx(); const m = malhaOk(i);
  const tb = toolbarRoda(p, () => renderPerfil(modo)); const body = p.querySelector('.body');
  if (!m) { body.innerHTML = '<div class="empty" style="margin:20px">Malha sem resultado.</div>'; return; }
  const w = curWheel(); const roda = w.lado, pre = tb.querySelector('.r-pre').checked;
  whoRoda(tb.querySelector('.r-who'));
  const key = `${i}|${roda}`;
  body.innerHTML = '<div class="empty" style="margin:20px">Gerando perfil…</div>';
  try {
    if (!perfilCache[key]) perfilCache[key] = await perfilParams(i, roda);
    const res = perfilCache[key];
    body.innerHTML = '';
    const wrap = drawToothProfile(res, { modo: modo === 'dente' ? 'dente' : 'roda', mostrarPre: pre });
    const svg = wrap.querySelector('svg'); svg.classList.add('draw'); svg.dataset.key = `perfil_${i}_${roda}`; svg.style.maxHeight = '100%';
    wrap.style.height = '100%'; body.appendChild(wrap);
    const sc = res.secao_critica || {};
    (res.avisos || []).forEach(a => { const d = document.createElement('div'); d.className = 'alert aviso'; d.style.margin = '8px 12px 0'; d.innerHTML = `<span class="ic">!</span><span>${a}</span>`; body.prepend(d); });
    tb.querySelector('.r-info').textContent = `z ${res.z} · m_n ${res.m_n} · x ${fmtNum(res.x, 4)} · s_t ${fmtNum(res.s_t_ref, 3)} mm · d_Ff ${fmtNum(res.circulos.d_Ff, 2)} mm · s_Fn ${fmtNum(sc.s_Fn, 3)} · ρ_F ${fmtNum(sc.rho_F, 3)}${res.retificado ? ` · retificado (q ${fmtNum(res.sobremetal.q, 3)}, s_pr ${fmtNum(res.sobremetal.s_pr, 3)})` : ''}`;
  } catch (e) { body.innerHTML = `<div class="alert erro" style="margin:16px"><span class="ic">✕</span><span>${e.message}</span></div>`; }
}
/** Perfil a partir dos parâmetros da malha calculada (stateless: não exige sessão salva). */
function perfilParams(i, roda) {
  const m = S.res.malhas[i]; const v = m.geometria.vars; const s = roda === 'pinhao' ? 'pinhao' : 'coroa';
  const fer = m.geometria[`ferramenta_${s}`] || {};
  const params = { m_n: v.m_n, z: v[`Z_${s}`], x: v[`x_${s}`], alpha_n: v.alpha_n, beta: v.beta, h_fP_star: fer.cp_dedendo, h_aP_star: fer.k_a, rho: v[`rk_${s}`] || 0, pr0: fer.pr || 0,
    q: (v[`op_acabamento_${s}`] === 'Retificação' || v[`op_acabamento_${s}`] === 'Rasqueteamento') ? (v[`SM_${s}`] || 0) : 0, d_a: v[`d_a_${s}`], d_f: v[`d_f_${s}`], d: v[`d_${s}`], db: v[`db_${s}`],
    d_Na: v[`d_na_${s}`], d_Nf: v[`d_nf_${s}`], b: v[`b_${s}`], d_i: v[`di_${s}`], z0: fer.Z_shaper, apelido: `${m.apelido} — ${s}` };
  return api.perfil2d({ params });
}

// ---------------- 3D ----------------
async function renderCad() {
  const p = panes.cad; const i = malhaIdx(); const m = malhaOk(i);
  if (!p.querySelector('.toolbar')) {
    p.innerHTML = `<div class="toolbar"><span class="r-who" title="Roda mostrada nesta vista (escolha na árvore à esquerda)"></span>
      <button class="btn sm primary v-gen">Gerar sólido</button>
      <span class="dd v-dl hidden"><button class="btn sm v-dl-btn">Baixar ▾</button><div class="dd-menu">
        <a class="v-step" download><b>STEP</b><small>sólido B-rep (AP214, mm) — CAD</small></a>
        <a class="v-glb" download><b>GLB</b><small>malha glTF binária — visualização</small></a>
        <a class="v-stl" download><b>STL</b><small>malha triangular — impressão 3D</small></a></div></span>
      <span class="muted small v-furo"></span>
      <span style="width:1px;height:18px;background:var(--line-2)"></span>
      <button class="btn sm v-conj" title="Todas as rodas do projeto montadas e em fase, num único arquivo">Gerar conjunto</button>
      <span class="dd v-cdl hidden"><button class="btn sm v-cdl-btn">Baixar conjunto ▾</button><div class="dd-menu">
        <a class="c-step" download><b>STEP</b><small>montagem: uma peça por roda, nome e cor</small></a>
        <a class="c-glb" download><b>GLB</b><small>malha glTF binária — visualização</small></a>
        <a class="c-stl" download><b>STL</b><small>malha triangular — impressão 3D</small></a>
        <a class="c-zip" download><b>ZIP</b><small>conjunto + peças separadas + posições</small></a></div></span>
      <span style="width:1px;height:18px;background:var(--line-2)"></span><button class="btn sm v-fit">Enquadrar</button><button class="btn sm v-cam">Ortográfica</button><button class="btn sm v-meas">Medir</button>
      <label>corte <input type="range" class="v-clip" min="0" max="100" value="100" style="width:110px"></label><button class="btn sm v-png">PNG</button>
      <label title="Padrão do SolidWorks: roda para frente afasta. Desmarque para roda para frente aproximar."><input type="checkbox" class="v-zoomsw" checked> roda como no SW</label>
      <span class="muted small" style="margin-left:auto" title="Mouse no padrão SolidWorks">meio: orbitar · Ctrl+meio: deslocar · Shift+meio: zoom · roda: zoom no cursor · 2× meio: enquadrar · Medir: 2 cliques</span></div><div class="body v-wrap" style="background:#f7f8fa"></div>`;
    const q = (s) => p.querySelector(s); let ortho = false, meas = false;
    const ensure = async () => { if (!viewer) { const mod = await import('../viewer3d.js'); viewer = mod.createViewer(q('.v-wrap')); q('.v-zoomsw').checked = viewer.zoomInvertido(); } return viewer; };
    q('.v-zoomsw').checked = localStorage.getItem('engr.zoomSW') !== '0';
    q('.v-zoomsw').addEventListener('change', (e) => { localStorage.setItem('engr.zoomSW', e.target.checked ? '1' : '0'); if (viewer) viewer.setZoomInvertido(e.target.checked); });
    const dd = q('.v-dl'), cdd = q('.v-cdl');
    for (const [d, b] of [[dd, '.v-dl-btn'], [cdd, '.v-cdl-btn']]) {
      q(b).addEventListener('click', (e) => { e.stopPropagation(); const was = d.classList.contains('open'); dd.classList.remove('open'); cdd.classList.remove('open'); d.classList.toggle('open', !was); });
      d.querySelectorAll('a').forEach(a => a.addEventListener('click', () => d.classList.remove('open')));
    }
    document.addEventListener('click', () => { dd.classList.remove('open'); cdd.classList.remove('open'); });
    q('.v-conj').addEventListener('click', async () => {
      const btn = q('.v-conj'); btn.disabled = true; btn.textContent = 'Gerando conjunto…';
      try {
        const spec = specConjunto(); if (!spec) throw new Error('todas as malhas precisam estar calculadas');
        const r = await api.perfil3dConjunto(spec);
        const vw = await ensure(); await vw.load(r.glb_url);
        const safe = `${S.proj.nome || 'projeto'}-conjunto`.replace(/[^\w.-]+/g, '_');
        for (const [cls, ext] of [['.c-step', 'step'], ['.c-glb', 'glb'], ['.c-stl', 'stl'], ['.c-zip', 'zip']]) { q(cls).href = r[`${ext}_url`]; q(cls).download = `${safe}.${ext}`; }
        cdd.classList.remove('hidden'); cdd.dataset.id = r.id;
        q('.v-furo').textContent = `conjunto: ${r.n_pecas} peças`;
        (r.avisos || []).forEach(a => toast(a, true, 9000));
        if (!(r.avisos || []).length) toast(`Conjunto gerado · ${r.n_pecas} peças${r.volume_mm3 ? ` · ${fmtNum(r.volume_mm3 / 1000, 2)} cm³` : ''}`);
      } catch (e) { toast(e.status === 501 ? 'CAD indisponível: instale build123d/cadquery-ocp no venv.' : e.message, true, 7000); }
      finally { btn.disabled = false; btn.textContent = 'Gerar conjunto'; }
    });
    q('.v-gen').addEventListener('click', async () => {
      const btn = q('.v-gen'); btn.disabled = true; btn.textContent = 'Gerando…';
      try {
        const mi = malhaIdx(); const mm = malhaOk(mi); if (!mm) throw new Error('malha sem resultado');
        const wsel = curWheel(); const roda = wsel.lado; const pr = perfilParamsFor3d(mi, roda);
        const r = await api.perfil3d({ params: pr });
        const vw = await ensure(); await vw.load(r.glb_url);
        const safe = `${mm.apelido}-${roda}`.replace(/[^\w.-]+/g, '_');
        q('.v-step').href = r.step_url; q('.v-step').download = `${safe}.step`;
        q('.v-glb').href = r.glb_url; q('.v-glb').download = `${safe}.glb`;
        q('.v-stl').href = r.stl_url; q('.v-stl').download = `${safe}.stl`;
        dd.classList.remove('hidden'); dd.dataset.id = r.id;
        q('.v-furo').textContent = r.furo_mm ? `furo do eixo Ø ${fmtNum(r.furo_mm, 2)} mm` : (pr.z < 0 ? '' : 'sem furo (roda maciça)');
        if (r.aviso) toast(r.aviso, true, 8000);
        else toast(`Sólido gerado${r.volume_mm3 ? ` · ${fmtNum(r.volume_mm3 / 1000, 2)} cm³` : ''}`);
      } catch (e) { toast(e.status === 501 ? 'CAD indisponível: instale build123d/cadquery-ocp no venv.' : e.message, true, 7000); }
      finally { btn.disabled = false; btn.textContent = 'Gerar sólido'; }
    });
    q('.v-fit').addEventListener('click', () => viewer && viewer.fit());
    q('.v-cam').addEventListener('click', (e) => { if (!viewer) return; ortho = !ortho; viewer.setCamera(ortho ? 'ortho' : 'persp'); e.target.textContent = ortho ? 'Perspectiva' : 'Ortográfica'; });
    q('.v-meas').addEventListener('click', (e) => { if (!viewer) return; meas = !meas; viewer.setMeasure(meas); e.target.classList.toggle('blue', meas); });
    q('.v-clip').addEventListener('input', (e) => viewer && viewer.setClip(e.target.value / 100));
    q('.v-png').addEventListener('click', () => { if (!viewer) return; const a = document.createElement('a'); a.href = viewer.snapshot(); a.download = 'engrenagem.png'; a.click(); });
  }
  whoRoda(p.querySelector('.r-who'));
  if (viewer) viewer.resize();
  void m;
}
/** Especificação do conjunto completo (todas as malhas calculadas, com a distância entre centros e as rodas de cada uma). */
function specConjunto() {
  if (!S.res || !S.res.malhas || !S.res.malhas.length || S.res.malhas.some(m => !m || m.erro)) return null;
  const ws = wheels(); const byMalha = (i, lado) => ws.find(w => (w.malha === i && w.lado === lado) || (w.extra && w.extra.malha === i && w.extra.lado === lado));
  const roda = (i, lado) => { const w = byMalha(i, lado); const v = S.res.malhas[i].geometria.vars; const nomeBase = w ? (w.estagio ? `${w.base} ${w.idx + 1}` : w.label) : lado;
    return { key: w ? w.key : `m${i}:${lado}`, nome: nomeBase, cor: w ? w.cor : null, params: perfilParamsFor3d(i, lado), z: v[`Z_${lado}`] }; };
  const malhas = S.res.malhas.map((m, i) => ({ a: m.geometria.vars.a, pinhao: roda(i, 'pinhao'), coroa: roda(i, 'coroa') }));
  const pl = S.proj.planetario || {};
  return { nome: S.proj.nome || 'projeto', tipo: S.proj.tipo === 'trem' ? 'trem' : 'planetario', malhas, N_cp: pl.N_cp || null, planetario_tipo: pl.tipo || null };
}
function perfilParamsFor3d(i, roda) { const m = S.res.malhas[i]; const v = m.geometria.vars; const s = roda; const fer = m.geometria[`ferramenta_${s}`] || {};
  return { m_n: v.m_n, z: v[`Z_${s}`], x: v[`x_${s}`], alpha_n: v.alpha_n, beta: v.beta, h_fP_star: fer.cp_dedendo, rho: v[`rk_${s}`] || 0, pr0: fer.pr || 0, q: (v[`op_acabamento_${s}`] === 'Retificação') ? (v[`SM_${s}`] || 0) : 0, d_a: v[`d_a_${s}`], b: v[`b_${s}`], d_i: v[`di_${s}`], d_sh: v[`d_sh_${s}`], membro: v[`membro_${s}`] || null, z0: fer.Z_shaper }; }

// ---------------- Tabelas ----------------
function renderTabelas() {
  const p = panes.tabelas; const i = malhaIdx(); const m = malhaOk(i);
  p.innerHTML = '';
  const tb = document.createElement('div'); tb.className = 'toolbar'; tb.innerHTML = `<b>${m ? m.apelido : '—'}</b><div class="search" style="margin-left:auto;width:260px"><span class="muted">⌕</span><input placeholder="filtrar grandeza…"></div>`; p.appendChild(tb);
  const body = document.createElement('div'); body.className = 'body'; p.appendChild(body);
  if (!m) { body.innerHTML = '<div class="empty" style="margin:20px">Malha sem resultado.</div>'; return; }
  const secs = [...m.geometria.secoes, ...(m.tensoes ? m.tensoes.secoes : [])];
  const draw = (filtro) => {
    body.innerHTML = '';
    for (const s of secs) {
      const linhas = filtro ? s.linhas.filter(l => l.label.toLowerCase().includes(filtro)) : s.linhas; if (!linhas.length) continue;
      const d = document.createElement('details'); d.className = 'sect'; d.open = !!filtro || s === secs[0]; d.innerHTML = `<summary><span>${s.titulo}</span><span class="muted small">${linhas.length}</span></summary>`;
      const t = document.createElement('table'); t.className = 'res'; const hasPc = linhas.some(l => l.pc);
      t.innerHTML = `<thead><tr><th>Grandeza</th>${hasPc ? '<th>Pinhão</th><th>Coroa</th>' : '<th>Valor</th>'}</tr></thead>`;
      const tbody = document.createElement('tbody');
      linhas.forEach(l => { const tr = document.createElement('tr'); const u = l.unit ? `<span class="unit">${l.unit}</span>` : ''; tr.innerHTML = l.pc ? `<td>${l.label}${u}</td><td class="num">${fmtNum(l.pc[0])}</td><td class="num">${fmtNum(l.pc[1])}</td>` : `<td>${l.label}${u}</td><td class="num" ${hasPc ? 'colspan=2' : ''}>${fmtNum(l.v)}</td>`; tbody.appendChild(tr); });
      t.appendChild(tbody); d.appendChild(t); body.appendChild(d);
    }
  };
  tb.querySelector('input').addEventListener('input', (e) => draw(e.target.value.trim().toLowerCase()));
  draw('');
}
