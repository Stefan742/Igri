<template>
  <div class="news-detail-wrapper">
    <Navbar />

    <section class="news-detail" v-if="news">
      <h1 class="news-detail-title">{{ news.title }}</h1>
      <p class="news-detail-date">{{ formatDate(news.created_at) }}</p>
      <img :src="news.image" alt="news image" class="news-detail-image" />
      <p class="news-detail-summary">{{ news.summary }}</p>
      <div v-if="news.content" class="news-detail-content" v-html="news.content"></div>
    </section>

    <p v-else class="loading">Вчитување...</p>

    <!-- Останати новости (освен тековната) -->
    <section v-if="otherNews.length" class="related-news">
      <h2 class="related-title">Други новости</h2>
      <div class="news-grid">
        <div
            v-for="item in otherNews"
            :key="item.id"
            class="news-card"
            @click="goToNews(item.id)"
        >
          <img :src="item.image" alt="news" class="related-image" />
          <div class="related-content">
            <h3>{{ item.title }}</h3>
            <p>{{ formatDate(item.created_at) }}</p>
          </div>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

const route = useRoute()
const router = useRouter()
const news = ref(null)
const otherNews = ref([])

onMounted(async () => {
  const id = route.params.id
  try {
    // Детали за веста
    const res = await fetch(`http://localhost:8000/api/news/${id}/`)
    news.value = await res.json()

    // Други новости (освен тековната)
    const allRes = await fetch(`http://localhost:8000/api/news/`)
    const allNews = await allRes.json()
    otherNews.value = allNews.filter(n => n.id !== Number(id))

  } catch (err) {
    console.error('Грешка при вчитување:', err)
  }
})

function formatDate(dateStr) {
  const date = new Date(dateStr)
  return date.toLocaleDateString('mk-MK', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

function goToNews(id) {
  router.push(`/news/${id}`)
}
</script>

<style scoped>
.news-detail-wrapper {
  background: #fff;
  min-height: 100vh;
  padding-top: 140px;
}

.news-detail {
  max-width: 860px;
  margin: 0 auto;
  padding: 2rem;
  color: #0b2559;
}

.news-detail-title {
  font-size: 2.5rem;
  font-weight: 900;
  margin-bottom: 1rem;
  text-align: center;
  text-transform: uppercase;
}

.news-detail-date {
  font-style: italic;
  opacity: 0.7;
  text-align: center;
  margin-bottom: 1.5rem;
}

.news-detail-image {
  width: 100%;
  border-radius: 12px;
  margin-bottom: 1.5rem;
}

.news-detail-summary {
  font-size: 1.2rem;
  line-height: 1.7;
  white-space: pre-line;
}

/* Related News */
.related-news {
  max-width: 1240px;
  margin: 4rem auto;
  padding: 0 1rem;
}

.related-title {
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 2rem;
  color: #0b2559;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.news-card {
  background: #f8f9fc;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 6px 12px rgba(11, 37, 89, 0.12);
  cursor: pointer;
  transition: transform 0.3s ease;
}

.news-card:hover {
  transform: translateY(-6px);
}

.related-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.related-content {
  padding: 1rem;
}

.related-content h3 {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #0b2559;
}

.related-content p {
  font-size: 0.95rem;
  opacity: 0.7;
}
.news-detail-content {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-top: 2rem;
  white-space: pre-line;
  color: #1b1b1b;
}

.news-detail-content h2,
.news-detail-content h3 {
  margin-top: 1.5rem;
  color: #0b2559;
}

.news-detail-content a {
  color: #0b2559;
  text-decoration: underline;
}

</style>
