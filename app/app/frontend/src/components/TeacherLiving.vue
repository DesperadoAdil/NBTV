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
          <MenuItem name="2-2" class="menuitentea" @click.native="teaselect">布置选择题目</MenuItem>
          <MenuItem name="2-2" class="menuitentea" @click.native="closetext">退出教学资源</MenuItem>
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

    <!--pdf等课件信息-->
    <Modal   v-model="modal1"    @on-ok=""    @on-cancel="">
      <p slot="header" style="font-size: 20px">
        <span>选择你要展示的课件</span>
      </p>
      <CellGroup v-for="item in pdfitems">
        <Cell style="font-size: 20px" @click.native="showpdf(item)">{{item.title}}</Cell>
      </CellGroup>
    </Modal>

    <Modal   v-model="modal2"    @on-ok=""    @on-cancel="">
      <p slot="header" style="font-size: 20px">
        <span>选择你要展示的选择题</span>
      </p>
      <CellGroup v-for="item in selectitems">
        <Cell style="font-size: 20px" @click.native="showselect(item)">{{item.title}}</Cell>
      </CellGroup>
    </Modal>

    <Card id="mainlivingcard" class="cardtealiving00">
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

    <Card id="mainselectcard" class="cardtealivingselect">
      <p class="selecttitle00">{{curtitle}}</p>
      <RadioGroup class="radiotea" v-model="ionselect" vertical>
        <Radio v-bind:label="curans[0]">
          <span>A、{{curans[0]}}</span>
        </Radio>
        <Radio v-bind:label="curans[1]">
          <span>B、{{curans[1]}}</span>
        </Radio>
        <Radio v-bind:label="curans[2]">
          <span>C、{{curans[2]}}</span>
        </Radio>
        <Radio v-bind:label="curans[3]">
          <span>D、{{curans[3]}}</span>
        </Radio>
      </RadioGroup>
      <p class="anstea00">本题目答案：{{curanswer}}</p>
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
      ionselect:'111',
      curtitle:'xjbx1',
      curans:['1','2','3','4'],
      curanswer:'A',
      selectitems: [
        {
          title:'xjbx1',
          ans:['1','2','3','4'],
          answer:'A'
        },
        {
          title:'xjbx2',
          ans:['1','2','3','4'],
          answer:'A'
        },
        {
          title:'xjbx3',
          ans:['1','2','3','4'],
          answer:'A'
        },
        {
          title:'xjbx4',
          ans:['1','2','3','4'],
          answer:'A'
        },
      ],
      pdfitems: [
        {
          title:'pdf1',
          url:'/static/pdf/1-1.pdf',
        },
        {
          title:'pdf2',
          url:'/static/pdf/1-1.pdf',
        },
        {
          title:'pdf3',
          url:'/static/pdf/1-1.pdf',
        },
        {
          title:'pdf4',
          url:'/static/pdf/1-1.pdf',
        }
      ],
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: '',
        job:'',
      },
      modal2: false,
      modal1: false,
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
      var params = new URLSearchParams();
      params.append('name', this.userInfo['username']);
      params.append('job',this.userInfo['job']);
      params.append('vid',this.vid);
      axios.post('/api/user/getpdfs',params).then((resp) => {
        this.pdfitems=resp.pdfitems;
      });
      this.modal1=true;

    },
    teaselect(){
      var params = new URLSearchParams();
      params.append('name', this.userInfo['username']);
      params.append('job',this.userInfo['job']);
      params.append('vid',this.vid);
      axios.post('/api/user/getselects',params).then((resp) => {
        this.selectitems=resp.selectitems;
      });
      this.modal2=true;
    },
    showpdf:function(ipdf){
      console.log("1321312");
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示'+ipdf.title,
        onOk: () => {
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
          var mainselectcard = document.getElementById("mainselectcard");
          mainselectcard.style.display="none";
          var mainpdfcard = document.getElementById("mainpdfcard");
          mainpdfcard.style.display="block";
          var liaotianshi= document.getElementById("liaotianshi");
          liaotianshi.style.top=400+"px";
          var frame = document.getElementById('displayPdfIframe');
          frame.src = "/static/pdfjs/web/viewer.html?file="+ipdf.url;
          this.modal1=false;
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel');
        }
      });

    },
    showselect:function(iselect){
      console.log("1321312");
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示: \n ' +iselect.title,
        onOk: () => {
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
          mainpdfcard.style.display="none";
          var mainselectcard = document.getElementById("mainselectcard");
          mainselectcard.style.display="block";
          var liaotianshi= document.getElementById("liaotianshi");
          liaotianshi.style.top=400+"px";
          this.curtitle=iselect.title;
          this.curans=iselect.ans;
          this.curanswer=iselect.answer;
          this.modal2=false;
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel');
        }
      });

    },
    closetext(){
      console.log("1321312");
      var mainlivingcard = document.getElementById("mainlivingcard");
      mainlivingcard.style.display="block";
      var mainselectcard = document.getElementById("mainselectcard");
      mainselectcard.style.display="none";
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
        this.$Modal.confirm({
          title: '提示',
          content: '是否确认开播',
          onOk: () => {
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
          },
          onCancel: () => {

          }
        });


      }
      else
      {
        this.$Modal.confirm({
          title: '提示',
          content: '是否确认关播',
          onOk: () => {
            this.toopen=true;
            this.opentext='开播';
            this.openclose='ios-videocam-outline';
            var params = new URLSearchParams();
            params.append('name', this.userInfo['username']);
            params.append('job',this.userInfo['job']);
            axios.post('/api/user/closeliving',params).then((resp) => {

            });
          },
          onCancel: () => {

          }
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
  .cardtealiving00{
    position:absolute;
    left: 19%;
    width: 59%;
    top:60px;
  }
  .cardtealivingpdf{
    position:absolute;
    left: 19%;
    width: 59%;
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
    left: 79%;
    width: 21%;
    top:60px;
  }
  .cardtealittleliving{
    position:absolute;
    left: 79%;
    width: 21%;
    top:60px;
    display: none;
  }
  .cardtealivingselect{
    position:absolute;
    left: 19%;
    width: 59%;
    height: 800px;
    top:60px;
    display: none;
  }
  .teamainvedio{
    width:100%;
    height:700px;
  }
  .selecttitle00{
    position:relative;
    left:40px;
    float:left;
  }
  .radiotea{
    float:left;
    position:relative;
    top:200px;
  }
  .anstea00{
    float:left;
    position:relative;
    top:500px;
    left:-50px;
  }
</style>

