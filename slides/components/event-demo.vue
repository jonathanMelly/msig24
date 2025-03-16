<!-- EventDemoComponent.vue -->
<template>
  <div class="event-demo-container" @keydown.capture="interceptArrowKeys">
    <div class="controls">
      <button @click="clearLog" class="control-button">Effacer le journal</button>
      <button @click="resetPosition" class="control-button">Réinitialiser la position</button>
    </div>

    <div class="demo-area">
      <div class="interactive-zone" ref="interactiveZone">
        <div
            class="target-element"
            ref="targetElement"
            tabindex="0"
            @mousedown="handleMouseDown"
            @click="handleClick"
            @dblclick="handleDblClick"
            @keydown="handleKeyDown"
            @keyup="handleKeyUp"
            @focus="handleFocus"
            @blur="handleBlur"
            :style="targetStyle"
            :class="{ 'active': isActive }"
        >
          Interagir
        </div>
      </div>

      <div class="log-panel" ref="logPanel">
        <div class="log-entry">Journal d'événements</div>
      </div>
    </div>

    <div class="key-info">
      <div class="info-box">
        <h3>Position de la souris</h3>
        <div class="info-value">{{ mousePosition }}</div>
      </div>

      <div class="info-box">
        <h3>Dernière touche</h3>
        <div class="info-value">{{ lastKey }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {computed, onMounted, onUnmounted, reactive, ref} from 'vue';

// Refs pour les éléments DOM
const targetElement = ref(null);
const interactiveZone = ref(null);
const logPanel = ref(null);

// État pour le drag & drop
const isDragging = ref(false);
const isActive = ref(false);
const offset = reactive({ x: 0, y: 0 });
const position = reactive({ x: 100, y: 100 });
const mousePosition = ref('x: 0, y: 0');
const lastKey = ref('-');

// Style calculé pour l'élément cible
const targetStyle = computed(() => {
  return {
    left: `${position.x}px`,
    top: `${position.y}px`
  };
});

// Fonction pour ajouter une entrée dans le journal
function addLogEntry(eventType, details, category = 'mouse') {
  const entry = document.createElement('div');
  entry.classList.add('log-entry', category);

  const timestamp = new Date().toLocaleTimeString('fr-FR', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    fractionalSecondDigits: 3
  });

  entry.innerHTML = `<span style="color: #999">${timestamp}</span> | <strong>${eventType}</strong>: ${details}`;

  if (logPanel.value) {
    logPanel.value.insertBefore(entry, logPanel.value.firstChild);

    // Limiter le nombre d'entrées
    if (logPanel.value.children.length > 30) {
      logPanel.value.removeChild(logPanel.value.lastChild);
    }
  }
}

// Fonction qui intercepte les touches flèches au niveau du conteneur
function interceptArrowKeys(e) {
  if (e.key.startsWith('Arrow')) {
    e.stopPropagation(); // Empêche la propagation aux gestionnaires de Slidev
  }
}

// Gestionnaires d'événements
function handleMouseDown(e) {
  e.preventDefault();
  isActive.value = true;
  isDragging.value = true;

  // Calculer le décalage
  const rect = targetElement.value.getBoundingClientRect();
  offset.x = e.clientX - rect.left;
  offset.y = e.clientY - rect.top;

  addLogEntry('mousedown', `Bouton: ${e.button}`, 'mouse');

  // Ajouter les gestionnaires sur le document
  document.addEventListener('mousemove', handleMouseMove);
  document.addEventListener('mouseup', handleMouseUp);
}

function handleMouseMove(e) {
  // Mise à jour de l'affichage de la position
  mousePosition.value = `x: ${e.clientX}, y: ${e.clientY}`;

  if (isDragging.value) {
    // Calculer la nouvelle position
    const zoneRect = interactiveZone.value.getBoundingClientRect();
    let newX = e.clientX - zoneRect.left - offset.x;
    let newY = e.clientY - zoneRect.top - offset.y;

    // Limiter la position à l'intérieur de la zone
    const maxX = zoneRect.width - targetElement.value.offsetWidth;
    const maxY = zoneRect.height - targetElement.value.offsetHeight;

    position.x = Math.max(0, Math.min(newX, maxX));
    position.y = Math.max(0, Math.min(newY, maxY));

    // Limiter les logs de mousemove pour éviter les surcharges
    if (Math.random() < 0.1) { // Enregistrer environ 10% des événements
      addLogEntry('mousemove', `x: ${Math.round(position.x)}, y: ${Math.round(position.y)}`, 'mouse');
    }
  }
}

function handleMouseUp() {
  if (isDragging.value) {
    isActive.value = false;
    isDragging.value = false;
    addLogEntry('mouseup', '', 'mouse');

    // Supprimer les gestionnaires du document
    document.removeEventListener('mousemove', handleMouseMove);
    document.removeEventListener('mouseup', handleMouseUp);
  }
}

function handleClick(e) {
  addLogEntry('click', `x: ${e.clientX}, y: ${e.clientY}`, 'mouse');
  // Mettre le focus sur l'élément pour les événements clavier
  targetElement.value.focus();
}

function handleDblClick() {
  addLogEntry('dblclick', '', 'mouse');
}

function handleKeyDown(e) {
  addLogEntry('keydown', `key: ${e.key}, code: ${e.code}`, 'keyboard');
  lastKey.value = e.key;

  // Changer la position pour les touches flèches
  if (e.key.startsWith('Arrow')) {
    // Empêcher le défilement de la page et l'avancement des slides avec les flèches
    e.preventDefault();
    e.stopPropagation(); // Empêche la propagation aux gestionnaires de Slidev

    // Obtenir la position actuelle
    const zoneRect = interactiveZone.value.getBoundingClientRect();

    // Ajuster la position en fonction de la touche
    const step = e.shiftKey ? 10 : 5; // Déplacement plus grand avec Shift

    switch (e.key) {
      case 'ArrowLeft':
        position.x = Math.max(0, position.x - step);
        break;
      case 'ArrowRight':
        position.x = Math.min(zoneRect.width - targetElement.value.offsetWidth, position.x + step);
        break;
      case 'ArrowUp':
        position.y = Math.max(0, position.y - step);
        break;
      case 'ArrowDown':
        position.y = Math.min(zoneRect.height - targetElement.value.offsetHeight, position.y + step);
        break;
    }
  }
}

function handleKeyUp(e) {
  addLogEntry('keyup', `key: ${e.key}, code: ${e.code}`, 'keyboard');
}

function handleFocus() {
  addLogEntry('focus', '', 'mouse');
}

function handleBlur() {
  addLogEntry('blur', '', 'mouse');
}

// Fonctions pour les boutons de contrôle
function clearLog() {
  if (logPanel.value) {
    // Effacer le journal tout en gardant l'en-tête
    while (logPanel.value.children.length > 1) {
      logPanel.value.removeChild(logPanel.value.lastChild);
    }
    addLogEntry('clear', 'Journal effacé', 'mouse');
  }
}

function resetPosition() {
  position.x = 100;
  position.y = 100;
  addLogEntry('reset', 'Position réinitialisée', 'mouse');
}

// Lifecycle hooks
onMounted(() => {
  // Ajouter un gestionnaire pour les mouvements de souris
  document.addEventListener('mousemove', (e) => {
    mousePosition.value = `x: ${e.clientX}, y: ${e.clientY}`;
  });

  // Message initial
  addLogEntry('init', 'Démo chargée et prête', 'mouse');
});

onUnmounted(() => {
  // Nettoyer les gestionnaires d'événements
  document.removeEventListener('mousemove', handleMouseMove);
  document.removeEventListener('mouseup', handleMouseUp);
});
</script>

<style scoped>
.event-demo-container {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0 auto;
  padding: 0.5rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  max-width: 100%;
}

.demo-area {
  display: flex;
  margin: 1rem 0;
  gap: 1rem;
}

.interactive-zone {
  flex: 1;
  height: 300px;
  border: 2px dashed #ccc;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  background-color: #f5f5f5;
}

.log-panel {
  flex: 1;
  height: 300px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow-y: auto;
  background-color: #f8f8f8;
  padding: 10px;
  font-family: monospace;
  font-size: 14px;
}

.target-element {
  width: 100px;
  height: 100px;
  background-color: #4f46e5;
  border-radius: 8px;
  position: absolute;
  cursor: pointer;
  user-select: none;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.target-element:focus {
  outline: 3px solid #818cf8;
}

.target-element.active {
  background-color: #4338ca;
}

.log-entry {
  margin-bottom: 4px;
  padding: 4px 8px;
  border-radius: 4px;
  transition: opacity 1s;
}

.log-entry.mouse {
  background-color: #e6f7ff;
  border-left: 3px solid #1890ff;
}

.log-entry.keyboard {
  background-color: #f6ffed;
  border-left: 3px solid #52c41a;
}

.controls {
  display: flex;
  gap: 10px;
  margin-bottom: 10px;
}

.control-button {
  background-color: #4f46e5;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
}

.control-button:hover {
  background-color: #4338ca;
}

.key-info {
  display: flex;
  gap: 20px;
  margin-top: 10px;
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 8px;
}

.info-box {
  flex: 1;
}

.info-box h3 {
  margin-top: 0;
  font-size: 16px;
  color: #333;
}

.info-value {
  font-family: monospace;
  background-color: white;
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #ddd;
}
</style>