<template>
  <div id="userInfo">
		<Form :model="formLeft" label-position="left" :label-width="100">
      <FormItem prop="username" label = "username">
        <Input type="text" v-model="formInline.username" name="username" placeholder="Username" readonly>
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>

      <FormItem prop="repeat password" label = "status">
        <Radio v-model="formInline.job" disabled>{{formInline.job}}</Radio>
      </FormItem>

      <FormItem>
        <Button type="primary" @click="value3 = true">Edit</Button>
         <Drawer
            title="Create"
            v-model="value3"
            width="720"
            :mask-closable="false"
            :styles="styles"
        >
            <Form :model="formData">

              <FormItem label="Name" label-position="top">
                  <Input v-model="formInline.username" placeholder="please enter user name" />
              </FormItem>

              <FormItem label="Password" label-position="top">
                  <Input v-model="formInline.password" placeholder="please enter password" />
              </FormItem>

              <FormItem label="Repeat Password" label-position="top">
                  <Input v-model="formInline.rpassword" placeholder="please re-enter password" />
              </FormItem>

              <FormItem label="Mobile" label-position="top">
                  <Input v-model="formInline.mobile" placeholder="please enter mobile number" />
              </FormItem>

              <FormItem label="Verification" label-position="top">
                  <Input v-model="formInline.Verification" placeholder="please enter verification" />
              </FormItem>

            </Form>
            <div class="demo-drawer-footer">
                <Button style="margin-right: 8px" @click="value3 = false">Cancel</Button>
                <Button type="primary" @click="value3 = false">Submit</Button>
            </div>
        </Drawer>
     </FormItem>
    </Form>
  </div>
</template>

<script type="es6">
import axios from 'axios'
import router from '../router'
export default {
  data () {
    return {
      value3: false,
      styles: {
        height: 'calc(100% - 55px)',
        overflow: 'auto',
        paddingBottom: '53px',
        position: 'static'
      },
      formInline: {
        username: 'Test_name',
        password: 'test-pass',
        rpassword: 'test-pass',
        mobile: '18800990099',
        verification: '909090',
        job: 'student'
      },
      ruleInline: {
        username: [
          { required: true, message: 'Please fill in the user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please fill in the password.', trigger: 'blur' },
          { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
        ]
      },
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: ''
      }
    }
  },
  created () {
    this.showUserInfo()
  },

  methods: {
    showUserInfo () {
      if (this.$cookies.get('user') === null) {
        return
      }
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['job'] = this.$cookies.get('user').job
      if (this.userInfo['status'] === 'success') {
        this.LoginOrLogout = this.userInfo['username']
      }
    },
    handleSubmit (name) {
      this.formInline['job'] = this.job
      const data = this.formInline
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$Message.success('Send to server!')
          console.log(data)
          axios.post('/api/user/register', data).then((resp) => {
            this.$Message.success(resp.data.status)
            if (resp.data.status === 'success') {
              router.push('/userInfo')
            } else {
              this.msg = `Status:${resp.data.status}`
            }
          })
        } else {
          this.$Message.error('Fail!')
        }
      })
    }

  }
}
</script>
<style type="text/css">
#userInfo {
  margin: 0 40%;
}
</style>
