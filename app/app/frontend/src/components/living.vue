<template>
    <el-container  style="height: 150%;"direction="vertical">
        <el-header style="height: 20%;">
            <el-row>
                <el-col :span="2"><el-button type="text">guide1</el-button></el-col>
                <el-col :span="2"><el-button type="text">guide2</el-button></el-col>
                <el-col :span="2"><el-button type="text">guide3</el-button></el-col>
                <el-col :span="2"><el-button type="text">guide4</el-button></el-col>
                <el-col :span="14"><el-button type="text"></el-button></el-col>
                <el-col :span="2"><el-button type="text">guide5</el-button></el-col>
            </el-row>
        </el-header>
        <el-container style="height: 130%;"direction=" horizontal">
            <el-main style="width: 80%;">
                <div id="mainVedio" style="float:left;width: 100%;height: 100%">
                    <video controls width="100%" height="100%"  border="1" uid="7181857ac2" vid="242544"><source src="" type="video/mp4"></video>
                </div>

            </el-main>
            <el-aside style="width: 20%;">
                <div id="littleVedio" style="float: right;width: 100%;height: 40%;margin-top: 2%;display:none;"">
                <video controls width="95%" height="95%"  border="1"><source src="" type="video/mp4"></video>
                </div>

                <div id="talk_sec" style="float: right;width: 100%;height: 100%;border:1px solid #666;background:#f9f9f9;">
                    <div id="words" style="width:95%;height:85%;/*320px*/border:1px solid #666;background:#fff;margin:10px auto 0;overflow:auto;">
                    </div>

                    <div id="talk_input" style="  width:95%; height:10%;margin:0.5%;">
                        <input type="text"  id="talkwords" style=" width:70%; height:95%;padding:0px; float:left; margin-left:10px; outline:none; text-indent:10px;">
                        <input type="button" value="send"  id="talksub"  @click="send_word()" style=" width:20%;height:80%;float:left;margin-left:2%;
                        outline: none;
                        cursor: pointer;
                        text-align: center;
                        text-decoration: none;
                        font: 14px/100% Arial, Helvetica, sans-serif;

                        text-shadow: 0 1px 1px rgba(0,0,0,.3);
                        -webkit-border-radius: .5em;
                        -moz-border-radius: .5em;
                        border-radius: .5em;
                        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.2);
                        -moz-box-shadow: 0 1px 2px rgba(0,0,0,.2);
                        box-shadow: 0 1px 2px rgba(0,0,0,.2);">
                    </div>
                </div>
            </el-aside>

        </el-container>
        <el-footer style="height: 20%;">
            <el-row style="">
                <el-col :span="2"> <el-button type="primary" @click="connect()" >connect</el-button></div></el-col>

            </el-row>
        </el-footer>
    </el-container>


</template>


<script type="es6">
export default{

	name: '登录',
	//<!--mounted: function () {-->
      //<!--&lt;!&ndash;this.vediosrc = this.$route.query.id&ndash;&gt;-->

      //<!--&lt;!&ndash;console.log(this.vediosrc)&ndash;&gt;-->
    //<!--},-->
	data() {

		return {
          //<!--vediosrc:'',-->

		 note: {
				position:"absolute",
				top:"0px",
				left:"0px",
				width: "100%",
				height:"100%",
				backgroundSize: "100% 100%",
				backgroundRepeat: "no-repeat",
			}
		};
		},
		methods: {
		  skip(a){
			this.$router.push(a)
		  },
		  send_word(){
		            var TalkWords = document.getElementById("talkwords");
		            var Words = document.getElementById("words");
	                var str = "";
	                if(TalkWords.value == ""){
	                     // 消息为空时弹窗
	                    alert("no blank");
	                    return;
	                }
	              	str = TalkWords.value ;

	                Words.innerHTML = Words.innerHTML + str;
		  },
		  connect(){
		    var littleVedio = document.getElementById("littleVedio");
		    var talk_sec = document.getElementById("talk_sec");
            littleVedio.style.display="block";
            talk_sec.style.height="58%";
		  }
		}
}</script>
<style>
    .login-container{
        box-shadow: 0 0px 8px 0 rgba(0,0,0,0.06),0 1px 0px 0 rgba(0,0,0, 0.02);
        -webkit-border-radius: 5px;
        border-radius: 5px;
        -moz-border-radius: 5px;
        background-clip: padding-box;
        margin: 180px auto;
        width: 350px;
        padding: 35px 35px 15px 35px;
        background: #fff;
        border: 1px solid #eaeaea;
        box-shadow: 0 0 25px #cac6c6;
    }
    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;

    }
    .el-aside {
        background-color: #D3DCE6;
        color: #333;

    }
    .el-main {
        background-color: #E9EEF3;
        color: #333;


    }
</style>