

<script >
import router from '../router'
import axios from 'axios'
export default {
  name: 'User',
  data () {
    return {
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
      newmobile: '',
      oldverification: '',
      newverification: '',
      oldpassword: '',
      newpassword: '',
      rnewpassword: '',
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
    SubmitPassword () {
      this.password.status = this.userInfo.status
      this.password.mobile = this.userInfo.mobile
      this.password.old_password = this.userInfo.password
      this.password.new_password = this.newpassword
      this.password.job = this.userInfo.job

      axios.post('/api/user/change_password', this.passSub).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('成功修改密码!')
          this.userInfo.password = this.newpassword
          this.$cookies.set('user', resp.data)
          window.location.reload()
          this.changepassword = false
          this.newpassword = ''
        } else {
          this.$Message.error('修改密码失败!')
        }
      })
    },
    SubmitMobile () {
      this.mobile.status = this.userInfo.status
      this.mobile.old_mobile = this.userInfo.mobile
      this.mobile.old_verification = this.oldverification
      this.mobile.new_mobile = this.newmobile
      this.mobile.new_verification = this.newverification
      this.mobile.job = this.userInfo.job

      axios.post('/api/user/change_mobile', this.mobileSub).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('成功修改手机号!')
          this.userInfo.mobile = this.newmobile
          this.$cookies.set('user', resp.data)
          window.location.reload()
          this.changemobile = false
          this.newmobile = ''
          this.oldverification = ''
          this.newverification = ''
        } else {
          this.$Message.error('修改手机号失败！')
        }
      })
    },
    Close () {
      this.changemobile = false
      this.changepassword = false
    },
    SendOldVerification () {
      this.verification.mobile = this.userInfo.mobile
      axios.post('/api/user/request_verification', this.verificationSub).then((resp) => {
        if (resp.data.status === 'success') {
          this.$.message('原手机验证码发送成功')
        }
      })
    },
    SendNewVerification () {
      this.verification.mobile = this.newmobile
      axios.post('/api/user/request_verification', this.verificationSub).then((resp) => {
        if (resp.data.status === 'success') {
          this.$.message('新手机验证码发送成功')
        }
      })
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
</style>
