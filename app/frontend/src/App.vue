<template>
  <div id="app">
    <vue-headful
      title="NBTV"
      />
    <Menu mode="horizontal" :theme="theme1" active-name="active">
      <MenuItem name="0" class="mylist" @click.native="handleJump('/')">
        <Icon type="ios-home" />
        首页
      </MenuItem>
      <MenuItem name="2" class="mylist" @click.native="handleJump('list')">
        <Icon type="ios-people" />
        课程广场
      </MenuItem>
      <MenuItem name="3" class="mylist" @click.native="handleJump('myWatchingList')">
        <Icon type="logo-youtube" />
        我参与的
      </MenuItem>

      <MenuItem name="1" style="float:right">
        <Dropdown trigger="custom" :visible="visible" placement="bottom-end" style="">
          <a href="javascript:void(0)" trigger="click" @click="handleOpen">
            <Icon v-if="LoginOrLogout === '登录'" type="ios-contact-outline"></Icon>
              {{ LoginOrLogout }}
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list" style="width: 120px">
            <DropdownItem>
              <div @click="handleJump('user')">
                用户信息
              </div>
            </DropdownItem>
            <DropdownItem divided>
              <div @click="logout()">
                登出
              </div>
            </DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </MenuItem>
      <MenuItem v-if="isTeacher()" name="4" style="float:right" @click.native="handleJump('myLivingList')">
        <Icon type="ios-videocam" />
        开播
      </MenuItem>
    </Menu>
    <transition :name="transitionName">
      <router-view/>
    </transition>
  </div>
</template>

<script >
import router from './router'
import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      transitionName: '',
      visible: false,
      theme1: 'light',
      active: '',
      userInfo: {
        status: 'success',
        username: '',
        password: '',
        mobile: '',
        job: 'teacher'
      },
      LoginOrLogout: '登录'
    }
  },
  created () {
    this.showUserInfo()
  },
  methods: {
    handleOpen () {
      if (this.LoginOrLogout === '登录') {
        router.push('/login')
        return
      }
      this.visible = this.visible !== true
    },
    isTeacher () {
      return this.userInfo['job'] === 'teacher'
    },
    handleJump (name) {
      this.visible = false
      if (name === '/') {
        router.push('/')
      } else if (this.userInfo['status'] !== 'success') { // 未登录
        router.push('/login')
      } else if (name === 'list') {
        router.push('/list')
      } else if (name === 'myLivingList') {
        router.push('/mylivinglist')
      } else if (name === 'myWatchingList') {
        router.push('/mywatchinglist')
      } else if (name === 'user') {
        router.push('/user')
      }
    },
    logout () {
      this.visible = false
      this.LoginOrLogout = '登录'
      this.userInfo = {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: ''
      }
      router.push('/login')
      this.$cookies.remove('user')
    },
    showUserInfo () {
      if (this.$cookies.get('user') === null) {
        return
      }
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['job'] = this.$cookies.get('user').job
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      if (this.userInfo['status'] === 'success') {
        this.LoginOrLogout = this.userInfo['username']
      }
    }
  },
  watch: {
    '$route' (to, from) {
      if (to.meta.index > from.meta.index) {
        this.transitionName = 'slide-right';
      } else {
        this.transitionName = 'slide-left';
      }
    }
  }
}

</script>

<style>
  #app {
    min-width: 1200px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  .mylist{
    font-size: 20px;
  }
  .router {
    padding: 0 5%;
  }

  .slide-right-enter-active,
  .slide-right-leave-active,
  .slide-left-enter-active,
  .slide-left-leave-active {
    will-change: transform;
    transition: all 500ms;
    position: absolute;
  }
  .slide-right-enter {
    opacity: 0;
    transform: translate3d(-100%, 0, 0);
  }
  .slide-right-leave-active {
    opacity: 0;
    transform: translate3d(100%, 0, 0);
  }
  .slide-left-enter {
    opacity: 0;
    transform: translate3d(100%, 0, 0);
  }
  .slide-left-leave-active {
    opacity: 0;
    transform: translate3d(-100%, 0, 0);
  }
</style>
