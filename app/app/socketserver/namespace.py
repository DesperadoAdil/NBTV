from flask_socketio import Namespace, join_room, leave_room, emit, send

class MyCustomNamespace(Namespace):
    def on_connect(self):
        print ('Client connected')
        emit('open')

    def on_disconnect(self):
        print ('Client disconnected')

    def on_join(self, data):
        print ('join!')
        username = data['username']
        join_room(username)
        send(username + ' has entered the classroom.')


    def on_sendMsg(self, data):
        print (data)
        type = data['type']
        if type == "broadcast":
            emit('broadcast', data)
        elif type == "whisper":
            emit('whisper', room = data['username'])
