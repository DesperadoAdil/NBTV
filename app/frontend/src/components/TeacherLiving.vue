<template>
  <div id="teacherLiving" class="tealivingmain">
    <div  class="cardtea">
      <!-- -----------侧边栏----------------- -->
      <Menu name="sidemenu" style="width: 100%">

        <!-- 资源 -->
        <Submenu name="post" class="menuitentea">
          <template slot="title" ><Icon type="ios-paper" />
            资源
          </template>
          <MenuItem @click.native="showPdfList()">PDF</MenuItem>
          <MenuItem @click.native="showMultiList()">Choice</MenuItem>
          <MenuItem @click.native="showCodeList()">Code</MenuItem>
        </Submenu>
        <!-- 资源 -->

        <!-- 添加 -->
        <Submenu name="add" class="menuitentea">
          <template slot="title" ><Icon type="ios-paper" />
            添加
          </template>
          <MenuItem @click.native="modal_pdf = true">PDF</MenuItem>
          <MenuItem @click.native="modal_multi = true">Choice</MenuItem>
          <MenuItem @click.native="modal_code = true">Code</MenuItem>
        </Submenu>
        <!-- 添加 -->

        <!-- 使用 -->
        <Submenu name="cancel" class="menuitentea">
          <template slot="title"><Icon type="ios-people" />
            使用
          </template>
          <MenuItem @click.native="closetext()">取消使用</MenuItem>
        </Submenu>
        <!-- 使用 -->

        <!-- 学生 -->
        <Submenu name="student" class="menuitentea"  >
          <template slot="title"><Icon type="ios-stats" />
            学生
          </template>
          <MenuItem @click.native="modal_student_xlsx = true">xlsx文档添加</MenuItem>
          <MenuItem @click.native="addStudent()">用户名添加</MenuItem>
        </Submenu>
        <!-- 学生 -->
      </Menu>
      <!-- -----------侧边栏----------------- -->

      <!-- 底部按钮：开播、关播、关麦 -->
      <Button class="btnopen" type="primary"  v-bind:icon="openclose"  @click="teaopenclose()">
        <span class="menuitentea">{{this.opentext}}</span>
      </Button>
      <Button type="primary" shape="circle" v-bind:icon="jinmai" @click="tojinmai"></Button>
      <Button type="primary" shape="circle" v-bind:icon="jinshipin" @click="tojinshipin()"></Button>
    </div>

    <!-------------Modal of the menus----------------->
    <!--PDFlist-->
    <Modal
      v-model="modal_pdflist" width="900"
      @on-ok="modal_pdflist = false" @on-cancel="modal_pdflist = false"
    >
      <Card>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_pdf">
          <div slot="left"  class="teacher-live-split-pane">
            <p>All</p>
            <br>
            <Table height="375" border :columns="pdfAll" :data="pdfAllList"></Table>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <p>This Classroom</p>
            <br>
            <Table height="375" border :columns="pdfThis" :data="pdfThisList"></Table>
          </div>
        </Split>
      </Card>
    </Modal>

    <!--multi_list-->
    <Modal
      v-model="modal_multilist" width="900"
      @on-ok="modal_multilist = false" @on-cancel="modal_multilist = false">
      <Card>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_multi">
          <div slot="left"  class="teacher-live-split-pane">
            <p>All</p>
            <br>
            <Table height="375" border :columns="multiAll" :data="multiAllList"></Table>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <p>This Classroom</p>
            <br>
            <Table height="375" border :columns="multiThis" :data="multiThisList"></Table>
          </div>
        </Split>
      </Card>
    </Modal>

    <!--code_list-->
    <Modal
      v-model="modal_codelist"
      @on-ok="modal_codelist = false"
      @on-cancel="modal_codelist = false"
      width="900"
    >
      <Card>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_code">
          <div slot="left"  class="teacher-live-split-pane">
            <p>All</p>
            <br>
            <Table height="375" border :columns="codeAll" :data="codeAllList"></Table>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <p>This Classroom</p>
            <br>
            <Table height="375" border :columns="codeThis" :data="codeThisList"></Table>
          </div>
        </Split>
      </Card>
    </Modal>

    <!--上传-->
    <Modal v-model="modal_pdf" @on-ok="addPDF()" @on-cancel="modal_pdf = false">
      <p slot="header" style="font-size: 20px">
        <span>上传课件</span>
      </p>
      <Form>
        <FormItem>
          <a href="javascript:;" class="upf">pdf upload
            <input type="file" name="pdfinput" id="pdfinput">
          </a>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="addPDF()">submit</Button>
        </FormItem>
      </Form>
    </Modal>

    <!--设置选择题-->
    <Modal   v-model="modal_multi"    @on-ok="addMulti()"    @on-cancel="modal_multi = false">
      <p slot="header" style="font-size: 20px">
        <span>设置选择题</span>
      </p>
      <Form ref="multi" model="sub_multi" label-width="80" style="width: 300px">
        <FormItem label="Statement">
          <Input type="textarea" v-model="sub_multi.statement" placeholder="Enter your Description"></Input>
        </FormItem>
        <!-- 以下为选项的动态添加删除  -->
        <FormItem
          v-for="(item, index) in multi_options"
          v-if="item.status"
          :key="index">
          <Row>
            <Col span="18">
              <Input type="text" placeholder="Enter Your Choice" v-model="multi_options[index].value"></Input>
            </Col>
            <Col span="4" offset="1">
              <Button @click="multi_delChoice(index)">Delete</Button>
            </Col>
          </Row>
        </FormItem>
        <FormItem>
          <Row>
            <Col span="12">
              <Button type="dashed" long @click="multi_addChoice()" icon="md-add">Add Choice</Button>
            </Col>
          </Row>
        </FormItem>
        <!-- 答案设置  -->
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
      <Form label-position="top">
        <FormItem label="Text">
          <!-- autosize="{minRows: 2,maxRows: 5}" may be used in input attribute-->
          <Input v-model="sub_code.statement"
                 type="textarea" rows="4"
                 placeholder="Enter Your Statement">
          </Input>
        </FormItem>
        <FormItem label="Language">
          <Input v-model="sub_code.language" placeholder="Set the language"></Input>
        </FormItem>
        <FormItem label="Example Code">
          <!-- autosize="{minRows: 2,maxRows: 5}" may be used in input attribute-->
          <template>
            <!-------------输入框的代码高亮还没好，现在仅能静态高亮------------>
            <prism-editor :code="sub_code.example" language="cpp"></prism-editor>
          </template>
        </FormItem>
      </Form>
    </Modal>

    <!--上传学生名单-->
    <Modal v-model="modal_student_xlsx" @on-ok="modal_student_xlsx = false" @on-cancel="modal_student_xlsx = false">
      <p slot="header" style="font-size: 20px">
        <span>上传学生名单</span>
      </p>
      <Form>
        <Poptip word-wrap width="200" trigger="hover" title="提示" content="格式要求：xlsx文件的单元格填写一个完整的用户名，否则无效。添加失败可以再次添加或者用户名添加">
          <FormItem>
            <a href="javascript:;" class="upf">
              添加xlsx
              <input type="file" name="xlsxinput" id="xlsxinput">
            </a>
          </FormItem>
        </Poptip>
        <FormItem>
          <Button @click="subxlsx()">submit</Button>
        </FormItem>
      </Form>
    </Modal>

    <!--view multi-->
    <Modal
      v-model="modal_viewmulti"
      @on-ok="modal_viewmulti = false"
      @on-cancel="modal_viewmulti = false"
      width="900">
      <Card>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_multicheck">
          <div slot="left"  class="teacher-live-split-pane">
            <div style="position:relative; height:400px; overflow:auto">
            <Form ref="multi" model="sub_multi" label-width="80" style="width: 300px">
              <FormItem label="Statement">
                {{sub_multi.statement}}
              </FormItem>
              <FormItem
                v-for="(item, index) in sub_multi.optionList"
                :key="index">
                {{String.fromCharCode(65+index)+" : "+item}}
              </FormItem>
              <!-- 答案设置  -->
              <FormItem label="The Answer">
                {{sub_multi.answer}}
              </FormItem>
            </Form>
            </div>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <Table height="420" stripe :columns="multiAnswer" :data="multiAnswerList"></Table>
          </div>
        </Split>
      </Card>
    </Modal>

    <!--view code-->
    <Modal
      v-model="modal_viewcode"
      @on-ok="modal_viewcode = false"
      @on-cancel="modal_viewcode = false"
      width="900"
    >
      <Card>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_codecheck">
          <div slot="left"  class="teacher-live-split-pane">
            <div style="position:relative; height:400px; overflow:auto">
              <Form label-position="top">
                <FormItem label="Text">
                  {{sub_code.statement}}
                </FormItem>
                <FormItem label="Language">
                  {{sub_code.language}}
                </FormItem>
                <FormItem label="Example Code">
                  <pre v-highlightjs="sub_code.example" height="100"><code class="cpp"></code></pre>
                </FormItem>
              </Form>
            </div>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <div slot="right"  class="teacher-live-split-pane">
              <Table height="400" stripe :columns="codeAnswer" :data="codeAnswerList"></Table>
            </div>
          </div>
        </Split>
      </Card>
    </Modal>

    <!---------main living 部分------------->
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

    <!---------main pdf 部分------------->
    <div id="mainpdfcard" class="cardtealivingpdf" :style="{display:mainpdfcarddisplay?'block':'none'}">
      <iframe id="displayPdfIframe" class="pdfframe" :src="displayPdfurl"/>
    </div>

    <!---------main 选择题 部分 在主界面显示选择题------------->
    <div id="mainselectcard" class="cardtealivingselect" :style="{display:mainselectcarddisplay?'block':'none'}">
      <p class="selecttitle00">{{curtitle}}</p>
      <!---------TODO: 不能只有四个选项------------->
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
    <div id="chatingRoom" :style="{top:chatingtop,height:chatinghei}">
      <div class="talk-contents">
        <div class="talk-inner">
          <div class="talk-nav">
            <div class="talk-title">
              <button @click="CHAT.socket.emit('refresh', {'url':cururl})">获取最新用户列表</button>
              <Dropdown @click.native="CHAT.list(userInfo.username, cururl)">
                <a href="javascript:void(0)">
                  聊天对象
                  <Icon type="ios-arrow-down"></Icon>
                </a>
                <DropdownMenu slot="list">
                  <DropdownItem v-for="student in CHAT.studentlist" @click.native="talkTo(student)">{{ student }}</DropdownItem>
                  <DropdownItem divided @click.native="talkTo('all')">all</DropdownItem>
                </DropdownMenu>
              </Dropdown>
              {{ username }}
            </div>
          </div>
          <div class="content">
            <div v-for="(msgObj, index) in CHAT.msgArr" :key="msgObj.msg">
              <div v-if="CHAT.msgArr[index].toUser === username && username !== userInfo.username">
                <div class="talk-space self-talk"
                     v-if="CHAT.msgArr[index].fromUser === userInfo.username">
                  <div class="talk-content">
                    <div class="talk-self-name">{{ msgObj.fromUser }}</div>
                    <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-self">{{ msgObj.msg }}</div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'audio'">
                      <audio :src="audioUrl(msgObj.msg)" controls></audio>
                    </div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'img'">
                      <img class="talk-image" :src="imageUrl(msgObj.msg)"/>
                    </div>
                    <div v-else></div>
                  </div>
                </div>
                <div class="talk-space user-talk" v-else>
                  <div class="talk-content">
                    <div class="talk-user-name">{{ msgObj.fromUser }}</div>
                    <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-user">{{ msgObj.msg }}</div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'audio'">
                      <audio :src="audioUrl(msgObj.msg)" controls></audio>
                    </div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'img'">
                      <img class="talk-image" :src="imageUrl(msgObj.msg)"/>
                    </div>
                    <div v-else></div>
                  </div>
                </div>
              </div>
              <div v-else-if="CHAT.msgArr[index].toUser === userInfo.username && username !== userInfo.username">
                <div  class="talk-space user-talk">
                  <div class="talk-content">
                    <div v-if="username === 'all'">
                      <div class="talk-user-name">[私信]：{{ msgObj.fromUser }}</div>
                    </div>
                    <div v-else-if="CHAT.msgArr[index].fromUser === username">
                      <div class="talk-user-name">{{ msgObj.fromUser }}</div>
                    </div>
                    <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-user">{{ msgObj.msg }}</div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'audio'">
                      <audio :src="audioUrl(msgObj.msg)" controls></audio>
                    </div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'img'">
                      <img class="talk-image" :src="imageUrl(msgObj.msg)"/>
                    </div>
                    <div v-else></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="talker">
            <Input v-if="msgType === 'text'" class="talker-input" v-model="msg" type="textarea" :autosize="true" placeholder="Enter something..." />
            <div v-if="msgType === 'audio'" class="recorder">
              <button @click="toggleRecorder()">录音</button>
              <button @click="stopRecorder">停止</button>
              <button
                class="record-audio"
                @click="removeRecord(idx)">删除</button>
              <div class="record-text">{{audio.duration}}</div>
            </div>
            <div v-if="msgType === 'img'" class="talker-image">已添加图片，按发送
            </div>
            <Button class="talker-send" type="success" @click="submit">发送</Button>
            <Button class="talker-send" @click="changeMsgType">{{ msgTypeInfo }}</Button>
            <a href="javascript:;" class=" upf talker-send" @click="chooseImg">图片
              <input type="file" name="fileinput" id="fileinput"/>
            </a>
          </div>
        </div>
      </div>
    </div>
    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->

  </div>
</template>

<script>
import axios from 'axios'
import {setSWFIsReady} from '../../static/js/livingrtmp.js'
import {RtmpStreamer} from '../../static/js/livingrtmp.js'
import CHAT from '../client'
import { convertTimeMMSS } from '../utils'
import Recorder from '../recorder'
import PrismEditor from 'vue-prism-editor'

export default{
  name: 'load',
  props: {
    micFailed: { type: Function },
    startRecord: { type: Function },
    stopRecord: { type: Function }
  },
  data () {
    return {
      /**
       * 以下为聊天室使用，请勿改动
       */

      chatingtop:60+'px',
      chatinghei:710+'px',
      msgTypeInfo: '语音',
      socket: null,
      msgType: 'text',
      talkType: 'broadcast',
      msg: '',
      CHAT,
      username: 'all',
      isUploading: false,
      recorder: new Recorder({
        afterStop: () => {
          this.audio = this.recorder.audio
          if (this.stopRecord) {
            this.stopRecord('stop record')
          }
        },
        attempts: this.attempts,
        time: this.time
      }),
      audio: {},
      selected: {},
      uploadStatus: null,
      uploaderOptions: {},
      /**
       * 以上为聊天室使用，请勿改动
       */

      // something to do with add student
      astu: '',
      // stream stuff
      jinmai: 'ios-mic',
      jinshipin: 'ios-eye',
      isjinmai: false,
      isjinshipin: false,
      videohei: 700 + 'px',
      classmain0: true,
      stream000: '',
      streamer: '',
      streamername: '7181857ac220181030221452650',

      // pdf, multiple and codes
      // pdf parameter
      split_pdf: 0.5,
      modal_pdflist: false,
      // framework to show pdf all
      pdfAll: [{title: 'Title', key: 'title'},
        {
          title: 'Action',
          key: 'action',
          fixed: 'right',
          width: 120,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.addPdfAll(params.index) }
                }
              }, 'Add'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delPdfAll(params.index) }
                }
              }, 'Del')])
          }
        }],
      pdfThis: [
        {title: 'Title', key: 'title'},
        {
          title: 'Action',
          key: 'action',
          fixed: 'right',
          width: 120,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.usePdf(params.index) }
                }
              }, 'Use'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delPdfClass(params.index) }
                }
              }, 'Del')])
          }
        }],
      pdfThisList: [
        {
          title: 'pdf1',
          url: '/static/pdf/1-1.pdf'
        },
        {
          title: 'pdf2',
          url: '/static/pdf/1-1.pdf'
        }],
      pdfAllList: [{title: 'Slide01', url: 'hide/slide01'}],
      // MULTI
      // MULTIPLE CHOICE PARAMETER
      split_multi: 0.5,
      split_multicheck: 0.5,
      modal_multilist: false,
      // FRAMEWORK TO SHOW MULTI
      multiAll: [{title: 'Description', key: 'statement'},
        {
          title: 'Action',
          key: 'action',
          fixed: 'right',
          width: 120,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.addMultiAll(params.index) }
                }
              }, 'Add'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delMultiAll(params.index) }
                }
              }, 'Del')])
          }
        }],
      multiThis: [{title: 'Description', key: 'statement'},
        {
          title: 'Action',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.useMulti(params.index) }
                }
              }, 'Use'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.viewMulti(params.index) }
                }
              }, 'View'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delMultiClass(params.index) }
                }
              }, 'Del')])
          }
        }],
      // MULTI LIST
      multiAllList: [
        {
          uniqueId: '',
          statement: 'Among the following people, who is the most gay one?',
          optionList: ['ADIL', 'XCJ', 'HYX', 'ZHQ ♂ ZSH'],
          answer: 'A'
        },
        {
          uniqueId: '',
          statement: 'What do you answer for "I don\'t know"?',
          optionList: ['something', 'somewhere', 'somehow', 'somewhat'],
          answer: 'A'
        }
      ],
      multiThisList: [{
        uniqueId: '',
        statement: 'Among the following people, who is the most gay one?',
        optionList: ['ADIL', 'XCJ', 'HYX', 'ZHQ ♂ ZSH'],
        answer: 'A'
      }, {
        uniqueId: '',
        statement: 'What do you answer for "I don\'t know"?',
        optionList: ['something', 'somewhere', 'somehow', 'somewhat'],
        answer: 'A'
      }],
      // MULTI STUDENT ANSWER LIST
      multiAnswer: [{title: 'student', key: 'student'}, {title: 'answer', key: 'answer'}],
      multiAnswerList: [{student: 'xcj', answer: 'A'}, {student: 'adil', answer: 'not answered'}],
      codeAnswer: [{title: 'student', key: 'student'}, {title: 'answer', key: 'answer'}],
      codeAnswerList: [{student: 'xcj', answer: '#include<iostream>'}, {student: 'adil', answer: 'not answered'}],
      // CODE
      // CODE PARAMETER
      split_code: 0.5,
      modal_codelist: false,
      split_codecheck: 0.5,
      modal_viewmulti: false,
      modal_viewcode: false,
      // FRAMEWORK TO SHOW CODE LIST
      codeAll: [
        {title: 'Title', key: 'title'},
        {
          title: 'Action',
          key: 'action',
          fixed: 'right',
          width: 120,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.addCodeAll(params.index) }
                }
              }, 'Add'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delCodeAll(params.index) }
                }
              }, 'Del')])
          }
        }],
      codeThis: [{title: 'Title', key: 'title'},
        {
          title: 'Action',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.useCode(params.index) }
                }
              }, 'Use'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.viewCode(params.index) }
                }
              }, 'View'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delCodeClass(params.index) }
                }
              }, 'Del')])
          }
        }],
      // CODE LIST
      codeAllList: [
        {
          title: 'Eight Queens'
        },
        {
          title: 'B-Tree'
        }
      ],
      codeThisList: [{
        title: 'B-Tree'
      }],

      // ADD PDF/MULTI/CODE MODALS
      // PDF
      modal_pdf: false,
      // MULTI
      modal_multi: false,
      multi_options: [
        {
          value: '',
          index: 1,
          status: 1
        }
      ], //
      multi_index: 1,
      sub_multi: {
        uniqueId: '',
        statement: 'We Are Going to test it.',
        optionList: ['something', 'somewhere', 'someplace', 'sometime'],
        answer: 'A',
        username: ''
      },
      // CODE
      modal_code: false,
      sub_code: {
        uniqueId: '',
        username: '',
        statement: 'Print something in the console',
        language: 'cpp',
        example: '#include<iostream>\nusing namespace std;\nint main(){\n  int c;\n  cout<<c++<<endl;\n  return 0\n}'
      },

      // ADD STUDENT LIST
      modal_student_xlsx: false,
      // Shihang'S PARAMETER
      displayPdfurl: '',
      littlelivingcarddisplay: false,
      mainselectcarddisplay: false,
      mainpdfcarddisplay: false,
      mainlivingcarddisplay: true,

      // COMMON INFO
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
      // STREAM PARAMETERS
      curstream: '',
      vid: '248980',
      cururl: '',
      curvideo: true,
      toopen: true,
      openclose: 'ios-videocam-outline',
      opentext: '开播',

      // SHIHANG'S STUFF
      curstu: 'zsh',
      // SEEM TO BE ABLE TO SHOW STUDENT CODE, SAVE FOR NOW
      curti: [
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
      curanswer: 'A'
    }
  },
  mounted () {
    /**
     * 以下为聊天室使用，请勿改动
     */
    CHAT.message(this.userInfo.username)
    /**
     * 以上为聊天室使用，请勿改动
     */
  },
  created () {
    this.cururl = this.$route.params.url
    // console.log(this.cururl)
    this.showUserInfo()
    /**
     * 以下为聊天室使用，请勿改动
     */
    this.chatingRoomInit()
    /**
     * 以上为聊天室使用，请勿改动
     */
  },
  computed: {
    isPause () {
      return this.recorder.isPause
    },
    isRecording () {
      return this.recorder.isRecording
    },
    message () {
      return this.uploadStatus === 'success' ? this.successfulUploadMsg : this.failedUploadMsg
    },
    recordedTime () {
      return convertTimeMMSS(this.recorder.duration)
    },
    volume () {
      return parseFloat(this.recorder.volume)
    }
  },
  components: {
    PrismEditor
  },
  methods: {
    // ADD METHODS
    // PDF
    addPDF () {
      // send pdf to backend
      let formData = new FormData()
      formData.append('username', this.userInfo['username'])
      formData.append('file', document.querySelector('input[id=pdfinput]').files[0])
      // console.log(document.querySelector('input[id=pdfinput]').files[0])
      let options = {
        url: '/api/resource/add_pdf',
        data: formData,
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios(options).then((resp) => {
        // console.log('addPDF success')
      })
      // IF SUCCESS, BACK END: ADD TO TEACHER & ROOM
      // FRONTEND: JUST SHOW
    },
    // MULTI
    multi_addChoice () {
      this.multi_index++
      this.multi_options.push({
        value: '',
        index: this.multi_index,
        status: 1
      })
    },
    multi_delChoice (i) {
      this.multi_options[i].status = 0
    },
    addMulti () {
      // send sub_multi should be set by now
      this.sub_multi.username = this.userInfo.username
      // 将multi_option这个列表改成可发送的数组
      for (var i = 0; i < this.multi_index; i++) {
        if (this.multi_options[i].status === 1) {
          this.sub_multi.optionList.push(this.multi_options[i].value)
        }
      }
      // test
      // console.log(this.sub_multi.statement)
      // console.log(this.sub_multi.optionList)
      // post
      axios.post('/api/resource/add_multiple', this.sub_multi).then((resp) => {
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
    // CODE
    addCode () {
      // sub_code should be set by now
      this.sub_code.username = this.userInfo.username
      // test
      console.log(this.sub_code.username)
      console.log(this.sub_code.language)
      console.log(this.sub_code.statement)
      // post
      axios.post('/api/resource/add_code', this.sub_code).then((resp) => {
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

    // LIST METHODS
    // PDF
    // SHOW LIST
    showPdfList () {
      this.modal_pdflist = true
      // get the input
      let pdfListInput = {username: '', url: ''}
      pdfListInput.username = this.userInfo.username
      pdfListInput.url = this.cururl
      // post
      axios.post('/api/resource/getpdfs', pdfListInput).then((resp) => {
        // resp.data 即是那个列表
        this.pdfAllList = resp.data.pdfAllList
        this.pdfThisList = resp.data.pdfThisList
      })
    },
    // ADD PDF TO CLASS
    addPdfAll (index) {
      // iPdf shape as : {title: 'Slide01', url: 'hide/slide01'}
      let iPdf = this.pdfAllList[index]
      let input = {username: '', url: '', pdf: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.pdf = iPdf
      // post
      axios.post('/api/resource/pdf_addclass', input).then((resp) => {
        // 接收返回的pdfThisList
        this.pdfThisList = resp.data.pdfThisList
      })
    },
    // DEL PDF FROM TEACHER
    delPdfAll (index) {
      let iPdf = this.pdfAllList[index]
      // input
      let delPdfAllInput = {username: '', url: '', pdf: {}}
      delPdfAllInput.username = this.userInfo.username
      delPdfAllInput.url = this.cururl
      delPdfAllInput.pdf = iPdf
      // post
      axios.post('/api/resource/delete_pdf', delPdfAllInput).then((resp) => {
        this.pdfAllList = resp.data.pdfAllList
        this.pdfThisList = resp.data.pdfThisList
      })
    },
    // USE IT TODO
    usePdf (index) {
      let ipdf = this.pdfThisList[index]
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

          let date = new Date()
          let time = date.getHours() + ':' + date.getMinutes()
          let obj = {
            type: 'pdf',
            msgType: 'pdf',
            url: this.cururl,
            time: time,
            msg: ipdf.url,
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)

          console.log('1321312')
          this.chatingtop = 330 + 'px'
          this.chatinghei = 440 + 'px'
          this.videohei = 260 + 'px'
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = true
          this.classmain0 = false
          console.log(this.classmain0)
          console.log(document.getElementById('rtmp-streamer1').class)
          // this.liaotianshiheight = 350 + 'px'
          this.displayPdfurl = '/static/pdfjs/web/viewer.html?file=' + ipdf.url
          this.curvideo = false
          this.modal_pdflist = false
          console.log('1321312')
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    // DEL PDF FROM CLASS
    delPdfClass (index) {
      let iPdf = this.pdfThisList[index]
      // get input
      let input = {username: '', url: '', pdf: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.pdf = iPdf
      // post
      axios.post('/api/resource/pdf_delclass', input).then((resp) => {
        this.pdfThisList = resp.data.pdfThisList
      })
    },

    // MULTI
    // SHOW LIST
    showMultiList () {
      this.modal_multilist = true
      // get input
      let input = {username: '', url: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      // post
      axios.post('/api/resource/getmultiples', input).then((resp) => {
        // resp.data 即是那个列表
        this.multiAllList = resp.data.multiAllList
        this.multiThisList = resp.data.multiThisList
      })
    },
    // ADD MULTI TO CLASS
    addMultiAll (index) {
      let iMulti = this.multiAllList[index]
      let input = {username: '', url: '', multi: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.multi = iMulti
      // post
      axios.post('/api/resource/multi_addclass', input).then((resp) => {
        // 接收返回的multiThisList
        this.multiThisList = resp.data.multiThisList
      })
    },
    // DEL PDF FROM TEACHER
    delMultiAll (index) {
      let iMulti = this.multiAllList[index]
      // input
      let input = {username: '', url: '', multi: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.multi = iMulti
      // post
      axios.post('/api/resource/delete_mutiple', input).then((resp) => {
        this.multiAllList = resp.data.multiAllList
        this.multiThisList = resp.data.multiThisList
      })
    },
    // USE IT TODO
    useMulti (index) {
      let iselect = this.multiThisList[index]
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

          var date = new Date()
          var time = date.getHours() + ':' + date.getMinutes()
          var obj = {
            type: 'select',
            msgType: 'select',
            url: this.cururl,
            time: time,
            msg: iselect,
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)

          this.videohei = 260 + 'px'
          this.chatingtop = 330 + 'px'
          this.chatinghei = 440 + 'px'
          this.mainselectcarddisplay = true
          this.mainpdfcarddisplay = false
          this.classmain0 = false
          this.curvideo = false
          this.curtitle = iselect.title
          this.curans = iselect.ans
          this.curanswer = iselect.answer
          this.modal_multilist = false
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    // VIEW
    viewMulti (index) {
      let iMulti = this.multiThisList[index]
      // input
      let input = {username: '', url: '', multi: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.multi = iMulti
      // post
      axios.post('/api/resource/multi_viewclass', input).then((resp) => {
        this.multiAnswerList = resp.data.multiAnswerList
      })
      this.sub_multi = iMulti
      this.modal_viewmulti = true
    },
    // DEL MULTI FROM CLASS
    delMultiClass (index) {
      let iMulti = this.multiThisList[index]
      // input
      let input = {username: '', url: '', multi: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.multi = iMulti
      // post
      axios.post('/api/resource/multi_delclass', input).then((resp) => {
        this.multiThisList = resp.data.multiThisList
      })
    },

    // CODE
    // SHOW LIST
    showCodeList () {
      this.modal_codelist = true
      // get input
      let input = {username: '', url: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      // post
      axios.post('/api/resource/getcodes', input).then((resp) => {
        // resp.data 即是那个列表
        this.codeAllList = resp.data.codeAllList
        this.codeThisList = resp.data.codeThisList
      })
    },
    // ADD CODE TO CLASS
    addCodeAll (index) {
      let iCode = this.codeAllList[index]
      let input = {username: '', url: '', code: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.code = iCode
      // post
      axios.post('/api/resource/code_addclass', input).then((resp) => {
        // 接收返回的codeThisList
        this.codeThisList = resp.data.codeThisList
      })
    },
    // DEL CODE FROM TEACHER
    delCodeAll (index) {
      let iCode = this.codeAllList[index]
      // input
      let input = {username: '', url: '', code: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.code = iCode
      // post
      axios.post('/api/resource/delete_code', input).then((resp) => {
        this.codeAllList = resp.data.codeAllList
        this.codeThisList = resp.data.codeThisList
      })
    },
    // USE IT TODO
    useCode (index) {
      let iCode = this.codeThisList[index]
      iCode.statement = ''
      // to be implemented
      let date = new Date()
      let time = date.getHours() + ':' + date.getMinutes()
      let obj = {
        type: 'code',
        msgType: 'code',
        url: this.cururl,
        time: time,
        msg: 'code',
        toUser: 'stu',
        fromUser: this.userInfo.username
      }
      CHAT.submit(obj)
    },
    // VIEW
    viewCode (index) {
      let iCode = this.codeThisList[index]
      // input
      let input = {username: '', url: '', code: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.code = iCode
      // post
      axios.post('/api/resource/code_viewclass', input).then((resp) => {
        this.codeAnswerList = resp.data.codeAnswerList
      })
      this.modal_viewcode = true
    },
    // DEL CODE FROM CLASS
    delCodeClass (index) {
      let iCode = this.codeThisList[index]
      // input
      let input = {username: '', url: '', code: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.code = iCode
      // post
      axios.post('/api/resource/code_delclass', input).then((resp) => {
        this.codeThisList = resp.data.codeThisList
      })
    },

    // Yuxuan's Methods Stops Here

    /**
     * 以下为聊天室使用，请勿改动
     */
    chatingRoomInit () {
      this.socket = CHAT.init(this.userInfo.username, this.cururl)
    },
    submit () {
      var date = new Date()
      var time = date.getHours() + ':' + date.getMinutes()
      var obj = {}
      if (this.msgType === 'text') {
        if (this.msg === '') return
        obj = {
          type: this.talkType,
          msgType: 'text',
          url: this.cururl,
          time: time,
          msg: this.msg,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        this.msg = ''
        CHAT.submit(obj)
      } else if (this.msgType === 'audio') {
        obj = {
          type: this.talkType,
          msgType: 'audio',
          url: this.cururl,
          time: time,
          msg: this.audio,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        console.log(obj)
        CHAT.submit(obj)
      } else if (this.msgType === 'img') {
        var blob = new Blob([document.querySelector('input[type=file]').files[0]], { type: 'image/png' })
        obj = {
          type: this.talkType,
          msgType: 'img',
          url: this.cururl,
          time: time,
          msg: blob,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        console.log(obj)
        CHAT.submit(obj)
        this.msgType = 'text'
      }
    },
    chooseImg () {
      this.msgType = 'img'
    },
    changeMsgType () {
      if (this.msgType === 'text') {
        this.msgTypeInfo = '语音'
        this.msgType = 'audio'
      } else if (this.msgType === 'audio') {
        this.msgTypeInfo = '文字'
        this.msgType = 'text'
      }
    },
    toggleRecorder () {
      if (!this.isRecording || (this.isRecording && this.isPause)) {
        this.recorder.start()
        if (this.startRecord) {
          this.startRecord('start record')
        }
      } else {
        this.recorder.pause()
        if (this.startRecord) {
          this.startRecord('pause record')
        }
      }
    },
    stopRecorder () {
      if (!this.isRecording) {
        return
      }
      this.recorder.stop()
    },
    audioUrl (obj) {
      var url = window.URL.createObjectURL(new Blob([obj.blob], { type: 'audio/wav' }))
      return url
    },
    imageUrl (obj) {
      var url = window.URL.createObjectURL(new Blob([obj], { type: 'image/png' }))
      return url
    },
    talkTo (p) {
      if (p === this.userInfo.username) return
      this.username = p
      if (p !== 'all') {
        this.msg = ''
        this.talkType = 'whisper'
      } else {
        this.msg = ''
        this.talkType = 'broadcast'
      }
    },
    /**
     * 以上为聊天室使用，请勿改动
     */
    subxlsx () {
      console.log('dhasjkhda')
      /* const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = document.querySelector('input[type=file]').files[0]
      console.log(data['item']) */
      var formData = new FormData()
      formData.append('url', this.cururl)
      formData.append('item', document.querySelector('input[id=xlsxinput]').files[0])
      var options = {
        url: '/api/classroom/xlsxaddstudents',
        data: formData,
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios(options).then((resp) => {
        this.studentitems = resp.studentitems
      })
    },
    addStudent () {
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
          axios.post('/api/classroom/aaddstudents', data).then((resp) => {
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
    // 用于显示学生的代码
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
    },
    closetext () {
      this.$Modal.confirm({
        title: '提示',
        content: '确认退出教学资源',
        onOk: () => {
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = false
          this.classmain0 = true
          this.videohei = 700 + 'px'
          this.chatingtop=60+'px'
          this.chatinghei=710+'px'
          this.curvideo = true
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          axios.post('/api/classroom/closepdfsec', data).then((resp) => {

          })

          var date = new Date()
          var time = date.getHours() + ':' + date.getMinutes()
          var obj = {
            type: 'close',
            msgType: 'close',
            url: this.cururl,
            time: time,
            msg: 'close',
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)
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
              this.streamername = resp.data.streamername
              console.log(resp.data.streamername)
              console.log(this.streamername)
              console.log(this.streamername)
              setSWFIsReady()
              this.streamer000 = document.getElementById('rtmp-streamer1')
              this.streamer000.setScreenPosition(-100, 0)
              this.streamer000.setScreenSize(700, 380)
              this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
            })
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
        this.streamer000.setMicRate(10000000000)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      } else {
        this.jinmai = 'ios-mic-off'
        this.isjinmai = true
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setMicRate(0)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
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
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      } else {
        this.jinshipin = 'ios-eye-off'
        this.isjinshipin = true
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setCamFrameInterval(1000000000)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      }
    }

  }
}

</script>
<style>
  #teacherLiving {
    padding: 0 5%;
  }
  /* 赵汉卿负责的聊天室部分，请勿修改 */
  #chatingRoom {
    position:absolute;
    left: 79%;
    width: 21%;

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
  .talk-word-user {
    border-bottom-right-radius: 0;
    margin-right: 10px;
    text-align: left;
  }
  .talk-word-self {
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
  .talk-image {
    width: 100px;
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
    font-size: 18px;
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
  .teacher-live-split{
    height: 430px;
    border: 1px solid #dcdee2;
  }
  .teacher-live-split-pane{
    padding: 10px;
  }
</style>
