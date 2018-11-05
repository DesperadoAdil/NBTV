<template>
  <div id="login" class="posi">
    <h1>
      登录
    </h1>
    <Form ref="formInline" :model="formInline" :rules="ruleInline">
      <FormItem prop="username">
        <Input type="text" v-model="formInline.username" name="username" v-bind:placeholder="loginway">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="password">
        <Input type="password" v-model="formInline.password" name="password" placeholder="Password">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="loginWay">
        <RadioGroup v-model="loginway">
          <Radio label="username"></Radio>
          <Radio label="phonenumber"></Radio>
        </RadioGroup>
      </FormItem>
      <FormItem prop="job">
        <RadioGroup v-model="job">
          <Radio label="student"></Radio>
          <Radio label="teacher"></Radio>
        </RadioGroup>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit('formInline')">Signin</Button>
      </FormItem>
    </Form>
    <router-link to="/Register">Register</router-link>
  </div>
</template>

<script type="es6">
import axios from 'axios'
import router from '../router'
export default {
  data () {
    return {
      formInline: {
        username: '',
        password: '',
        rpassword: '',
        mobile: '',
        verification: '',
        job: '',
        loginway: ''
      },
      job: 'student',
      loginway: 'username',
      ruleInline: {
        username: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleSubmit (name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$Message.success('Send to server!')
          this.formInline['job'] = this.job
          this.formInline['loginway'] = this.loginway
          const data = this.formInline
          axios.post('/api/user/login', data).then((resp) => {
            this.$Message.success(resp.data.status)
            if (resp.data.status === 'success') {
              this.$cookies.set('user', resp.data)
              router.push('/list')
              window.location.reload()
            } else {
              this.$Message.error('用户名或密码错误')
            }
          })
        } else {
          this.$Message.error('用户名或密码格式不正确')
        }
      })
    }
  }
}
</script>
<style type="text/css">
#login{
  position: absolute;
  width: 100%;
  top: 60px;
  padding: 15% 40%;
}
</style>
