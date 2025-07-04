<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const sport = route.params.sport
const matches = ref([])

const savingMatchId = ref(null)
const message = ref('')

let socket = null

async function loadMatches() {
  try {
    const res = await fetch(`http://localhost:8000/api/matches/by-sport/${sport}/`)
    if (!res.ok) throw new Error('Грешка при вчитување на податоци')
    matches.value = await res.json()
  } catch (err) {
    console.error('Грешка при вчитување на податоци:', err)
  }
}


onMounted(() => {
  loadMatches()

  socket = new WebSocket(`ws://localhost:8000/ws/results/${sport}/`)

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    const index = matches.value.findIndex(m => m.id === data.match_id)
    if (index !== -1) {
      matches.value[index].score = data.score
      matches.value[index].time = data.time
      if (data.status) matches.value[index].status = data.status
      if (data.scheduled_time) matches.value[index].scheduled_time = data.scheduled_time
    }
  }


  socket.onclose = () => {
    console.log('WebSocket connection closed')
  }
})

onBeforeUnmount(() => {
  if (socket) {
    socket.close()
  }
})

async function updateMatch(match) {
  savingMatchId.value = match.id
  message.value = ''
  try {
    const res = await fetch(`http://localhost:8000/api/matches/${match.id}/update_score/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        score: match.score,
        time: match.time,
        status: match.status,
        scheduled_time: match.scheduled_time,
      }),
    })
    if (!res.ok) throw new Error('Грешка при зачувување')
    message.value = 'Успешно зачувано!'
  } catch (e) {
    message.value = 'Грешка при зачувување!'
  } finally {
    savingMatchId.value = null
  }
}
</script>

<style scoped>
section {
  max-width: 600px;
  margin: 1rem auto;
  font-family: Arial, sans-serif;
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #004080;
}

.admin-match {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
  box-shadow: 0 0 8px rgba(0,0,0,0.05);
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.admin-match p {
  flex: 1 1 40%;
  font-weight: bold;
  color: #333;
  margin: 0;
}

.admin-match input {
  flex: 1 1 20%;
  padding: 0.3rem 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.admin-match button {
  flex: 0 0 auto;
  padding: 0.4rem 0.8rem;
  background-color: #004080;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.admin-match button:disabled {
  background-color: #7a9ccc;
  cursor: not-allowed;
}

.admin-match button:hover:not(:disabled) {
  background-color: #002f5d;
}

.message {
  text-align: center;
  margin-top: 1rem;
  color: #007700;
  font-weight: 600;
}
</style>

<template>
  <section>
    <h2>Админ: Уредување натпревари - {{ sport }}</h2>

    <div v-for="match in matches" :key="match.id" class="admin-match">
      <p>{{ match.teams }}</p>

      <input
          v-model="match.score"
          type="text"
          placeholder="Резултат"
      />

      <input
          v-model="match.time"
          type="text"
          placeholder="Време"
      />

      <select v-model="match.status">
        <option value="scheduled">Scheduled</option>
        <option value="active">Active</option>
        <option value="finished">Finished</option>
      </select>

      <input
          v-if="match.status === 'scheduled'"
          v-model="match.scheduled_time"
          type="datetime-local"
      />

      <button
          :disabled="savingMatchId === match.id"
          @click="updateMatch(match)"
      >
        {{ savingMatchId === match.id ? 'Се зачувува...' : 'Зачувај' }}
      </button>
    </div>

    <p class="message" v-if="message">{{ message }}</p>
  </section>
</template>