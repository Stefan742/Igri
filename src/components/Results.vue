<template>
  <Navbar/>
  <section class="results" data-aos="fade-up">
    <h2 class="text-3xl font-bold text-center mb-6">Резултати</h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 px-4">
      <SportCard
          v-for="sport in sports"
          :key="sport.name"
          :name="sport.name"
          :icon="sport.icon"
          @click="goToSport(sport.name)"
      />
    </div>
  </section>
  <Footer/>
</template>

<script setup>
import SportCard from '@/components/SportCard.vue'
import { useRouter } from 'vue-router'
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

const router = useRouter()

const sports = [
  { name: 'Кошарка', icon: '🏀' },
  { name: 'Одбојка', icon: '🏐' },
  { name: 'Тенис', icon: '🎾' },
  { name: 'Фудбал', icon: '⚽' }
]

function goToSport(sportName) {
  router.push({ name: 'SportMatches', params: { sport: sportName.toLowerCase() } })
}
</script>
