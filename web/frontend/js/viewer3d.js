// Visualizador 3D (three.js): GLB, órbita, orto/persp, medição por 2 cliques, plano de corte com tampa (sólido, não casca),
// tríade de eixos XYZ no canto inferior esquerdo que acompanha a câmera.
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

export function createViewer(container) {
  const W = () => container.clientWidth || 800, H = () => container.clientHeight || 520;
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, preserveDrawingBuffer: true, stencil: true });
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio)); renderer.setSize(W(), H());
  renderer.localClippingEnabled = true; renderer.autoClear = false;
  container.appendChild(renderer.domElement);
  const scene = new THREE.Scene(); scene.background = new THREE.Color(0xf7f8fa);
  const persp = new THREE.PerspectiveCamera(40, W() / H(), 0.1, 10000);
  const ortho = new THREE.OrthographicCamera(-100, 100, 100, -100, -5000, 5000);
  let camera = persp;
  const controls = new OrbitControls(camera, renderer.domElement); controls.enableDamping = true; controls.dampingFactor = 0.12;
  // ---- mouse no padrão SolidWorks: botão do MEIO orbita; Ctrl+meio desloca (pan); Shift+meio = zoom arrastando; roda = zoom no
  // ponto sob o cursor (para frente AFASTA, como o padrão do SW — invertível); duplo clique do meio = enquadrar.
  // Botão esquerdo também orbita (notebook sem botão do meio) e o direito desloca; o clique esquerdo simples continua medindo.
  controls.mouseButtons = { LEFT: THREE.MOUSE.ROTATE, MIDDLE: THREE.MOUSE.ROTATE, RIGHT: THREE.MOUSE.PAN };
  controls.zoomToCursor = true; controls.rotateSpeed = 0.9; controls.panSpeed = 1.0; controls.screenSpacePanning = true;
  let zoomInvertido = localStorage.getItem('engr.zoomSW') !== '0';           // padrão SW: roda para frente afasta
  const aplicarZoom = () => { controls.zoomSpeed = zoomInvertido ? -1.0 : 1.0; };
  aplicarZoom();
  let ultimoMeio = 0;
  renderer.domElement.addEventListener('pointerdown', (e) => {
    if (e.button !== 1) return;
    controls.mouseButtons.MIDDLE = e.shiftKey ? THREE.MOUSE.DOLLY : THREE.MOUSE.ROTATE;      // Ctrl+meio vira pan dentro do ROTATE
  }, true);
  renderer.domElement.addEventListener('mousedown', (e) => { if (e.button === 1) e.preventDefault(); });   // sem auto-rolagem do Chrome
  renderer.domElement.addEventListener('auxclick', (e) => { if (e.button === 1) e.preventDefault(); });
  renderer.domElement.addEventListener('pointerup', (e) => {
    if (e.button !== 1) return;
    const t = performance.now(); if (t - ultimoMeio < 350) { fit(); ultimoMeio = 0; } else ultimoMeio = t;
  });
  scene.add(new THREE.HemisphereLight(0xffffff, 0x8899aa, 1.1));
  const dl = new THREE.DirectionalLight(0xffffff, 1.2); dl.position.set(1, 1.5, 2); scene.add(dl);
  const dl2 = new THREE.DirectionalLight(0xffffff, 0.5); dl2.position.set(-2, -1, -1); scene.add(dl2);
  const grid = new THREE.GridHelper(200, 20, 0xcccccc, 0xe5e5e5); grid.rotation.x = Math.PI / 2; grid.visible = false; scene.add(grid);

  // ---- tríade de eixos (canto inferior esquerdo): cena própria, câmera ortográfica que copia a orientação da câmera principal.
  // Z = eixo da roda (como no cálculo), X e Y no plano transversal.
  const TRI = 96;                                                   // px
  const triScene = new THREE.Scene();
  const triCam = new THREE.OrthographicCamera(-1.6, 1.6, 1.6, -1.6, 0.1, 10);
  const axisColor = { x: 0xb8282c, y: 0x1f7a34, z: 0x0b4fa8 };
  function arrow(dir, color) {
    const g = new THREE.Group();
    const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 0.78, 12), new THREE.MeshBasicMaterial({ color }));
    shaft.position.y = 0.39;
    const tip = new THREE.Mesh(new THREE.ConeGeometry(0.12, 0.26, 16), new THREE.MeshBasicMaterial({ color })); tip.position.y = 0.91;
    g.add(shaft, tip); g.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir);
    return g;
  }
  function label(txt, color, dir) {
    const c = document.createElement('canvas'); c.width = c.height = 64; const ctx = c.getContext('2d');
    ctx.font = 'bold 44px Inter, Segoe UI, sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillStyle = '#' + color.toString(16).padStart(6, '0'); ctx.fillText(txt, 32, 34);
    const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(c), depthTest: false, transparent: true }));
    sp.scale.setScalar(0.42); sp.position.copy(dir).multiplyScalar(1.3); return sp;
  }
  triScene.add(new THREE.Mesh(new THREE.SphereGeometry(0.08, 16, 16), new THREE.MeshBasicMaterial({ color: 0x4b5560 })));
  [['x', new THREE.Vector3(1, 0, 0)], ['y', new THREE.Vector3(0, 1, 0)], ['z', new THREE.Vector3(0, 0, 1)]].forEach(([k, d]) => {
    triScene.add(arrow(d, axisColor[k])); triScene.add(label(k.toUpperCase(), axisColor[k], d));
  });

  let model = null, bbox = null, clipping = false;
  const clipPlane = new THREE.Plane(new THREE.Vector3(0, 0, -1), 1e9);
  const measure = { pts: [], markers: [], line: null, label: null, active: false };
  const overlay = document.createElement('div'); overlay.style.cssText = 'position:absolute;left:110px;bottom:.5rem;background:rgba(255,255,255,.92);border:1px solid #d9dde2;border-radius:6px;padding:.3rem .55rem;font-size:.78rem;font-family:Inter,sans-serif;color:#353c43;pointer-events:none;display:none';
  container.style.position = 'relative'; container.appendChild(overlay);

  const raycaster = new THREE.Raycaster();
  const mat = new THREE.MeshStandardMaterial({ color: 0x8e9aab, metalness: 0.55, roughness: 0.35, side: THREE.DoubleSide, clippingPlanes: [clipPlane], clipShadows: true });
  const mats = [mat];                                                        // materiais ativos (um por cor de peça, no conjunto)
  const GRAY = 0x8e9aab;
  /** Material da peça: cor do GLB (conjunto: uma cor por roda) ou o cinza padrão; cores são clareadas para ler bem no fundo claro. */
  function matFor(srcMat) {
    const c = srcMat && srcMat.color && !(srcMat.color.r > 0.78 && srcMat.color.g > 0.78 && srcMat.color.b > 0.78) ? srcMat.color.clone().lerp(new THREE.Color(0xffffff), 0.35) : null;
    if (!c) return mat;
    const m = new THREE.MeshStandardMaterial({ color: c, metalness: 0.45, roughness: 0.4, side: THREE.DoubleSide, clippingPlanes: [clipPlane], clipShadows: true });
    mats.push(m); return m;
  }
  // ---- tampa do corte (técnica de stencil): faces traseiras incrementam, frontais decrementam; onde sobra ≠ 0 o plano de corte
  // está "dentro" do sólido e um quad no plano é pintado com a cor da seção. Assim o corte mostra material, não uma casca oca.
  const stencilBase = { clippingPlanes: [clipPlane], stencilWrite: true, stencilFunc: THREE.AlwaysStencilFunc, depthWrite: false, depthTest: false, colorWrite: false };
  const matBack = new THREE.MeshBasicMaterial({ ...stencilBase, side: THREE.BackSide, stencilFail: THREE.IncrementWrapStencilOp, stencilZFail: THREE.IncrementWrapStencilOp, stencilZPass: THREE.IncrementWrapStencilOp });
  const matFront = new THREE.MeshBasicMaterial({ ...stencilBase, side: THREE.FrontSide, stencilFail: THREE.DecrementWrapStencilOp, stencilZFail: THREE.DecrementWrapStencilOp, stencilZPass: THREE.DecrementWrapStencilOp });
  const capMat = new THREE.MeshStandardMaterial({ color: 0xc9a46a, metalness: 0.2, roughness: 0.6, stencilWrite: true, stencilRef: 0, stencilFunc: THREE.NotEqualStencilFunc, stencilFail: THREE.ReplaceStencilOp, stencilZFail: THREE.ReplaceStencilOp, stencilZPass: THREE.ReplaceStencilOp });
  const cap = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), capMat); cap.renderOrder = 1; cap.visible = false; scene.add(cap);
  const stencilGroup = new THREE.Group(); stencilGroup.visible = false; scene.add(stencilGroup);

  function fit() {
    if (!bbox) return;
    const size = bbox.getSize(new THREE.Vector3()); const center = bbox.getCenter(new THREE.Vector3());
    const r = size.length() / 2;
    controls.target.copy(center);
    persp.position.copy(center).add(new THREE.Vector3(r * 1.2, -r * 1.6, r * 1.3)); persp.near = r / 100; persp.far = r * 50; persp.updateProjectionMatrix();
    const a = W() / H(); ortho.left = -r * a; ortho.right = r * a; ortho.top = r; ortho.bottom = -r; ortho.position.copy(persp.position); ortho.updateProjectionMatrix();
    grid.scale.setScalar(r / 100); grid.position.copy(center); grid.position.z = bbox.min.z - 0.01;
    cap.scale.set(size.x * 1.2, size.y * 1.2, 1); cap.position.set(center.x, center.y, cap.position.z);
    controls.update();
  }
  function setCamera(type) {
    const pos = camera.position.clone(); camera = type === 'ortho' ? ortho : persp; camera.position.copy(pos); camera.lookAt(controls.target);
    controls.object = camera; controls.update();
  }
  function clearModel() {
    if (model) { scene.remove(model); model.traverse(o => { if (o.geometry) o.geometry.dispose(); }); model = null; bbox = null; }
    mats.splice(1).forEach(m => m.dispose());
    stencilGroup.clear(); cap.visible = false; clipping = false; clearMeasure();
  }
  function load(url) {
    return new Promise((resolve, reject) => {
      new GLTFLoader().load(url, (g) => {
        clearModel();
        // build123d exporta glTF em METROS e com rotação Y-up (−90° em X). Desfaz a rotação dos nós e converte para mm,
        // de modo que o modelo fique em mm com o eixo da engrenagem em +Z, como no cálculo.
        const src = g.scene; src.updateMatrixWorld(true);
        model = new THREE.Group();
        src.traverse(o => {
          if (!o.isMesh) return;
          const geom = o.geometry.clone(); geom.applyMatrix4(o.matrixWorld);                 // posição mundial (Y-up, m)
          geom.applyMatrix4(new THREE.Matrix4().makeRotationX(Math.PI / 2));                // Y-up -> Z-up
          geom.scale(1000, 1000, 1000);                                                      // m -> mm
          geom.computeVertexNormals();
          model.add(new THREE.Mesh(geom, matFor(o.material)));
          stencilGroup.add(new THREE.Mesh(geom, matBack), new THREE.Mesh(geom, matFront));
        });
        scene.add(model); bbox = new THREE.Box3().setFromObject(model); fit();
        clipPlane.constant = bbox.max.z + 1; resolve(bbox);
      }, undefined, reject);
    });
  }
  function clearMeasure() {
    measure.markers.forEach(m => scene.remove(m)); measure.markers = []; measure.pts = [];
    if (measure.line) { scene.remove(measure.line); measure.line = null; }
    overlay.style.display = 'none';
  }
  function onClick(ev) {
    if (!measure.active || !model) return;
    const r = renderer.domElement.getBoundingClientRect();
    const m = new THREE.Vector2(((ev.clientX - r.left) / r.width) * 2 - 1, -((ev.clientY - r.top) / r.height) * 2 + 1);
    raycaster.setFromCamera(m, camera);
    const hits = raycaster.intersectObject(model, true).filter(h => !clipping || clipPlane.distanceToPoint(h.point) >= -1e-6);
    if (!hits.length) return;
    const p = hits[0].point.clone();
    if (measure.pts.length === 2) clearMeasure();
    measure.pts.push(p);
    const s = bbox ? bbox.getSize(new THREE.Vector3()).length() / 250 : 0.5;
    const mk = new THREE.Mesh(new THREE.SphereGeometry(s, 16, 16), new THREE.MeshBasicMaterial({ color: 0xb8282c })); mk.position.copy(p); scene.add(mk); measure.markers.push(mk);
    if (measure.pts.length === 2) {
      const [a, b] = measure.pts;
      measure.line = new THREE.Line(new THREE.BufferGeometry().setFromPoints([a, b]), new THREE.LineBasicMaterial({ color: 0xb8282c })); scene.add(measure.line);
      const d = a.distanceTo(b); const dv = b.clone().sub(a);
      overlay.innerHTML = `<b>Distância: ${d.toFixed(3)} mm</b><br>Δx ${dv.x.toFixed(3)} · Δy ${dv.y.toFixed(3)} · Δz ${dv.z.toFixed(3)}<br>r₁ ${Math.hypot(a.x, a.y).toFixed(3)} · r₂ ${Math.hypot(b.x, b.y).toFixed(3)} (raios ao eixo)`;
      overlay.style.display = '';
    } else {
      overlay.innerHTML = `P₁ (${p.x.toFixed(3)}, ${p.y.toFixed(3)}, ${p.z.toFixed(3)}) · r = ${Math.hypot(p.x, p.y).toFixed(3)} mm — clique no 2º ponto`; overlay.style.display = '';
    }
  }
  renderer.domElement.addEventListener('click', onClick);
  function setClip(frac) { // 0..1 ao longo de z (eixo da roda)
    if (!bbox) return; clipping = frac < 0.999;
    const zc = bbox.min.z + (bbox.max.z - bbox.min.z) * frac;
    clipPlane.constant = zc + (clipping ? 0 : 1);
    cap.visible = clipping; stencilGroup.visible = clipping; cap.position.z = zc - 1e-3 * (bbox.max.z - bbox.min.z);
  }
  function resize() { const w = W(), h = H(); renderer.setSize(w, h); persp.aspect = w / h; persp.updateProjectionMatrix(); const a = w / h; const r = ortho.top; ortho.left = -r * a; ortho.right = r * a; ortho.updateProjectionMatrix(); }
  window.addEventListener('resize', resize);
  let running = true;
  function render() {
    renderer.clear(true, true, true);
    renderer.setViewport(0, 0, W(), H()); renderer.setScissorTest(false);
    renderer.render(scene, camera);
    // tríade: mesma orientação da câmera principal, olhando para a origem
    triCam.position.copy(camera.position).sub(controls.target).normalize().multiplyScalar(5); triCam.quaternion.copy(camera.quaternion);
    renderer.clearDepth(); renderer.setViewport(8, 8, TRI, TRI); renderer.setScissor(8, 8, TRI, TRI); renderer.setScissorTest(true);
    renderer.render(triScene, triCam); renderer.setScissorTest(false);
  }
  (function loop() { if (!running) return; requestAnimationFrame(loop); controls.update(); render(); })();
  return {
    load, fit, setCamera, setClip, clearMeasure, resize,
    setMeasure(on) { measure.active = on; renderer.domElement.style.cursor = on ? 'crosshair' : ''; if (!on) clearMeasure(); },
    setGrid(on) { grid.visible = on; },
    setColor(hex) { mat.color.set(hex); },
    isAssembly() { return mats.length > 1; },
    zoomInvertido() { return zoomInvertido; },
    setZoomInvertido(on) { zoomInvertido = !!on; localStorage.setItem('engr.zoomSW', on ? '1' : '0'); aplicarZoom(); },
    snapshot() { render(); return renderer.domElement.toDataURL('image/png'); },
    dispose() { running = false; clearModel(); controls.dispose(); renderer.dispose(); renderer.forceContextLoss(); renderer.domElement.remove(); overlay.remove(); window.removeEventListener('resize', resize); },
  };
}
