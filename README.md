### Create .env
#### Example
```
SERVER_PORT=3000

PING_PROCESSOR=[𝘴𝘵𝘳𝘪𝘤𝘵|𝘳𝘢𝘯𝘥𝘰𝘮]
PING_STRICT_EXEC=../../processing/pong/pong.py
```


### Start a proxy server
#### Node
* `cd proxy/node`
* `npm run serve`

#### Bottle
* `cd proxy/bottle`
* `python index.py`


### Start a client
#### Ping PyQt GUI
* `cd client/ping/gui/pyqt`
* `python ping.py`

#### Ping Terminal
* `cd client/ping/term`
* `python ping.py`
