<template>
  <div id="app">
    <Menu mode="horizontal" active-name="1">
      <MenuItem name="1">
        <Icon type="ios-paper" />
        登录
      </MenuItem>
      <MenuItem name="2">
        <Icon type="ios-people" />
        教室列表
      </MenuItem>
      <MenuItem name="3">
        <Icon type="ios-construct" />
        我的信息
      </MenuItem>
    </Menu>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      theme1: 'light'
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
</style>
