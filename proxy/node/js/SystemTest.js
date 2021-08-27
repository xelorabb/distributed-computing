module.exports = class SystemTest {
  constructor(app){ this.app = app}
  listen() {
    this.app.get('/', (req, res) => {
      res.send('It Works!')
    })

    this.app.get('/systemtest', (req, res) => {
      let n = 'Node Version: ' + process.version + '</br></br>'
      n += 'V8 Version: ' + process.versions.v8 + '</br></br>'
      res.send(n)
    })
  }
}
