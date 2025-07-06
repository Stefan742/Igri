import { createRouter, createWebHistory } from 'vue-router'
import Home from "@/Pages/Home.vue";
import Results from "@/components/Results.vue";
import SportMatches from "@/components/SportMatches.vue";
import AdminMatches from "@/components/AdminMatches.vue";
import NewsPage from "@/Pages/NewsPage.vue";
const routes = [
    { path: '/', name: 'Home', component: Home },
    {path: '/results', name: 'Results', component: Results},
    { path: '/results/:sport', name: 'SportMatches', component: SportMatches },
    {
        path: '/admin/:sport',
        name: 'AdminMatches',
        component: AdminMatches,
        props: true
    },
    {path: '/news',name: 'News', component: NewsPage},
    {
        path: '/news/:id',
        name: 'NewsDetail',
        component: () => import('@/pages/NewsDetail.vue'),
    }


]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router