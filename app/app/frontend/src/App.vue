<template>
  <div id="app">
    <Menu mode="horizontal" :theme="theme1" active-name="active" class="nav">

      <router-link to="/list">
        <MenuItem name="2" class="mylist">
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
          登录
        </MenuItem>
      </router-link>
    </Menu>
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
  /*padding-left: 5%;*/
  width: 100%;
  margin: 0 auto;
  /*padding-right: 7%;*/
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
