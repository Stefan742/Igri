<template>
  <div class="match-page-wrapper">
    <Navbar />

    <section class="matches" data-aos="fade-in">
      <h2 class="title">Натпревари: {{ sport }}</h2>

      <div v-if="matches.length" class="match-grid">
        <MatchCard
            v-for="match in matches"
            :key="match.id"
            :match="match"
            data-aos="fade-up"
        />
      </div>

      <div v-else class="no-matches" data-aos="fade-up">
        <span>😕</span><br />
        Нема активни натпревари во моментов.
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import MatchCard from '@/components/MatchCard.vue'

const route = useRoute()
const sport = ref(route.params.sport)
const matches = ref([])
let socket = null

const loadMatches = async () => {
  const normalized = sport.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase()

  try {
    const response = await fetch(`http://localhost:8000/api/matches/by-sport/${normalized}/`)
    if (!response.ok) throw new Error('Failed to fetch matches')
    const data = await response.json()
    matches.value = data
  } catch (error) {
    console.error('Error loading matches:', error)
    matches.value = []
  }

  if (socket) socket.close()

  socket = new WebSocket(`ws://localhost:8000/ws/results/${normalized}/`)
  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    const index = matches.value.findIndex(m => m.id === data.match_id)
    if (index !== -1) {
      matches.value[index].score = data.score
      matches.value[index].time = data.time
    }
  }
}

onMounted(() => {
  loadMatches()
})

watch(() => route.params.sport, (newVal) => {
  sport.value = newVal
  loadMatches()
})

onUnmounted(() => {
  if (socket) socket.close()
})
</script>

<style scoped>
.match-page-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: #fff;
}

.matches {
  flex: 1;
  padding: 140px 1.5rem 3rem;
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
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  max-width: 600px;
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
