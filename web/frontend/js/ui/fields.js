// Campos ligados a um caminho do projeto (binding bidirecional), tooltips "?" com figura e link "saiba mais"
import { S, getPath, setPath, commit } from '../app.js';
import { helpIcon } from '../tooltips.js';

function parse(meta, raw) {
  if (raw === '' || raw == null) return meta.nullable ? null : null;
  if (meta.type === 'int') { const v = parseInt(raw, 10); return Number.isNaN(v) ? null : v; }
  if (meta.type === 'number') { const v = parseFloat(String(raw).replace(',', '.')); return Number.isNaN(v) ? null : v; }
  if (meta.type === 'choice') { const ch = meta.choices || []; return ch.length && typeof ch[0] === 'number' ? Number(raw) : raw; }
  if (meta.type === 'bool') return !!raw;
  return raw;
}
const fmt = (v) => (v == null ? '' : String(v));

/** Campo ligado a `path` no projeto. opts: {meta (do metadata), label, unit, help, auto (texto quando vazio), choices, type, step, min, max, fig, docKey, onChange} */
export function field(path, opts = {}) {
  const meta = Object.assign({}, opts.meta || {}, opts);
  const key = opts.key || path.split('.').pop();
  const wrap = document.createElement('div'); wrap.className = 'fld'; wrap.dataset.path = path;
  const label = document.createElement('label');
  const t = document.createElement('span'); t.className = 't'; t.textContent = meta.label || key; t.title = meta.label || key; label.appendChild(t);
  // tema do Aprender: o informado no campo, senão o do metadata (todo parâmetro conhecido tem um)
  if (meta.help) label.appendChild(helpIcon(Object.assign({}, meta, { docKey: opts.docKey || meta.doc })));
  const ctl = document.createElement('div'); ctl.className = 'ctl';
  let inp;
  if (meta.type === 'choice') {
    inp = document.createElement('select');
    if (meta.nullable) { const o = document.createElement('option'); o.value = ''; o.textContent = meta.auto || '—'; inp.appendChild(o); }
    (meta.choices || []).forEach(c => { const o = document.createElement('option'); o.value = String(c); o.textContent = (meta.labels && meta.labels[c]) || String(c); inp.appendChild(o); });
  } else if (meta.type === 'bool') { inp = document.createElement('input'); inp.type = 'checkbox'; }
  else {
    inp = document.createElement('input'); inp.type = (meta.type === 'number' || meta.type === 'int') ? 'number' : 'text';
    if (meta.type === 'int') inp.step = '1'; else if (meta.type === 'number') inp.step = meta.step || 'any';
    if (meta.min != null) inp.min = meta.min; if (meta.max != null) inp.max = meta.max;
    if (meta.auto) inp.placeholder = meta.auto;
  }
  inp.name = key;
  const R = () => opts.root || S.proj;   // objeto-raiz do caminho (opts.root: estado local, fora do projeto)
  const cur = getPath(R(), path);
  if (meta.type === 'bool') inp.checked = !!cur; else inp.value = fmt(cur);
  if (cur !== undefined && cur !== meta.default && !(cur == null && meta.default == null)) wrap.classList.add('changed');
  const apply = () => {
    const v = parse(meta, meta.type === 'bool' ? inp.checked : inp.value);
    if (v !== null && meta.type !== 'text' && meta.type !== 'choice' && meta.type !== 'bool') {
      if ((meta.min != null && v < meta.min) || (meta.max != null && v > meta.max)) { setErr(wrap, `Fora da faixa (${meta.min ?? '…'} a ${meta.max ?? '…'}).`); return; }
    }
    setErr(wrap, null);
    if (JSON.stringify(getPath(R(), path)) === JSON.stringify(v)) return;
    setPath(R(), path, v); wrap.classList.toggle('changed', v !== meta.default);
    if (opts.onChange) opts.onChange(v);
    if (!opts.root) commit(key);
  };
  inp.addEventListener('input', apply); inp.addEventListener('change', apply);
  ctl.appendChild(inp);
  if (meta.unit) { const u = document.createElement('span'); u.className = 'unit'; u.textContent = meta.unit; ctl.appendChild(u); }
  wrap.appendChild(label); wrap.appendChild(ctl);
  return wrap;
}
export function setErr(wrap, msg) {
  wrap.classList.toggle('err', !!msg);
  let m = wrap.querySelector('.msg');
  if (!msg) { if (m) m.remove(); return; }
  if (!m) { m = document.createElement('div'); m.className = 'msg'; wrap.appendChild(m); }
  m.textContent = msg;
}
/** Aplica erros {caminho: msg} do backend aos campos renderizados (prefixo compatível). */
export function applyErrors(container, erros) {
  container.querySelectorAll('.fld').forEach(f => { if (!f.dataset.path) return; const msg = erros && (erros[f.dataset.path] || erros[f.dataset.path.replace(/^planetario\.(sol|planeta|anelar)\./, 'planetario.$1.')]); if (msg) setErr(f, msg); else if (!f.classList.contains('err') || f.dataset.serverErr) { setErr(f, null); } if (msg) f.dataset.serverErr = '1'; else delete f.dataset.serverErr; });
}

/** Sub-objeto (material/ferramenta/lubrificante): preset ou personalizado. */
export function subobject(path, stage, title) {
  const presets = S.presets[stage] || {};
  const box = document.createElement('div'); box.className = 'sub'; box.dataset.path = path;
  const row = document.createElement('div'); row.className = 'row';
  const b = document.createElement('b'); b.textContent = title;
  const sel = document.createElement('select');
  const oC = document.createElement('option'); oC.value = '__custom__'; oC.textContent = 'Personalizado…'; sel.appendChild(oC);
  Object.keys(presets).sort().forEach(n => { const o = document.createElement('option'); o.value = n; o.textContent = `${presets[n]._apelido || n}`.slice(0, 48); o.title = n; sel.appendChild(o); });
  row.appendChild(b); row.appendChild(sel); box.appendChild(row);
  const fields = document.createElement('div'); fields.className = 'fields'; box.appendChild(fields);
  const cur = getPath(S.proj, path) || {};
  const pref = { material: 'mat_', ferramenta: 'fer_', lubrificante: 'lub_' }[stage];
  const render = () => {
    fields.innerHTML = '';
    const val = getPath(S.proj, path) || {};
    if (val.preset) { sel.value = val.preset; box.classList.remove('custom'); return; }
    sel.value = '__custom__'; box.classList.add('custom');
    for (const [k, meta] of Object.entries(S.meta.params).filter(([, m]) => m.stage === stage)) {
      fields.appendChild(field(`${path}.${k}`, { meta, key: k }));
    }
  };
  sel.addEventListener('change', () => {
    if (sel.value === '__custom__') {
      const base = presets[(getPath(S.proj, path) || {}).preset] || {}; const o = {};
      for (const [k, v] of Object.entries(base)) if (!k.startsWith('_')) o[k] = v;
      setPath(S.proj, path, o);
    } else setPath(S.proj, path, { preset: sel.value });
    commit(stage); render();
  });
  render();
  return box;
}

/** Bloco do inspetor (título + contagem opcional). */
export function block(titulo, cnt) {
  const d = document.createElement('div'); d.className = 'block';
  if (titulo) { const h = document.createElement('h3'); h.innerHTML = `<span>${titulo}</span>${cnt != null ? `<span class="cnt">${cnt}</span>` : ''}`; d.appendChild(h); }
  return d;
}
/** Acordeão "Avançado". */
export function adv(titulo, children, open = false) {
  const d = document.createElement('details'); d.className = 'adv'; if (open) d.open = true;
  d.innerHTML = `<summary>${titulo}<span class="cnt">${children.length} campos</span></summary>`;
  const inner = document.createElement('div'); inner.className = 'inner'; children.forEach(c => inner.appendChild(c)); d.appendChild(inner);
  return d;
}
