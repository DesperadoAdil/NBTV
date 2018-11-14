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
  selectall: {
    title: 'choice 02',
    ans: ['something', 'somewhere', 'somehow', 'somewhat'],
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
  },
  blackList: function (obj) {
    this.socket.emit('blacklist', obj)
  },
  list: function (username, url) {
    console.log('list')
    this.socket.emit('list', {'username': username, 'url': url})
  },
  beenShutUp: function (username) {
    this.socket.on('shutup', function (obj) {
      this.$Message.warning('您已被禁言')
    })
  },
  beenKickOut: function (username) {
    this.socket.on('blacklist', function (obj) {
      router.push('/list')
      this.$Message.warning('您已被永久踢出房间')
    })
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
      CHAT.frametype = 'pdf'
      CHAT.pdfurl = obj.msg
    })
    this.socket.on('select', function (obj) {
      CHAT.frametype = 'select'
      CHAT.selectall = obj.msg
    })
    this.socket.on('code', function (obj) {
      CHAT.frametype = 'code'
    })
    this.socket.on('close', function (obj) {
      CHAT.frametype = 'close'
    })
    this.socket.on('page', function (obj) {
      CHAT.curpage0 = obj.msg
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
