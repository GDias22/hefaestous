// Chamadas à API local
async function req(method, url, body) {
  const opt = { method, headers: {} };
  if (body !== undefined) { opt.headers['Content-Type'] = 'application/json'; opt.body = JSON.stringify(body); }
  const r = await fetch(url, opt);
  let data = null;
  const txt = await r.text();
  try { data = txt ? JSON.parse(txt) : null; } catch { data = { detail: txt }; }
  if (!r.ok) {
    const d = data && data.detail !== undefined ? data.detail : data;
    const msg = typeof d === 'string' ? d : (d && (d.mensagem || d.erro)) || JSON.stringify(d);
    const err = new Error(msg); err.detail = d; err.status = r.status; throw err;
  }
  return data;
}
export const api = {
  meta: () => req('GET', '/api/meta/params'),
  presets: () => req('GET', '/api/presets'),
  sessoes: () => req('GET', '/api/sessoes'),
  sessao: (id) => req('GET', `/api/sessoes/${id}`),
  geometria: (body) => req('POST', '/api/geometria', body),
  tensoes: (body) => req('POST', '/api/tensoes', body),
  cinJobStart: (body) => req('POST', '/api/cinematica/jobs', body),
  cinJob: (id) => req('GET', `/api/cinematica/jobs/${id}`),
  cinJobResult: (id, limit = 300) => req('GET', `/api/cinematica/jobs/${id}/result?limit=${limit}`),
  cinJobCancel: (id) => req('DELETE', `/api/cinematica/jobs/${id}`),
  cinPrefill: (body) => req('POST', '/api/cinematica/prefill', body),
  perfil2d: (body) => req('POST', '/api/perfil/2d', body),
  perfil3d: (body) => req('POST', '/api/perfil/3d', body),
  perfil3dConjunto: (body) => req('POST', '/api/perfil/3d/conjunto', body),
  sobremetal: (body) => req('POST', '/api/perfil/sobremetal', body),
  projetoPadrao: (tipo) => req('GET', `/api/projeto/padrao/${tipo}`),
  projetoVocabulario: () => req('GET', '/api/projeto/vocabulario'),
  projetoCalcular: (body) => req('POST', '/api/projeto/calcular', body),
  projetoSalvar: (body) => req('POST', '/api/projeto/salvar', body),
  projetoCarregar: (id) => req('GET', `/api/projeto/${id}`),
  femEmpacotar: (body) => req('POST', '/api/fem/empacotar', body),
  femLer: (body) => req('POST', '/api/fem/ler', body),
  layoutPadrao: (body) => req('POST', '/api/projeto/layout_padrao', body),
  explicar: (body) => req('POST', '/api/projeto/explicar', body),
  buscaTrem: (body) => req('POST', '/api/projeto/busca_trem', body),
  sensibilidade: (body) => req('POST', '/api/projeto/sensibilidade', body),
  docs: (chave) => req('GET', `/api/docs/${chave}`),
  docsIndex: () => req('GET', '/api/docs'),
  updateCheck: (forcar = false) => req('GET', `/api/update/check${forcar ? '?forcar=true' : ''}`),
  updateApply: () => req('POST', '/api/update/apply'),
  vidaPing: () => req('POST', '/api/vida/ping'),
};
