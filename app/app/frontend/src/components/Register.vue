<template>
  <div id="register" class="posi">
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
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        this.$Message.error('Please enter your password again')
        callback()
      } else if (value !== this.formInline.password) {
        this.$Message.error('The two input passwords do not match!')
        callback()
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
      msgBox: '发送验证码',
      job: 'student',
      ruleInline: {
        username: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ],
        verification: [
          { validater: validatePassCheck, trigger: 'blur' }
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
  padding: 0 40%;
}
</style>
