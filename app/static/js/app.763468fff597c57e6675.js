webpackJsonp([1],{"+skl":function(e,t){},"4SYA":function(e,t){},NHnr:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n("7+uW"),s={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("Menu",{attrs:{mode:"horizontal","active-name":"1"}},[t("MenuItem",{attrs:{name:"1"}},[t("Icon",{attrs:{type:"ios-paper"}}),this._v("\n      登录\n    ")],1),this._v(" "),t("MenuItem",{attrs:{name:"2"}},[t("Icon",{attrs:{type:"ios-people"}}),this._v("\n      教室列表\n    ")],1),this._v(" "),t("MenuItem",{attrs:{name:"3"}},[t("Icon",{attrs:{type:"ios-construct"}}),this._v("\n      我的信息\n    ")],1)],1),this._v(" "),t("router-view")],1)},staticRenderFns:[]};var o=n("VU/8")({name:"App",data:function(){return{theme1:"light"}}},s,!1,function(e){n("4SYA")},null,null).exports,a=n("/ocq"),i=n("Dd8w"),l=n.n(i),u=n("mtWM"),p=n.n(u),m=n("NYxO"),c={data:function(){return{formInline:{username:"",password:"",rpassword:"",mobile:"",verification:"",job:""},job:"student",ruleInline:{username:[{required:!0,message:"Please fill in the user name",trigger:"blur"}],password:[{required:!0,message:"Please fill in the password.",trigger:"blur"},{type:"string",min:6,message:"The password length cannot be less than 6 bits",trigger:"blur"}]}}},computed:l()({},Object(m.b)("account",["status"])),methods:l()({},Object(m.a)("account",["login","logout"]),{handleSubmit:function(e){var t=this;this.$refs[e].validate(function(e){if(e){t.$Message.success("Send to server!"),t.formInline.job=t.job;var n=t.formInline;p.a.post("/api/user/login",n).then(function(e){"success"===e.data.status?(t.set_login(),t.get_user_info()):t.$Message.error("用户名或密码错误")})}else t.$Message.error("用户名或密码格式不正确")})}})},d={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"login"}},[n("Form",{ref:"formInline",attrs:{model:e.formInline,rules:e.ruleInline,inline:""}},[n("FormItem",{attrs:{prop:"username"}},[n("Input",{attrs:{type:"text",name:"username",placeholder:"Username"},model:{value:e.formInline.username,callback:function(t){e.$set(e.formInline,"username",t)},expression:"formInline.username"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-person-outline"},slot:"prepend"})],1)],1),e._v(" "),n("FormItem",{attrs:{prop:"password"}},[n("Input",{attrs:{type:"password",name:"password",placeholder:"Password"},model:{value:e.formInline.password,callback:function(t){e.$set(e.formInline,"password",t)},expression:"formInline.password"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-lock-outline"},slot:"prepend"})],1)],1),e._v(" "),n("FormItem",{attrs:{prop:"job"}},[n("RadioGroup",{model:{value:e.job,callback:function(t){e.job=t},expression:"job"}},[n("Radio",{attrs:{label:"student"}}),e._v(" "),n("Radio",{attrs:{label:"teacher"}})],1)],1),e._v(" "),n("FormItem",[n("Button",{attrs:{type:"primary"},on:{click:function(t){e.handleSubmit("formInline")}}},[e._v("Signin")])],1)],1),e._v(" "),n("router-link",{attrs:{to:"/Register"}},[e._v("Register")])],1)},staticRenderFns:[]};var f=n("VU/8")(c,d,!1,function(e){n("exD0")},null,null).exports,I={data:function(){return{formInline:{username:"",password:"",rpassword:"",mobile:"",verification:"",job:""},msgBox:"发送验证码",job:"student",ruleInline:{username:[{required:!0,message:"Please fill in the user name",trigger:"blur"}],password:[{required:!0,message:"Please fill in the password.",trigger:"blur"},{type:"string",min:6,message:"The password length cannot be less than 6 bits",trigger:"blur"}]}}},computed:l()({},Object(m.b)("account",["status"])),methods:l()({},Object(m.a)("account",["login","logout"]),{handleSubmit:function(e){var t=this;this.$refs[e].validate(function(e){if(e){t.$Message.success("Send to server!");var n=t.form;p.a.post("/api/user/login",n).then(function(e){"success"===e.data.status?(t.set_login(),t.get_user_info()):t.msg="Status:"+e.data.status})}else t.$Message.error("Fail!")})},sendMsg:function(e){var t=this;p.a.get("/api/user/verification").then(function(e){"success"===e.data.status&&(t.msgBox="验证码发送成功")})}})},v={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"register"}},[n("Form",{ref:"formInline",attrs:{model:e.formInline,rules:e.ruleInline,inline:""}},[n("FormItem",{attrs:{prop:"username"}},[n("Input",{attrs:{type:"text",placeholder:"Username"},model:{value:e.formInline.username,callback:function(t){e.$set(e.formInline,"username",t)},expression:"formInline.username"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-person-outline"},slot:"prepend"})],1)],1),e._v(" "),n("FormItem",{attrs:{prop:"password"}},[n("Input",{attrs:{type:"password",placeholder:"Password"},model:{value:e.formInline.password,callback:function(t){e.$set(e.formInline,"password",t)},expression:"formInline.password"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-lock-outline"},slot:"prepend"})],1)],1),e._v(" "),n("FormItem",{attrs:{prop:"rpassword"}},[n("Input",{attrs:{type:"text",placeholder:"Password Again"},model:{value:e.formInline.rpassword,callback:function(t){e.$set(e.formInline,"rpassword",t)},expression:"formInline.rpassword"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-lock-outline"},slot:"prepend"})],1)],1),e._v(" "),n("FormItem",{attrs:{prop:"mobile"}},[n("Input",{attrs:{type:"password",placeholder:"Phone number"},model:{value:e.formInline.mobile,callback:function(t){e.$set(e.formInline,"mobile",t)},expression:"formInline.mobile"}})],1),e._v(" "),n("FormItem",{attrs:{prop:"verification"}},[n("Input",{attrs:{type:"password",placeholder:"verification"},model:{value:e.formInline.verification,callback:function(t){e.$set(e.formInline,"verification",t)},expression:"formInline.verification"}})],1),e._v(" "),n("FormItem",{attrs:{prop:"job"}},[n("RadioGroup",{model:{value:e.job,callback:function(t){e.job=t},expression:"job"}},[n("Radio",{attrs:{label:"student"}}),e._v(" "),n("Radio",{attrs:{label:"teacher"}})],1)],1),e._v(" "),n("FormItem",[n("Button",{attrs:{type:"primary"},on:{click:function(t){e.handleSubmit("formInline")}}},[e._v("Signin")]),e._v(" "),n("Button",{on:{click:function(t){e.sendMsg("formInline")}}},[e._v(e._s(e.msgBox))])],1)],1),e._v(" "),n("router-link",{attrs:{to:"/login"}},[e._v("Cancel")])],1)},staticRenderFns:[]},g=n("VU/8")(I,v,!1,null,null,null).exports;r.default.use(a.a);var b=new a.a({mode:"history",routes:[{path:"/Login",name:"Login",component:f},{path:"/Register",name:"Register",component:g},{path:"*",redirect:"/Login"}]}),h=n("BTaQ"),_=n.n(h);n("+skl");r.default.use(_.a),r.default.config.productionTip=!1,new r.default({el:"#app",router:b,components:{App:o},template:"<App/>"})},exD0:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.763468fff597c57e6675.js.map