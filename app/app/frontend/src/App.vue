<template>
  <div id="app">
    <Menu mode="horizontal" :theme="theme1" active-name="active">
      <MenuItem name="2" class="mylist" @click.native="handleJump('list')">
        <Icon type="ios-people" />
        教室列表
      </MenuItem>
      <MenuItem name="3" class="mylist" @click.native="handleJump('myWatchingList')">
        <Icon type="logo-youtube" />
        我加入的直播间
      </MenuItem>
      <MenuItem v-if="isTeacher()" name="4" class="mylist" @click.native="handleJump('myLivingList')">
        <Icon type="logo-youtube" />
        我开的直播间
      </MenuItem>

      <!--

      将登出部分整合到下拉菜单中

      <MenuItem v-if="LoginOrLogout !== '登录'" name="5" style="float:right" class="ilogin" @click.native="logout">
        {{ '登出' }}
      </MenuItem>
      -->

      <MenuItem name="1" style="float:right;" class="ilogin" @click.native="handleJump('UserInfo')">
        <Icon v-if="LoginOrLogout === '登录'" type="ios-contact-outline" />
          {{ LoginOrLogout }}
      </MenuItem>
    </Menu>
    <router-view/>
  </div>
</template>

<script >
import router from './router'
export default {
  name: 'App',
  data () {
    return {
      theme1: 'light',
      active: '',
      userInfo: {
        status: 'success',
        username: 'adil',
        password: '123456',
        mobile: '18810081008',
        job: 'teacher'
      },
      // changed this to 已登录 to debug
      LoginOrLogout: '已登录'
    }
  },
  created () {
    this.showUserInfo()
  },
  methods: {
    logout () {
      this.LoginOrLogout = '登录'
      this.userInfo = {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: ''
      }
      this.$cookies.remove('user')
      router.push('/Login')
    },
    isTeacher () {
      return this.userInfo['job'] === 'teacher'
    },
    handleJump (name) {
      if (this.userInfo['status'] !== 'success') { // 未登录
        router.push('/login')
      } else if (name === 'list') {
        router.push('/list')
      } else if (name === 'myLivingList') {
        router.push('/MyLivingList')
      } else if (name === 'myWatchingList') {
        router.push('/mywatchinglist')
      } else if (name === 'UserInfo') {
        router.push('/UserInfo')
      }
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
  margin-right: 20px;
  font-size: 20px;
}
.ilogin{
  font-size: 20px;
}
</style>
