<template>
  <div id="app">
    <vue-headful
      title="NBTV"
      />
    <Menu mode="horizontal" :theme="theme1" active-name="active">
      <MenuItem name="2" class="mylist" @click.native="handleJump('list')">
        <Icon type="ios-people" />
        课程广场
      </MenuItem>
      <MenuItem name="3" class="mylist" @click.native="handleJump('myWatchingList')">
        <Icon type="logo-youtube" />
        我参与的
      </MenuItem>

      <MenuItem name="1" style="float:right" @click.native="showInfo = true">

        <Dropdown trigger="custom" :visible="visible" placement="bottom-end" style="">
          <a href="javascript:void(0)" trigger="click" @click="handleOpen">
            <Icon v-if="LoginOrLogout === '登录'" type="ios-contact-outline"></Icon>
              {{ LoginOrLogout }}
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list" style="width: 400px">

            <Form>
              <!-- 用户名称 -->
              <FormItem label="Name" label-position="left" label-width="80">
                {{userInfo.username}}
              </FormItem>
              <!-- 用户身份 -->
              <FormItem label="Job" label-position="left" label-width="80">
                {{userInfo.job}}
              </FormItem>
              <!-- 用户手机号 -->
              <FormItem label="Current Mobile" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                    <Input type="text" v-model="userInfo.mobile" readonly></Input>
                  </Col>
                  <Col span="10">
                    <Button @click="changeMobile()">{{mobileButton}}</Button>
                  </Col>
                </Row>
              </FormItem>
              <!-- 用户的新手机号 -->
              <FormItem v-if="showNewMobile" label="New Mobile" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                      <Input type="text" v-model="this.newMobile" placeholder="New Phone Number Here"></Input>
                  </Col>
                  <Col span="10">
                      <Button @click="sendVerification()">Send</Button>
                  </Col>
                </Row>
              </FormItem>
              <!-- 设置旧手机的验证码 -->
              <FormItem v-if="showNewMobile" label="Verification" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                     <Input v-model="oldVerification" placeholder="Old Verification Code Here"></Input>
                  </Col>
                </Row>
              </FormItem>
              <!-- 设置新手机的验证码 -->
              <FormItem v-if="showNewMobile" label="Verification" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                     <Input v-model="newVerification" placeholder="New Verification Code Here"></Input>
                  </Col>
                  <Col span="10">
                    <Button @click="submitMobileChange()">Verify</Button>
                  </Col>
                </Row>
              </FormItem>
              <!-- 用户密码 -->
              <FormItem label="Current Password" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                    <Input type="text" v-model="newPassword"></Input>
                  </Col>
                  <Col span="10">
                     <Button @click="changePassword()">{{passButton}}</Button>
                  </Col>
                </Row>
              </FormItem>
              <!-- 重复的用户密码 -->
              <FormItem v-if="showRpass" label="New Password" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                    <Input type="text" v-model="this.newRpassword"></Input>
                  </Col>
                  <Col span="10">
                    <Button @click="submitPassChange()">Apply</Button>
                  </Col>
                </Row>
              </FormItem>
            </Form>
            <div class="demo-drawer-footer">
              <Button  @click="handleClose">返回</Button>
              <Button style="margin: 8px" @click="showInfo = false">更改</Button>
              <Button type="primary" @click="logout">注销</Button>
            </div>
          </DropdownMenu>
        </Dropdown>
      </MenuItem>
      <MenuItem v-if="isTeacher()" name="4" style="float:right" @click.native="handleJump('myLivingList')">
        <Icon type="ios-videocam" />
        开播
      </MenuItem>
    </Menu>
    <router-view class="router"/>
  </div>
</template>

<script >
import router from './router'
import axios from 'axios'
export default {
  name: 'App',
  data () {
    return {
      visible: false,
      // boolean to show or not
      showInfo: false,
      showRpass: false,
      showNewMobile: false,
      // mobile and password
      newMobile: '',
      newPassword: '',
      newRpassword: '',
      oldVerification: '',
      newVerification: '',
      // buttons
      mobileButton: 'Edit',
      passButton: 'Edit',
      // hanky's var
      theme1: 'light',
      active: '',
      userInfo: {
        status: 'success',
        username: '',
        password: '',
        mobile: '',
        job: 'teacher'
      },
      // changed this to 已登录 to debug
      LoginOrLogout: '登录',
      // Password Submit
      passSub: {
        status: 'login/logout',
        mobile: '',
        old_password: '',
        new_password: '',
        job: ''
      },
      mobileSub: {
        status: 'login/logout',
        old_mobile: '',
        old_verification: '',
        new_mobile: '',
        new_verification: '',
        job: ''
      },
      verificationSub: {
        mobile: ''
      }
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
    handleClose () {
      this.visible = false
    },
    submitMobileChange () {
      // set input variable
      this.mobileSub.old_mobile = this.userInfo.mobile
      this.mobileSub.old_verification = this.oldVerification
      this.mobileSub.new_mobile = this.newMobile
      this.mobileSub.new_verification = this.newVerification
      this.mobileSub.job = this.userInfo.job
      // post
      axios.post('/api/user/change_mobile', this.mobileSub).then((resp) => {
        // this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 更改userInfo
          this.userInfo.mobile = this.newMobile
          // 需要更改一下Cookie 现在还没好
          // this.$cookies.set('user', resp.data)
          window.location.reload()
        } else { // 如果失败
          this.$Message.error('更改失败')
        }
      })
      // Hide the bars
      this.showNewMobile = false
    },
    submitPassChange () {
      // set input variable
      this.passSub.mobile = this.userInfo.mobile
      this.passSub.old_password = this.userInfo.password
      this.passSub.new_password = this.newPassword
      this.passSub.job = this.userInfo.job
      // post
      axios.post('/api/user/change_password', this.passSub).then((resp) => {
        // this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 更改userInfo
          this.userInfo.password = this.newPassword
          // 需要更改一下Cookie 现在还没好
          // this.$cookies.set('user', resp.data)
          window.location.reload()
        } else { // 如果失败
          this.$Message.error('更改失败')
        }
      })
      // Hide the bars
      this.showRpass = false
    },
    sendVerification () {
      // send verification to both phones
      this.verificationSub.mobile = this.userInfo.mobile

      axios.post('/api/user/request_verification', this.verificationSub).then((resp) => {
        if (resp.data.status === 'success') {
          this.$.message('原手机验证码发送成功')
        }
      })

      // send to new phone
      this.verificationSub.mobile = this.newMobile
      axios.post('/api/user/request_verification', this.verificationSub).then((resp) => {
        if (resp.data.status === 'success') {
          this.$.message('新手机验证码发送成功')
        }
      })
    },
    changeMobile () {
      if (this.showNewMobile === false) {
        this.showNewMobile = true
        this.mobileButton = 'Cancel'
      } else {
        this.showNewMobile = false
        this.mobileButton = 'Edit'
      }
    },
    changePassword () {
      // Edit / Cancel Password Change
      if (this.showRpass === false) {
        this.showRpass = true
        this.newPassword = ''
        this.passButton = 'Cancel'
      } else {
        this.showRpass = false
        this.passButton = 'Edit'
      }
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
  .demo-drawer-footer{
    width: 100%;
    border-top: 1px solid #e8e8e8;
    padding: 10px 16px;
    text-align: right;
    background: #fff;
  }
  .router {
    padding: 0 5%;
  }
</style>
