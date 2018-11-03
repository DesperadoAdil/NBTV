<template>
  <div class="tealivingmain">

    <Button type="primary" @click="showpdf0">展示pdf</Button>
    <Button type="primary" @click="showselect0">展示选择题</Button>
    <Button type="primary" @click="showcode0">展示编程题</Button>
    <Button type="primary" @click="exitliving0">回退界面</Button>

    <div id="mainlivingcard" class="cardtealiving11" :style="{display:mainlivingcarddisplay?'block':'none'}">
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <div id='player'></div>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </div>

    <div id="littlelivingcard" class="cardtealittleliving11" :style="{display:littlelivingcarddisplay?'block':'none'}">
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <div id='player2'></div>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </div>

    <div id="mainpdfcard" class="cardtealivingpdf11" :style="{display:mainpdfcarddisplay?'block':'none'}">
      <iframe id="displayPdfIframe" class="pdfframe" :src="displayPdfurl0"/>
    </div>

    <div id="maincodecard" class="cardtealivingcdode00" :style="{display:maincodecarddisplay?'block':'none'}">
      <h>编程题</h>
    </div>

    <div id="mainselectcard" class="cardtealivingselect00" :style="{display:mainselectcarddisplay?'block':'none'}">
      <p class="selecttitle00">{{curtitle}}</p>
      <RadioGroup class="radiotea" v-model="ionselect" vertical>
        <Radio v-bind:label="curans[0]" style="font-size: 15px">
          <span>A、{{curans[0]}}</span>
        </Radio>
        <Radio v-bind:label="curans[1]" style="font-size: 15px">
          <span>B、{{curans[1]}}</span>
        </Radio>
        <Radio v-bind:label="curans[2]" style="font-size: 15px">
          <span>C、{{curans[2]}}</span>
        </Radio>
        <Radio v-bind:label="curans[3]" style="font-size: 15px">
          <span>D、{{curans[3]}}</span>
        </Radio>
      </RadioGroup>
      <p class="anstea00">本题目答案：{{curanswer}}</p>
    </div>

    <div id="liaotianshi" class="danmuxinxi00" :style="{top:liaotianshiheight}">
        <h3>聊天室信息显示部分（待修改）</h3>
    </div>


  </div>
</template>


<script>
  import axios from 'axios';
  export default{
    name: 'load',
    mounted() {
    var xxx=this.videohei0
    console.log(xxx)
    var yyy=this.curvid
    console.log(yyy)
    var timer = setTimeout(function(){
      doItPerSecond();
    },1000)
    var num = 0;
    function doItPerSecond() {
      var player = polyvObject('#player').livePlayer({
        'width':'100%',
        'height':xxx,
        'uid':'7181857ac2',
        'vid':yyy
      });
      var player = polyvObject('#player2').livePlayer({
        'width':'100%',
        'height':200+'px',
        'uid':'7181857ac2',
        'vid':yyy
      });
      num++;
      console.log(num);
    };
  },
  created:function(){
    this.cururl = this.$route.params.url;
    console.log(this.cururl);
    const data = this.curuser;
    data['username'] = this.userInfo['username'];
    data['job'] = this.userInfo['job'];
    data['url'] = this.cururl;
    axios.post('/api/user/urlgetvid', data).then((resp) => {
        this.curvid=resp.data.vid ;
    });
    const s = document.createElement('script');
    s.type = 'text/javascript';
    s.src = 'https://player.polyv.net/livescript/liveplayer.js';
    document.body.appendChild(s);
    this.showUserInfo();
  },

  data() {
    return {
      maincodecarddisplay:false,
      curpdfurl:'/static/pdf/1-1.pdf',
      videohei0:600+'px',
      classmain11:true,
      curvid:'242522',
      cururl:'',
      displayPdfurl0:'',
      liaotianshiheight:150+'px',
      littlelivingcarddisplay:false,
      mainselectcarddisplay:false,
      mainpdfcarddisplay:false,
      mainlivingcarddisplay:true,
      curtitle:'xjbx1',
      curans:['1','2','3','4'],
      curanswer:'A',
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: '',
        job:'',
      },
      curuser:{
        username: '',
        job: '',
        url: '',
        item:'',
      },
    };
  },
  methods: {
    showUserInfo() {
      console.log("1234567");
        this.userInfo['username'] = this.$cookies.get('user').username;
        this.userInfo['status']= this.$cookies.get('user').status;
        this.userInfo['password'] = this.$cookies.get('user').password;
        this.userInfo['mobile'] = this.$cookies.get('user').mobile;
        this.userInfo['job'] = this.$cookies.get('user').job;
      },
      showpdf0(){
        console.log("weqweqwe")
        this.liaotianshiheight=500+'px'
        this.littlelivingcarddisplay=true
        this.mainselectcarddisplay=false
        this.mainpdfcarddisplay=true
        this.mainlivingcarddisplay=false
        this.maincodecarddisplay=false
        this.displayPdfurl0 = '/static/pdfjs/web/viewer.html?file=' + this.curpdfurl
      },
      showselect0(){
        console.log("weqweqwe")
        this.liaotianshiheight=500+'px'
        this.littlelivingcarddisplay=true
        this.mainselectcarddisplay=true
        this.mainpdfcarddisplay=false
        this.mainlivingcarddisplay=false
         this.maincodecarddisplay=false
      },
      showcode0(){
        console.log("weqweqwe")
        this.liaotianshiheight=500+'px'
        this.littlelivingcarddisplay=true
        this.mainselectcarddisplay=false
        this.mainpdfcarddisplay=false
        this.mainlivingcarddisplay=false
        this.maincodecarddisplay=true
       },
      exitliving0(){
        console.log("weqweqwe")
        this.liaotianshiheight=150+'px'
        this.littlelivingcarddisplay=false
        this.mainselectcarddisplay=false
        this.mainpdfcarddisplay=false
        this.mainlivingcarddisplay=true
        this.maincodecarddisplay=false
      }
    }


  };
</script>
<style>

  .tealivingmain{
    width: 100%;
  }

  .cardtealiving11{
    position:absolute;
    left: 10%;
    width: 59%;
    top:150px;
  }
  .cardtealivingpdf11{
    position:absolute;
    left: 10%;
    width: 59%;
    top:150px;
    display: none;
  }
  .pdfframe{
    width:100% ;
    height:600px;
  }
  .topveido{
    height: auto;
  }
  .bottomveido{
    height: auto;
  }
  .cardtealittleliving11{
    position:absolute;
    left: 70%;
    width: 20%;
    top:150px;
  }
  .danmuxinxi00{
    position:absolute;
    left: 70%;
    width: 20%;
    top:150px;
  }

  .cardtealivingselect00{
    position:absolute;
    left: 10%;
    width: 59%;
    height: 800px;
    top:150px;
    display: none;
  }
  .cardtealivingcdode00{
    position:absolute;
    left: 10%;
    width: 59%;
    height: 800px;
    top:150px;
    display: none;
  }

  .selecttitle00{
    padding-top: 3%;
    position:relative;
    left:40px;
    float:left;
    font-size: 15px;
  }
  .radiotea{
    float:left;
    position:relative;
    top:300px;

  }
  .anstea00{
    float:left;
    position:relative;
    top:500px;
    left:-50px;
    font-size: 15px;
  }

</style>

