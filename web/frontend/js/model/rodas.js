// Rodas do projeto: identidade, cor, malha/lado e seleção. Fonte única para esquema, árvore, inspetor, resultados e perfis.
import { S } from '../app.js';

export const COR = { pinhao: '#b8282c', coroa: '#003882', interna: '#1f7a34', sol: '#b8282c', planeta_maior: '#003882', planeta_menor: '#0e8aa6', anelar: '#1f7a34', carrier: '#7c8792' };
export const WHEEL_KINDS = ['estagio', 'sol', 'planeta_maior', 'planeta_menor', 'anelar'];
export const isWheelKind = (k) => WHEEL_KINDS.includes(k);
export const keyTrem = (i, r) => `estagio:${i}:${r}`;
const absz = (v) => (v == null ? null : Math.abs(v));

/** Todas as rodas do projeto, na ordem do fluxo de potência. */
export function wheels(p = S.proj) {
  if (!p) return [];
  if (p.tipo === 'trem') {
    return (p.estagios || []).flatMap((e, i) => {
      const m = e.malha || {}; const interna = m.Z_coroa < 0; const nome = e.nome || `Estágio ${i + 1}`;
      return [
        { key: keyTrem(i, 'pinhao'), kind: 'estagio', idx: i, roda: 'pinhao', malha: i, lado: 'pinhao', base: 'Pinhão', label: `Pinhão ${i + 1}`, curto: `P${i + 1}`, cor: COR.pinhao, z: absz(m.Z_pinhao), estagio: nome },
        { key: keyTrem(i, 'coroa'), kind: 'estagio', idx: i, roda: 'coroa', malha: i, lado: 'coroa', base: interna ? 'Anelar' : 'Coroa', label: `${interna ? 'Anelar' : 'Coroa'} ${i + 1}`, curto: `${interna ? 'A' : 'C'}${i + 1}`, cor: interna ? COR.interna : COR.coroa, z: absz(m.Z_coroa), interna, estagio: nome },
      ];
    });
  }
  const pl = p.planetario; if (!pl) return [];
  const comp = pl.tipo === 'Composto';
  const w = [
    { key: 'sol', kind: 'sol', idx: 0, roda: null, malha: 0, lado: 'pinhao', base: 'Sol', label: 'Sol', curto: 'S', cor: COR.sol, z: absz(pl.sol && pl.sol.z) },
    { key: 'planeta_maior', kind: 'planeta_maior', idx: 0, roda: null, malha: 0, lado: 'coroa', extra: comp ? null : { malha: 1, lado: 'pinhao' }, base: comp ? 'Planeta maior' : 'Planeta', label: comp ? 'Planeta maior' : 'Planeta', curto: comp ? 'PM' : 'P', cor: COR.planeta_maior, z: absz(pl.planeta_maior && pl.planeta_maior.z) },
  ];
  if (comp) w.push({ key: 'planeta_menor', kind: 'planeta_menor', idx: 0, roda: null, malha: 1, lado: 'pinhao', base: 'Planeta menor', label: 'Planeta menor', curto: 'Pm', cor: COR.planeta_menor, z: absz(pl.planeta_menor && pl.planeta_menor.z) });
  w.push({ key: 'anelar', kind: 'anelar', idx: 0, roda: null, malha: 1, lado: 'coroa', base: 'Anelar', label: 'Anelar', curto: 'A', cor: COR.anelar, z: absz(pl.anelar && pl.anelar.z) });
  return w;
}
export function keyOfSel(sel) { return sel.kind === 'estagio' ? keyTrem(sel.idx, sel.roda || 'pinhao') : sel.kind; }
export function wheelByKey(key, p) { return wheels(p).find(w => w.key === key) || null; }
export function wheelOf(sel, p) { return sel && isWheelKind(sel.kind) ? wheelByKey(keyOfSel(sel), p) : null; }
export const selFromWheel = (w) => ({ kind: w.kind, idx: w.idx, roda: w.roda });
/** Roda "em foco": a selecionada; se o passo atual não é uma roda, a última selecionada; senão a primeira. */
export function curWheel() { return wheelOf(S.sel) || wheelOf(S.wheel) || wheels()[0] || null; }
export function defaultSel(p) { return p.tipo === 'trem' ? { kind: 'estagio', idx: 0, roda: 'pinhao' } : { kind: 'sol', idx: 0, roda: null }; }

export const ladoCard = (lado) => (lado === 'pinhao' ? 'pinhão' : 'coroa');
/** Cartões de segurança (S_H/S_F) da roda; no planetário simples o planeta aparece nas duas malhas. */
export function cardsOf(w) {
  const out = [];
  const add = (malha, lado) => { const m = S.res && S.res.malhas && S.res.malhas[malha]; ((m && m.cards) || []).forEach(c => { if (c.roda === ladoCard(lado)) out.push({ ...c, malha }); }); };
  add(w.malha, w.lado); if (w.extra) add(w.extra.malha, w.extra.lado);
  return out;
}
export function minSeg(w) {
  const cs = cardsOf(w); const pick = (f) => { const v = cs.filter(c => c.fator === f && c.valor != null).map(c => c.valor); return v.length ? Math.min(...v) : null; };
  return { SH: pick('S_H'), SF: pick('S_F') };
}
const NOMES = { arquitetura: 'Arquitetura', entrada: 'Entrada', dentes: 'Busca de dentes', layout: 'Layout de eixos e mancais', operacao: 'Operação e materiais', analise: 'Análise ISO 6336', saida: 'Saída', carrier: 'Porta-planetas e cinemática' };
/** Texto do selo "Editando: …" (cor só quando é uma roda). */
export function selInfo() {
  const w = wheelOf(S.sel);
  if (w) return { cor: w.cor, titulo: w.estagio ? `${w.estagio} › ${w.base}` : w.label, sub: `z ${w.z}`, roda: true };
  return { cor: null, titulo: NOMES[S.sel.kind] || S.sel.kind, sub: '', roda: false };
}
/** Planeta menor ausente (ex.: projeto que era Simples): cria a partir do planeta maior. */
export function ensurePlanetas(pl) {
  if (!pl.planeta_maior) pl.planeta_maior = {};
  if (!pl.planeta_menor || !Object.keys(pl.planeta_menor).length) pl.planeta_menor = { ...JSON.parse(JSON.stringify(pl.planeta_maior)) };
}
