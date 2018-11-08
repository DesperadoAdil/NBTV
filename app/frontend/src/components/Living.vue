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
              <div class="talk-space self-talk"
                   v-if="CHAT.msgArr[index].fromUser !== userInfo.username && CHAT.msgArr[index].toUser === username">
                <div class="talk-content">
                  <div class="talk-self-name">{{ msgObj.fromUser }}</div>
                  <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-self">{{ msgObj.msg }}</div>
                  <div v-else></div>
                  <div v-if="msgObj.msgType === 'audio'">
                    <audio :src="audioUrl(msgObj.msg)" controls></audio>
                  </div>
                  <div v-else></div>

                </div>
              </div>
              <div v-else></div>
              <div  class="talk-space user-talk"
                    v-if="CHAT.msgArr[index].toUser === username && CHAT.msgArr[index].fromUser === userInfo.username">
                <div class="talk-content">
                  <div class="talk-user-name">{{ msgObj.fromUser }}</div>
                  <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-user">{{ msgObj.msg }}</div>
                  <div v-else></div>
                  <div v-if="msgObj.msgType === 'audio'">
                    <audio :src="audioUrl(msgObj.msg)" controls></audio>
                  </div>
                  <div v-else></div>
                </div>
              </div>
              <div v-else></div>
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
            <Button class="talker-send" type="success" @click="submit">发送</Button>
            <Button class="talker-send" @click="changeMsgType">{{ msgTypeInfo }}</Button>
          </div>
        </div>
      </div>
    </Card>
    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->

  </div>
</template>

<script>
import axios from 'axios'
import CHAT from '../client'
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
      socket: null,
      msgType: 'text',
      msgTypeInfo: '文字',
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
      maincodecarddisplay: false,
      curpdfurl: '/static/pdf/1-1.pdf',
      videohei0: 600 + 'px',
      classmain11: true,
      curvid: '',
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
    var xxx = this.videohei0
    console.log(xxx)
    var yyy = this.curvid
     console.log(yyy)
    var timer = setTimeout(function () {
      doItPerSecond()
    }, 1000)
    var num = 0
    function doItPerSecond () {

      var player = polyvObject('#player').livePlayer({
        'width': '100%',
        'height': xxx,
        'uid': '7181857ac2',
        'vid': yyy
      })
      var player = polyvObject('#player2').livePlayer({
        'width': '100%',
        'height': 200 + 'px',
        'uid': '7181857ac2',
        'vid': yyy
      })
      num++
      console.log(num)
    };
  },
  created: function () {
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
    })
    const s = document.createElement('script')
    s.type = 'text/javascript'
    s.src = 'https://player.polyv.net/livescript/liveplayer.js'
    document.body.appendChild(s)
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
        obj = {
          type: 'broadcast',
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
          type: 'broadcast',
          msgType: 'audio',
          url: this.cururl,
          time: time,
          msg: this.audio,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        console.log(obj)
        CHAT.submit(obj)
      }
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
    showpdf0 () {
      console.log('weqweqwe')
      this.liaotianshiheight = 500 + 'px'
      this.littlelivingcarddisplay = true
      this.mainselectcarddisplay = false
      this.mainpdfcarddisplay = true
      this.mainlivingcarddisplay = false
      this.maincodecarddisplay = false
      this.displayPdfurl0 = '/static/pdfjs/web/viewer.html?file=' + this.curpdfurl
    },
    showselect0 () {
      console.log('weqweqwe')
      this.liaotianshiheight = 500 + 'px'
      this.littlelivingcarddisplay = true
      this.mainselectcarddisplay = true
      this.mainpdfcarddisplay = false
      this.mainlivingcarddisplay = false
      this.maincodecarddisplay = false
    },
    showcode0 () {
      console.log('weqweqwe')
      this.liaotianshiheight = 500 + 'px'
      this.littlelivingcarddisplay = true
      this.mainselectcarddisplay = false
      this.mainpdfcarddisplay = false
      this.mainlivingcarddisplay = false
      this.maincodecarddisplay = true
    },
    exitliving0 () {
      console.log('weqweqwe')
      this.liaotianshiheight = 150 + 'px'
      this.littlelivingcarddisplay = false
      this.mainselectcarddisplay = false
      this.mainpdfcarddisplay = false
      this.mainlivingcarddisplay = true
      this.maincodecarddisplay = false
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
