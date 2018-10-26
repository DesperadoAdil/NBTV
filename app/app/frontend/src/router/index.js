import Vue from 'vue'
import Router from 'vue-router'
import VueCookies from 'vue-cookies'

import Login from '@/components/Login'
import Register from '@/components/Register'
import List from '@/components/List'
import Living from '@/components/Living'
import MyLivingList from '@/components/MyLivingList'
import MyWatchingList from '@/components/MyWatchinglist'
import UserInfo from '@/components/UserInfo'
import TeacherLiving from '@/components/TeacherLiving'

Vue.use(Router)
Vue.use(VueCookies)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/teacherliving/:url',
      name: 'TeacherLiving',
      component: TeacherLiving
    },
    {
      path: '/mywatchinglist',
      name: 'MyWatchingList',
      component: MyWatchingList
    },
    //  {
    //    path: '/',
    //    name: 'Login',
    //    component: Login
    //  },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/list',
      name: 'List',
      component: List
    },
    {
      path: '/living',
      name: 'Living',
      component: Living
    },
    {
      path: '/MyLivingList',
      name: 'MyLivingList',
      component: MyLivingList
    },
    {
      path: '/UserInfo',
      name: 'UserInfo',
      component: UserInfo
    }

  ]
})

export default router

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page

  // if (to.path !== '/login' && window.$cookies.get('user') === null) {
  //  return next('/login');
  // }
  // const publicPages = ['/login', '/Register', '/living','/teacherliving', '/mywatchinglist', '/list', '/MyLivingList', '/UserInfo', '/teacherliving', '/developer']
  // const authRequired = !publicPages.includes(to.path)
  //
  // if (authRequired) {
  //  return next('/list')
  // }

  next()
})
