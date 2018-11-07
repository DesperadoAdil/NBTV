from app import app, socketio

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

socketio.run(app, debug = True, host = "0.0.0.0", port = 80)
