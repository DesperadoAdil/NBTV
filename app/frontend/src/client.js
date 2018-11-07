import io from 'socket.io-client'
import settings from './settings.js'
const CHAT = {
  msgObj: document.getElementsByClassName('body-wrapper')[0],
  username: null,
  socket: null,
  msgArr: [{
    type: 'broadcast',
    url: '242544',
    time: '00:30',
    msg: 'from God to all',
    toUser: 'all',
    fromUser: 'God'
  }, {
    type: 'broadcast',
    url: '242544',
    time: '00:32',
    msg: 'from Hanky to all',
    toUser: 'all',
    fromUser: 'Hanky'
  }, {
    type: 'broadcast',
    url: '242544',
    time: '00:34',
    msg: 'from God to all',
    toUser: 'all',
    fromUser: 'God'
  }, {
    type: 'broadcast',
    url: '242544',
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
      console.log('CHAT.msgArr(whisper)', obj)
    })
    this.socket.on('broadcast', function (obj) {
      CHAT.msgArr.push(obj)
      console.log('CHAT.msgArr(broadcast)', obj)
    })
  },
  init: function (username, url) {
    this.socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port, {'username': username})
    this.socket.on('open', function () {
      console.log('已连接')
    })
    console.log(username, url)
    this.socket.emit('join', {'username': username, 'url': url})
    return this.socket
  }
}
export default CHAT
