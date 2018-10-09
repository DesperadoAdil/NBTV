<template>
	<div id="register">
		<Form ref="formInline" :model="formInline" :rules="ruleInline" inline>
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
	            <Input type="text" v-model="formInline.rpassword" placeholder="Password Again">
	                <Icon type="ios-lock-outline" slot="prepend"></Icon>
	            </Input>
	        </FormItem>
	        <FormItem prop="mobile">
	            <Input type="password" v-model="formInline.mobile" placeholder="Phone number">
	            </Input>
	        </FormItem>
	        <FormItem prop="verification">
	            <Input type="password" v-model="formInline.verification" placeholder="verification">
	            </Input>
	        </FormItem>
	        <FormItem>
	            <Button type="primary" @click="handleSubmit('formInline')">Signin</Button>
	            <Button @click="sendMsg('formInline')">发送验证码</Button>
	        </FormItem>
    	</Form>
    	<router-link to="/login">Cancel</router-link>
	</div>
</template>

<script>
	import axios from 'axios';
	import { mapState, mapActions } from 'vuex';

    export default {
        data () {
            return {
                formInline: {
                    username: '',
                    password: '',
                    rpassword: '',
                    mobile: '',
                    verification: '',
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
            }
        },
        computed: {
        	...mapState('account', ['status'])
        },
        methods: {
        	...mapActions('account', ['login', 'logout']),
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        this.$Message.success('Send to server!');
                        const data = this.form;
					    axios.post('/api/user/login', data).then((resp) => {
					        if (resp.data.status === 'success') {
					    	    this.set_login();
					          	this.get_user_info();
					        } else {
					          	this.msg = `Status:${resp.data.status}`;
					        }
					    });
                    } else {
                        this.$Message.error('Fail!');
                    }
                })
            },
            sendMsg(name) {
            	axios.get('/api/user/verification').then((resp) => {

            	})
            }
        }
    };
</script>