<template>
  <div class="match-card">
    <div class="teams">
      <h3>{{ match.teams }}</h3>
      <p>{{ match.time }}</p>
    </div>
    <div class="score">{{ match.score }}</div>
  </div>
</template>

<script setup>
defineProps(['match'])
</script>

<style scoped>
.match-card {
  background-color: white;
  padding: 1rem 1.25rem;
  border-radius: 12px;
  box-shadow: 0 2px 6px rgb(0 0 0 / 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  cursor: default;
}

.teams h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #0b2559;
  margin-bottom: 0.25rem;
}

.teams p {
  font-size: 0.875rem;
  color: #888;
  margin: 0;
}

.score {
  font-size: 1.25rem;
  font-weight: 700;
  color: #ffc800;
}
</style>
