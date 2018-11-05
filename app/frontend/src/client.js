import io from 'socket.io-client'
import settings from './settings.js'
const CHAT = {
  msgObj: document.getElementsByClassName('body-wrapper')[0],
  username: null,
  socket: null,
  msgArr: [{
    time: '00:30',
    msg: 'from God to all',
    toUser: 'all',
    fromUser: 'God'
  }, {
    time: '00:32',
    msg: 'from Hanky to all',
    toUser: 'all',
    fromUser: 'Hanky'
  }, {
    time: '00:34',
    msg: 'from God to all',
    toUser: 'all',
    fromUser: 'God'
  }, {
    time: '00:35',
    msg: 'from Devil to all',
    toUser: 'all',
    fromUser: 'Devil'
  }],
  logout: function () {
    this.socket.disconnect()
  },
  submit: function (obj) {
    this.socket.emit('sendMsg', obj)
  },
  message: function (username) {
    console.log('message')
    this.socket.on('to' + username, function (obj) {
      CHAT.msgArr.push(obj)
      console.log('CHAT.msgArr', obj)
    })
  },
  init: function (username) {
    this.socket = io.connect(settings.socket, {'force new connection': true})
    this.socket.on('open', function () {
      console.log('已连接')
    })
    this.socket.emit('addUser', username)
  }
}
export default CHAT
