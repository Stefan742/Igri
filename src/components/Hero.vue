<template>
  <section class="hero" @mousemove="handleMouseMove">
    <div class="video-container">
      <video src="/videos/hero-video.mp4" autoplay muted loop></video>
      <div class="hue-overlay"></div> <!-- ова е ново -->

      <h1
          class="outline-text"
          :style="{
          transform: `translate(${offsetX}px, ${offsetY}px)`
        }"
      >
        СПОРТСКИ ИГРИ ВЕЛЕС
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
.hue-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /*background-color: #ffc800;*/
  /*!*opacity: 0.70; !* или прилагоди колку да биде интензивно *!*!*/
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1000;
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
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 100px;  font-weight: bold;
  color: transparent;
  -webkit-text-stroke: 2px #ffc800; /* outline */
  text-align: center;
  pointer-events: none;
  transition: transform 0.1s ease-out;
  text-transform: uppercase;
  z-index: 3;
}
</style>

