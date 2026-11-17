// Renderização de resultados: tabelas por seção, cards de segurança, avisos
function fmtNum(v, nd = 4) {
  if (v === null || v === undefined) return '—';
  if (typeof v === 'boolean') return v ? 'sim' : 'não';
  if (typeof v !== 'number') return String(v);
  if (Number.isInteger(v)) return String(v);
  const a = Math.abs(v);
  if (a !== 0 && (a < 1e-3 || a >= 1e7)) return v.toExponential(3);
  let s = v.toFixed(a >= 1000 ? 2 : nd);
  if (s.includes('.')) s = s.replace(/0+$/, '').replace(/\.$/, '');   // remove zeros finais só da parte decimal
  return s === '-0' ? '0' : s;
}
export { fmtNum };

export function tableSection(sec, { pinhaoLabel = 'Pinhão', coroaLabel = 'Coroa', open = false } = {}) {
  const d = document.createElement('details'); d.className = 'sec'; if (open) d.open = true;
  const s = document.createElement('summary'); s.innerHTML = `<span>${sec.titulo}</span>`; d.appendChild(s);
  const body = document.createElement('div'); body.className = 'body';
  const hasPc = sec.linhas.some(l => l.pc);
  const t = document.createElement('table'); t.className = 'res';
  t.innerHTML = `<thead><tr><th>Grandeza</th>${hasPc ? `<th>${pinhaoLabel}</th><th>${coroaLabel}</th>` : '<th>Valor</th>'}</tr></thead>`;
  const tb = document.createElement('tbody');
  for (const l of sec.linhas) {
    const tr = document.createElement('tr');
    const unit = l.unit ? `<span class="unit">${l.unit}</span>` : '';
    if (l.pc) tr.innerHTML = `<td>${l.label}${unit}</td><td class="num">${fmtNum(l.pc[0])}</td><td class="num">${fmtNum(l.pc[1])}</td>`;
    else tr.innerHTML = `<td>${l.label}${unit}</td><td class="num" ${hasPc ? 'colspan="2"' : ''}>${fmtNum(l.v)}</td>`;
    tb.appendChild(tr);
  }
  t.appendChild(tb); body.appendChild(t); d.appendChild(body);
  return d;
}

export function renderSections(container, secoes, opts = {}) {
  const wrap = document.createElement('div'); wrap.className = 'tables';
  secoes.forEach((s, i) => wrap.appendChild(tableSection(s, { ...opts, open: i < 2 })));
  container.appendChild(wrap);
}

export function renderAvisos(container, avisos, titulo = 'Avisos') {
  const box = document.createElement('div'); box.className = 'card white'; box.style.marginBottom = '1rem';
  const h = document.createElement('h3'); h.innerHTML = `<span>${titulo}</span><span class="count">${avisos.length}</span>`; box.appendChild(h);
  if (!avisos.length) { const p = document.createElement('div'); p.className = 'aviso ok'; p.innerHTML = '<span class="ic">✓</span><span>Nenhum aviso.</span>'; box.appendChild(p); }
  else {
    const list = document.createElement('div'); list.className = 'avisos';
    for (const a of avisos) {
      const d = document.createElement('div'); d.className = 'aviso ' + (a.nivel || 'aviso');
      const ic = a.nivel === 'ok' ? '✓' : a.nivel === 'erro' ? '✕' : '!';
      d.innerHTML = `<span class="ic">${ic}</span><span>${a.texto.replace(/^AVISO\s*:\s*/i, '')}</span>`;
      list.appendChild(d);
    }
    box.appendChild(list);
  }
  container.appendChild(box);
}

export function renderSafetyCards(container, cards, titulo) {
  if (titulo) { const h = document.createElement('h3'); h.textContent = titulo; container.appendChild(h); }
  const g = document.createElement('div'); g.className = 'safety';
  for (const c of cards) {
    const d = document.createElement('div'); d.className = 'scard ' + c.status;
    d.innerHTML = `<div class="f">${c.fator} · ${c.roda}</div><div class="v">${fmtNum(c.valor, 3)}</div><div class="m">mínimo ${fmtNum(c.minimo, 2)} · ${
      c.status === 'ok' ? 'atende' : c.status === 'atencao' ? 'margem < 10 %' : c.status === 'ruim' ? 'NÃO atende' : 'n/d'}</div>`;
    g.appendChild(d);
  }
  container.appendChild(g);
}

export function kv(obj) {
  const dl = document.createElement('dl'); dl.className = 'kv';
  for (const [k, v] of Object.entries(obj)) { const dt = document.createElement('dt'); dt.textContent = k; const dd = document.createElement('dd'); dd.textContent = fmtNum(v); dl.appendChild(dt); dl.appendChild(dd); }
  return dl;
}
