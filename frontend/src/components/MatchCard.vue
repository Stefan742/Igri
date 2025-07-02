<template>
  <div class="match-card" data-aos="fade-up">
    <div class="match-info">
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
  background: #0B2559;
  border-left: 6px solid #ffc800;
  padding: 1.5rem;
  border-radius: 20px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.match-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}

.match-info h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: white;
  margin-bottom: 0.5rem;
}

.match-info p {
  font-size: 0.875rem;
  color: red;
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0;
}

.dot {
  width: 10px;
  height: 10px;
  background-color: red;
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
    transform: scale(1.4);
    opacity: 0.6;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.score {
  font-size: 1.75rem;
  font-weight: 800;
  color: #ffc800;
  align-self: flex-end;
}
</style>
