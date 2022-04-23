import { createRouter, createWebHistory } from 'vue-router'
import AddCarForm from '../components/AddCarForm.vue'
import ExploreView from '../views/ExploreView.vue'
import HomeView from '../views/HomeView.vue'
import Profile from '../views/Profile.vue'
import LoginpageView from '../views/LoginpageView.vue'
import RegisterForm from '../components/RegisterForm.vue'
import FrontpageView from '../views/FrontpageView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Frontpage',
      component: FrontpageView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/car',
      name: 'car',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AddCarForm
    },
    {
    path: '/explore',
    name: 'explore',
      component: ExploreView
    },
    {
      path: '/Profile',
      name: 'Profile',
      component: Profile
      },
      {
        path: '/Login',
        name: 'Login',
        component: LoginpageView
        },
        {
          path: '/register',
          name: 'register',
          component: RegisterForm
          }

  ]
});

export default router
