import sys
import bottle
from bottle import route

class SystemTest:
    def __init__(self):
        return

    def listen(self):
        @route('/')
        def index():
            return 'It works!'

        @route('/systemtest')
        def systemtest():
            n = 'Python Version: ' + sys.version + '</br></br>'
            n += 'Bottle Version: ' + bottle.__version__ + '</br></br>'
            return n
