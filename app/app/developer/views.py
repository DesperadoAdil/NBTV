from . import developer

@developer.route('/')
def hello():
    return 'hello world!'
