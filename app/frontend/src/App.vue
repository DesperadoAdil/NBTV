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

      <MenuItem name="1" style="float:right;" @click.native="showinfo = true" type="primary">
        <Icon v-if="LoginOrLogout === '登录'" type="ios-contact-outline" />
          {{ LoginOrLogout }}
        <Drawer title="User Info" v-model="showinfo" width="480">
          <Form>
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Name" label-position="left" label-width="80">
                  {{userInfo.username}}
                </FormItem>
              </Col>
              <Col span="6">
              </Col>
            </Row>
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Job" label-position="left" label-width="80">
                  {{userInfo.job}}
                </FormItem>
              </Col>
              <Col span="6">
              </Col>
            </Row>
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Password" label-position="left" label-width="80">
                  <Input v-model="userInfo.password" placeholder="please enter user name" />
                </FormItem>
              </Col>
              <Col span="6">
                <FormItem>
                  <Button>Edit</Button>
                </FormItem>
              </Col>
            </Row>
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Mobile" label-position="left" label-width="80">
                  <Input v-model="userInfo.mobile" placeholder="please enter user name" />
                </FormItem>
              </Col>
              <Col span="6">
                <FormItem>
                  <Button>Edit</Button>
                </FormItem>
              </Col>
            </Row>
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Status" label-position="left" label-width="80">
                  <Input v-model="userInfo.status" placeholder="please enter user name" />
                </FormItem>
              </Col>
              <Col span="6">
                <FormItem>
                  <Button>Edit</Button>
                </FormItem>
              </Col>
            </Row>
            <!--
            <FormItem label="Name" label-position = "left" label-width="80">
              <Input v-model="userInfo.username" placeholder="enter name" readonly="true"/>
            </FormItem>
            <FormItem label="mobile" label-position = "left" label-width="80" >
              <Input v-model="userInfo.mobile" placeholder="enter mobile" readonly="editmobile = true"/>
            </FormItem>
            <FormItem label="password" label-position = "left" label-width="80" >
              <Input v-model="userInfo.password" placeholder="enter mobile" readonly="editmobile = true"/>
            </FormItem>
            <FormItem  label="repeat password" label-position = "left" label-width="80" >
              <Input v-model="userInfo.password" placeholder="enter mobile" readonly="editmobile = true"/>
            </FormItem>
            <FormItem label="status" label-position = "left" label-width="80" >
              <Input v-model="userInfo.status" placeholder="enter mobile" readonly="editmobile = true"/>
            </FormItem>

            -->
          </Form>
          <div class="demo-drawer-footer">
            <Button style="margin-right: 8px" @click="showinfo = false">Apply</Button>
            <Button type="primary" @click.native="logout">Log out</Button>
          </div>
        </Drawer>
      </MenuItem>
    </Menu>
    <router-view/>
    <!--
    <Drawer title="show" v-model="showinfo" width="720">
      <Form :model="infopage">
        <FormItem label="Name" label-position="top">
          <Input v-model="userInfo.username" placeholder="please enter user name" />
        </FormItem>

        <FormItem label="Password" label-position="top">
          <Input v-model="formInline.password" placeholder="please enter password" />
        </FormItem>

        <FormItem label="Repeat Password" label-position="top">
          <Input v-model="formInline.rpassword" placeholder="please re-enter password" />
        </FormItem>

        <FormItem label="Mobile" label-position="top">
          <Input v-model="userInfo.mobile" placeholder="please enter mobile number" />
        </FormItem>

        <FormItem label="Verification" label-position="top">
          <Input v-model="formInline.Verification" placeholder="please enter verification" />
        </FormItem>

      </Form>
      <div class="demo-drawer-footer">
        <Button style="margin-right: 8px" @click="showinfo = false">Cancel</Button>
        <Button type="primary" @click="showinfo = false">Submit</Button>
      </div>
    </Drawer>
    -->
  </div>
</template>

<script >
import router from './router'
export default {
  name: 'App',
  data () {
    return {
      showinfo: false,
      editmobile: false,
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
.demo-drawer-footer{
  width: 100%;
  position: absolute;
  bottom: 0;
  left: 0;
  border-top: 1px solid #e8e8e8;
  padding: 10px 16px;
  text-align: right;
  background: #fff;
}
</style>
