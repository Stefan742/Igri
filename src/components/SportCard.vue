<template>
  <div class="sport-card" @click="$emit('click')" data-aos="zoom-in">
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
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  text-align: center;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  user-select: none;
}

.sport-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.icon {
  font-size: 3rem;
  margin-bottom: 0.75rem;
  color: #ffc800; /* жолта икона */
}

.name {
  font-weight: 700;
  font-size: 1.125rem;
  color: #0b2559;
  letter-spacing: 0.5px;
}
</style>
