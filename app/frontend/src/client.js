import io from 'socket.io-client'
import router from './router'
const CHAT = {
  msgObj: document.getElementsByClassName('body-wrapper')[0],
  username: null,
  socket: null,
  msgArr: [],
  studentlist: [],
  curpage0:'1',
  frametype: 'close',
  pdfurl: '/static/pdf/1-1.pdf',
  codeall: {
    uniqueId: '',
    statement: 'B-Tree',
    language: 'cpp',
    example: 'cout << "hello world" << endl;'
  },
  selectall: {
    uniqueId: '1',
    statement: 'choice 02',
    optionList: ['something', 'somewhere', 'somehow', 'somewhat'],
    answer: 'A'
  },
  logout: function () {
    this.socket.disconnect()
  },
  submit: function (obj) {
    this.socket.emit('sendMsg', obj)
  },
  shutUp: function (obj) {
    this.socket.emit('shutup', obj)
    console.log('shut up')
  },
  blackList: function (obj) {
    this.socket.emit('blacklist', obj)
    console.log('black list')
  },
  list: function (username, url) {
    console.log('list')
    this.socket.emit('list', {'username': username, 'url': url})
  },
  beenShutUp: function (username) {
    this.socket.on('shutup', function () {
      this.$Message.error('您已被禁言')
    })
  },
  beenKickOut: function (username) {
    this.socket.on('blacklist', function () {
      router.push('/list')
      this.$Message.error('您已被永久踢出房间')
    })
  },
  youCanTalk: function (username, url) {
    this.socket.emit('noShutUp', {'username': username, 'url': url})
  },
  message: function (username) {
    console.log('message')
    this.socket.on('message', function (msg) {
      var date = new Date()
      var time = date.getHours() + ':' + date.getMinutes()
      var obj = {
        type: 'broadcast',
        msgType: 'text',
        url: this.cururl,
        time: time,
        msg: msg,
        toUser: 'all',
        fromUser: '[系统]'
      }
      CHAT.msgArr.push(obj)
      //let message = document.getElementById('content-id')
      //message.scrollTop = message.scrollHeight
      console.log('CHAT.msgArr(system)', obj)
    })
    this.socket.on('whisper', function (obj) {
      CHAT.msgArr.push(obj)
      console.log('CHAT.msgArr(whisper)', obj)
    })
    this.socket.on('broadcast', function (obj) {
      CHAT.msgArr.push(obj)
      console.log('CHAT.msgArr(broadcast)', obj)
    })
    this.socket.on('list', function (obj) {
      CHAT.studentlist = obj
    })
    this.socket.on('pdf', function (obj) {
      console.log("pdf")
      CHAT.frametype = 'pdf'
      CHAT.pdfurl = obj.msg
    })
    this.socket.on('select', function (obj) {
      CHAT.frametype = 'select'
      console.log(obj.msg)
      CHAT.selectall = obj.msg
    })
    this.socket.on('code', function (obj) {
      CHAT.frametype = 'code'
      CHAT.codeall = obj.msg
    })
    this.socket.on('close', function (obj) {
      console.log("close")
      CHAT.frametype = 'close'
    })
    this.socket.on('page', function (obj) {

      CHAT.pdfurl=obj.msg.pdfurl
      CHAT.curpage0 = obj.msg.page
      //alert(obj.msg.pdfurl)
      //alert(obj.msg.page)
      console.log(obj.msg.pdfurl)
      console.log(obj.msg.page)
    })

  },
  init: function (username, url) {
    this.socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)
    this.socket.on('open', function () {
      console.log('已连接')
    })
    console.log(username, url)
    this.socket.emit('join', {'username': username, 'url': url})
    this.socket.on('check', function () {
      CHAT.socket.emit('check', {'username': username, 'url': url})
    })
    return this.socket
  }
}
export default CHAT
