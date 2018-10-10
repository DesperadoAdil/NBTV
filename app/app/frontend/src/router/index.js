import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Register from '@/components/Register'
import NotFound from '@/components/NotFound'
Vue.use(Router)




export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    { path: '*', component: 'NotFound' },
    {
      path:'/living',
      name: 'Living',
      component:Living
    }
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
