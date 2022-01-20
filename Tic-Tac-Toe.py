# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtWidgets
from itertools import cycle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(60, 50, 71, 71))
        self.pushButton1.setText("")
        self.pushButton1.setObjectName("pushButton1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(140, 20, 31, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 20, 31, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(140, 130, 71, 71))
        self.pushButton5.setText("")
        self.pushButton5.setObjectName("pushButton5")
        self.buttonGroup.addButton(self.pushButton5, 5)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(60, 130, 71, 71))
        self.pushButton4.setText("")
        self.pushButton4.setObjectName("pushButton4")
        self.buttonGroup.addButton(self.pushButton4, 4)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(140, 50, 71, 71))
        self.pushButton2.setText("")
        self.pushButton2.setObjectName("pushButton2")
        self.buttonGroup.addButton(self.pushButton2, 2)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(220, 50, 71, 71))
        self.pushButton3.setText("")
        self.pushButton3.setObjectName("pushButton3")
        self.buttonGroup.addButton(self.pushButton3, 3)
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(220, 130, 71, 71))
        self.pushButton6.setText("")
        self.pushButton6.setObjectName("pushButton6")
        self.buttonGroup.addButton(self.pushButton6, 6)
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(60, 210, 71, 71))
        self.pushButton7.setText("")
        self.pushButton7.setObjectName("pushButton7")
        self.buttonGroup.addButton(self.pushButton7, 7)
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(QtCore.QRect(140, 210, 71, 71))
        self.pushButton8.setText("")
        self.pushButton8.setObjectName("pushButton8")
        self.buttonGroup.addButton(self.pushButton8, 8)
        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton9.setGeometry(QtCore.QRect(220, 210, 71, 71))
        self.pushButton9.setText("")
        self.pushButton9.setObjectName("pushButton9")
        self.buttonGroup.addButton(self.pushButton9, 9)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 300, 300, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(124, 330, 101, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Крестики-нолики"))
        self.radioButton.setText(_translate("MainWindow", "X"))
        self.radioButton_2.setText(_translate("MainWindow", "O"))
        self.pushButton_10.setText(_translate("MainWindow", "Новая игра"))


class Tik(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tik, self).__init__()
        self.setupUi(self)
        self.number = 1
        self.x_o = cycle(("X", "O"))
        self.win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        self.pushButton_10.clicked.connect(self.run)
        for i in self.buttonGroup.buttons():
            i.clicked.connect(self.push)
        self.flug = True

    def run(self):
        if self.radioButton.isChecked():
            self.x_o = cycle(("X", "O"))
        else:
            self.x_o = cycle(("O", "X"))
        for i in self.buttonGroup.buttons():
            i.setText("")
            i.setEnabled(True)
        self.flug = True
        self.label.setText("")

    def checking(self, sign):
        if self.flug:
            for each in self.win_coord:
                if self.buttonGroup.button(each[0]).text() == self.buttonGroup.button(each[1]).text() == \
                        self.buttonGroup.button(each[2]).text() == sign:
                    self.label.setText(f"         Победил {sign}")
                    self.flug = False

    def push(self):
        self.sign = next(self.x_o)
        id = self.sender().objectName()[-1]
        self.but = self.buttonGroup.button(int(id))
        if self.but.isEnabled():
            self.but.setText(self.sign)
            self.but.setEnabled(False)
        self.checking(self.sign)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Tik()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
