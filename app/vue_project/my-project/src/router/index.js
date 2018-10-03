import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Register from '@/components/Register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    { path: '*', redirect: '/Login' }
  ]
});

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