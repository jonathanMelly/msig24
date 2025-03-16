<!-- EventPropagationDemo.vue -->
<template>
  <div class="propagation-demo">
    <div class="controls mb-4">
      <button @click="clearLogs" class="demo-btn mr-2">Effacer journal</button>
      <button @click="resetDemo" class="demo-btn">Réinitialiser démo</button>
    </div>

    <div class="demo-flex">
      <div class="demo-area">
        <div
            ref="grandparent"
            class="grandparent"
            :class="{ 'highlight': highlightGrandparent }"
            @click="handleClick($event, 'grandparent')"
        >
          Grand-parent
          <div
              ref="parent"
              class="parent"
              :class="{ 'highlight': highlightParent }"
              @click="handleClick($event, 'parent')"
          >
            Parent
            <button
                ref="child"
                class="child"
                :class="{ 'highlight': highlightChild }"
                @click="handleClick($event, 'child')"
            >
              Cliquez-moi
            </button>
          </div>
        </div>
      </div>

      <div class="log-area">
        <div class="options mb-2">
          <label class="mr-4">
            <input type="checkbox" v-model="useCapture" @change="resetDemo">
            Activer phase de capture
          </label>
          <label>
            <input type="checkbox" v-model="stopPropagation">
            Arrêter la propagation
          </label>
        </div>

        <div class="phases-diagram">
          <div class="phase-arrow">
            <div class="arrow down" :class="{ 'active': phaseCapture }">↓</div>
            <div class="phase-name">Capture</div>
          </div>
          <div class="phase-arrow">
            <div class="arrow up" :class="{ 'active': phaseBubbling }">↑</div>
            <div class="phase-name">Bouillonnement</div>
          </div>
        </div>

        <div class="log-panel" ref="logPanel">
          <div v-if="logs.length === 0" class="text-center text-gray-500 my-4">
            Cliquez sur l'élément pour voir la propagation
          </div>
          <div v-for="(log, index) in logs" :key="index" :class="['log-entry', log.phase]">
            <span class="element-name">{{ log.element }}</span>
            <span class="phase-label">{{ log.phase === 'capture' ? 'capture ↓' : 'bubbling ↑' }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="info-box mt-4">
      <h3 class="text-lg font-semibold mb-2">Comment ça marche :</h3>
      <ul class="text-sm text-gray-700">
        <li><strong>Phase de capture</strong> : l'événement descend dans le DOM (window → cible)</li>
        <li><strong>Phase de bouillonnement</strong> : l'événement remonte (cible → window)</li>
        <li>Le troisième paramètre de <code>addEventListener(event, handler, useCapture)</code> détermine la phase</li>
        <li><code>useCapture = true</code> : écoute pendant la phase de capture (descente)</li>
        <li><code>useCapture = false</code> : écoute pendant la phase de bouillonnement (remontée, par défaut)</li>
        <li><code>event.stopPropagation()</code> arrête la propagation aux éléments parents/enfants</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import {onBeforeUnmount, onMounted, ref, watch} from 'vue';

// Références DOM
const grandparent = ref(null);
const parent = ref(null);
const child = ref(null);
const logPanel = ref(null);

// État
const logs = ref([]);
const useCapture = ref(false);
const stopPropagation = ref(false);
const highlightGrandparent = ref(false);
const highlightParent = ref(false);
const highlightChild = ref(false);
const phaseCapture = ref(false);
const phaseBubbling = ref(false);

// Animation de propagation
let animationTimer = null;

// Gestionnaires d'événements
const eventListeners = [];

function addEventListeners() {
  // Supprimer les anciens gestionnaires
  removeEventListeners();

  // Ajouter les nouveaux gestionnaires avec useCapture actuel
  const elements = [
    { ref: grandparent.value, name: 'grandparent' },
    { ref: parent.value, name: 'parent' },
    { ref: child.value, name: 'child' }
  ];

  elements.forEach(({ ref, name }) => {
    // Gestionnaire pour la phase de capture
    const captureHandler = (e) => {
      phaseCapture.value = true;
      phaseBubbling.value = false;
      logs.value.push({ element: name, phase: 'capture' });
      highlightElement(name, true);

      // Si stopPropagation est activé et que c'est le premier élément à capturer l'événement
      if (stopPropagation.value && logs.value.length === 1) {
        e.stopPropagation();
        addLogMessage('⛔ Propagation arrêtée');
      }
    };

    // Gestionnaire pour la phase de bouillonnement
    const bubblingHandler = (e) => {
      phaseCapture.value = false;
      phaseBubbling.value = true;
      logs.value.push({ element: name, phase: 'bubbling' });
      highlightElement(name, true);

      // Si stopPropagation est activé et que c'est le premier élément à capturer l'événement en phase de bouillonnement
      if (stopPropagation.value &&
          logs.value.filter(log => log.phase === 'bubbling').length === 1) {
        e.stopPropagation();
        addLogMessage('⛔ Propagation arrêtée');
      }
    };

    // Ajout des gestionnaires
    ref.addEventListener('click', captureHandler, true); // Phase de capture
    ref.addEventListener('click', bubblingHandler, false); // Phase de bouillonnement

    // Stocker les références pour le nettoyage
    eventListeners.push({
      element: ref,
      event: 'click',
      handler: captureHandler,
      options: true
    });

    eventListeners.push({
      element: ref,
      event: 'click',
      handler: bubblingHandler,
      options: false
    });
  });
}

function removeEventListeners() {
  eventListeners.forEach(({ element, event, handler, options }) => {
    element?.removeEventListener(event, handler, options);
  });
  eventListeners.length = 0;
}

function addLogMessage(message) {
  logs.value.push({
    element: message,
    phase: 'message'
  });
}

function highlightElement(elementName, state) {
  if (elementName === 'grandparent') highlightGrandparent.value = state;
  else if (elementName === 'parent') highlightParent.value = state;
  else if (elementName === 'child') highlightChild.value = state;

  // Réinitialiser la mise en évidence après un délai
  if (state) {
    setTimeout(() => {
      highlightElement(elementName, false);
    }, 500);
  }
}

function handleClick(event, elementName) {
  // Arrêter la propagation native pour gérer nous-mêmes l'animation
  event.stopPropagation();

  // Réinitialiser les logs et l'état d'animation
  clearLogs();
  clearAnimationTimers();

  // Simuler la capture et le bouillonnement avec notre propre logique
  // Cet événement est juste pour déclencher l'animation visuelle
  // Les logs seront gérés par les gestionnaires d'événements réels
}

function clearLogs() {
  logs.value = [];
  phaseCapture.value = false;
  phaseBubbling.value = false;
  clearAnimationTimers();
}

function clearAnimationTimers() {
  if (animationTimer) {
    clearTimeout(animationTimer);
    animationTimer = null;
  }
}

function resetDemo() {
  clearLogs();
  addEventListeners();
}

// Observateurs
watch(useCapture, () => {
  resetDemo();
});

// Cycle de vie du composant
onMounted(() => {
  resetDemo();
});

onBeforeUnmount(() => {
  removeEventListeners();
  clearAnimationTimers();
});
</script>

<style scoped>
.propagation-demo {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 16px;
}

.demo-flex {
  display: flex;
  gap: 16px;
}

.demo-area {
  flex: 1;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.log-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.phases-diagram {
  display: flex;
  justify-content: center;
  gap: 48px;
  margin-bottom: 12px;
}

.phase-arrow {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.arrow {
  font-size: 24px;
  opacity: 0.3;
  transition: all 0.3s;
}

.arrow.active {
  opacity: 1;
  transform: scale(1.2);
  color: #4f46e5;
}

.phase-name {
  font-size: 12px;
  margin-top: 4px;
}

.grandparent {
  width: 300px;
  height: 220px;
  background-color: #f0f4f8;
  border: 2px solid #cbd5e1;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: background-color 0.3s;
}

.parent {
  width: 220px;
  height: 160px;
  background-color: #e0e7ff;
  border: 2px solid #a5b4fc;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: background-color 0.3s;
}

.child {
  padding: 8px 16px;
  background-color: #4f46e5;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.child:hover {
  background-color: #4338ca;
}

.highlight {
  background-color: #fef08a !important;
  border-color: #facc15 !important;
}

.child.highlight {
  background-color: #eab308 !important;
  color: black;
}

.log-panel {
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  height: 200px;
  overflow-y: auto;
  padding: 8px;
  background-color: #f8fafc;
  font-family: monospace;
  font-size: 14px;
}

.log-entry {
  padding: 6px 8px;
  margin-bottom: 4px;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
}

.log-entry.capture {
  background-color: #e0f2fe;
  border-left: 3px solid #0ea5e9;
}

.log-entry.bubbling {
  background-color: #fef9c3;
  border-left: 3px solid #eab308;
}

.log-entry.message {
  background-color: #fee2e2;
  border-left: 3px solid #ef4444;
  justify-content: center;
  font-weight: bold;
}

.element-name {
  font-weight: 500;
}

.phase-label {
  color: #64748b;
}

.demo-btn {
  background-color: #4f46e5;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

.demo-btn:hover {
  background-color: #4338ca;
}

.options {
  display: flex;
  font-size: 14px;
}

.info-box {
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 12px;
}

.mb-2 {
  margin-bottom: 8px;
}

.mb-4 {
  margin-bottom: 16px;
}

.mt-4 {
  margin-top: 16px;
}

.mr-2 {
  margin-right: 8px;
}

.mr-4 {
  margin-right: 16px;
}

.text-center {
  text-align: center;
}

.text-gray-500 {
  color: #64748b;
}

.text-gray-700 {
  color: #334155;
}

.text-sm {
  font-size: 14px;
}

.text-lg {
  font-size: 18px;
}

.font-semibold {
  font-weight: 600;
}

.my-4 {
  margin-top: 16px;
  margin-bottom: 16px;
}
</style>