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

      <MenuItem name="1" style="float:right" @click.native="showInfo = true" type="primary">

        <Dropdown trigger="custom" :visible="visible" placement="bottom-end" style="">
          <a href="javascript:void(0)" trigger="click" @click="handleOpen">
            <Icon v-if="LoginOrLogout === '登录'" type="ios-contact-outline" />{{ LoginOrLogout }}
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
            <div v-if="showNewMobile">
              <FormItem label="New Mobile" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                      <Input type="text" v-model="this.newMobile" placeholder="New Phone Number Here"></Input>
                  </Col>
                  <Col span="10">
                      <Button @click="sendVerification()">Send</Button>
                  </Col>
                </Row>
              </FormItem>
            </div>

            <!-- 设置旧手机的验证码 -->
            <div v-if="showNewMobile">
              <FormItem label="Verification" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                     <Input v-model="oldVerification" placeholder="Old Verification Code Here"></Input>
                  </Col>
                </Row>
              </FormItem>
            </div>

            <!-- 设置新手机的验证码 -->
            <div v-if="showNewMobile">
              <FormItem label="Verification" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                     <Input v-model="newVerification" placeholder="New Verification Code Here"></Input>
                  </Col>
                  <Col span="10">
                    <Button @click="submitMobileChange()">Verify</Button>
                  </Col>
                </Row>
              </FormItem>
            </div>

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
              <div v-if="showRpass">
              <FormItem label="New Password" label-position="left" label-width="80">
                <Row>
                  <Col span="14">
                  <Input type="text" v-model="this.newRpassword"></Input>
                  </Col>
                  <Col span="10">
                  <Button @click="submitPassChange()">Apply</Button>
                  </Col>
                </Row>
              </FormItem>
              </div>
            </Form>

            <div class="demo-drawer-footer">
            <Button type="primary" @click="handleClose">exit</Button>
            <Button style="margin: 8px" @click="showInfo = false">Apply</Button>
            <Button type="primary" @click.native="logout">Log out</Button>
            </div>


          </DropdownMenu>
        </Dropdown>
        <!--<Drawer title="User Information" v-model="showInfo" width="480">-->
          <!--<Form>-->
            <!--<br>-->
            <!--<br>-->
            <!--&lt;!&ndash; 用户名称 &ndash;&gt;-->
            <!--<Row :gutter="32">-->
              <!--<Col span="18">-->
                <!--<FormItem label="Name" label-position="left" label-width="80">-->
                  <!--{{userInfo.username}}-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
              <!--</Col>-->
            <!--</Row>-->
            <!--<br>-->
            <!--<br>-->
            <!--&lt;!&ndash; 用户身份 &ndash;&gt;-->
            <!--<Row :gutter="32">-->
              <!--<Col span="18">-->
                <!--<FormItem label="Job" label-position="left" label-width="80">-->
                  <!--{{userInfo.job}}-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
              <!--</Col>-->
            <!--</Row>-->
            <!--<br>-->
            <!--<br>-->
            <!--&lt;!&ndash; 用户手机号 &ndash;&gt;-->
            <!--<Row :gutter="32">-->
              <!--<Col span="18">-->
                <!--<FormItem label="Current Mobile" label-position="left" label-width="80">-->
                  <!--<Input type="text" v-model="userInfo.mobile" readonly></Input>-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
                <!--<FormItem>-->
                  <!--<Button @click="changeMobile()">{{mobileButton}}</Button>-->
                <!--</FormItem>-->
              <!--</Col>-->
            <!--</Row>-->

            <!--&lt;!&ndash; 用户的新手机号 &ndash;&gt;-->
            <!--<Row :gutter="32" v-if="showNewMobile">-->
              <!--<Col span="18">-->
                <!--<FormItem label="New Mobile" label-position="left" label-width="80">-->
                  <!--<Input type="text" v-model="this.newMobile" placeholder="New Phone Number Here"></Input>-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
                <!--<FormItem>-->
                  <!--<Button @click="sendVerification()">Send</Button>-->
                <!--</FormItem>-->
              <!--</Col>-->
            <!--</Row>-->

            <!--&lt;!&ndash; 设置旧手机的验证码 &ndash;&gt;-->
            <!--<Row :gutter="32" v-if="showNewMobile">-->
              <!--<Col span="18">-->
                <!--<FormItem label="Verification" label-position="left" label-width="80">-->
                  <!--<Input v-model="oldVerification" placeholder="Old Verification Code Here"></Input>-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
              <!--</Col>-->
            <!--</Row>-->

            <!--&lt;!&ndash; 设置新手机的验证码 &ndash;&gt;-->
            <!--<Row :gutter="32" v-if="showNewMobile">-->
              <!--<Col span="18">-->
                <!--<FormItem label="Verification" label-position="left" label-width="80">-->
                  <!--<Input v-model="newVerification" placeholder="New Verification Code Here"></Input>-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
                <!--<FormItem>-->
                  <!--<Button @click="submitMobileChange()">Verify</Button>-->
                <!--</FormItem>-->
              <!--</Col>-->
            <!--</Row>-->

            <!--<br>-->
            <!--<br>-->

            <!--&lt;!&ndash; 用户密码 &ndash;&gt;-->
            <!--<Row :gutter="32" >-->
              <!--<Col span="18">-->
                <!--<FormItem label="Current Password" label-position="left" label-width="80">-->
                  <!--<Input type="text" v-model="newPassword"></Input>-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
                <!--<FormItem>-->
                  <!--<Button @click="changePassword()">{{passButton}}</Button>-->
                <!--</FormItem>-->
              <!--</Col>-->
            <!--</Row>-->

            <!--&lt;!&ndash; 重复的用户密码 &ndash;&gt;-->
            <!--<Row :gutter="32" v-if="showRpass">-->
              <!--<Col span="18">-->
                <!--<FormItem label="New Password" label-position="left" label-width="80">-->
                  <!--<Input type="text" v-model="this.newRpassword"></Input>-->
                <!--</FormItem>-->
              <!--</Col>-->
              <!--<Col span="6">-->
                <!--<FormItem>-->
                  <!--<Button @click="submitPassChange()">Apply</Button>-->
                <!--</FormItem>-->
              <!--</Col>-->
            <!--</Row>-->

          <!--</Form>-->

          <!--<div class="demo-drawer-footer">-->
            <!--<Button style="margin-right: 8px" @click="showInfo = false">Apply</Button>-->
            <!--<Button type="primary" @click.native="logout">Log out</Button>-->
          <!--</div>-->
        <!--</Drawer>-->
      </MenuItem>
    </Menu>
    <router-view/>
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
      newPassword: '******',
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
        username: 'adil',
        password: '123456',
        mobile: '18810081008',
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
      if(this.visible == true)
      this.visible = false;
      else
        this.visible = true;
    },
    handleClose () {
      this.visible = false;
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
      this.visible = false;
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
    border-top: 1px solid #e8e8e8;
    padding: 10px 16px;
    text-align: right;
    background: #fff;
  }
</style>
