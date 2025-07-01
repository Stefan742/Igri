<template>
  <section class="gallery" id="gallery" data-aos="zoom-in">
    <div
        ref="scrollContainer"
        class="scroll-container"
    >
      <div
          v-for="(i, idx) in originalImages"
          :key="idx"
          class="slide-image"
      >
        <img :src="`/src/assets/images/${i}.jpg`" :alt="`Image ${i}`" />
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';

export default {
  name: 'Gallery',
  setup() {
    const totalImages = 12;
    const scrollContainer = ref(null);
    let intervalId = null;

    const scrollStep = 300; // пиксели за секој скрол чекор
    const scrollInterval = 5000; // време на интервал во милисекунди

    const originalImages = Array.from({ length: totalImages }, (_, i) => i + 1);

    const scrollLeft = () => {
      if (!scrollContainer.value) return;
      const container = scrollContainer.value;

      const maxScrollLeft = container.scrollWidth - container.clientWidth;

      if (container.scrollLeft + scrollStep >= maxScrollLeft) {
        // Ако ќе стигнеме/надминеме крај, се враќаме на почеток без анимација
        container.style.scrollBehavior = 'auto';
        container.scrollLeft = 0;

        // Мал timeout за да се применува промена пред да вратиме scrollBehavior
        setTimeout(() => {
          container.style.scrollBehavior = 'smooth';
          container.scrollLeft += scrollStep;
        }, 50);
      } else {
        // Обично скролирање со плаво движење
        container.scrollBy({ left: scrollStep, behavior: 'smooth' });
      }
    };

    onMounted(() => {
      intervalId = setInterval(scrollLeft, scrollInterval);
    });

    onBeforeUnmount(() => {
      clearInterval(intervalId);
    });

    return {
      scrollContainer,
      originalImages,
    };
  },
};
</script>

<style scoped>
.gallery {
  padding: 80px 20px;
  background-color: #0B2559;
  text-align: center;
  color: white;
  overflow: hidden;
}

.gallery h2 {
  font-size: 36px;
  margin-bottom: 2rem;
  font-family: 'Race Sport', sans-serif;
  color: #ffc800;
}

.scroll-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  scroll-behavior: smooth;
  padding-bottom: 20px;
  scrollbar-width: none; /* Firefox */
  scroll-snap-type: x mandatory;
}

.scroll-container::-webkit-scrollbar {
  display: none; /* Chrome, Safari */
}

.slide-image {
  min-width: 300px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  flex-shrink: 0;
  transition: transform 0.3s ease;
  scroll-snap-align: start;
}

.slide-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.slide-image:hover {
  transform: scale(1.03);
}
</style>
