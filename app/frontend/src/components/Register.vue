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
        <Input type="text" v-model="formInline.mobile" placeholder="Phone number">
          <Icon type="ios-call" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="verification">
        <Input type="text" v-model="formInline.verification" placeholder="verification">
        </Input>
      </FormItem>
      <FormItem prop="job">
        <RadioGroup v-model="job">
          <Radio label="student"></Radio>
          <Radio label="teacher"></Radio>
        </RadioGroup>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit('formInline')">Signin</Button>
        <Button @click="sendMsg('formInline')">{{ msgBox }}</Button>
      </FormItem>
    </Form>
    <router-link to="/login">Cancel</router-link>
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
    };
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter the password!'))
      } else if (!/^[a-zA-Z\d]{6,16}$/.test(value)) {
        callback(new Error('Password unmatch or too long!'))
      } else {
        callback()
      }
    };
    const validateRpassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter the password again!'))
      } else if (value !== this.formInline.password) {
        callback(new Error('The two input passwords do not match!'))
      } else {
        callback()
      }
    };
    const validateMobileCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your phonenumber!'))
      } else if (!/^\d{11}$/.test(value)) {
        callback(new Error('Please enter the right phonenumber!'))
      } else {
        callback()
      }
    };
    const validateVerificationCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your verification!'))
      } else if (!/^\d{6}$/.test(value)) {
        callback(new Error('Please enter the right verification!'))
      } else {
        callback()
      }
    };
    return {
      formInline: {
        username: '',
        password: '',
        rpassword: '',
        mobile: '',
        verification: '',
        job: ''
      },
      msgBox: '发送验证码',
      job: 'student',
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
          this.$Message.success('Send to server!')
          axios.post('/api/user/register', data).then((resp) => {
            this.$Message.success(resp.data.status)
            if (resp.data.status === 'success') {
              router.push('/login')
            } else {
              this.msg = `Status:${resp.data.status}`
            }
          })
        } else {
          this.$Message.error('Fail!')
        }
      })
    },
    sendMsg (name) {
      const data = this.formInline
      axios.post('/api/user/request_verification', data).then((resp) => {
        if (resp.data.status === 'success') {
          this.msgBox = '验证码发送成功'
        }
      })
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
