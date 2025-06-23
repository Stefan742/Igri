<template>
  <div class="match-card" data-aos="fade-up">
    <div class="teams">
      <h3>{{ match.teams }}</h3>
      <p><span class="dot" /> {{ match.time }}</p>
    </div>
    <div class="score">{{ match.score }}</div>
  </div>
</template>

<script setup>
defineProps(['match'])
</script>

<style scoped>
.match-card {
  background: white;
  padding: 1rem 1.25rem;
  border-radius: 16px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.match-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

.teams h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #0b2559;
  margin-bottom: 0.25rem;
}

.teams p {
  font-size: 0.875rem;
  color: #666;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 6px;
}

.dot {
  width: 8px;
  height: 8px;
  background-color: #ffc800;
  border-radius: 50%;
  animation: pulse 1.5s infinite;
  display: inline-block;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.5);
    opacity: 0.5;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.score {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffc800;
}
</style>
