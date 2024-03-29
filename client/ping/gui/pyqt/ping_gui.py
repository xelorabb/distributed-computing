# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ping.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MessageComp = QtWidgets.QTableWidget(self.centralwidget)
        self.MessageComp.setObjectName("MessageComp")
        self.MessageComp.setColumnCount(10)
        self.MessageComp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.MessageComp.setHorizontalHeaderItem(9, item)
        self.MessageComp.horizontalHeader().setCascadingSectionResizes(False)
        self.MessageComp.horizontalHeader().setMinimumSectionSize(50)
        self.MessageComp.horizontalHeader().setSortIndicatorShown(False)
        self.MessageComp.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.MessageComp)
        self.ProgressComp = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressComp.setMaximum(1)
        self.ProgressComp.setProperty("value", -1)
        self.ProgressComp.setInvertedAppearance(False)
        self.ProgressComp.setObjectName("ProgressComp")
        self.verticalLayout.addWidget(self.ProgressComp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.DelayComp = QtWidgets.QSpinBox(self.centralwidget)
        self.DelayComp.setMinimum(1)
        self.DelayComp.setObjectName("DelayComp")
        self.horizontalLayout.addWidget(self.DelayComp)
        self.StartStopComp = QtWidgets.QPushButton(self.centralwidget)
        self.StartStopComp.setObjectName("StartStopComp")
        self.horizontalLayout.addWidget(self.StartStopComp)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ClearComp = QtWidgets.QPushButton(self.centralwidget)
        self.ClearComp.setObjectName("ClearComp")
        self.horizontalLayout.addWidget(self.ClearComp)
        self.PingComp = QtWidgets.QPushButton(self.centralwidget)
        self.PingComp.setObjectName("PingComp")
        self.horizontalLayout.addWidget(self.PingComp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ping"))
        item = self.MessageComp.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "start"))
        item = self.MessageComp.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "received"))
        item = self.MessageComp.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "created"))
        item = self.MessageComp.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "sent"))
        item = self.MessageComp.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "end"))
        item = self.MessageComp.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "duration"))
        item = self.MessageComp.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "status"))
        item = self.MessageComp.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "process"))
        item = self.MessageComp.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "server"))
        item = self.MessageComp.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "msg"))
        self.label.setText(_translate("MainWindow", "Auto Ping (delay in sec):"))
        self.StartStopComp.setText(_translate("MainWindow", "Start"))
        self.ClearComp.setText(_translate("MainWindow", "Clear"))
        self.PingComp.setText(_translate("MainWindow", "Ping!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
