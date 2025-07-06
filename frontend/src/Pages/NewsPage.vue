<template>
  <div class="news-wrapper">
    <Navbar />

    <section class="news-page" data-aos="fade-up">
      <div class="watermark">NEWS</div>


      <!-- Наслов -->
      <h1 class="news-title">Новости и Известувања</h1>

      <div class="news-grid">
        <div v-for="news in newsList" :key="news.id" class="news-card">
          <div class="image-container">
            <img :src="news.image" alt="news" class="news-image" />
            <div class="title-preview">{{ news.title }}</div>

            <div class="overlay">
              <p class="overlay-date">{{ formatDate(news.created_at) }}</p>
              <router-link :to="`/news/${news.id}`" class="overlay-button">Прочитај</router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

const newsList = ref([])

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/api/news/')
    const data = await res.json()
    newsList.value = data
  } catch (err) {
    console.error('Грешка при вчитување новости:', err)
  }
})

function formatDate(dateStr) {
  if (!dateStr) return "Непознат датум"
  const date = new Date(dateStr)
  if (isNaN(date.getTime())) return "Невалиден датум"
  return date.toLocaleDateString('en-GB', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}
</script>

<style scoped>
.news-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: #fff;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
}

.news-page {
  flex: 1;
  padding: 140px 1rem 3rem;
  max-width: 1240px;
  margin: 0 auto;
  position: relative;
}

.watermark {
  position: fixed;
  top: 0;
  left: 0;
  font-family: 'Race Sport', sans-serif;
  font-size: 40vw;
  color: rgba(11, 37, 89, 0.05);
  pointer-events: none;
  user-select: none;
  line-height: 1;
  white-space: nowrap;
  margin-left: -300px;
  z-index: 0;
}



.news-title {
  font-size: 3rem;
  color: #0b2559;
  font-weight: 900;
  margin-bottom: 3rem;
  text-align: center;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  user-select: none;
  text-shadow: 0 2px 6px rgba(11, 37, 89, 0.15);
  position: relative;
  z-index: 10;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 2.5rem;
  padding: 0 0.5rem;
  position: relative;
  z-index: 10;
}

.news-card {
  position: relative;
  border-radius: 22px;
  overflow: hidden;
  cursor: pointer;
  box-shadow:
      0 6px 12px rgba(11, 37, 89, 0.12),
      0 10px 30px rgba(11, 37, 89, 0.08);
  transition: transform 0.4s cubic-bezier(0.22, 1, 0.36, 1),
  box-shadow 0.4s ease;
  height: 240px;
  background: #f8f9fc;
}

.news-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow:
      0 12px 20px rgba(11, 37, 89, 0.2),
      0 20px 45px rgba(11, 37, 89, 0.15);
}

.image-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 22px;
  background: #ddd;
}

.news-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1);
  will-change: transform;
}

.news-card:hover .news-image {
  transform: scale(1.15);
}

.title-preview {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(11, 37, 89, 0.75);
  color: white;
  padding: 1rem 1.5rem;
  font-weight: 700;
  font-size: 1.3rem;
  border-bottom-left-radius: 22px;
  border-bottom-right-radius: 22px;
  user-select: none;
  box-shadow: 0 -4px 12px rgba(0,0,0,0.4);
  transition: background-color 0.3s ease;
  letter-spacing: 0.015em;
  text-shadow:
      0 2px 6px rgba(0, 0, 0, 0.5);
}

.news-card:hover .title-preview {
  background: rgba(11, 37, 89, 0.9);
}

.overlay {
  position: absolute;
  inset: 0;
  background:
      linear-gradient(180deg, rgba(11,37,89,0.6) 20%, rgba(11,37,89,0.9) 85%),
      rgba(11,37,89,0.4);
  backdrop-filter: saturate(180%) blur(8px);
  opacity: 0;
  transition: opacity 0.35s ease;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 2rem 2.5rem 2.5rem;
  border-radius: 22px;
  color: #fff;
  pointer-events: none;
  user-select: none;
  box-sizing: border-box;
}

.news-card:hover .overlay {
  opacity: 1;
  pointer-events: auto;
}

.overlay-date {
  font-size: 0.95rem;
  font-weight: 600;
  opacity: 0.75;
  font-style: italic;
  margin-bottom: 1.6rem;
  letter-spacing: 0.05em;
  text-shadow:
      0 2px 5px rgba(0, 0, 0, 0.4);
  user-select: text;
}

.overlay-button {
  align-self: flex-start;
  background: #ffd700;
  color: #0b2559;
  font-weight: 800;
  font-size: 1.05rem;
  padding: 0.7rem 1.8rem;
  border-radius: 9999px;
  text-decoration: none;
  box-shadow:
      0 6px 10px rgba(255, 215, 0, 0.5);
  transition:
      background-color 0.35s ease,
      box-shadow 0.35s ease,
      transform 0.3s cubic-bezier(0.22, 1, 0.36, 1);
  user-select: none;
}

.overlay-button:hover {
  background-color: #e6c200;
  box-shadow:
      0 8px 20px rgba(230, 194, 0, 0.7);
  transform: translateY(-2px) scale(1.05);
  color: #041c3b;
}

@media (max-width: 520px) {
  .news-card {
    height: 280px;
  }
  .title-preview {
    font-size: 1.1rem;
    padding: 0.9rem 1.2rem;
  }
  .overlay-button {
    font-size: 1rem;
    padding: 0.6rem 1.4rem;
  }
}
</style>
