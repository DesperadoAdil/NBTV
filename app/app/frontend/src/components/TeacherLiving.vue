<template>
  <div class="tealivingmain">

    <card  class="cardtea">
      <p slot="title" style="font-size: 20px">选项</p>
      <Menu style="width: 100%">
        <Submenu name="1" class="menuitentea">
          <template slot="title" >
            <Icon type="ios-paper" />
            添加教学资源
          </template>
          <MenuItem name="1-1" class="menuitentea">添加课件</MenuItem>
          <MenuItem name="1-2" class="menuitentea">添加题目</MenuItem>
        </Submenu>
        <Submenu name="2" class="menuitentea">
          <template slot="title">
            <Icon type="ios-people" />
            使用教学资源
          </template>
          <MenuItem name="2-1" class="menuitentea" @click.native="teatext">使用教学课件</MenuItem>
          <MenuItem name="2-2" class="menuitentea">布置题目</MenuItem>
          <MenuItem name="2-2" class="menuitentea" @click.native="closetext">关闭题目或教学资源</MenuItem>
        </Submenu>
        <Submenu name="3" class="menuitentea">
          <template slot="title">
            <Icon type="ios-stats" />
            学生做题情况
          </template>
          <MenuItem name="3-1" class="menuitentea">学生列表</MenuItem>
        </Submenu>
      </Menu>
      <Button class="btnopen" type="primary"  v-bind:icon="openclose"  @click="teaopenclose()">
        <span class="menuitentea">{{this.opentext}}</span>
      </Button>
    </card>


    <Card id="mainlivingcard" class="cardtealiving">
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <div id='player' ></div>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </Card>

    <Card id="mainpdfcard" class="cardtealivingpdf">
      <iframe id="displayPdfIframe" class="pdfframe"/>
    </Card>

    <Card id="littlelivingcard" class="cardtealittleliving">

      <div id='littleplayer' ></div>

    </Card>

    <div id="liaotianshi" class="danmuxinxi">
      <Card style="height: 800px">
        <h3>聊天室信息显示部分（待修改）</h3>
      </Card>
    </div>







  </div>
</template>

<!--<script src="https://player.polyv.net/livescript/liveplayer.js"></script>-->
<script>
  import axios from 'axios';
  export default{

    name: 'load',
    mounted() {
      var timer = setTimeout(function(){
        doItPerSecond();
      },1000)
      var num = 0;
      function doItPerSecond() {
        //dosomething...
        var player = polyvObject('#player').livePlayer({
          'width':'100%',
          'height':700+'px',
          'uid':'7181857ac2',
          'vid':'242544'
        });
        num++;
        console.log(num);
      };
    },
    created:function(){

      const s = document.createElement('script');
      s.type = 'text/javascript';
      s.src = 'https://player.polyv.net/livescript/liveplayer.js';
      document.body.appendChild(s);
      this.showUserInfo();
    },

    data() {


    return {
      //<!--vediosrc:'',-->
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: '',
        job:'',
      },
      vid:'242544',
      theme1: 'light',
      toopen:true,
      openclose:'ios-videocam-outline',
      opentext:'开播',
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
    teatext(){
      console.log("1321312");
      var mainlivingcard = document.getElementById("mainlivingcard");
      mainlivingcard.style.display="none";
      var littlelivingcard = document.getElementById("littlelivingcard");
      littlelivingcard.style.display="block";
      var player = polyvObject('#littleplayer').livePlayer({
        'width':'100%',
        'height':360+'px',
        'uid':'7181857ac2',
        'vid':this.vid,
      });
      var mainpdfcard = document.getElementById("mainpdfcard");
      mainpdfcard.style.display="block";
      var liaotianshi= document.getElementById("liaotianshi");
      liaotianshi.style.top=400+"px";
      var frame = document.getElementById('displayPdfIframe');
      frame.src = "/static/pdfjs/web/viewer.html?file=/static/pdf/1-1.pdf";

    },
    closetext(){
      console.log("1321312");
      var mainlivingcard = document.getElementById("mainlivingcard");
      mainlivingcard.style.display="block";
      var littlelivingcard = document.getElementById("littlelivingcard");
      littlelivingcard.style.display="none";
      var mainpdfcard = document.getElementById("mainpdfcard");
      mainpdfcard.style.display="none";
      var liaotianshi= document.getElementById("liaotianshi");
      liaotianshi.style.top=60+"px";
    },
    showUserInfo() {
      console.log("1234567");
      this.userInfo['username'] = this.$cookies.get('user').username;
      this.userInfo['status']= this.$cookies.get('user').status;
      this.userInfo['password'] = this.$cookies.get('user').password;
      this.userInfo['mobile'] = this.$cookies.get('user').mobile;
      this.userInfo['job'] = this.$cookies.get('user').job;
    },

    teaopenclose(){

      if(this.toopen)
      {

          this.toopen=false;
          this.opentext='关播';
          this.openclose='ios-power';
          var params = new URLSearchParams();
          params.append('name', this.userInfo['username']);
          params.append('job',this.userInfo['job']);
          axios.post('/api/user/openliving',params).then((resp) => {
           this.vid=reap.vid;
            var div = document.getElementById("player");
            div.style.vid=resp.vid;
        });
      }
      else
      {
        this.toopen=true;
        this.opentext='开播';
        this.openclose='ios-videocam-outline';
        var params = new URLSearchParams();
        params.append('name', this.userInfo['username']);
        params.append('job',this.userInfo['job']);
        axios.post('/api/user/closeliving',params).then((resp) => {

      });
      }
    },

  }
  };
</script>
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
  .tealivingmain{
    width: 100%;
  }
  .cardtea{
    width: 18%;
  }
  .menuitentea{
    font-size: 20px;
  }
  .btnopen{
    padding-:5%;
    margin:5%;
  }
  .cardtealiving{
    position:absolute;
    left: 18%;
    width: 60%;
    top:60px;
  }
  .cardtealivingpdf{
    position:absolute;
    left: 18%;
    width: 60%;
    top:60px;
    display: none;
  }
  .pdfframe{
     width:100% ;
     height:800px;
  }
  .topveido{
    height: auto;
  }
  .bottomveido{
    height: auto;
  }
  .danmuxinxi{
    position:absolute;
    left: 78%;
    width: 22%;
    top:60px;
  }
  .cardtealittleliving{
    position:absolute;
    left: 78%;
    width: 22%;
    top:60px;
    display: none;
  }
  .teamainvedio{
   width:100%;
   height:700px;
  }
</style>

