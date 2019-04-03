# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_anniu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_anniu.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pushButton_anniu.setObjectName("pushButton_anniu")
        self.lineEdit_shuru = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_shuru.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.lineEdit_shuru.setObjectName("lineEdit_shuru")
        self.textEdit_shuchu = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_shuchu.setGeometry(QtCore.QRect(90, 170, 104, 71))
        self.textEdit_shuchu.setObjectName("textEdit_shuchu")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##############################################################
        self.pushButton_anniu.clicked.connect(lambda: self.transform())
        ##############################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_anniu.setText(_translate("MainWindow", "PushButton"))

    ##############################################################
    def transform(self):
        _translate = QtCore.QCoreApplication.translate
        text1 = self.lineEdit_shuru.text()
        print(text1)
        self.textEdit_shuchu.setText(text1)
    ##############################################################


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
