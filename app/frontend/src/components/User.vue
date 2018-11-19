<template>
  <div id="user" class="posi">
    <h1>
      用户信息
    </h1><br>
    <Form ref="formInline" :model="formInline" :rules="ruleInline">
      <FormItem label="用户名" label-position="left" label-width="150" prop="username">
        <p>
          {{userInfo.username}}
        </p>
      </FormItem>
      <FormItem label="用户类型" label-position="left" label-width="150" prop="job">
        <p>
          {{userInfo.job}}
        </p>
      </FormItem>
      <FormItem label="手机号" label-position="left" label-width="150" prop="mobile">
        <p>
          {{userInfo.mobile}}
        </p>
      </FormItem>
      <FormItem v-if="!changepassword && !changemobile">
        <Button type="primary" @click="ChangePassword()">修改密码</Button>
        <Button type="primary" @click="ChangeMobile()">修改手机号</Button>
      </FormItem>
      <FormItem v-if="changemobile" label="原手机验证码" label-position="left" label-width="150" prop="oldverification">
        <Row>
          <Col span="16">
            <Input type="text" v-model="formInline.oldverification"/>
          </Col>
          <Col span="8">
            <Button id="sv1" @click="SendVerification(userInfo.mobile, 'sv1')" :disabled="oldverificationsend">发送验证码</Button>
          </Col>
        </Row>
      </FormItem>
      <FormItem v-if="changemobile" label="新手机号" label-position="left" label-width="150" prop="newmobile">
        <Row>
          <Col span="16">
              <Input type="text" v-model="formInline.newmobile" :disabled="send"/>
          </Col>
          <Col span="8">
            <Button id="sv" @click="send=false,newverificationsend=true,formInline.newmobile=''" :disabled="newverificationsend">重新填写</Button>
          </Col>
      </FormItem>
      <FormItem v-if="changemobile" label="新手机验证码" label-position="left" label-width="150" prop="newverification">
        <Row>
          <Col span="16">
            <Input type="text" v-model="formInline.newverification"/>
          </Col>
          <Col span="8">
            <Button id="sv2" @click="SendVerification(formInline.newmobile, 'sv2')" :disabled="newverificationsend">发送验证码</Button>
          </Col>
        </Row>
      </FormItem>
      <FormItem v-if="changepassword" label="原密码" label-position="left" label-width="150" prop="oldpassword">
        <Input type="text" v-model="formInline.oldpassword" type="password"/>
      </FormItem>
      <FormItem v-if="changepassword" label="新密码" label-position="left" label-width="150" prop="newpassword">
        <Input type="text" v-model="formInline.newpassword" type="password"/>
      </FormItem>
      <FormItem v-if="changepassword" label="确认密码" label-position="left" label-width="150" prop="rnewpassword">
        <Input type="text" v-model="formInline.rnewpassword" type="password"/>
      </FormItem>
      <FormItem v-if="changepassword || changemobile">
        <Button  v-if="changepassword" @click="SubmitPassword('formInline')">提交</Button>
        <Button  v-else @click="SubmitMobile('formInline')">提交</Button>
        <Button  @click="Reload()">返回</Button>
      </FormItem>
    </Form>
  </div>
</template>

<script >
import router from '../router'
import axios from 'axios'
export default {
  name: 'User',
  data () {
    const validatePassCheck = (rule, value, callback) => {
      if (this.changepassword) {
        if (value === '') {
          callback(new Error('Please enter the password!'))
        } else if (!/^[a-zA-Z\d]{6,16}$/.test(value)) {
          callback(new Error('Password unmatch or too long!'))
        } else if (value !== this.userInfo.password) {
          callback(new Error('Please enter the right password!'))
        } else {
          callback()
        }
      }
    };
    const validateNewPassCheck = (rule, value, callback) => {
      if (this.changepassword) {
        if (value === this.userInfo.password) {
          callback(new Error('Same password!'))
        } else if (value === '') {
          callback(new Error('Please enter the password!'))
        } else if (!/^[a-zA-Z\d]{6,16}$/.test(value)) {
          callback(new Error('Password unmatch or too long!'))
        } else {
          callback()
        }
      }
    };
    const validateRpassCheck = (rule, value, callback) => {
      if (this.changepassword) {
        if (value === '') {
          callback(new Error('Please enter the password again!'))
        } else if (value !== this.formInline.newpassword) {
          callback(new Error('The two input passwords do not match!'))
        } else {
          callback()
        }
      }
    };
    const validateVerificationCheck = (rule, value, callback) => {
      if (this.changemobile) {
        if (value === '') {
          callback(new Error('Please enter your verification!'))
        } else if (!/^\d{6}$/.test(value)) {
          callback(new Error('Please enter the right verification!'))
        } else {
          callback()
        }
      }
    };
    const validateMobileCheck = (rule, value, callback) => {
      if (this.changemobile) {
        if (value === this.userInfo.mobile) {
          this.newverificationsend = true
          callback(new Error('Same phonenumber!'))
        } else if (value === '') {
          this.newverificationsend = true
          callback(new Error('Please enter your phonenumber!'))
        } else if (!/^\d{11}$/.test(value)) {
          this.newverificationsend = true
          callback(new Error('Please enter the right phonenumber!'))
        } else {
          this.newverificationsend = false
          callback()
        }
      }
    };
    return {
      formInline: {
        username: '',
        oldpassword: '',
        newpassword: '',
        rnewpassword: '',
        mobile: '',
        newmobile: '',
        oldverification: '',
        newverification: '',
        job: ''
      },
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: ''
      },
      LoginOrLogout: '登录',
      changepassword: false,
      changemobile: false,
      oldverificationsend: false,
      newverificationsend: true,
      send: false,
      verification: {
        mobile: ''
      },
      password: {
        status: '',
        mobile: '',
        old_password: '',
        new_password: '',
        job: ''
      },
      mobile: {
        status: '',
        old_mobile: '',
        old_verification: '',
        new_mobile: '',
        new_verification: '',
        job: ''
      },
      ruleInline: {
        oldpassword: [
          { validator: validatePassCheck, trigger: 'blur' }
        ],
        newpassword: [
          { validator: validateNewPassCheck, trigger: 'blur' }
        ],
        rnewpassword: [
          { validator: validateRpassCheck, trigger: 'blur' }
        ],
        newmobile: [
          { validator: validateMobileCheck, trigger: 'blur' }
        ],
        oldverification: [
          { validator: validateVerificationCheck, trigger: 'blur' }
        ],
        newverification: [
          { validator: validateVerificationCheck, trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.showUserInfo()
  },
  methods: {
    showUserInfo () {
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      this.userInfo['job'] = this.$cookies.get('user').job
      if (this.userInfo['status'] === 'success') {
        this.LoginOrLogout = this.userInfo['username']
      }
    },
    ChangePassword () {
      this.changepassword = true
      this.changemobile = false
    },
    ChangeMobile () {
      this.changemobile = true
      this.changepassword = false
    },
    SubmitPassword (form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          if (this.userInfo.status === 'success') this.password.status = 'login'
          else this.password.status = 'logout'
          this.password.mobile = this.userInfo.mobile
          this.password.old_password = this.userInfo.password
          this.password.new_password = this.formInline.newpassword
          this.password.job = this.userInfo.job

          axios.post('/api/user/change_password', this.password).then((resp) => {
            if (resp.data.status === 'success') {
              this.$Message.success('成功修改密码!')
              this.userInfo.password = this.formInline.newpassword
              this.$cookies.set('user', this.userInfo)
              this.Reload()
              this.showUserInfo()
              this.changepassword = false
              this.formInline.newpassword = ''
            } else {
              this.$Message.error('修改密码失败!')
            }
          })
        } else {
          this.$Message.error('请填写完整信息!')
        }
      })
    },
    SubmitMobile (form) {
      this.$refs[form].validate((valid) => {
        if (valid) {
          if (this.userInfo.status === 'success') this.mobile.status = 'login'
          else this.mobile.status = 'logout'
          this.mobile.old_mobile = this.userInfo.mobile
          this.mobile.old_verification = this.formInline.oldverification
          this.mobile.new_mobile = this.formInline.newmobile
          this.mobile.new_verification = this.formInline.newverification
          this.mobile.job = this.userInfo.job

          axios.post('/api/user/change_mobile', this.mobile).then((resp) => {
            if (resp.data.status === 'success') {
              this.$Message.success('成功修改手机号!')
              this.userInfo.mobile = this.formInline.newmobile
              this.$cookies.set('user', this.userInfo)
              this.Reload()
              this.showUserInfo()
              this.changemobile = false
              this.formInline.newmobile = ''
              this.formInline.oldverification = ''
              this.formInline.newverification = ''
            } else {
              this.$Message.error('修改手机号失败！')
            }
          })
        } else {
          this.$Message.error('请填写完整信息!')
        }
      })
    },
    SendVerification (mobile, id) {
      this.verification.mobile = mobile
      axios.post('/api/user/request_verification', this.verification).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('验证码发送成功!')
          this.CountTime(id, 60)
        } else {
          this.$Message.error('验证码发送失败!')
        }
      })
    },
    Reload () {
      window.location.reload()
    },
    CountTime (id, time) {
      if (time <= 0) {
        document.getElementById(id).innerHTML = "发送验证码"
        if (id === "sv1") this.oldverificationsend = false
        else this.newverificationsend = false
      } else {
        if (id === "sv1") {
          this.oldverificationsend = true
          document.getElementById(id).innerHTML = time.toString()+"秒"
          setTimeout(this.CountTime, 1000, 'sv1', time-1)
        } else {
          this.newverificationsend = true
          this.send = true
          document.getElementById(id).innerHTML = time.toString()+"秒"
          setTimeout(this.CountTime, 1000, 'sv2', time-1)
        }
      }
    }
  }
}
</script>
<style>
#user {
  position: absolute;
  width: 100%;
  top: 60px;
  padding: 15% 40%;
}
#sv, #sv1, #sv2 {
  width: 95px;
}
</style>
