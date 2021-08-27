const fs = require('fs')
const { exec } = require('child_process')
const {
    addTimestamps,
    getTimestamp
} = require('./helper/timestamps')

module.exports = class Ping {
  constructor(app){ this.app = app}
  listen() {
    this.app.get('/ping', (req, res) => {
      console.log("#### PING REQUEST ###################")
      const received = getTimestamp()

      const ping_processor = process.env.PING_PROCESSOR
      const ping_strict_exec = process.env.PING_STRICT_EXEC

      switch (ping_processor) {
        case 'random':
          console.log('random ping processor')

          const dir = '../../processing/pong/'
          let files = []
          fs.readdirSync(dir).forEach(file => { files.push(file) })

          const n = Math.floor(Math.random() * files.length)
          this.send_pong(dir + files[n], res, received)

          break
        case 'strict':
          console.log('strict ping processor')
          this.send_pong(ping_strict_exec, res, received)

          break
        default:
          console.log('default ping processor')
          data = '{"msg": "pong": "process": "server"}'
          this.send_pong_data('server', data, res, received)

          break
      }
    })
  }

  send_pong(exec_str, res, received) {
    exec(exec_str, (error, stdout, stderr) => {
      if (error) {
        res.status(400)
        res.send(`{"msg": ${JSON.stringify(error)}}`)
        return
      }

      this.send_pong_data(exec_str, stdout, res, received)
    })
  }

  send_pong_data(exec_str, data, res, received) {
    console.log(`reveiced pong data: ${data}`);
    data = addTimestamps(data, received)
    data.exec = exec_str
    data.server.type = 'node'
    console.log(`sent pong data: ${JSON.stringify(data)}`);
    res.send(data)
  }
}
