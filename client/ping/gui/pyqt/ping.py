import sys
import json
import requests
from requests.exceptions import ConnectionError

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem as TableItem
from datetime import datetime
from ping_gui import Ui_MainWindow

class App():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.PingComp.clicked.connect(self.createTableRow)
        self.ui.ClearComp.clicked.connect(self.clearTable)
        self.ui.StartStopComp.clicked.connect(self.autoPing)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.createTableRow)

    def autoPing(self):
        but = self.ui.StartStopComp
        title = but.text()

        if title == 'Start':
            but.setText('Stop')
            self.ui.PingComp.setEnabled(False)
            self.ui.ClearComp.setEnabled(False)
            self.ui.DelayComp.setEnabled(False)
            self.ui.ProgressComp.setMaximum(0)

            self.createTableRow()
            self.timer.setInterval(self.ui.DelayComp.value() * 1000)
            self.timer.start()
        else:
            but.setText('Start')
            self.ui.PingComp.setEnabled(True)
            self.ui.ClearComp.setEnabled(True)
            self.ui.DelayComp.setEnabled(True)
            self.ui.ProgressComp.setMaximum(1)

            self.timer.stop()

    def clearTable(self):
        self.ui.MessageComp.setRowCount(0)

    def getData(self):
        req = None
        data = None
        err = None

        self.start_time = datetime.utcnow()

        try:
            req = requests.get('http://localhost:3000/ping')
        except ConnectionError:
            err = 'connection error'
        except:
            err = 'unknown error'

        self.end_time = datetime.utcnow()
        self.duration = self.end_time - self.start_time

        if not req == None:
            data = req.text
            self.status = req.status_code
        else:
            data = '{"msg": "' + err + '"}'
            self.status = 500

        return data

    def formatData(self):
        data = None

        if not self.getData() == None:
            dd = json.loads(self.getData())
            data = [''] * 10
            data[0] = self.start_time.isoformat()[11:23]
            data[1] = self.getDictEntry(dd, 'server', 'received')[11:23]
            data[2] = self.getDictEntry(dd, 'created')[11:23]
            data[3] = self.getDictEntry(dd, 'server', 'sent')[11:23]
            data[4] = self.end_time.isoformat()[11:23]
            data[5] = str(self.duration.total_seconds()) + 's'
            data[6] = str(self.status)
            data[7] = self.getDictEntry(dd, 'process')
            data[8] = self.getDictEntry(dd, 'server', 'type')
            data[9] = self.getDictEntry(dd, 'msg')

        return data

    def createTableRow(self):
        self.addTableRow(self.formatData())

    def addTableRow(self, data):
        if not data == None:
            table = self.ui.MessageComp
            rowPos = table.rowCount()
            table.insertRow(rowPos)

            for i, elem in enumerate(data):
                table.setItem(rowPos , i, TableItem(elem))

            item = table.item(rowPos,0)
            table.scrollToItem(item)
            table.selectRow(rowPos)

    def getDictEntry(self, dict, key1, key2 = None):
        entry = ''

        if key2 == None:
            entry = dict[key1] if key1 in dict else ''
        else:
            entry = dict[key1][key2] if key1 in dict and key2 in dict[key1] else ''

        return str(entry)

    def show(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = App()
    app.show()
