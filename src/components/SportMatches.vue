<template>
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
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import MatchCard from '@/components/MatchCard.vue'

const route = useRoute()
const sport = route.params.sport

const matches = ref([])

onMounted(() => {
  const dummyData = {
    kosarka: [
      { id: 1, teams: 'Вардар vs Работнички', score: '65 - 60', time: '3rd Q' },
      { id: 2, teams: 'АВ Охрид vs Пелистер', score: '47 - 51', time: '2nd Q' }
    ],
    fudbal: [
      { id: 3, teams: 'Шкупи vs Вардар', score: '1 - 0', time: '45+2’' }
    ],
    tenis: [],
    odbojka: []
  }

  matches.value = dummyData[sport] || []
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
