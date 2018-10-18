import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Register from '@/components/Register'
import NotFound from '@/components/NotFound'
import List from '@/components/List'
import Living from '@/components/Living'
import MyLivingList from '@/components/MyLivingList'
import MyWatchingList from '@/components/MyWatchinglist'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/mywatchinglist',
      name: 'MyWatchingList',
      component: MyWatchingList
    },
    {
      path: '/',
      name: 'Login',
      component: Login
    },
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
      path: '*',
      component: NotFound
    }
  ],
});
export default router;
/*
router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/Login', '/Register'];
  const authRequired = !publicPages.includes(to.path);
  //const loggedIn = localStorage.getItem('user');

  if (authRequired) {
    return next('/Login');
  }

  next();
})
*/
