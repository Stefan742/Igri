<template>
  <section class="hero" @mousemove="handleMouseMove">
    <div class="video-container">
      <video src="/videos/hero-video.mp4" autoplay muted loop></video>
      <div class="hue-overlay"></div> <!-- ова е ново -->

      <h1
          class="outline-text"
          :style="textStyle"
      >
        СПОРТСКИ<br />
        ИГРИ<br />
        ВЕЛЕС
      </h1>
    </div>
  </section>
</template>
<script>
export default {
  data() {
    return {
      offsetX: 0,
      offsetY: 0,
    };
  },
  methods: {
    handleMouseMove(e) {
      const centerX = window.innerWidth / 2;
      const centerY = window.innerHeight / 2;
      const moveFactor = 20;

      this.offsetX = ((e.clientX - centerX) / centerX) * moveFactor;
      this.offsetY = ((e.clientY - centerY) / centerY) * moveFactor;
    },
  },
  computed: {
    textStyle() {
      const isMobile = window.innerWidth < 768;

      if (isMobile) {
        return {
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          textAlign: 'center',
          width: '90%',
          fontSize: '32px',
          WebkitTextStroke: '1px #ffc800'
        };
      } else {
        return {
          bottom: '30px',
          right: '40px',
          textAlign: 'right',
          transform: `translate(${this.offsetX}px, ${this.offsetY}px)`
        };
      }
    }
  }




};
</script>


<style scoped>
.hero {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #0B2559;
  overflow: hidden;
  position: relative;
}

.video-container {
  margin-top: 70px;
  position: relative;
  width: 90vw;
  height: 70vh;
  overflow: hidden;
  border-radius: 20px;

}

.video-container video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.outline-text {
  position: absolute;
  font-size: 100px;
  font-weight: bold;
  color: transparent;
  -webkit-text-stroke: 2px #ffc800;
  pointer-events: none;
  text-transform: uppercase;
  z-index: 3;
  transition: transform 0.1s ease-out;
}

@media (max-width: 768px) {
  .video-container {
    position: relative;

    width: 95vw;
    height: 50vh;
    margin-top: 140px;
    border-radius: 12px;
  }
  .outline-text {
    top: 50%;
    left: 50%;
    right: auto;
    bottom: auto;
    transform: translate(-50%, -50%);
    font-size: 32px;
    -webkit-text-stroke: 1px #ffc800;
    text-align: center;
    width: 90%;
    padding: 0 10px;
  }


  .hero {
    height: auto;
    padding-bottom: 2rem;
  }
}

</style>

