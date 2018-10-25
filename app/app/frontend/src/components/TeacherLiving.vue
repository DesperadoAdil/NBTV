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
          <MenuItem name="1-1" class="menuitentea" @click.native="upload">添加课件</MenuItem>
          <MenuItem name="1-2" class="menuitentea" @click.native="exam">添加题目</MenuItem>
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
        <Submenu name="3" class="menuitentea"  >
          <template slot="title">
            <Icon type="ios-stats" />
            学生做题情况
          </template>
          <MenuItem name="3-1" class="menuitentea" v-for="item in studentitems" @click.native="showstudentti(item)">{{item}}</MenuItem>
        </Submenu>
      </Menu>
      <Button class="btnopen" type="primary"  v-bind:icon="openclose"  @click="teaopenclose()">
        <span class="menuitentea">{{this.opentext}}</span>
      </Button>
    </card>

    <!--上传-->
    <Modal   v-model="modal4"    @on-ok=""    @on-cancel="">
      <p slot="header" style="font-size: 20px">
        <span>上传课件</span>
      </p>
      <Upload action="//jsonplaceholder.typicode.com/posts/">
        <Button icon="ios-cloud-upload-outline">Upload files</Button>
      </Upload>
    </Modal>

    <Modal   v-model="modal5"    @on-ok=""    @on-cancel="">
      <p slot="header" style="font-size: 20px">
        <span>设置选择题</span>
      </p>
      <Form ref="examOptions" :model="examOptions" :rules="ruleInline">
        <FormItem prop="Description">
          <Input type="text" v-model="examOptions.Description" placeholder="Description"></Input>
        </FormItem>
        <FormItem prop="OptionA">
          <Input type="text" v-model="examOptions.OptionA" placeholder="OptionA"></Input>
        </FormItem>
        <FormItem prop="OptionB">
          <Input type="text" v-model="examOptions.OptionB" placeholder="OptionB"></Input>
        </FormItem>
        <FormItem prop="OptionC">
          <Input type="text" v-model="examOptions.OptionC" placeholder="OptionC"></Input>
        </FormItem>
        <FormItem prop="OptionD">
          <Input type="text" v-model="examOptions.OptionD" placeholder="OptionD"></Input>
        </FormItem>
      </Form>
    </Modal>

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

    <Modal   v-model="modal3"    @on-ok=""    @on-cancel="">
      <p slot="header" style="font-size: 20px">
        <span>{{curstu}}的做题情况如下：</span>
      </p>
      <Table stripe border :columns="columns1" :data="curti" ref="table"></Table>
      <Button class="databutton" type="primary" size="large" @click.native="exportData(1)"><Icon type="ios-download-outline"></Icon>导出原始数据</Button>
    </Modal>

    <div id="mainlivingcard" class="cardtealiving00">
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <div id='player' ></div>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </div>

    <div id="mainpdfcard" class="cardtealivingpdf">
      <iframe id="displayPdfIframe" class="pdfframe"/>
    </div>

    <div id="mainselectcard" class="cardtealivingselect">
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

    <div id="littlelivingcard" class="cardtealittleliving">

      <div id='littleplayer' ></div>

    </div>

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
        'height':600+'px',
        'uid':'7181857ac2',
        'vid':'248980'
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
      examOptions: {
        Description: '',
        OptionA: '',
        OptionB: '',
        OptionC: '',
        OptionD: ''
      },
      columns1: [
        {
          title: '题目',
          key: 'title'
        },
        {
          title: '答案',
          key: 'ans'
        },
      ],
      curstu:'zsh',
      curti:[
        {
          title:'1',
          ans:'A',
        },
        {
          title:'2',
          ans:'B',
        },
        {
          title:'3',
          ans:'int main()',
        },
        {
          title:'4',
          ans:'#include<> \n using namespace std; int main(){ int c; cout<<c++<<endl; return 0}',
        },
      ],
      studentitems:['zsh','adil','zhq','hyx','xcj'],
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
      modal3: false,
      modal2: false,
      modal1: false,
      modal4: false,
      modal5: false,
      vid:'248980',
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
      exportData (type)
      {
        if (type === 1) {
          this.$refs.table.exportCsv({
            filename: this.curstu+'数据统计'
          });
        }
      },
      getstudents(){
      console.log("1321312");
      var params = new URLSearchParams();
      params.append('name', this.userInfo['username']);
      params.append('job',this.userInfo['job']);
      params.append('vid',this.vid);
      axios.post('/api/user/getstudents',params).then((resp) => {
        this.studentitems=resp.studentitems;
      });
    },
    showstudentti(item){
      console.log("1321312");
      this.curstu=item;
      var params = new URLSearchParams();
      params.append('name', this.userInfo['username']);
      params.append('job',this.userInfo['job']);
      params.append('stu',this.curstu);
      params.append('vid',this.vid);
      axios.post('/api/user/getstudentsti',params).then((resp) => {
        this.curti=resp.curti;
      });
      this.modal3=true;
    },
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
    upload () {
      var params = new URLSearchParams()
      this.modal4 = true
    },
    exam () {
      var params = new URLSearchParams()
      this.modal5 = true
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
          var params = new URLSearchParams();
          params.append('name', this.userInfo['username']);
          params.append('job',this.userInfo['job']);
          params.append('vid',this.vid);
          params.append('pdf',ipdf.title);
          axios.post('/api/user/showpdfs',params).then((resp) => {

          });
          var mainlivingcard = document.getElementById("mainlivingcard");
          mainlivingcard.style.display="none";
          var littlelivingcard = document.getElementById("littlelivingcard");
          littlelivingcard.style.display="block";
          var player = polyvObject('#littleplayer').livePlayer({
            'width':'100%',
            'height':260+'px',
            'uid':'7181857ac2',
            'vid':this.vid,
          });
          var mainselectcard = document.getElementById("mainselectcard");
          mainselectcard.style.display="none";
          var mainpdfcard = document.getElementById("mainpdfcard");
          mainpdfcard.style.display="block";
          var liaotianshi= document.getElementById("liaotianshi");
          liaotianshi.style.top=330+"px";
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
          var params = new URLSearchParams();
          params.append('name', this.userInfo['username']);
          params.append('job',this.userInfo['job']);
          params.append('vid',this.vid);
          params.append('select',iselect.title);
          axios.post('/api/user/showselect',params).then((resp) => {
          });
          var mainlivingcard = document.getElementById("mainlivingcard");
          mainlivingcard.style.display="none";
          var littlelivingcard = document.getElementById("littlelivingcard");
          littlelivingcard.style.display="block";
          var player = polyvObject('#littleplayer').livePlayer({
            'width':'100%',
            'height':260+'px',
            'uid':'7181857ac2',
            'vid':this.vid,
          });
          var mainpdfcard = document.getElementById("mainpdfcard");
          mainpdfcard.style.display="none";
          var mainselectcard = document.getElementById("mainselectcard");
          mainselectcard.style.display="block";
          var liaotianshi= document.getElementById("liaotianshi");
          liaotianshi.style.top=330+"px";
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
      this.$Modal.confirm({
        title: '提示',
        content: '确认退出教学资源',
        onOk: () => {
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
        onCancel: () => {
          this.$Message.info('Clicked cancel');
        }
      });
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
            this.getstudents();
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
    height:600px;
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
  .databutton{
    margin-top: 15px;
  }
</style>

