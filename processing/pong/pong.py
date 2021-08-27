#!/usr/bin/env python

from datetime import datetime

print('{"msg": "pong", "process": "python", "created": "' + str(datetime.utcnow().isoformat()) + '"}')
