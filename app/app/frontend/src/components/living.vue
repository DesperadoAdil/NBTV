<template>
    <div id="living" style="height: 100%;">
        <Layout>

            <Layout>
                <Content style="width: 60%">
                    <div id="mainVedio" style="float:left;width: 100%;height: 100%">
                        <video controls width="100%" height="100%"  border="1" ><source src="" type="video/mp4"></video>
                    </div>
                </Content >

                <Sider style="width: 40%">
                    <div id="littleVedio" style="width: 100%;display: none">
                        <video controls border="1"><source src="" type="video/mp4"></video>
                    </div>

                    <div id="talk_sec" style="width: 150%;border:1px solid #666;background:#f9f9f9;">
                        <div id="words" style="width:95%;height: 700px;/*500px*/border:1px solid #666;background:#fff;margin:10px auto 0;overflow:auto;">
                        </div>

                        <div id="talk_input" style="  width:95%; height: 40px;margin-bottom:0.5%;">
                            <input type="text"  id="talkwords" style=" width:70%; height:95%;padding:0px; float:left; margin-left:10px; outline:none; text-indent:10px;">
                            <Button  id="talksub"  @click="send_word()" type="primary" style=" ">send</Button>
                        </div>
                    </div>
                </Sider>
            </Layout>
            <Footer>
                <Button type="primary" @click="connect()"> connect</Button>
            </Footer>
        </Layout>

    </div>



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
         theme1: 'light',

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
		    var words = document.getElementById("words");
            littleVedio.style.display="block";
            words.style.height=500+'px';
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




</style>