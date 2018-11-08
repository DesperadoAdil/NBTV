import io from 'socket.io-client'
const CHAT = {
  msgObj: document.getElementsByClassName('body-wrapper')[0],
  username: null,
  socket: null,
  msgArr: [],
  studentlist: [],
  logout: function () {
    this.socket.disconnect()
  },
  submit: function (obj) {
    this.socket.emit('sendMsg', obj)
  },
  list: function (username, url) {
    console.log('list')
    this.socket.emit('list', {'username': username, 'url': url})
  },
  message: function (username) {
    console.log('message')
    this.socket.on('message', function (msg) {
      msg = '[system]: ' + msg
      var date = new Date()
      var time = date.getHours() + ':' + date.getMinutes()
      var obj = {
        type: 'broadcast',
        msgType: 'text',
        url: this.cururl,
        time: time,
        msg: msg,
        toUser: 'all',
        fromUser: 'system'
      }
      CHAT.msgArr.push(obj)
      console.log('CHAT.msgArr(system)', obj)
    })
    this.socket.on('whisper', function (obj) {
      obj.msg = obj.fromUser + ' whispered to you: ' + obj.msg
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
  },
  init: function (username, url) {
    this.socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)
    this.socket.on('open', function () {
      console.log('已连接')
    })
    console.log(username, url)
    this.socket.emit('join', {'username': username, 'url': url})
    this.socket.on('check', function () {
      this.socket.emit('check', {'username': username})
    })
    return this.socket
  }
}
export default CHAT
