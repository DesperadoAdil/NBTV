<template>
  <div id="app">
    <Menu mode="horizontal" active-name="1" class="nav">
      <router-link to="/login">
        <MenuItem name="1">
          <Icon type="ios-paper" />
          登录
        </MenuItem>
      </router-link>
      <router-link to="/list">
        <MenuItem name="2">
          <Icon type="ios-people" />
          教室列表
        </MenuItem>
      </router-link>
      <MenuItem name="3" class="userInfo">
        我的信息
      </MenuItem>
      <router-link to="/mylist">
      <MenuItem name="4" class="mylist">
        我加入的直播间
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
      theme1: 'light'
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
  }
</style>
