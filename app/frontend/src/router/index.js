import Vue from 'vue'
import Router from 'vue-router'
import VueCookies from 'vue-cookies'
import RTMP from 'rtmp-streamer'

import Login from '@/components/Login'
import User from '@/components/User'
import Register from '@/components/Register'
import List from '@/components/List'
import Living from '@/components/Living'
import MyLivingList from '@/components/MyLivingList'
import MyWatchingList from '@/components/MyWatchinglist'
import TeacherLiving from '@/components/TeacherLiving'
import HomePage from '@/components/HomePage'

Vue.use(Router)
Vue.use(VueCookies)
Vue.use(RTMP)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      meta: { index: 3 },
      component: Login
    },
    {
      path: '/user',
      name: 'User',
      meta: { index: 2 },
      component: User
    },
    {
      path: '/teacherliving/:url',
      name: 'TeacherLiving',
      meta: { index: 7 },
      component: TeacherLiving
    },
    {
      path: '/mywatchinglist',
      name: 'MyWatchingList',
      meta: { index: 5 },
      component: MyWatchingList
    },
    {
      path: '/register',
      name: 'Register',
      meta: { index: 1 },
      component: Register
    },
    {
      path: '/list',
      name: 'List',
      meta: { index: 4 },
      component: List
    },
    {
      path: '/living/:url',
      name: 'Living',
      meta: { index: 8 },
      component: Living
    },
    {
      path: '/MyLivingList',
      name: 'MyLivingList',
      meta: { index: 6 },
      component: MyLivingList
    },
    {
      path: '/',
      name: 'HomePage',
      meta: { index: 0 },
      component: HomePage
    }
  ]
})

export default router

/*
router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/register', '/living', '/teacherliving', '/mywatchinglist', '/list', '/MyLivingList', '/UserInfo', '/teacherliving', '/developer']
  const authRequired = !publicPages.includes(to.path)
  if (window.$cookies.get('user') === null) {
    if (to.path === '/login') {
      next('/login')
    } else if (to.path === '/register') {
      next('/register')
    } else {
      next('login')
    }
  } else {
    console.log(to.path)
    if (authRequired) {
      if (/^\/(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,16}$/.test(to.path)) {
        next('/teacherliving' + to.path)
      } else {
        next('/list')
      }
    }
  }
  next()
})
*/
