<template>
  <section class="contact" id="contact" data-aos="fade-up">
    <div class="scroll-text-wrapper">
      <div class="scroll-text">
        <span v-for="n in 20" :key="n">SPORTSKI IGRI VELES</span>
      </div>
    </div>

    <h2>Контакт</h2>
    <p>
      За повеќе информации пишете ни на:
      <a href="mailto:kontakt@veleski-igri.mk">kontakt@veleski-igri.mk</a>
    </p>

    <div class="social-icons">
      <a href="https://facebook.com" target="_blank" aria-label="Facebook">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="https://instagram.com" target="_blank" aria-label="Instagram">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="https://youtube.com" target="_blank" aria-label="YouTube">
        <i class="fab fa-youtube"></i>
      </a>
    </div>
  </section>
</template>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.contact {
  background-color: #ffc800;
  color: #0B2559;
  text-align: center;
  padding: 100px 20px;
  position: relative;
  overflow: hidden;
}

.contact h2 {
  font-size: 36px;
  margin-bottom: 20px;
  font-weight: bold;
}

.contact p {
  font-size: 18px;
  margin-bottom: 40px;
}

.contact a {
  color: #0B2559;
  font-weight: bold;
  text-decoration: underline;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 20px;
}

.social-icons a {
  font-size: 28px;
  color: #0B2559;
  transition: transform 0.3s ease, color 0.3s ease;
}

.social-icons a:hover {
  color: white;
}

/* Scroll Text */
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
  animation: scrollLeft 80s linear infinite;
  font-size: 80px;
  font-weight: bold;
  color: transparent;
  -webkit-text-stroke: 1px #0B2559;
  opacity: 0.45;
  text-transform: uppercase;
  margin-bottom: 50px;
}

.scroll-text span {
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
