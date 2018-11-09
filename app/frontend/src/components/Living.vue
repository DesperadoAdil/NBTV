<template>
  <div class="tealivingmain">



    <div v-if="CHAT.frametype === 'close'" id="mainlivingcard" class="cardtealiving11">
      <!--<div id="mainlivingcard" class="cardtealiving11" :style="{display:mainlivingcarddisplay?'block':'none'}">-->
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <div id='player'></div>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </div>

    <div v-if="CHAT.frametype !== 'close'" id="littlelivingcard" class="cardtealittleliving11" >
      <!--<div id="littlelivingcard" class="cardtealittleliving11" :style="{display:littlelivingcarddisplay?'block':'none'}">-->
      <div class="topveido">
        <h3>教室信息显示部分（待修改）</h3>
      </div>
      <div id='player2'></div>
      <div class="bottomveido">
        <h3>礼物等其他显示部分（待修改）</h3>
      </div>
    </div>

    <!--<div id="mainpdfcard" class="cardtealivingpdf11" :style="{display:mainpdfcarddisplay?'block':'none'}">-->
    <div v-if="CHAT.frametype === 'pdf'" id="mainpdfcard" class="cardtealivingpdf11" >
      <iframe id="displayPdfIframe" class="pdfframe" :src="CHAT.pdfurl"/>
    </div>

    <!--<div id="maincodecard" class="cardtealivingcdode00" :style="{display:maincodecarddisplay?'block':'none'}">-->
    <div v-if="CHAT.frametype === 'code'" id="maincodecard" class="cardtealivingcdode00" >
      <h>编程题</h>
    </div>

    <!--<div id="mainselectcard" class="cardtealivingselect00" :style="{display:mainselectcarddisplay?'block':'none'}">-->
    <div v-if="CHAT.frametype === 'select'" id="mainselectcard" class="cardtealivingselect00" >
      <p class="selecttitle00">{{CHAT.selectall.title}}</p>
      <RadioGroup  class="radiotea" v-model="stuans" vertical>
        <Radio label="A" style="font-size: 15px">
          <span>A、{{CHAT.selectall.ans[0]}}</span>
        </Radio>
        <Radio label="B" style="font-size: 15px">
          <span>B、{{CHAT.selectall.ans[1]}}</span>
        </Radio>
        <Radio label="C" style="font-size: 15px">
          <span>C、{{CHAT.selectall.ans[2]}}</span>
        </Radio>
        <Radio label="D" style="font-size: 15px">
          <span>D、{{CHAT.selectall.ans[3]}}</span>
        </Radio>
      </RadioGroup>
      <Button class="selectsubmit00" type="primary" @click="selectsubmit">提交答案: {{stuans}}</Button>
    </div>

    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->
    <div id="chatingRoom2" :style="{height:CHAT.frametype === 'close'? 650+'px':350+'px',top:CHAT.frametype === 'close'? 150+'px':450+'px'}">
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
import CHAT from '../client'
import { convertTimeMMSS } from '../utils'
import Recorder from '../recorder'
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
      chathei: 600+'px',
        chattop:150+'px',
      socket: null,
      msgType: 'text',
      msgTypeInfo: '文字',
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
      stuans:'',
      maincodecarddisplay: false,
      curpdfurl: '/static/pdf/1-1.pdf',
      videohei0: 600 + 'px',
      classmain11: true,
      curvid: '250810',
      cururl: '',
      displayPdfurl0: '',
      liaotianshiheight: 150 + 'px',
      littlelivingcarddisplay: false,
      mainselectcarddisplay: false,
      mainpdfcarddisplay: false,
      mainlivingcarddisplay: true,
      curtitle: 'xjbx1',
      curans: ['1', '2', '3', '4'],
      curanswer: 'A',
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
      }
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
//    var xxx = this.videohei0
//    console.log(xxx)
//    var yyy = this.curvid
//     console.log(yyy)
//    var timer = setTimeout(function () {
//      doItPerSecond()
//    }, 1000)
//    var num = 0
//    function doItPerSecond () {
//      var player = polyvObject('#player').livePlayer({
//        'width': '100%',
//        'height': 600 + 'px',
//        'uid': '7181857ac2',
//        'vid': '250810'
//      })
//      var player = polyvObject('#player2').livePlayer({
//        'width': '100%',
//        'height': 200 + 'px',
//        'uid': '7181857ac2',
//        'vid': '250810'
//      })
//      num++
//      console.log(num)
//    };
  },
  created: function () {
    const s = document.createElement('script')
    s.type = 'text/javascript'
    s.src = 'https://player.polyv.net/livescript/liveplayer.js'
    document.body.appendChild(s)
    this.showUserInfo()
    this.cururl = this.$route.params.url
    console.log(this.cururl)
    const data = this.curuser
    data['username'] = this.userInfo['username']
    data['job'] = this.userInfo['job']
    data['url'] = this.cururl
    axios.post('/api/classroom_stu/urlgetvid', data).then((resp) => {
      this.curvid = resp.data.vid
      console.log("vid:"+resp.data.vid)
      console.log("vid:"+this.curvid)
      var player = polyvObject('#player').livePlayer({
        'width': '100%',
        'height': 600 + 'px',
        'uid': '7181857ac2',
        'vid': this.curvid
      })
      var player = polyvObject('#player2').livePlayer({
        'width': '100%',
        'height': 200 + 'px',
        'uid': '7181857ac2',
        'vid': this.curvid
      })
    })

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
  methods: {
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
      }
      else {
        this.msg = ''
        this.talkType = 'broadcast'
      }
    },
    /**
     * 以上为聊天室使用，请勿改动
     */
    showUserInfo () {
      console.log('1234567')
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      this.userInfo['job'] = this.$cookies.get('user').job
    },
    selectsubmit(){
      console.log("dasdas")
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = this.stuans
      axios.post('/api/classroom/selectsubmit', data).then((resp) => {

      })
    },
  }

}
</script>
<style>
  /* 赵汉卿负责的聊天室部分，请勿修改 */
  #chatingRoom2 {
    position:absolute;
    left: 70%;
    width: 20%;
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
  /* 赵汉卿负责的聊天室部分，请勿修改 */
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

  }
  .cardtealivingcdode00{
    position:absolute;
    left: 10%;
    width: 59%;
    height: 800px;
    top:150px;

  }

  .selecttitle00{
    padding-top: 3%;
    position:relative;
    left:100px;
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
  .selectsubmit00{
    float:left;
    position:relative;
    top:600px;
    left:-100px;
  }

</style>
