<template>
  <div class="loading-screen">
    <div class="container">
      <div class="ball">
        <div class="inner">
          <div class="line"></div>
          <div class="line line--two"></div>
          <div class="oval"></div>
          <div class="oval oval--two"></div>
        </div>
      </div>
      <div class="shadow"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoadingScreen',
};
</script>

<style scoped>
.loading-screen {
  position: fixed;
  inset: 0;
  background-color: #0B2559;
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* ANIMATION: Ball & Shadow */
@keyframes rotateBall {
  0% {
    transform: rotateY(0deg) rotateX(0deg) rotateZ(0deg);
  }
  50% {
    transform: rotateY(360deg) rotateX(360deg) rotateZ(0deg);
  }
  100% {
    transform: rotateY(720deg) rotateX(720deg) rotateZ(360deg);
  }
}

@keyframes bounceBall {
  0% {
    transform: translateY(-70px) scale(1, 1);
  }
  15% {
    transform: translateY(-56px) scale(1, 1);
  }
  45% {
    transform: translateY(70px) scale(1, 1);
  }
  50% {
    transform: translateY(73.5px) scale(1, 0.92);
  }
  55% {
    transform: translateY(70px) scale(1, 0.95);
  }
  85% {
    transform: translateY(-56px) scale(1, 1);
  }
  95% {
    transform: translateY(-70px) scale(1, 1);
  }
  100% {
    transform: translateY(-70px) scale(1, 1);
  }
}

@keyframes bounceShadow {
  0% {
    filter: blur(3px);
    opacity: 0.6;
    transform: translateY(73px) scale(0.5, 0.5);
  }
  45% {
    filter: blur(1px);
    opacity: 0.9;
    transform: translateY(73px) scale(1, 1);
  }
  55% {
    filter: blur(1px);
    opacity: 0.9;
    transform: translateY(73px) scale(1, 1);
  }
  100% {
    filter: blur(3px);
    opacity: 0.6;
    transform: translateY(73px) scale(0.5, 0.5);
  }
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.ball {
  animation: bounceBall 1.2s infinite cubic-bezier(0.42, 0, 0.58, 1);
  border-radius: 50%;
  height: 60px;
  width: 60px;
  transform: translateY(-70px);
  transform-style: preserve-3d;
  position: relative;
  z-index: 1;
}

.ball::before {
  background: radial-gradient(circle at 36px 20px, #ff8c16, #b35100);
  border: 2px solid #333;
  border-radius: 50%;
  content: "";
  height: calc(100% + 6px);
  left: -6px;
  position: absolute;
  top: -3px;
  transform: translateZ(1vmin);
  width: calc(100% + 6px);
}

.ball .inner {
  animation: rotateBall 25s linear infinite;
  border-radius: 50%;
  height: 100%;
  width: 100%;
  position: absolute;
  transform-style: preserve-3d;
}

.line::before,
.line::after {
  border: 2px solid #333;
  border-radius: 50%;
  content: "";
  height: 99%;
  position: absolute;
  width: 99%;
}

.line::before {
  transform: rotate3d(0, 0, 0, 0);
}

.line::after {
  transform: rotate3d(1, 0, 0, 90deg);
}

.line--two::before {
  transform: rotate3d(0, 0, 0, 2deg);
}

.line--two::after {
  transform: rotate3d(1, 0, 0, 88deg);
}

.oval::before,
.oval::after {
  border-top: 4px solid #333;
  border-radius: 50%;
  content: "";
  height: 99%;
  position: absolute;
  width: 99%;
}

.oval::before {
  transform: rotate3d(1, 0, 0, 45deg) translate3d(0, 0, 6px);
}

.oval::after {
  transform: rotate3d(1, 0, 0, -45deg) translate3d(0, 0, -6px);
}

.oval--two::before {
  transform: rotate3d(1, 0, 0, 135deg) translate3d(0, 0, -6px);
}

.oval--two::after {
  transform: rotate3d(1, 0, 0, -135deg) translate3d(0, 0, 6px);
}

.shadow {
  animation: bounceShadow 1.2s infinite cubic-bezier(0.42, 0, 0.58, 1);
  background: black;
  filter: blur(2px);
  border-radius: 50%;
  height: 6px;
  width: 54px;
  transform: translateY(73px);
}
</style>
