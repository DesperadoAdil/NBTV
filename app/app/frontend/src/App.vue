<template>
  <div id="app">
    <Menu mode="horizontal" :theme="theme1" active-name="active" class="nav">

      <router-link to="/list">
        <MenuItem name="2" style="font-size: 20px">
          <Icon type="ios-people" />
          教室列表
        </MenuItem>
      </router-link>

      <router-link to="/mywatchinglist">
      <MenuItem name="4" class="mylist">
        <Icon type="logo-youtube" />
        我加入的直播间
      </MenuItem>
      </router-link>
      <router-link to="/login">
        <MenuItem name="1" style="float: right;" class="ilogin">
          <Icon type="ios-contact-outline" />
          {{ LoginOrLogout }}
        </MenuItem>
      </router-link>
    </Menu>
  </br>
  </br>
    <router-view/>
  </div>
</template>

<script type="es6">
export default {
  name: 'App',
  data () {
    return {
      theme1: 'light',
      active:"",
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: '',
      },
      LoginOrLogout: '登录',
    }
  },
  created() {
    this.showUserInfo();
  },
  methods: {
    showUserInfo() {
      this.userInfo['username'] = this.$cookies.get('user').username;
      this.userInfo['status']= this.$cookies.get('user').status;
      this.userInfo['password'] = this.$cookies.get('user').password;
      this.userInfo['mobile'] = this.$cookies.get('user').mobile;
      if (this.userInfo['status'] === 'success') {
        this.LoginOrLogout = this.userInfo['username'];
      }
    }
  }
};

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
.nav {
  width: 100%;
  margin: 0 auto;
}
.userInfo {
  margin-right: 20px;
}
  .mylist{
    margin-right: 20px;
    font-size: 20px;
  }
  .ilogin{
    float:right;
    font-size: 20px;
  }
</style>
