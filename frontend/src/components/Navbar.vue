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

      <!-- Burger Menu Icon -->
      <div class="burger" @click="toggleMenu">
        <span :class="{ open: menuOpen }"></span>
        <span :class="{ open: menuOpen }"></span>
        <span :class="{ open: menuOpen }"></span>
      </div>

      <!-- Nav Links -->
      <ul :class="['nav-links', { open: menuOpen }]">
        <li><a href="#about" @click="closeMenu">ABOUT US</a></li>
        <li><router-link to="/results" @click.native="closeMenu">SPORTS</router-link></li>
        <li><router-link to="/news" @click.native="closeMenu">NEWS</router-link></li>
        <li><a href="#contact" @click="closeMenu">CONTACT</a></li>
      </ul>
    </div>
  </nav>
</template>


<script>
export default {
  data() {
    return {
      hovered: false,
      menuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
    },
    closeMenu() {
      this.menuOpen = false;
    },
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

/* Logo */
.logo-iv {
  display: flex;
  align-items: center;
  font-family: 'Race Sport', sans-serif;
  overflow: hidden;
  font-size: 28px;
  color: #ffc800;
  transition: all 0.5s ease;
  gap: 0;
  margin-left: -100px;
}

.main-i,
.main-v,
.igrispan,
.velesspan {
  font-size: 48px;
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

.main-v {
  margin-left: -100px;
  transition: transform 0.4s ease-in-out;
}
.logo-iv.expand .main-v {
  transform: translateX(100px);
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
.logo-iv.expand .velesspan {
  margin-left: 100px;
  opacity: 1;
  transform: translateX(0);
}

/* Nav Links - Desktop */
.nav-links {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin-right: -100px;
}
.nav-links a,
.nav-links router-link {
  color: white;
  text-decoration: none;
  font-size: 18px;
  transition: color 0.3s ease;
}
.nav-links a:hover {
  color: #ffc800;
}
a {
  text-decoration: none;
}

/* Burger Menu Icon */
.burger {
  display: none;
  flex-direction: column;
  cursor: pointer;
  gap: 6px;
}
.burger span {
  width: 25px;
  height: 3px;
  background: white;
  border-radius: 2px;
  transition: all 0.3s ease;
}
.burger span.open:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}
.burger span.open:nth-child(2) {
  opacity: 0;
}
.burger span.open:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

/* Responsive Styles */
@media (max-width: 768px) {
  .burger {
    display: flex;
  }

  .nav-links {
    position: absolute;
    top: 100px;
    left: 0;
    width: 100vw;
    flex-direction: column;
    background-color: rgba(11, 37, 89, 0.95);
    padding: 1rem 0;
    align-items: center;
    gap: 1rem;
    transform: translateY(-200%);
    transition: transform 0.3s ease-in-out;
  }

  .nav-links.open {
    transform: translateY(0);
  }

  .nav-links li {
    margin: 0.5rem 0;
  }
}
@media (max-width: 768px) {
  .logo-iv {
    margin-left: 0 !important;
    gap: 4px;
  }

  .main-v {
    margin-left: 0 !important;
    transform: none !important;
  }

  .logo-iv.expand .main-v {
    transform: none !important;
  }

  /* СКРИЈ ги анимираните зборови */
  .igrispan,
  .velesspan {
    display: none !important;
  }
}


</style>
