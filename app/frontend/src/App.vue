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
        <Drawer title="User Information" v-model="showinfo" width="480">
          <Form>

            <!-- 用户名称 -->
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Name" label-position="left" label-width="80">
                  {{userInfo.username}}
                </FormItem>
              </Col>
              <Col span="6">
              </Col>
            </Row>

            <!-- 用户身份 -->
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Job" label-position="left" label-width="80">
                  {{userInfo.job}}
                </FormItem>
              </Col>
              <Col span="6">
              </Col>
            </Row>

            <!-- 用户手机号 -->
            <Row :gutter="32">
              <Col span="18">
                <FormItem label="Mobile" label-position="left" label-width="80">
                  {{userInfo.mobile}}
                </FormItem>
              </Col>
              <Col span="6">
                <FormItem>
                  <Button @click="modalmobile = true">Edit</Button>
                  <Modal
                    v-model="modalmobile"
                    title="Change your mobile"
                    @on-ok="changemobile"
                    @on-cancel="cancel">
                    <Input label="old phone number" v-model="userInfo.mobile" readonly="true"></Input>
                    <Input label="enter new mobile" v-model="newMobile"></Input>
                  </Modal>
                </FormItem>
              </Col>
            </Row>

            <!-- 用户密码 -->
            <Row :gutter="32" >
              <Col span="18">
                <FormItem label="Password" label-position="left" label-width="80">
                  {{userInfo.password}}
                </FormItem>
              </Col>
              <Col span="6">
                <FormItem>
                  <Button @click="changepassword()">Edit</Button>
                </FormItem>
              </Col>
            </Row>
          </Form>
          <div class="demo-drawer-footer">
            <Button style="margin-right: 8px" @click="showinfo = false">Apply</Button>
            <Button type="primary" @click.native="logout">Log out</Button>
          </div>
        </Drawer>
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
        showinfo: false,
        editmobile: false,
        showrpass: false,
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
      cancel () {
        this.$Message.info('Cancel the change of password')
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
      changepassword () {
        this.showrpass = false
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
