import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PricetrendView from '../views/PricetrendView.vue'
import PricehistoryView from '../views/PricehistoryView.vue'
import AboutusView from '../views/AboutusView.vue'
import ContactView from '../views/ContactView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/pricetrend',
    name: 'pricetrend',
    component: PricetrendView,
  },
  {
    path: '/pricehistory',
    name: 'pricehistory',
    component: PricehistoryView,
  },
  {
    path: '/aboutus',
    name: 'aboutus',
    component: AboutusView,
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
