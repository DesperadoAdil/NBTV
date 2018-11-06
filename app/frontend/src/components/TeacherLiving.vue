<template>
  <div class="tealivingmain">

    <div  class="cardtea">
      <p slot="title" style="font-size: 20px">选项</p>
      <Menu name="0" style="width: 100%">
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
        <Submenu name="4" class="menuitentea"  >
          <template slot="title">
            <Icon type="ios-stats" />
            添加学生
          </template>
          <MenuItem name="4-1" class="menuitentea" >
            <a href="javascript:;" class="upf">xlsx添加学生
              <input type="file" name="fileinput" id="fileinput">
            </a>
            <Button type="primary" @click="subxlsx">submit</Button>

          </MenuItem>
          <MenuItem name="4-2" class="menuitentea" @click.native="addstua">用户名添加学生</MenuItem>
        </Submenu>
      </Menu>
      <Button class="btnopen" type="primary"  v-bind:icon="openclose"  @click="teaopenclose()">
        <span class="menuitentea">{{this.opentext}}</span>
      </Button>
      <Button type="primary" shape="circle" v-bind:icon="jinmai" @click="tojinmai"></Button>
      <Button type="primary" shape="circle" v-bind:icon="jinshipin" @click="tojinshipin()"></Button>
    </div>

    <!--上传-->
    <Modal v-model="modal_pdf" @on-ok="addPDF()" @on-cancel="modal_pdf = false">
      <p slot="header" style="font-size: 20px">
        <span>上传课件</span>
      </p>
      <Upload action="上传的地址" headers="设置上传的请求头部">
        <Button icon="ios-cloud-upload-outline">Upload files</Button>
      </Upload>
    </Modal>

    <!--设置选择题-->
    <Modal   v-model="modal_multi"    @on-ok="addMulti()"    @on-cancel="modal_multi = false">
      <p slot="header" style="font-size: 20px">
        <span>设置选择题</span>
      </p>
      <Form ref="multi" model="sub_multi" label-width="80" style="width: 300px">
        <FormItem label="Statement">
          <Input v-model="sub_multi.statement"></Input>
        </FormItem>
        <!-- 以下为可以实现选项的动态添加删除的代码  -->
        <FormItem
          v-for="(item, index) in multi_options"
          v-if="item.status"
          :key="index">
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
        <FormItem label="The Answer">
          <Input v-model="sub_multi.answer" placeholder="a number"></Input>
        </FormItem>
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

    <div  id="mainlivingcard" v-bind:class="classmain0 ? 'cardtealiving00' : 'cardtealittleliving00'" >
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <object >
        <embed id="rtmp-streamer1" src="/static/swfdir/RtmpStreamer.swf" bgcolor="#999999" quality="high"
               width="100%" :style="{height:videohei}"  allowScriptAccess="sameDomain" type="application/x-shockwave-flash"  allowfullscreen="true"></embed>
      </object>
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
    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->
    <Card id="chatingRoom">
      <div class="talk-contents">
        <div class="talk-inner">
          <div class="talk-nav">
            <div class="talk-title">
              {{username}}
            </div>
          </div>
          <div class="content">
            <div v-for="(msgObj, index) in CHAT.msgArr" :key="msgObj.msg">
              <div  class="talk-space self-talk"
                    v-if="CHAT.msgArr[index].fromUser !== userInfo.username && CHAT.msgArr[index].toUser === username">
                <div class="talk-content">
                  <div class="talk-self-name">{{ msgObj.fromUser }}</div>
                  <div class="talk-word talk-word-self">{{ msgObj.msg }}</div>
                </div>
              </div>
              <div v-else></div>
              <div  class="talk-space user-talk"
                    v-if="CHAT.msgArr[index].toUser === username && CHAT.msgArr[index].fromUser === userInfo.username">
                <div class="talk-content">
                  <div class="talk-user-name">{{ msgObj.fromUser }}</div>
                  <div class="talk-word talk-word-user">{{ msgObj.msg }}</div>
                </div>
              </div>
              <div v-else></div>
            </div>
          </div>
          <div class="talker">
            <Input class="talker-input" v-model="msg" type="textarea" :autosize="true" placeholder="Enter something..." />
            <Button class="talker-send" type="success">发送</Button>
          </div>
        </div>
      </div>
    </Card>
    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->
  </div>
</template>

<script>
import axios from 'axios'
import {setSWFIsReady} from '../../static/js/livingrtmp.js'
import {RtmpStreamer} from '../../static/js/livingrtmp.js'
import CHAT from '../client'
export default{
  name: 'load',
  data () {
    return {
      /**
       * 以下为聊天室使用，请勿改动
       */
      msg: '',
      CHAT,
      username: 'all',
      /**
       * 以上为聊天室使用，请勿改动
       */
      astu: '',
      jinmai: 'ios-mic',
      jinshipin: 'ios-eye',
      isjinmai: false,
      isjinshipin: false,
      videohei: 700 + 'px',
      classmain0: true,
      stream000: '',
      streamer: '',
      streamername: '7181857ac220181025144543640',
      modal_pdf: false,
      modal_multi: false,
      multi_options: [
        {
          value: '',
          index: 1,
          status: 1
        }
      ],
      multi_index: 1,
      sub_multi: {
        statement: '',
        optionList: [],
        answer: '',
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
          type: 'select',
          ans: 'A',
          standardans: ''
        },
        {
          title: '4',
          type: 'code',
          ans: '#include<> \n using namespace std; int main(){ int c; cout<<c++<<endl; return 0}',
          standardans: ''
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
        }

      ]
    }
  },
  mounted () {
    /**
     * 以下为聊天室使用，请勿改动
     */
    // CHAT.message(this.userInfo.username)
    /**
     * 以上为聊天室使用，请勿改动
     */
  },
  created () {
    this.cururl = this.$route.params.url
    console.log(this.cururl)
    this.showUserInfo()
    /**
     * 以下为聊天室使用，请勿改动
     */
    this.chatingRoomInit()
    /**
     * 以上为聊天室使用，请勿改动
     */
  },
  methods: {
    /**
     * 以下为聊天室使用，请勿改动
     */
    chatingRoomInit () {
      // CHAT.init(this.userInfo.username)
    },
    submit () {
      var date = new Date()
      var time = date.getHours() + ':' + date.getMinutes()
      var obj = {
        time: time,
        msg: this.msg,
        toUser: this.username,
        fromUser: this.userInfo.username
      }
      this.msg = ''
      // CHAT.submit(obj)
    },
    /**
     * 以上为聊天室使用，请勿改动
     */
    subxlsx () {
      console.log('dhasjkhda')
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = document.querySelector('input[type=file]').files[0]
      console.log(data['item'])
      axios.post('/api/classroom/xlsxaddstudents', data).then((resp) => {
        this.studentitems = resp.studentitems
      })
    },
    addstua () {
      console.log('dhasjkhda')
      this.$Modal.confirm({
        render: (h) => {
          return h('Input', {
            props: {
              id: 'passinput',
              autofocus: true,
              placeholder: 'Please enter the username of this student'
            },
            on: {
              input: (val) => {
                this.astu = val
              }
            }
          })
        },
        onOk: () => {
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          data['item'] = this.astu
          console.log('dhasjkhda')
          console.log(this.astu)
          axios.post('/api/user/aaddstudents', data).then((resp) => {
            this.studentitems = resp.studentitems
          })
        }
      })
    },
    exportData (type) {
      if (type === 1) {
        this.$refs.table.exportCsv({
          filename: this.curstu + '数据统计'
        })
      }
    },
    getstudents () {
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      axios.post('/api/classroom/getstudents', data).then((resp) => {
        this.studentitems = resp.studentitems
      })
    },
    showstudentti (item) {
      this.curstu = item
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = this.curstu
      axios.post('/api/classroom/getstudentsti', data).then((resp) => {
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
    addPDF () {
      // send pdf to backend
    },
    handleReset (name) {
      this.$refs[name].resetFields()
    },
    handleAdd () {
      this.index++
      this.multi_options.push({
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
      this.multi_options[index].status = 0
    },
    addMulti () {
      // send sub_multi should be set by now
      this.sub_multi.url = this.cururl
      // 将multi_option这个列表改成可发送的数组
      for (var i = 0; i < this.index; i++) {
        if (this.multi_options[i].status === 1) {
          this.sub_multi.optionList.push(this.multi_options[i].value)
        }
      }
      // post
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
    },
    addCode () {
      // sub_code should be set by now
      // post
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
    },
    // Yuxuan's Methods Stops Here

    showpdf: function (ipdf) {
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示' + ipdf.title,
        onOk: () => {
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          data['item'] = ipdf.title
          axios.post('/api/classroom/showpdfs', data).then((resp) => {

          })
          console.log('1321312')
          this.videohei = 260 + 'px'
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = true
          this.classmain0 = false
          console.log(this.classmain0)
          console.log(document.getElementById('rtmp-streamer1').class)
          this.liaotianshiheight = 350 + 'px'
          this.displayPdfurl = '/static/pdfjs/web/viewer.html?file=' + ipdf.url
          this.curvideo = false
          this.modal1 = false
          console.log('1321312')
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    showselect: function (iselect) {
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示: \n ' + iselect.title,
        onOk: () => {
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          data['item'] = iselect.title
          axios.post('/api/classroom/showselect', data).then((resp) => {

          })
          this.videohei = 260 + 'px'
          this.mainselectcarddisplay = true
          this.mainpdfcarddisplay = false
          this.classmain0 = false
          this.liaotianshiheight = 350 + 'px'
          this.curvideo = false
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
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = false
          this.classmain0 = true
          this.liaotianshiheight = 60 + 'px'
          this.videohei = 700 + 'px'
          this.curvideo = true
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          axios.post('/api/classroom/closepdfsec', data).then((resp) => {

          })
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    showUserInfo () {
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
            this.toopen = false
            this.opentext = '关播'
            this.openclose = 'ios-power'
            this.getstudents()
            const data = this.curuser
            data['username'] = this.userInfo['username']
            data['job'] = this.userInfo['job']
            data['url'] = this.cururl
            axios.post('/api/classroom/openliving', data).then((resp) => {
              this.streamername = resp.streamername
            })
            setSWFIsReady()
            this.streamer000 = new RtmpStreamer(document.getElementById('rtmp-streamer1'))
            this.streamer000.setScreenPosition(-100, 0)
            this.streamer000.setScreenSize(700, 380)
            this.streamer000.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
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
            axios.post('/api/classroom/closeliving', data).then((resp) => {
            })
          },
          onCancel: () => {

          }
        })
      }
    },
    tojinmai () {
      if (this.isjinmai) {
        this.jinmai = 'ios-mic'
        this.isjinmai = false
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setMicRate(0)
        this.streamer000.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
      } else {
        this.jinmai = 'ios-mic-off'
        this.isjinmai = true
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setMicRate(0)
        this.streamer000.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
      }
    },
    tojinshipin () {
      if (this.isjinshipin) {
        this.jinshipin = 'ios-eye'
        this.isjinshipin = false
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setCamFrameInterval(15)
        this.streamer000.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
      } else {
        this.jinshipin = 'ios-eye-off'
        this.isjinshipin = true
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setCamFrameInterval(100000)
        this.streamer000.publish('rtmp://push-c1.videocc.net/recordf', this.streamername)
      }
    }

  }
}

</script>
<style>
  /* 赵汉卿负责的聊天室部分，请勿修改 */
  #chatingRoom {
    position:absolute;
    left: 79%;
    width: 21%;
    top:60px;
    height: 90%;
  }
  .talk-contents {
    height: 100%;
    margin-left: 10px;
  }
  .talk-nav {
    background-color: #eee;
    margin-left: 10px;
    text-align: center;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    line-height: 30px;
  }
  .talk-title {
    position: relative;
    padding: 10px 0;
    margin: 0 19px;
    border-bottom: 1px solid #d6d6d6;
    background-color: #eee;
    z-index: 1024;
  }
  .content {
    background-color: #eee;
    position: absolute;
    bottom: 50px;
    padding: 0 19px;
    margin-left: 10px;
    top: 51px;
    right: 0;
    left: 0;
    overflow: scroll;
  }
  .talker {
    margin-left: 10px;
    padding-right: 19px;
    border-top: 1px solid #d6d6d6;
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
  }

  .talk-space {
    width: 100%;
    margin-bottom: 16px;
  }
  .talk-word {
    display: inline-block;
    position: relative;
    background: -webkit-linear-gradient(left top, rgba(246, 94, 84, 1), rgba(218, 43, 101, 1)); /* Safari 5.1 - 6.0 */
    color: #fff;
    max-width: 60%;
    min-height: 25px;
    line-height: 25px;
    margin: 0 1%;
    padding: 4px 12px 2px 11px;
    border-radius: 5px;
    font-size: 12px;
    word-break: break-all;
  }
  .talk-word-self {
    border-bottom-right-radius: 0;
    margin-right: 10px;
    text-align: left;
  }
  .talk-word-user {
    background: rgba(243, 243, 243, 1) none;
    color: rgba(0, 0, 0, 1);
    border-bottom-left-radius: 0;
    margin-left: 10px;
    text-align: right;
  }
  .self-talk {
    margin-top: 10px;
  }
  .talk-content {
    text-align: right;
    position: relative;
  }
  .user-talk {
    margin-top: 10px;
  }
  .talk-content {
    text-align: left;
    position: relative;
    margin-left: 0px;
  }
  /* 赵汉卿负责的聊天室部分，请勿修改 */
  .tealivingmain{
    width: 100%;
  }
  .cardtea{
    position:absolute;
    left: 0;
    top:60px;
    width: 18%;
  }
  .cardtealiving00{
    position:absolute;
    left: 19%;
    width: 59%;
    top:60px;
  }
  .cardtealittleliving00{
    position:absolute;
    left: 79%;
    width: 21%;
    top:60px;
  }

  .menuitentea{
    font-size: 20px;
  }
  .btnopen{
    padding-:5%;
    margin:5%;
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
    height: auto;
    text-align: center;
  }
  .cardtealivingselect{
    position:absolute;
    left: 19%;
    width: 59%;
    height: 800px;
    top:60px;
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
  .databutton{
    margin-top: 15px;
  }
  .upf {
    position: relative;
    display: inline-block;
    background: #D0EEFF;
    border: 1px solid #99D3F5;
    border-radius: 4px;
    padding: 4px 12px;
    overflow: hidden;
    color: #1E88C7;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
  }
  .upf input {
    position: absolute;
    font-size: 100px;
    right: 0;
    top: 0;
    opacity: 0;
  }
  .upf:hover {
    background: #AADFFD;
    border-color: #78C3F3;
    color: #004974;
    text-decoration: none;
  }
</style>
