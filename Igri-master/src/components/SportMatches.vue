<template>
  <section className="matches" data-aos="fade-in">
    <h2 className="title">Натпревари: {{ sport }}</h2>

    <div v-if="matches.length" className="match-grid">
      <MatchCard
          v-for="match in matches"
          :key="match.id"
          :match="match"
          data-aos="fade-up"
      />
    </div>

    <div v-else className="no-matches" data-aos="fade-up">
      <span>😕</span><br/>
      Нема активни натпревари во моментов.
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import MatchCard from '@/components/MatchCard.vue'

const route = useRoute()
const sport = route.params.sport
const matches = ref([])

let socket = null

async function loadMatches() {
  try {
    const res = await fetch(`http://localhost:8000/api/matches/?sport=${sport}`)
    const data = await res.json()
    matches.value = data
  } catch (err) {
    console.error('Грешка при вчитување на податоци:', err)
  }
}

onMounted(() => {
  loadMatches()

  socket = new WebSocket(`ws://localhost:8000/ws/results/${sport}/`)

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    // Најди натпреварот што се менува и ажурирај го score и time
    const idx = matches.value.findIndex(m => m.id === data.match_id)
    if (idx !== -1) {
      matches.value[idx].score = data.score
      matches.value[idx].time = data.time
    }
  }

  socket.onclose = () => {
    console.log('WebSocket connection closed')
  }
})

onBeforeUnmount(() => {
  if (socket) socket.close()
})
</script>


<style scoped>
.matches {
  padding: 3rem 1.5rem;
  min-height: 100vh;
  background: linear-gradient(to right, #eef2f3, #dce3e9);
}

.title {
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 2rem;
  color: #0b2559;
  text-align: center;
  text-transform: capitalize;
}

.match-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 1rem;
}

.no-matches {
  text-align: center;
  font-size: 1.125rem;
  font-style: italic;
  color: #666;
  margin-top: 4rem;
  opacity: 0.8;
  line-height: 1.6;
}
</style>
