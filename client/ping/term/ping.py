#!/usr/bin/env python

import requests
from requests.exceptions import ConnectionError

req = None
err = None

try:
    req = requests.get('http://localhost:3000/ping')
except ConnectionError:
    err = 'connection error'
except:
    err = 'unknown error'

print('Status Code:', req.status_code if not req == None else 500)
print(req.text if not req == None else err)
