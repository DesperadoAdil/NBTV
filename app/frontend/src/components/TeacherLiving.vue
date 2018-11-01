<template>
  <div class="tealivingmain">

    <div  class="cardtea">
      <p slot="title" style="font-size: 20px">选项</p>
      <Menu style="width: 100%">
        <!-- 添加教学资源 -->
        <Submenu name="1" class="menuitentea">
          <template slot="title" >
            <Icon type="ios-paper" />
            添加教学资源
          </template>
          <MenuItem @click.native="modal_pdf = true">添加课件</MenuItem>
          <MenuItem @click.native="modal_multi = true">添加选择题</MenuItem>
          <MenuItem @click.native="modal_code = true">添加编程题</MenuItem>
        </Submenu>
        <!-- 使用教学资源 -->
        <Submenu name="2" class="menuitentea">
          <template slot="title">
            <Icon type="ios-people" />
            使用教学资源
          </template>
          <MenuItem name="2-1" class="menuitentea" @click.native="teatext">使用教学课件</MenuItem>
          <MenuItem name="2-2" class="menuitentea" @click.native="teaselect">布置选择题目</MenuItem>
          <MenuItem name="2-2" class="menuitentea" @click.native="closetext">退出教学资源</MenuItem>
        </Submenu>
        <!-- 学生做题情况 -->
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
    </div>

    <!--上传-->
    <Modal v-model="modal_pdf" @on-ok="addPDF()" @on-cancel="modal_pdf = false">
      <p slot="header" style="font-size: 20px">
        <span>上传课件</span>
      </p>
      <Upload action="//jsonplaceholder.typicode.com/posts/">
        <Button icon="ios-cloud-upload-outline">Upload files</Button>
      </Upload>
    </Modal>

    <!--设置选择题-->
    <Modal   v-model="modal_multi"    @on-ok="addMulti()"    @on-cancel="modal_multi = false">
      <p slot="header" style="font-size: 20px">
        <span>设置选择题</span>
      </p>
      <Form model="sub_multi" label-width="80" style="width: 300px">
        <FormItem label="Statement">
          <Input v-model="sub_multi.statement"></Input>
        </FormItem>
        <!-- 现在仅实现四个选项 -->
        <FormItem label="OptionA">
          <Input v-model="answer1"></Input>
        </FormItem>
        <FormItem label="OptionB">
          <Input v-model="answer2"></Input>
        </FormItem>
        <FormItem label="OptionC">
          <Input v-model="answer3"></Input>
        </FormItem>
        <FormItem label="OptionD">
          <Input v-model="answer4"></Input>
        </FormItem>
        <FormItem label="The Answer">
          <Input v-model="sub_multi.answer"></Input>
        </FormItem>
        <!-- 以下为可以实现选项的动态添加删除的原型代码
        <FormItem
          v-for="option in sub_multi.optionList">
          <Row>
            <Col span="18">
              <Input type="text" placeholder="Enter Your Choice"></Input>
            </Col>
            <Col span="4" offset="1">
              <Button @click="handleRemove(index)">Delete</Button>
            </Col>
          </Row>
        </FormItem>
        <FormItem>
          <Row>
            <Col span="12">
              <Button type="dashed" long @click="handleAdd" icon="md-add">Add a Choice</Button>
            </Col>
          </Row>
        </FormItem>
        -->
      </Form>
    </Modal>

    <!--设置编程题-->
    <Modal   v-model="modal_code"    @on-ok="addCode()"    @on-cancel="modal_code = false">
      <p slot="header" style="font-size: 20px">
        <span>设置编程题</span>
      </p>
      <Form>
        <FormItem label="Text">
          <!-- autosize="{minRows: 2,maxRows: 5}" may be used in input attribute-->
          <Input v-model="sub_code.statement"
                 type="textarea" rows="4"
                 placeholder="Enter Your Statement">
          </Input>
        </FormItem>
        <FormItem label="Language">
          <Select v-model="sub_code.language">
            <Option>python</Option>
            <Option>C++</Option>
            <Option>Java</Option>
            <Option>JavaScript</Option>
            <Option>Vue.js</Option>
          </Select>
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

    <div  id="mainlivingcard" class="cardtealiving00" :style="{display:mainlivingcarddisplay?'block':'none'}">
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <object >
        <embed id="rtmp-streamer" src="../../static/swfdir/RtmpStreamer.swf" bgcolor="#999999" quality="high"
               width="100%" height="600px" allowScriptAccess="sameDomain" type="application/x-shockwave-flash"  allowfullscreen="true"></embed>
      </object>
      <canvas id="canvas" width="100%" height="600"></canvas>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </div>

    <div id="mainpdfcard" class="cardtealivingpdf" :style="{display:mainpdfcarddisplay?'block':'none'}">
      <iframe id="displayPdfIframe" class="pdfframe" :src="displayPdfurl"/>
    </div>

    <div id="mainselectcard" class="cardtealivingselect" :style="{display:mainselectcarddisplay?'block':'none'}">
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

    <div id="littlelivingcard" class="cardtealittleliving" :style="{display:littlelivingcarddisplay?'block':'none'}">
      <object >
        <embed id="rtmp-streamer2" src="../../static/swfdir/RtmpStreamer.swf" bgcolor="#999999" quality="high"
               width="100%" height="260px" allowScriptAccess="sameDomain" type="application/x-shockwave-flash"  allowfullscreen="true"></embed>
      </object>
    </div>

    <div id="liaotianshi" class="danmuxinxi" :style="{top:liaotianshiheight}">
      <Card style="height: 800px">
        <h3>聊天室信息显示部分（待修改）</h3>
      </Card>
    </div>

  </div>
</template>

<!-- script starts
    -->
<!--<script src="https://player.polyv.net/livescript/liveplayer.js"></script>-->

<script>
import axios from 'axios'
import {setSWFIsReady} from '../../static/js/livingrtmp.js'
import {RtmpStreamer} from '../../static/js/livingrtmp.js'
export default{
  name: 'load',
  data () {
    return {
      // <!--vediosrc:'',-->
      //      mainlivingcarddispaly:block,
      //      mainlivingcarddispaly:'none',
      // 功能对话框

      // Yuxuan's variables:
      stream: '',
      streamer: '',
      streamername: '7181857ac220181025144543640',
      modal_pdf: false,
      modal_multi: false,
      sub_multi: {
        statement: '',
        optionList: [this.answer1, this.answer2, this.answer3, this.answer4],
        answer: '一个数字',
        url: '教室url'
      },
      answer1: '',
      answer2: '',
      answer3: '',
      answer4: '',
      modal_code: false,
      sub_code: {
        statement: '',
        language: '' // language 应当是个多选框
      },

      // Shihang
      modal3: false,
      modal2: false,
      modal1: false,
      displayPdfurl: '',
      liaotianshiheight: 60 + 'px',
      littlelivingcarddisplay: false,
      mainselectcarddisplay: false,
      mainpdfcarddisplay: false,
      mainlivingcarddisplay: true,
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: '',
        job: ''
      },
      curuser: {
        username: '',
        job: '',
        url: '',
        item: ''
      },
      curstream: '',
      vid: '248980',
      cururl: '',
      curvideo: true,
      theme1: 'light',
      toopen: true,
      openclose: 'ios-videocam-outline',
      opentext: '开播',
      note: {
        position: 'absolute',
        top: '0px',
        left: '0px',
        width: '100%',
        height: '100%',
        backgroundSize: '100% 100%',
        backgroundRepeat: 'no-repeat'
      },
      // 题目数据
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
        }
      ],
      curstu: 'zsh',
      curti: [
        {
          title: '1',
          ans: 'A'
        },
        {
          title: '2',
          ans: 'B'
        },
        {
          title: '3',
          ans: 'int main()'
        },
        {
          title: '4',
          ans: '#include<> \n using namespace std; int main(){ int c; cout<<c++<<endl; return 0}'
        }
      ],
      studentitems: ['zsh', 'adil', 'zhq', 'hyx', 'xcj'],
      ionselect: '111',
      curtitle: 'xjbx1',
      curans: ['1', '2', '3', '4'],
      curanswer: 'A',
      selectitems: [
        {
          title: 'xjbx1',
          ans: ['1', '2', '3', '4'],
          answer: 'A'
        },
        {
          title: 'xjbx2',
          ans: ['1', '2', '3', '4'],
          answer: 'A'
        },
        {
          title: 'xjbx3',
          ans: ['1', '2', '3', '4'],
          answer: 'A'
        },
        {
          title: 'xjbx4',
          ans: ['1', '2', '3', '4'],
          answer: 'A'
        }
      ],
      pdfitems: [
        {
          title: 'pdf1',
          url: '/static/pdf/1-1.pdf'
        },
        {
          title: 'pdf2',
          url: '/static/pdf/1-1.pdf'
        },
        {
          title: 'pdf3',
          url: '/static/pdf/1-1.pdf'
        },
        {
          title: 'pdf4',
          url: '/static/pdf/1-1.pdf'
        }
      ]
    }
  },
  mounted () {
    //    var timer = setTimeout(function(){
    //      doItPerSecond();
    //    },1000)
    //    var num = 0;
    //    function doItPerSecond() {
    //      //dosomething...
    //      var player = polyvObject('#player').livePlayer({
    //        'width':'100%',
    //        'height':600+'px',
    //        'uid':'7181857ac2',
    //        'vid':'248980'
    //      });
    //      num++;
    //      console.log(num);
    //    };
  },
  created () {
    this.cururl = this.$route.params.url
    //    const s = document.createElement('script');
    //    s.type = 'text/javascript';
    //    s.src = 'https://player.polyv.net/livescript/liveplayer.js';
    //    document.body.appendChild(s);
    this.showUserInfo()
    //    window.location.reload()
  },
  methods: {
    exportData (type) {
      if (type === 1) {
        this.$refs.table.exportCsv({
          filename: this.curstu + '数据统计'
        })
      }
    },
    getstudents () {
      console.log('1321312')
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      axios.post('/api/user/getstudents', data).then((resp) => {
        this.studentitems = resp.studentitems
      })
    },
    showstudentti (item) {
      console.log('1321312')
      this.curstu = item
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = this.curstu
      axios.post('/api/user/getstudentsti', data).then((resp) => {
        this.curti = resp.curti
      })
      this.modal3 = true
    },

    teatext () {
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      axios.post('/api/resourse/getpdfs', data).then((resp) => {
        this.pdfitems = resp.pdfitems
      }
      )

      this.modal1 = true
    },

    // Yuxuan's Methods Starts Here
    addPDF () {
      // send pdf to backend
    },

    handleReset (name) {
      this.$refs[name].resetFields()
    },
    handleAdd () {
      this.index++
      this.sub_multi.optionList.push({
        value: '',
        index: this.index,
        status: 1
      })
    },

    teaselect () {
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      axios.post('/api/resourse/getselects', data).then((resp) => {
        this.selectitems = resp.selectitems
      }
      )

      this.modal2 = true
    },
    handleRemove (index) {
      this.sub_multi.optionList[index].status = 0
    },
    addMulti () {
      // send sub_multi should be set by now
      // need to get url but I am waiting for hanky
      /*
      axios.post('/api/resourse/add_multiple', this.sub_multi).then((resp) => {
        this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 维护选择题列表,此处尚无
          window.location.reload()
          // 如果失败
        } else {
          this.$Message.error('添加选择题失败')
        }
      })
      */
    },
    addCode () {
      // sub_code should be set by now
      // post
      /*
      axios.post('/api/resourse/add_code', this.sub_code).then((resp) => {
        this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 应当要维护一下代码题的列表,此处未添加
          window.location.reload()
        // 如果失败
        } else {
          this.$Message.error('添加代码题失败')
        }
      })
      */
    },
    // Yuxuan's Methods Stops Here

    showpdf: function (ipdf) {
      console.log('1321312')
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示' + ipdf.title,
        onOk: () => {
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          data['item'] = ipdf.title
          axios.post('/api/user/showpdfs', data).then((resp) => {

          })
          this.littlelivingcarddisplay = true
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = true
          this.mainlivingcarddisplay = false
          this.liaotianshiheight = 330 + 'px'
          this.displayPdfurl = '/static/pdfjs/web/viewer.html?file=' + ipdf.url
          this.curvideo = false
          this.modal1 = false
          console.log('1321312')
          if (!this.toopen) {
            var streamer = new RtmpStreamer(document.getElementById('rtmp-streamer'))
            var streamer2 = new RtmpStreamer(document.getElementById('rtmp-streamer2'))
            //streamer2.setScreenPosition(-100, 0)
           // streamer2.setScreenSize(700, 380)
            console.log('1321312')
            streamer.disconnect()
            streamer2.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
          }
          console.log('1321312')
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    showselect: function (iselect) {
      console.log('1321312')
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示: \n ' + iselect.title,
        onOk: () => {
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          data['item'] = iselect.title
          axios.post('/api/user/showselect', data).then((resp) => {

          })
          this.littlelivingcarddisplay = true
          this.mainselectcarddisplay = true
          this.mainpdfcarddisplay = false
          this.mainlivingcarddisplay = false
          this.liaotianshiheight = 330 + 'px'
          this.curvideo = false
          if (!this.toopen) {
            var streamer = new RtmpStreamer(document.getElementById('rtmp-streamer'))
            var streamer2 = new RtmpStreamer(document.getElementById('rtmp-streamer2'))
            streamer2.setScreenPosition(-100, 0)
            streamer2.setScreenSize(700, 380)
            streamer2.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
            streamer.disconnect()
          }

          this.curtitle = iselect.title
          this.curans = iselect.ans
          this.curanswer = iselect.answer
          this.modal2 = false
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    closetext () {
      this.$Modal.confirm({
        title: '提示',
        content: '确认退出教学资源',
        onOk: () => {
          console.log('1321312')
          this.littlelivingcarddisplay = false
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = false
          this.mainlivingcarddisplay = true
          this.liaotianshiheight = 60 + 'px'
          this.curvideo = true

          if (!this.toopen) {
            setSWFIsReady()
            var streamer = new RtmpStreamer(document.getElementById('rtmp-streamer'))
            var streamer2 = new RtmpStreamer(document.getElementById('rtmp-streamer2'))
            streamer.setScreenPosition(-100, 0)
            streamer.setScreenSize(700, 380)
            streamer.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
            streamer2.disconnect()
          }
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    showUserInfo () {
      console.log('1234567')
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      this.userInfo['job'] = this.$cookies.get('user').job
    },
    teaopenclose () {
      if (this.toopen) {
        this.$Modal.confirm({
          title: '提示',
          content: '是否确认开播',
          onOk: () => {
            console.log('sadasdsad')
            this.toopen = false
            this.opentext = '关播'
            this.openclose = 'ios-power'
            this.getstudents()
            const data = this.curuser
            data['username'] = this.userInfo['username']
            data['job'] = this.userInfo['job']
            data['url'] = this.cururl
            axios.post('/api/user/openliving', data).then((resp) => {
              this.streamername = resp.streamername
            })
            if (this.curvideo) {
              setSWFIsReady()
               var streamer000 = new RtmpStreamer(document.getElementById('rtmp-streamer'))
               var streamer222 = new RtmpStreamer(document.getElementById('rtmp-streamer2'))
              //streamer000 = document.getElementById('rtmp-streamer')
              //streamer222 = document.getElementById('rtmp-streamer2')

              //streamer.setScreenPosition(-100, 0)
              //streamer.setScreenSize(700, 380)
              streamer000.publish('rtmp://push-c1.videocc.net/recordf', '7181857ac220181025144543640')
              streamer222.disconnect()
            } else {
              setSWFIsReady()
              var streamer000 = new RtmpStreamer(document.getElementById('rtmp-streamer'))
              var streamer222 = new RtmpStreamer(document.getElementById('rtmp-streamer2'))
             // streamer2.setScreenPosition(-100, 0)
              //streamer2.setScreenSize(700, 380)
              streamer222.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
              streamer000.disconnect()
            }
          },
          onCancel: () => {
          }
        })
      } else {
        this.$Modal.confirm({
          title: '提示',
          content: '是否确认关播',
          onOk: () => {
            this.toopen = true
            this.opentext = '开播'
            this.openclose = 'ios-videocam-outline'
            window.location.reload()

            const data = this.curuser
            data['username'] = this.userInfo['username']
            data['job'] = this.userInfo['job']
            data['url'] = this.cururl
            axios.post('/api/user/closeliving', data).then((resp) => {
            })
          },
          onCancel: () => {

          }
        })
      }
    },

  }
}

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
    position:absolute;
    left: 0;
    top:60px;
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
    float: left;
  }
  .bottomveido{
    position:absolute;
    height: auto;
    top:660px;
    text-align: center;
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
