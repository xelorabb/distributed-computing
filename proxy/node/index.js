require('dotenv').config({path: `${__dirname}/../../.env`})

const express = require('express')
const app = express()
const server = require('http').createServer(app)
const port = process.env.SERVER_PORT

const SystemTest = require('./js/SystemTest')
const Ping = require('./js/Ping')

new SystemTest(app).listen()
new Ping(app).listen()

server.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`)
})
