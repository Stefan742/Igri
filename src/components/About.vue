<template>
  <section class="about-cards">
    <div class="scroll-text-wrapper">
      <div class="scroll-text">
        <span v-for="n in 20" :key="n">SPORTSKI IGRI VELES</span>
      </div>
    </div>

    <div class="grid-container">
      <div
          class="info-card"
          v-for="(card, index) in cards"
          :key="index"
          :style="{ backgroundImage: `url(${card.image})` }"
      >
        <div class="overlay">
          <h3>{{ card.title }}</h3>
          <p>{{ card.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      cards: [
        {
          title: 'СПОРТ',
          description: 'Фудбал, кошарка, одбојка и повеќе активности кои го поттикнуваат тимскиот дух.',
          image: 'src/assets/images/1.jpg',
        },
        {
          title: 'ЗАБАВА',
          description: 'Настани исполнети со смеа, игри и позитивна енергија за сите генерации.',
          image: 'src/assets/images/3.jpg',
        },
        {
          title: 'МУЗИКА',
          description: 'Вечерни настапи, диџеи и музика што ги поврзува младите.',
          image: 'src/assets/images/music.jpg',
        },
        {
          title: 'ПРИЈАТЕЛСТВО',
          description: 'Создавање трајни пријателства и поврзување преку спорт и дружење.',
          image: 'src/assets/images/2.jpg',
        },
      ],
    };
  },
};
</script>

<style scoped>
.about-cards {
  background-color: #0B2559;
  padding: 100px 20px;
  min-height: 100vh;
  position: relative; /* Додади ова */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}
.about h2 {
  font-size: 36px;
  margin-bottom: 1rem;
  color: white;
}

.about p {
  font-size: 18px;
  max-width: 800px;
  margin: auto;
  color: white;
}

/* ANIMATED SCROLL TEXT */
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
  animation: scrollLeft 60s linear infinite;
  font-size: 80px;
  font-weight: bold;
  color: transparent;
  -webkit-text-stroke: 1px white;
  opacity: 0.45;
  text-transform: uppercase;
}

.scroll-text span {
  margin-right: 60px;
}

/* keyframes */
@keyframes scrollLeft {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

.grid-container {
  display: grid;
  padding-top: 100px;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 30px;
  max-width: 1300px;
  width: 100%;
}

@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}

.info-card {
  position: relative;
  height: 400px;
  border-radius: 20px;
  background-size: cover;
  background-position: center;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.info-card:hover {
  transform: scale(1.02);
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: rgba(11, 37, 89, 0.4);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: all 0.4s ease-in-out;
  padding: 20px;
  text-align: center;
}

.overlay h3 {
  font-size: 32px;
  font-weight: bold;
  color: white;
  margin-bottom: 0;
  transition: transform 0.3s ease, margin-bottom 0.3s ease;
}

.overlay p {
  font-size: 16px;
  color: white;
  opacity: 0;
  max-height: 0;
  overflow: hidden;
  transition: opacity 0.3s ease, max-height 0.3s ease;
}

.info-card:hover .overlay h3 {
  transform: translateY(-20px);
  margin-bottom: 10px;
}

.info-card:hover .overlay p {
  opacity: 1;
  max-height: 200px;
}
</style>
