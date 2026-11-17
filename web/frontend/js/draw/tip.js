// Tooltip HTML flutuante para os esquemas (segue o mouse; não captura eventos)
let box = null;
function ensure() { if (box) return box; box = document.createElement('div'); box.className = 'schtip'; document.body.appendChild(box); return box; }
export function showTip(e, html) {
  const b = ensure(); b.innerHTML = html; b.classList.add('show');
  const w = b.offsetWidth, h = b.offsetHeight; let x = e.clientX + 14, y = e.clientY + 14;
  if (x + w > window.innerWidth - 8) x = e.clientX - w - 14; if (y + h > window.innerHeight - 8) y = e.clientY - h - 14;
  b.style.left = Math.max(4, x) + 'px'; b.style.top = Math.max(4, y) + 'px';
}
export function hideTip() { if (box) box.classList.remove('show'); }
