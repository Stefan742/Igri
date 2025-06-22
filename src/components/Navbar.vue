<template>
  <nav class="navbar">
    <div class="navbar-container">
     <router-link to="/">
      <div
          class="logo-iv"
          @mouseenter="hovered = true"
          @mouseleave="hovered = false"
          :class="{ expand: hovered }"
      >
        <span class="main-i">I</span>
        <span class="expanding igrispan">GRI</span>
        <span class="main-v">V</span>
        <span class="expanding velesspan">ELES</span>
      </div>
     </router-link>
      <ul class="nav-links">
        <li><a href="#about">ABOUT US</a></li>
        <li><router-link to="/results">SPORTS</router-link></li>
        <li><a href="#gallery">GALLERY</a></li>
        <li><a href="#contact">CONTACT</a></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      hovered: false,
    };
  },
};
</script>

<style scoped>

.navbar {
  position: fixed;
  top: 0;
  width: 100%;
  height: 100px;
  background-color: rgba(11, 37, 89, 0.9);
  padding: 1rem 0;
  z-index: 999;
}

.navbar-container {
  max-width: 1200px;
  margin: auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* ... останати стилови ... */

.logo-iv {
  display: flex;
  align-items: center;
  font-family: 'Race Sport', sans-serif;
  overflow: hidden;
  font-size: 28px;  /* основен фонт, ама main-i и main-v ќе го надесиме */
  color: #ffc800;
  transition: all 0.5s ease;
  gap: 0;
  margin-left: -100px;
}

.main-i,
.main-v,
.igrispan,
.velesspan  {
  font-size: 48px;  /* зголемен фонт */
  font-weight: 700;
  transition: inherit;
}

.expanding {
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s ease-in-out;
  opacity: 1;
}

.logo-iv.expand .expanding {
  transform: scaleX(1);
  margin-left: 4px;
}

.logo-iv .igrispan {
  transition-delay: 0s;
}

.logo-iv .velesspan {
  transition-delay: 0.1s;
  margin-left: 8px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin-right: -100px;
}

.nav-links a,
.nav-links  router-link{
  color: white;
  text-decoration: none;
  font-size: 18px;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #ffc800;
}
.main-v {
  margin-left: -100px;
  transition: transform 0.4s ease-in-out;
}

.logo-iv.expand .main-v {
  transform: translateX(100px); /* прилагоди според ширина на "IGRI" */
}
.velesspan {
  margin-left: 2px;
  opacity: 0;
  transform: translateX(-20px);
  transition:
      margin-left 0.4s ease-in-out,
      opacity 0.2s ease-in-out,
      transform 0.4s ease-in-out;
}
a{
  text-decoration: none;
}
.logo-iv.expand .velesspan {
  margin-left: 100px;
  opacity: 1;
  transform: translateX(0);
}
</style>
