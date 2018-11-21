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
      path: '/mylivinglist',
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

import axios from 'axios'
router.beforeEach((to, from, next) => {
  console.log("from "+from.path+" to "+to.path)
  const publicPages = ['/', '/register', '/Register', '/login', '/Login']
  const privatePages = ['/user', '/list', '/mywatchinglist', '/mylivinglist']
  const developerPages = ['developer']
  if (window.$cookies.get('user') === null) {
    if (publicPages.includes(to.path)) {
      next()
    } else {
      next('/login')
    }
  } else {
    if (to.path === '/') next()
    else if (publicPages.includes(to.path)) {
      next('/')
    } else if (to.path === '/mylivinglist') {
      if (window.$cookies.get('user').job === 'teacher') next()
      else next('/list')
    } else if (privatePages.includes(to.path)) {
      next()
    } else if (/^\/living\/[a-zA-Z\d]+$/.test(to.path)) {
      const data = {
        'username': window.$cookies.get('user').username,
        'url': to.path.split('/')[2]
      }
      axios.post('/api/classroom/urlcheck', data).then((resp) => {
        if (resp.data.status === "success") {
          window.$Message.success('成功进入直播间!')
          next()
        } else if (resp.data.status === "password") {
          console.log("password needed!")
          var currentpassword = ''
          next()
          /*this.$Modal.confirm({
            render: (h) => {
              return h('Input', {
                props: {
                  id: 'passinput',
                  autofocus: true,
                  placeholder: 'Please enter the password of this room'
                },
                on: {
                  input: (val) => {
                    this.currentpassword = val
                  }
                }
              })
            },
            onOk: () => {
              if (this.currentpassword === resp.data.password) {
                next()
              } else {
                window.$Notice.error({
                  title: '消息提示',
                  desc: '您输入的密码错误，请仔细检查!'
                })
                next(from.path)
              }
            }
          })*/
        } else if (resp.data.status === "error") {
          window.$Message.success('权限不足，进入直播间失败!')
          next(from.path)
        } else {
          window.$Message.success('发生未知错误!')
          next(from.path)
        }
      })
      //next()
    } else if (/^\/teacherliving\/[a-zA-Z\d]+$/.test(to.path)) {
      if (window.$cookies.get('user').job === 'teacher') next()
      else next('/list')
    } else {
      next('/list')
    }
  }
})
