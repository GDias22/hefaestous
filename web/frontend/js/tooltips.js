// Tooltip "?" com título, explicação, unidade, faixa, figura e link "saiba mais" (abre o painel Explicar/Aprender)
let pop = null, hideTimer = null;
function ensure() {
  if (pop) return pop;
  pop = document.createElement('div'); pop.className = 'popover';
  pop.addEventListener('mouseenter', () => clearTimeout(hideTimer));
  pop.addEventListener('mouseleave', hide);
  document.body.appendChild(pop);
  document.addEventListener('scroll', hide, true);
  return pop;
}
function hide() { if (pop) pop.classList.remove('show'); }
export function showHelp(anchor, meta) {
  const p = ensure();
  const faixa = (meta.min != null || meta.max != null) ? `Faixa: ${meta.min ?? '…'} a ${meta.max ?? '…'}` : '';
  const def = meta.default != null && meta.default !== '' ? `Padrão: ${meta.default}` : 'Padrão: automático';
  p.innerHTML = `<h4>${meta.label || ''}${meta.unit ? ` <small>[${meta.unit}]</small>` : ''}</h4><div>${meta.help || ''}</div>
    <div class="meta"><span>${def}</span>${faixa ? `<span>${faixa}</span>` : ''}</div>
    ${meta.fig ? `<img src="/api/figuras/${meta.fig}" alt="">` : ''}
    ${meta.docKey ? `<div class="more"><a href="#" class="doc-link" data-doc="${meta.docKey}">📖 Ver no Aprender: explicação completa ›</a></div>` : ''}`;
  const a = p.querySelector('[data-doc]'); if (a) a.addEventListener('click', (e) => { e.preventDefault(); hide(); document.dispatchEvent(new CustomEvent('open-doc', { detail: meta.docKey })); });
  p.classList.add('show');
  const r = anchor.getBoundingClientRect(); const pw = Math.min(360, window.innerWidth - 24);
  let left = r.left - pw - 8; if (left < 8) left = Math.min(r.right + 8, window.innerWidth - pw - 8);
  p.style.left = left + 'px'; p.style.top = Math.max(8, r.top - 8) + 'px'; p.style.maxWidth = pw + 'px';
  requestAnimationFrame(() => { const h = p.offsetHeight; if (r.top - 8 + h > window.innerHeight - 12) p.style.top = Math.max(8, window.innerHeight - h - 12) + 'px'; });
}
export function helpIcon(meta) {
  const s = document.createElement('span'); s.className = 'help'; s.textContent = '?'; s.tabIndex = 0; s.setAttribute('role', 'button');
  s.addEventListener('mouseenter', () => { clearTimeout(hideTimer); showHelp(s, meta); });
  s.addEventListener('mouseleave', () => { hideTimer = setTimeout(hide, 300); });
  s.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); showHelp(s, meta); });
  return s;
}
document.addEventListener('click', (e) => { if (pop && !pop.contains(e.target) && !e.target.classList.contains('help')) hide(); });
