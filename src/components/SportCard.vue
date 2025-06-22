<template>
  <div class="sport-card" @click="$emit('click')">
    <div class="icon">{{ icon }}</div>
    <h3 class="name">{{ name }}</h3>
  </div>
</template>

<script setup>
defineProps(['name', 'icon'])
</script>

<style scoped>
.sport-card {
  cursor: pointer;
  background-color: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
  text-align: center;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  user-select: none;
}

.sport-card:hover {
  background-color: #fef3c7; /* светло жолта боја */
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.15);
}

.icon {
  font-size: 3rem;
  margin-bottom: 0.75rem;
}

.name {
  font-weight: 700;
  font-size: 1.125rem;
  color: #0b2559;
  user-select: none;
}
</style>
