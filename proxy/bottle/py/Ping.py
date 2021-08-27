import os
import sys
import math

from bottle import route, response
from random import randint
from os import walk
from json.decoder import JSONDecodeError

from py.helper import timestamps as ts

class Ping:
    def __init__(self, config):
        self.config = config
        return

    def listen(self):
        @route('/ping')
        def ping():
            print("#### PING REQUEST ###################")
            received = ts.getTimestamp()

            ping_processor = self.config['PING_PROCESSOR']
            ping_strict_exec = self.config['PING_STRICT_EXEC']

            if ping_processor == 'random':
                print('random ping processor')

                dir = '../../processing/pong/'
                files = []
                for (dirpath, dirnames, filenames) in walk(dir):
                    files.extend(filenames)
                    break

                n = randint(0, len(files)-1)
                return self.send_pong(dir + files[n], received)

            elif ping_processor == 'strict':
                print('strict ping processor')
                return self.send_pong(ping_strict_exec, received)

            else:
                print('default ping processor')
                return self.send_pong_data('server', '{"msg": "pong"}', received)


    def send_pong(self, exec_str, received):
        result = ''
        response.status = 200

        try:
            stream = os.popen(exec_str)
            data = stream.read()
            result = self.send_pong_data(exec_str, data, received)
        except JSONDecodeError as err:
            response.status = 400
            result = 'JSONDecodeError: ' + format(err)
        except:
            response.status = 400
            result = 'Unknown Error'

        return result

    def send_pong_data(self, exec_str, data, received):
        print("reveiced pong data:", data)
        data = ts.addTimestamps(data, received)
        data['exec'] = exec_str
        data['server']['type'] = 'bottle'
        print("sent pong data:", str(data))
        return data
