import json
from datetime import datetime

def getTimestamp():
    return str(datetime.utcnow().isoformat())

def addTimestamps(data, received):
    d = json.loads(data)

    d['server'] = {}
    d['server']['received'] = received
    d['server']['sent'] = getTimestamp()

    return d
