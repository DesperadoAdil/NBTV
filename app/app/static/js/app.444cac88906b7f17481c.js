webpackJsonp([1],{"+skl":function(t,e){},Eq5K:function(t,e){},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=n("7+uW"),r={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[n("Menu",{attrs:{mode:"horizontal","active-name":"1"}},[n("router-link",{attrs:{to:"/login"}},[n("MenuItem",{attrs:{name:"1"}},[n("Icon",{attrs:{type:"ios-paper"}}),t._v("\n        登录\n\n    ")],1)],1),t._v(" "),n("router-link",{attrs:{to:"/list"}},[n("MenuItem",{attrs:{name:"2"}},[n("Icon",{attrs:{type:"ios-people"}}),t._v("\n        教室列表\n\n    ")],1)],1),t._v(" "),n("MenuItem",{attrs:{name:"3"}},[n("Icon",{attrs:{type:"ios-construct"}}),t._v("\n      我的信息\n    ")],1)],1),t._v(" "),n("br"),t._v(" "),n("br"),t._v(" "),n("router-view")],1)},staticRenderFns:[]};var o=n("VU/8")({name:"App",data:function(){return{theme1:"light"}}},r,!1,function(t){n("Eq5K")},null,null).exports,a=n("/ocq"),i=n("Dd8w"),l=n.n(i),u=n("mtWM"),c=n.n(u),d=n("NYxO"),p={data:function(){return{formInline:{username:"",password:"",rpassword:"",mobile:"",verification:"",job:""},job:"student",ruleInline:{username:[{required:!0,message:"Please fill in the user name",trigger:"blur"}],password:[{required:!0,message:"Please fill in the password.",trigger:"blur"},{type:"string",min:6,message:"The password length cannot be less than 6 bits",trigger:"blur"}]}}},computed:l()({},Object(d.c)("account",["status"])),methods:l()({},Object(d.b)("account",["login","logout"]),{handleSubmit:function(t){var e=this;this.$refs[t].validate(function(t){if(t){e.$Message.success("Send to server!"),e.formInline.job=e.job;var n=e.formInline;c.a.post("/api/user/login",n).then(function(t){console.log(t),console.log(t.data),e.$Message.success(t.data.status),"success"===t.data.status?S.push("/list"):e.$Message.error("用户名或密码错误")})}else e.$Message.error("用户名或密码格式不正确")})}})},m={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"login"}},[n("Form",{ref:"formInline",attrs:{model:t.formInline,rules:t.ruleInline,inline:""}},[n("FormItem",{attrs:{prop:"username"}},[n("Input",{attrs:{type:"text",name:"username",placeholder:"Username"},model:{value:t.formInline.username,callback:function(e){t.$set(t.formInline,"username",e)},expression:"formInline.username"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-person-outline"},slot:"prepend"})],1)],1),t._v(" "),n("FormItem",{attrs:{prop:"password"}},[n("Input",{attrs:{type:"password",name:"password",placeholder:"Password"},model:{value:t.formInline.password,callback:function(e){t.$set(t.formInline,"password",e)},expression:"formInline.password"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-lock-outline"},slot:"prepend"})],1)],1),t._v(" "),n("FormItem",{attrs:{prop:"job"}},[n("RadioGroup",{model:{value:t.job,callback:function(e){t.job=e},expression:"job"}},[n("Radio",{attrs:{label:"student"}}),t._v(" "),n("Radio",{attrs:{label:"teacher"}})],1)],1),t._v(" "),n("FormItem",[n("Button",{attrs:{type:"primary"},on:{click:function(e){t.handleSubmit("formInline")}}},[t._v("Signin")])],1)],1),t._v(" "),n("router-link",{attrs:{to:"/Register"}},[t._v("Register")])],1)},staticRenderFns:[]};var f=n("VU/8")(p,m,!1,function(t){n("e/Aw")},null,null).exports,v={data:function(){var t=this;return{formInline:{username:"",password:"",rpassword:"",mobile:"",verification:"",job:""},msgBox:"发送验证码",job:"student",ruleInline:{username:[{required:!0,message:"Please fill in the user name",trigger:"blur"}],password:[{required:!0,message:"Please fill in the password.",trigger:"blur"},{type:"string",min:6,message:"The password length cannot be less than 6 bits",trigger:"blur"}],verification:[{validater:function(e,n,s){""===n?(t.$Message.error("Please enter your password again"),s()):n!==t.formInline.password?(t.$Message.error("The two input passwords do not match!"),s()):s()},trigger:"blur"}]}}},computed:l()({},Object(d.c)("account",["status"])),methods:l()({},Object(d.b)("account",["login","logout"]),{handleSubmit:function(t){var e=this;this.formInline.job=this.job;var n=this.formInline;this.$refs[t].validate(function(t){t?(e.$Message.success("Send to server!"),console.log(n),c.a.post("/api/user/register",n).then(function(t){e.$Message.success(t.data.status),"success"===t.data.status?S.push("/login"):e.msg="Status:"+t.data.status})):e.$Message.error("Fail!")})},sendMsg:function(t){var e=this,n=this.formInline;c.a.post("/api/user/request_verification",n).then(function(t){"success"===t.data.status&&(e.msgBox="验证码发送成功")})}})},g={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"register"}},[n("Form",{ref:"formInline",attrs:{model:t.formInline,rules:t.ruleInline,inline:""}},[n("FormItem",{attrs:{prop:"username"}},[n("Input",{attrs:{type:"text",placeholder:"Username"},model:{value:t.formInline.username,callback:function(e){t.$set(t.formInline,"username",e)},expression:"formInline.username"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-person-outline"},slot:"prepend"})],1)],1),t._v(" "),n("FormItem",{attrs:{prop:"password"}},[n("Input",{attrs:{type:"password",placeholder:"Password"},model:{value:t.formInline.password,callback:function(e){t.$set(t.formInline,"password",e)},expression:"formInline.password"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-lock-outline"},slot:"prepend"})],1)],1),t._v(" "),n("FormItem",{attrs:{prop:"rpassword"}},[n("Input",{attrs:{type:"password",placeholder:"Password Again"},model:{value:t.formInline.rpassword,callback:function(e){t.$set(t.formInline,"rpassword",e)},expression:"formInline.rpassword"}},[n("Icon",{attrs:{slot:"prepend",type:"ios-lock-outline"},slot:"prepend"})],1)],1),t._v(" "),n("FormItem",{attrs:{prop:"mobile"}},[n("Input",{attrs:{type:"text",placeholder:"Phone number"},model:{value:t.formInline.mobile,callback:function(e){t.$set(t.formInline,"mobile",e)},expression:"formInline.mobile"}})],1),t._v(" "),n("FormItem",{attrs:{prop:"verification"}},[n("Input",{attrs:{type:"text",placeholder:"verification"},model:{value:t.formInline.verification,callback:function(e){t.$set(t.formInline,"verification",e)},expression:"formInline.verification"}})],1),t._v(" "),n("FormItem",{attrs:{prop:"job"}},[n("RadioGroup",{model:{value:t.job,callback:function(e){t.job=e},expression:"job"}},[n("Radio",{attrs:{label:"student"}}),t._v(" "),n("Radio",{attrs:{label:"teacher"}})],1)],1),t._v(" "),n("FormItem",[n("Button",{attrs:{type:"primary"},on:{click:function(e){t.handleSubmit("formInline")}}},[t._v("Signin")]),t._v(" "),n("Button",{on:{click:function(e){t.sendMsg("formInline")}}},[t._v(t._s(t.msgBox))])],1)],1),t._v(" "),n("router-link",{attrs:{to:"/login"}},[t._v("Cancel")])],1)},staticRenderFns:[]},h=n("VU/8")(v,g,!1,null,null,null).exports,b={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",[e("p",[this._v("404 - Not Found")])])}]},I=n("VU/8")(null,b,!1,null,null,null).exports,_={name:"List",data:function(){return{items:[{className:"第一课",teacherName:"习近平",viewing:"100亿人正在观看",image:"这里应该是一个图片的url",id:""}]}},created:function(){this.getList()},methods:{getList:function(){var t=this;c.a.get("/api/list").then(function(e){console.log(e),t.items=e.data})}}},w={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"list"}},[n("ul",t._l(t.items,function(e){return n("li",[n("Card",{staticClass:"card"},[n("router-link",{attrs:{to:"/living"}},[n("img",{staticClass:"previewPicture",attrs:{src:e.image}})]),t._v(" "),n("div",{staticClass:"classroomDetail",staticStyle:{"text-align":"center"}},[n("span",{staticClass:"className"},[t._v("\n\t\t\t\t\t\t"+t._s(e.className)+"\n\t\t\t\t\t")]),t._v(" "),n("span",{staticClass:"teacherName"},[t._v("\n\t\t\t\t\t\t"+t._s(e.teacherName)+"\n\t\t\t\t\t")]),t._v(" "),n("span",{staticClass:"viewingNumber"},[t._v("\n\t\t\t\t\t\t"+t._s(e.viewing)+"\n\t\t\t\t\t")])])],1)],1)}))])},staticRenderFns:[]};var y=n("VU/8")(_,w,!1,function(t){n("SROZ")},null,null).exports,x={name:"��¼",data:function(){return{theme1:"light",note:{position:"absolute",top:"0px",left:"0px",width:"100%",height:"100%",backgroundSize:"100% 100%",backgroundRepeat:"no-repeat"}}},methods:{skip:function(t){this.$router.push(t)},send_word:function(){var t,e=document.getElementById("talkwords"),n=document.getElementById("words");""!=e.value?(t=e.value,n.innerHTML=n.innerHTML+t):alert("no blank")},connect:function(){var t=document.getElementById("littleVedio"),e=document.getElementById("words");t.style.display="block",e.style.height="500px"}}},k={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticStyle:{height:"100%"},attrs:{id:"living"}},[n("Layout",[n("Layout",[n("Content",{staticStyle:{width:"60%"}},[n("div",{staticStyle:{float:"left",width:"100%",height:"100%"},attrs:{id:"mainVedio"}},[n("video",{attrs:{controls:"",width:"100%",height:"100%",border:"1"}},[n("source",{attrs:{src:"",type:"video/mp4"}})])])]),t._v(" "),n("Sider",{staticStyle:{width:"40%"}},[n("div",{staticStyle:{width:"100%",display:"none"},attrs:{id:"littleVedio"}},[n("video",{attrs:{controls:"",border:"1"}},[n("source",{attrs:{src:"",type:"video/mp4"}})])]),t._v(" "),n("div",{staticStyle:{width:"150%",border:"1px solid #666",background:"#f9f9f9"},attrs:{id:"talk_sec"}},[n("div",{staticStyle:{width:"95%",height:"700px","/*500px*/border":"1px solid #666",background:"#fff",margin:"10px auto 0",overflow:"auto"},attrs:{id:"words"}}),t._v(" "),n("div",{staticStyle:{width:"95%",height:"40px","margin-bottom":"0.5%"},attrs:{id:"talk_input"}},[n("input",{staticStyle:{width:"70%",height:"95%",padding:"0px",float:"left","margin-left":"10px",outline:"none","text-indent":"10px"},attrs:{type:"text",id:"talkwords"}}),t._v(" "),n("Button",{staticStyle:{},attrs:{id:"talksub",type:"primary"},on:{click:function(e){t.send_word()}}},[t._v("send")])],1)])])],1),t._v(" "),n("Footer",[n("Button",{attrs:{type:"primary"},on:{click:function(e){t.connect()}}},[t._v(" connect")])],1)],1)],1)},staticRenderFns:[]};var $=n("VU/8")(x,k,!1,function(t){n("PeB4")},null,null).exports;s.default.use(a.a);var S=new a.a({mode:"history",routes:[{path:"/login",name:"Login",component:f},{path:"/",name:"Login",component:f},{path:"/register",name:"Register",component:h},{path:"/list",name:"List",component:y},{path:"/living",name:"Living",component:$},{path:"*",component:I}]}),F=n("BTaQ"),j=n.n(F);n("+skl");s.default.use(j.a),s.default.config.productionTip=!1,s.default.use(d.a),new s.default({el:"#app",router:S,components:{App:o},template:"<App/>"});new d.a.Store({state:{count:0},mutations:{increment:function(t){t.count++}}})},PeB4:function(t,e){},SROZ:function(t,e){},"e/Aw":function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.444cac88906b7f17481c.js.map