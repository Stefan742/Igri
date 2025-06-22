<template>
  <section class="matches" data-aos="fade-in">
    <h2 class="title">Натпревари: {{ sport }}</h2>

    <div v-if="matches.length">
      <MatchCard v-for="match in matches" :key="match.id" :match="match" />
    </div>
    <div v-else class="no-matches">Нема активни натпревари во моментов.</div>
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
      { id: 3, teams: 'Шкупи vs Вардар', score: '1 - 0', time: '45+2’' },
    ],
    tenis: [],
    odbojka: []
  }
  matches.value = dummyData[sport] || []
})
</script>

<style scoped>
.matches {
  padding: 1.5rem 1rem;
}

.title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  text-transform: capitalize;
  color: #0b2559;
}

.no-matches {
  color: #666;
  font-style: italic;
  text-align: center;
  margin-top: 2rem;
}
</style>
