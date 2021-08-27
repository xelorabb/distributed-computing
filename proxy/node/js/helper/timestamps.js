module.exports = {
    addTimestamps,
    getTimestamp
}

function addTimestamps(data, received) {
  const d = JSON.parse(data)

  d.server = {}
  d.server.received = received
  d.server.sent = getTimestamp()

  return d
}

function getTimestamp() {
  return new Date(Date.now()).toISOString()
}
