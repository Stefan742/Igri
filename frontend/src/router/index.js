import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/Pages/Home.vue";
import Results from "@/components/Results.vue";
import SportMatches from "@/components/SportMatches.vue";
const routes = [
    { path: '/', name: 'Home', component: Home },
    {path: '/results', name: 'Results', component: Results},
    { path: '/results/:sport', name: 'SportMatches', component: SportMatches }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router