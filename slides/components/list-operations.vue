<template>
  <div class="mx-auto">
    <div class="space-y-0">
      <!-- Boutons d'opération -->
      <div class="flex space-x-4 justify-center mb-8">
        <button @click="handleOperation('add')" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Add</button>
        <button :disabled="!currentList.includes('orange')"  @click="handleOperation('remove')" class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">Remove</button>
        <button @click="handleOperation('access')" class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">Access</button>
        <button @click="handleOperation('clear')" class="px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600">Clear</button>
        <button @click="handleOperation('reset')" class="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600">Reset</button>
      </div>

      <!-- Code en cours -->
      <div v-if="operationLog" class="text-center text-black font-red font-mono bg-gray-100 p-2 rounded">
        {{ operationLog }}
      </div>

      <!-- SVG de la liste -->
      <svg viewBox="0 0 450 200" class="w-full h-64">
        <text x="200" y="30" text-anchor="middle" font-size="2" fill="#333">List&lt;string&gt; fruits = new(){'pomme', 'poire', 'orange', 'banane', 'kiwi'}</text>

        <rect x="50" y="50" :width="currentList.length*60" height="100" fill="#f0f0f0" stroke="#666" stroke-width="2"/>

        <template v-for="(_, index) in currentList" :key="'line-' + index">
          <line
            :x1="110 + index * 60"
            y1="50"
            :x2="110 + index * 60"
            y2="150"
            stroke="#666"
            stroke-width="1"
          />
        </template>
        
        <template v-for="(fruit, index) in currentList" :key="'box-' + index">
          <g>
            <rect
              :x="50 + index * 60"
              y="50"
              width="60"
              height="100"
              :fill="highlightedBox === index || highlightedBox === 'all' ? '#ffeb3c' : 'transparent'"
              fill-opacity="0.5"
            />
            <text
              :x="80 + index * 60"
              y="170"
              text-anchor="middle"
              font-size="7"
              fill="#666"
            >
              [{{ index }}]
            </text>
            <text
              :x="80 + index * 60"
              y="100"
              text-anchor="middle"
              font-size="4"
              fill="#333"
            >
              {{ fruit }}
            </text>
          </g>
        </template>
      </svg>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const highlightedBox = ref(null)
const currentList = ref(['pomme', 'poire', 'orange', 'banane', 'kiwi'])
const operationLog = ref('')
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const handleOperation = async (operation) => {
  switch(operation) {
    case 'add':
      highlightedBox.value = currentList.value.length
      operationLog.value = 'fruits.Add("fraise")'
      currentList.value = [...currentList.value, 'fraise']
      break
    case 'remove':
      operationLog.value = 'fruits.Remove("orange")'
      for (let i = 0; i < 5; i++) {
        highlightedBox.value = (i % 2===0 ? 2:null);
        await sleep(500)
      }

      currentList.value = currentList.value.filter((fruit, _) => fruit !== "orange")
      highlightedBox.value = null

      break
    case 'access':
      highlightedBox.value = 0
      operationLog.value = 'string first = fruits[0]'
      break
    case 'clear':
      highlightedBox.value = 'all'
      operationLog.value = 'fruits.Clear()'
      currentList.value = []
      break
    case 'reset':
      highlightedBox.value = null
      operationLog.value = ''
      currentList.value = ['pomme', 'poire', 'orange', 'banane', 'kiwi']
      break
  }
  setTimeout(() => {
    highlightedBox.value = null
  }, 3000)
}
</script>
