#!/usr/bin/env python

from dotenv import dotenv_values
from bottle import run

from py.SystemTest import SystemTest
from py.Ping import Ping

config = dotenv_values("../../.env")

SystemTest().listen()
Ping(config).listen()

run(host='localhost', port=3000, reloader=True)
