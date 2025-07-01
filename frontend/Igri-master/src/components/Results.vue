<template>
  <Navbar />

  <section class="results" data-aos="fade-up">
    <div class="watermark">REZULTATI</div>
    <div class="scroll-text">
      <span v-for="n in 20" :key="n">SPORTSKI IGRI VELES</span>
    </div>
    <div class="sports-grid">
      <SportCard
          v-for="sport in sports"
          :key="sport.name"
          :name="sport.name"
          :icon="sport.icon"
          @click="goToSport(sport.name)"
      />
    </div>
  </section>

  <Footer />
</template>

<script setup>
import SportCard from '@/components/SportCard.vue'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import { useRouter } from 'vue-router'

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

<style scoped>
.results {
  background-color: #0b2559;
  padding-top: 150px;
  min-height: 100vh;
  text-align: center;
}

.title {
  font-size: 2.25rem;
  font-weight: 800;
  margin-bottom: 2rem;
  color: white;
}

.sports-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1.5rem;
  max-width: 900px;
  margin: 0 auto;
  padding: 0 1rem;
}
.watermark {
  position: absolute;
  top: 0;
  left: 0;
  font-family: 'Race Sport', sans-serif;
  font-size: 40vw;
  color: rgba(255, 255, 255, 0.03);
  pointer-events: none;
  z-index: 0;
  line-height: 1;
  white-space: nowrap;
  user-select: none;
  margin-left: -400px;
}
@media (max-width: 600px) {
  h1 {
    font-size: 32px;
  }

  .fixed-text {
    min-width: auto;
    white-space: normal;
  }

  .highlighted-word {
    font-size: 32px;
  }

  .rotating-headline {
    padding: 60px 20px;
  }

  .watermark {
    font-size: 60vw;
    margin-left: -200px;
  }

  .reveal-text {
    font-size: 16px;
  }
}
.scroll-text-wrapper {
  position: absolute;
  top: 20px;
  left: 0;
  width: 200%;
  white-space: nowrap;
  overflow: hidden;
  z-index: 1;
  pointer-events: none;
}

.scroll-text {
  display: inline-block;
  white-space: nowrap;
  animation: scrollLeft 90s linear infinite;
  font-size: 80px;
  font-weight: bold;
  color: transparent;
  -webkit-text-stroke: 1px white;
  opacity: 0.45;
  text-transform: uppercase;
}

.scroll-text span {
  display: inline;
  margin-right: 60px;
}

@keyframes scrollLeft {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}
</style>
