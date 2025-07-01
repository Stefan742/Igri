<template>
  <section class="rotating-headline">
    <div class="headline-container">
      <h1>
        <span class="fixed-text">Во Велес живее</span>
        <span class="highlighted-word" :key="currentWord">{{ currentWord }}</span>
      </h1>

      <!-- Позадински watermark -->
      <div class="watermark">IGRI VELES</div>

      <!-- Reveal текст -->
      <p class="reveal-text" ref="scrollText">
        Во Велес живее спортот, но и нешто многу повеќе.<br><br>
        Тука младите се среќаваат на терените, но и надвор од нив.<br>
        Натпреварите се водат со страст, но се завршуваат со пријателство.<br>
        Забавата не престанува кога ќе се изгаси светлото на стадионот – таа штотуку започнува.<br>
        Музика, енергија, и моменти што се паметат цел живот.<br><br>
        <strong>Велешките Спортски Игри</strong> не се само спортски настан – тие се празник на духот, заедништвото и младоста.
      </p>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      words: ["страста", "спортот", "пријателството", "енергијата"],
      currentWordIndex: 0,
    };
  },
  computed: {
    currentWord() {
      return this.words[this.currentWordIndex];
    },
  },
  mounted() {
    setInterval(() => {
      this.currentWordIndex = (this.currentWordIndex + 1) % this.words.length;
    }, 2000);

    const observer = new IntersectionObserver(
        ([entry]) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
          }
        },
        { threshold: 0.2 }
    );
    observer.observe(this.$refs.scrollText);
  },
};
</script>



<style scoped>
@font-face {
  font-family: 'Race Sport';
  src: local('Race Sport');
}

.rotating-headline {
  position: relative;
  padding: 100px 40px;
  background-color: #0B2559;
  color: white;
  text-align: left;
  overflow: hidden;
  margin-top: -100px;
}

.headline-container {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

h1 {
  font-size: 48px;
  font-weight: bold;
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.fixed-text {
  min-width: 240px;
}

.highlighted-word {
  display: inline-block;
  color: #ffc800;
  animation: slideUp 0.5s ease;
}

@keyframes slideUp {
  0% {
    opacity: 0;
    transform: translateY(100%);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.reveal-text {
  color: white;
  font-size: 18px;
  line-height: 1.8;
  opacity: 0.3;
  filter: blur(4px);
  transition: opacity 1s ease, filter 1s ease;
  font-style: italic;
  position: relative;
  z-index: 2;
}

.reveal-text.revealed {
  opacity: 1;
  filter: blur(0);
}

/* Watermark */
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
</style>
