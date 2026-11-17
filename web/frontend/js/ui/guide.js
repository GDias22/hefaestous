// Modo guiado: checklist de 7 passos (mesma ordem do fluxo do projeto) com conclusão automática pelos dados; tour de primeira abertura
import { S, on, select } from '../app.js';

const roda1 = () => (S.proj.tipo === 'trem' ? select('estagio', 0, 'pinhao') : select('sol'));
const STEPS = [
  { id: 'arquitetura', t: '1 · Arquitetura', d: 'Escolha trem de engrenagens ou planetário (simples/composto), o número de planetas, quem recebe e quem entrega o torque, e a redução alvo. Tudo o mais depende disso.', go: () => select('arquitetura'), done: (p) => !!p.entrada.i_alvo && (p.tipo === 'trem' ? p.estagios.length > 0 : !!(p.planetario && p.planetario.entrada !== p.planetario.saida)) },
  { id: 'entrada', t: '2 · Entrada', d: 'Informe rotação e torque de entrada e as irregularidades das máquinas (define K_A). A redução alvo e, no planetário, quem recebe/entrega o torque ficam na Arquitetura.', go: () => select('entrada'), done: (p) => p.entrada.n > 0 && p.entrada.T > 0 },
  { id: 'dentes', t: '3 · Buscar números de dentes', d: 'Rode a busca, compare os candidatos e veja o esboço de cada um. "Usar este candidato" preenche sol, planetas e anelar (ou os estágios do trem).', go: () => select('dentes'), done: () => !!S.flags.dentes },
  { id: 'rodas', t: '4 · Rodas: módulo, largura e perfil', d: 'Clique numa roda no esquema para editá-la (largura, qualidade, material, ferramenta). Na aba "Dente" confira undercut, interferência e recobrimento.', go: roda1, done: (p, r) => !!(r && r.ok && r.malhas.every(m => !(m.avisos || []).some(a => /undercut|interfer|recobrimento/i.test(a.texto)))) },
  { id: 'layout', t: '5 · Layout de eixos e mancais', d: 'Defina o diâmetro do eixo, o vão entre mancais e a posição de cada roda (arraste no desenho). O programa deduz s, o arranjo físico e K′; ative para valer nos cálculos.', go: () => select('layout'), done: (p) => !!(p.layout && p.layout.ativo) },
  { id: 'operacao', t: '6 · Operação e materiais', d: 'Vida requerida, seguranças mínimas, lubrificante e temperaturas. Esses dados entram em Z_NT, Y_NT, Z_R e K_v.', go: () => select('operacao'), done: (p) => (p.operacao.Vr || 0) > 0 },
  { id: 'resistencia', t: '7 · Verificar resistência', d: 'Todas as seguranças S_H e S_F devem atender aos mínimos. Clique em "por quê?" para entender cada fator e use a sensibilidade para decidir o que mudar.', go: roda1, done: (p, r) => !!(r && r.resumo && r.resumo.todos_atendem) },
  { id: 'relatorio', t: '8 · Salvar e gerar relatório', d: 'Salve o projeto (Ctrl+S) e gere o relatório HTML/PDF, o STEP das rodas e as planilhas.', go: () => document.getElementById('b-relatorio').focus(), done: () => !!S.session_id && !S.dirty },
];
let root, cur = 0;
export function init() {
  root = document.getElementById('guide');
  document.addEventListener('modo', (e) => { root.classList.toggle('show', e.detail === 'guiado'); render(); });
  on(ev => { if (['result', 'saved', 'load'].includes(ev.type)) render(); });
}
function render() {
  if (!root.classList.contains('show') || !S.proj) return;
  root.innerHTML = '<h3 style="margin-bottom:6px">Passo a passo</h3>';
  const st = document.createElement('div'); st.className = 'steps';
  STEPS.forEach((s, i) => {
    const done = (() => { try { return s.done(S.proj, S.res); } catch { return false; } })();
    const d = document.createElement('div'); d.className = 'gstep' + (done ? ' done' : '') + (i === cur ? ' on' : '');
    d.innerHTML = `<span class="n">${done ? '✓' : i + 1}</span><span class="txt"><b>${s.t}</b><small>${s.d}</small></span>`;
    d.addEventListener('click', () => { cur = i; s.go(); render(); });
    st.appendChild(d);
  });
  root.appendChild(st);
}
export function maybeTour() {
  if (localStorage.getItem('engr.tour') === '1') return;
  const steps = [
    ['#tree', 'Fluxo do projeto', 'A árvore é a única navegação: 1 Arquitetura → 2 Entrada → 3 Busca de dentes → 4 Rodas (cada engrenagem separada, com cor própria) → 5 Layout de eixos → 6 Operação → 7 Análise ISO.'],
    ['#inspector', 'Inspetor', 'Os campos essenciais aparecem primeiro; o restante fica em "Avançado", já com valores padrão. Tudo recalcula enquanto você digita. O "?" explica cada parâmetro.'],
    ['#tabs', 'Vistas do centro', 'O trilho à esquerda diz em que passo você está. Os botões são só vistas do mesmo projeto: Esquema, Dente, Roda 2D, 3D e Tabelas seguem a roda selecionada; Arquitetura, Busca de dentes e Layout têm painel próprio ao serem escolhidos na árvore.'],
  ];
  let i = 0; let box = null;
  const show = () => {
    if (box) box.remove(); document.querySelectorAll('.hl').forEach(e => e.classList.remove('hl'));
    if (i >= steps.length) { localStorage.setItem('engr.tour', '1'); return; }
    const [sel, t, d] = steps[i]; const target = document.querySelector(sel); if (!target) { i++; show(); return; }
    target.classList.add('hl'); const r = target.getBoundingClientRect();
    box = document.createElement('div'); box.className = 'tour'; box.innerHTML = `<b>${t}</b>${d}<div class="acts"><button class="btn sm ghost">Pular</button><button class="btn sm">${i === steps.length - 1 ? 'Concluir' : 'Próximo'}</button></div>`;
    box.style.left = Math.min(window.innerWidth - 350, r.left + 20) + 'px'; box.style.top = Math.min(window.innerHeight - 180, r.top + 60) + 'px';
    box.querySelector('.ghost').addEventListener('click', () => { i = steps.length; show(); }); box.querySelectorAll('.btn')[1].addEventListener('click', () => { i++; show(); });
    document.body.appendChild(box);
  };
  setTimeout(show, 900);
}
