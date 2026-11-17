export function openModal(title, bodyEl) {
  const m = document.getElementById('modal'); document.getElementById('modal-title').textContent = title;
  const b = document.getElementById('modal-body'); b.innerHTML = ''; b.appendChild(bodyEl); m.classList.add('show');
}
export function closeModal() { document.getElementById('modal').classList.remove('show'); }
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('modal-close').addEventListener('click', closeModal);
  document.getElementById('modal').addEventListener('click', (e) => { if (e.target.id === 'modal') closeModal(); });
});
