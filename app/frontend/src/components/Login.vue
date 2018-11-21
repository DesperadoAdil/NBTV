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
        <Button type="primary" @click="handleSubmit('formInline')">登录</Button>
      </FormItem>
    </Form>
    <router-link to="/register">注册</router-link>
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
          { validator: validateUsernameCheck, trigger: 'blur' }
        ],
        password: [
          { validator: validatePassCheck, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleSubmit (name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.formInline['job'] = this.job
          this.formInline['loginway'] = this.loginway
          const data = this.formInline
          axios.post('/api/user/login', data).then((resp) => {
            if (resp.data.status === 'success') {
              this.$Message.success('登陆成功!')
              this.$cookies.set('user', resp.data)
              router.push('/list')
              window.location.reload()
            } else {
              this.$Message.error('用户名或密码错误!')
            }
          })
        } else {
          this.$Message.error('请正确填写信息!')
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
