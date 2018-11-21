<template>
  <div id="register" class="posi">
    <h1>
      注册
    </h1>
    <Form ref="formInline" :model="formInline" :rules="ruleInline">
      <FormItem prop="username">
        <Input type="text" v-model="formInline.username" placeholder="Username">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="password">
        <Input type="password" v-model="formInline.password" placeholder="Password">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="rpassword">
        <Input type="password" v-model="formInline.rpassword" placeholder="Password Again">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="mobile">
        <Row>
          <Col span="16">
            <Input type="text" v-model="formInline.mobile" placeholder="Phone number" :disabled="send">
              <Icon type="ios-call" slot="prepend"></Icon>
            </Input>
          </Col>
          <Col span="8">
            <Button @click="send=false,verificationsend=true,formInline.mobile=''" :disabled="verificationsend">重新填写</Button>
          </Col>
        </Row>
      </FormItem>
      <FormItem prop="verification">
        <Row>
          <Col span="16">
            <Input type="text" v-model="formInline.verification" placeholder="verification">
              <Icon type="md-checkmark" slot="prepend"/>
            </Input>
          </Col>
          <Col span="8">
            <Button id="sv" @click="sendMsg('formInline')" :disabled="verificationsend">发送验证码</Button>
          </Col>
        </Row>
      </FormItem>
      <FormItem prop="job">
        <RadioGroup v-model="job">
          <Radio label="student"></Radio>
          <Radio label="teacher"></Radio>
        </RadioGroup>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit('formInline')">注册</Button>
      </FormItem>
    </Form>
    <router-link to="/login">返回</router-link>
  </div>
</template>

<script type="es6">
import axios from 'axios'
import router from '../router'
export default {
  data () {
    const validateUsernameCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your username!'))
      } else if (!/^[a-zA-Z\d\u4e00-\u9fa5]{1,20}$/.test(value)) {
        callback(new Error('Username unmatch or too long!'))
      } else {
        callback()
      }
    }
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter the password!'))
      } else if (!/^[a-zA-Z\d]{6,16}$/.test(value)) {
        callback(new Error('Password unmatch or too long!'))
      } else {
        callback()
      }
    }
    const validateRpassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter the password again!'))
      } else if (value !== this.formInline.password) {
        callback(new Error('The two input passwords do not match!'))
      } else {
        callback()
      }
    }
    const validateMobileCheck = (rule, value, callback) => {
      if (value === '') {
        this.verificationsend = true
        callback(new Error('Please enter your phonenumber!'))
      } else if (!/^\d{11}$/.test(value)) {
        this.verificationsend = true
        callback(new Error('Please enter the right phonenumber!'))
      } else {
        this.verificationsend = false
        callback()
      }
    }
    const validateVerificationCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your verification!'))
      } else if (!/^\d{6}$/.test(value)) {
        callback(new Error('Please enter the right verification!'))
      } else {
        callback()
      }
    }
    return {
      formInline: {
        username: '',
        password: '',
        rpassword: '',
        mobile: '',
        verification: '',
        job: ''
      },
      job: 'student',
      verificationsend: true,
      send: false,
      ruleInline: {
        username: [
          { validator: validateUsernameCheck, trigger: 'blur' }
        ],
        password: [
          { validator: validatePassCheck, trigger: 'blur' }
        ],
        rpassword: [
          { validator: validateRpassCheck, trigger: 'blur' }
        ],
        mobile: [
          { validator: validateMobileCheck, trigger: 'blur' }
        ],
        verification: [
          { validator: validateVerificationCheck, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleSubmit (name) {
      this.formInline['job'] = this.job
      const data = this.formInline
      this.$refs[name].validate((valid) => {
        if (valid) {
          axios.post('/api/user/register', data).then((resp) => {
            if (resp.data.status === 'success') {
              this.$Message.success('注册成功!')
              router.push('/login')
            } else {
              this.$Message.error('注册失败,验证码错误或用户已存在!')
              this.msg = `Status:${resp.data.status}`
            }
          })
        } else {
          this.$Message.error('请正确填写信息!')
        }
      })
    },
    sendMsg (name) {
      const data = this.formInline
      axios.post('/api/user/request_verification', data).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('验证码发送成功!')
          this.CountTime(60)
        } else {
          this.$Message.error('验证码发送失败!')
        }
      })
    },
    CountTime (time) {
      if (time <= 0) {
        document.getElementById('sv').innerHTML = '发送验证码'
        this.verificationsend = false
      } else {
        this.verificationsend = true
        this.send = true
        document.getElementById('sv').innerHTML = time.toString() + '秒'
        setTimeout(this.CountTime, 1000, time - 1)
      }
    }
  }
}
</script>
<style>
#register{
  position: absolute;
  width: 100%;
  top: 60px;
  padding: 15% 40%;
}
</style>
