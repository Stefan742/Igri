<template>
  <div class="main-container">
    <LoadingScreen v-if="loading" />

    <template v-else>
      <Navbar />
      <Hero />
      <About />
      <Sports />
      <Gallery />
      <Contact />
      <Footer />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

import Navbar from "@/components/Navbar.vue";
import Hero from '@/components/Hero.vue'
import About from '@/components/About.vue'
import Sports from '@/components/Sports.vue'
import Gallery from '@/components/Gallery.vue'
import Contact from '@/components/Contact.vue'
import Footer from '@/components/Footer.vue'
import LoadingScreen from '@/components/LoadingScreen.vue'

const loading = ref(true)

onMounted(() => {
  // Симулирај loading 2 секунди (или смени со fetch/axios ако имаш API)
  setTimeout(() => {
    loading.value = false
  }, 2000)
})
</script>

<style scoped>
.main-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
