# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
###############################################################
import Functions
import json


###############################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 80, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 60, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 60, 12))
        self.label_3.setObjectName("label_3")
        self.textEditCetou = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditCetou.setGeometry(QtCore.QRect(100, 80, 141, 20))
        self.textEditCetou.setObjectName("textEditCetou")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 84, 12))
        self.label_4.setObjectName("label_4")
        self.textEditCaiyang = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditCaiyang.setGeometry(QtCore.QRect(100, 110, 141, 20))
        self.textEditCaiyang.setObjectName("textEditCaiyang")
        self.textEditXuanzhuan = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditXuanzhuan.setGeometry(QtCore.QRect(100, 140, 141, 20))
        self.textEditXuanzhuan.setObjectName("textEditXuanzhuan")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 80, 18))
        self.label_5.setObjectName("label_5")
        self.ButtonLilun = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonLilun.setGeometry(QtCore.QRect(100, 400, 75, 23))
        self.ButtonLilun.setObjectName("ButtonLilun")
        self.ButtonDaoru = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDaoru.setGeometry(QtCore.QRect(100, 430, 80, 23))
        self.ButtonDaoru.setObjectName("ButtonDaoru")
        self.ButtonShiji = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonShiji.setGeometry(QtCore.QRect(100, 460, 75, 23))
        self.ButtonShiji.setObjectName("ButtonShiji")
        self.ButtonPiancha = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPiancha.setGeometry(QtCore.QRect(100, 490, 80, 23))
        self.ButtonPiancha.setObjectName("ButtonPiancha")
        self.ButtonPinding = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPinding.setGeometry(QtCore.QRect(100, 520, 75, 23))
        self.ButtonPinding.setObjectName("ButtonPinding")
        self.ButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSave.setGeometry(QtCore.QRect(100, 550, 75, 23))
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonQingchu = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonQingchu.setGeometry(QtCore.QRect(100, 580, 75, 23))
        self.ButtonQingchu.setObjectName("ButtonQingchu")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(295, 40, 541, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 90, 80, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(860, 130, 72, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(860, 170, 96, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(860, 210, 84, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(860, 250, 72, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(860, 290, 78, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(860, 330, 78, 12))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(860, 370, 84, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(860, 410, 84, 12))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(860, 450, 60, 12))
        self.label_15.setObjectName("label_15")
        self.textEditWucha = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditWucha.setGeometry(QtCore.QRect(970, 130, 281, 20))
        self.textEditWucha.setObjectName("textEditWucha")
        self.ButtonClose = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonClose.setGeometry(QtCore.QRect(100, 610, 75, 23))
        self.ButtonClose.setObjectName("ButtonClose")
        self.textEditBiaozhuncha = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditBiaozhuncha.setGeometry(QtCore.QRect(970, 170, 281, 20))
        self.textEditBiaozhuncha.setObjectName("textEditBiaozhuncha")
        self.textEditJuli = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditJuli.setGeometry(QtCore.QRect(970, 210, 281, 20))
        self.textEditJuli.setObjectName("textEditJuli")
        self.textEditYalijiao = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditYalijiao.setGeometry(QtCore.QRect(970, 250, 281, 20))
        self.textEditYalijiao.setObjectName("textEditYalijiao")
        self.textEditBzengyi = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditBzengyi.setGeometry(QtCore.QRect(970, 290, 281, 20))
        self.textEditBzengyi.setObjectName("textEditBzengyi")
        self.textEditBzhihou = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditBzhihou.setGeometry(QtCore.QRect(970, 330, 281, 20))
        self.textEditBzhihou.setObjectName("textEditBzhihou")
        self.textEditGuzengyi = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditGuzengyi.setGeometry(QtCore.QRect(970, 370, 281, 20))
        self.textEditGuzengyi.setObjectName("textEditGuzengyi")
        self.textEditGuzhihou = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditGuzhihou.setGeometry(QtCore.QRect(970, 410, 281, 20))
        self.textEditGuzhihou.setObjectName("textEditGuzhihou")
        self.textEditBuchang = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditBuchang.setGeometry(QtCore.QRect(970, 450, 281, 20))
        self.textEditBuchang.setObjectName("textEditBuchang")
        self.textEditCeliangshuju = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditCeliangshuju.setGeometry(QtCore.QRect(10, 200, 261, 191))
        self.textEditCeliangshuju.setObjectName("textEditCeliangshuju")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #################################################################
        self.ButtonLilun.clicked.connect(lambda: self.theoretical_curve())

        #################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">参数设置：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "测头半径："))
        self.label_3.setText(_translate("MainWindow", "采样间隔："))
        self.label_4.setText(_translate("MainWindow", "样板旋转角度："))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">测量数据：</span></p></body></html>"))
        self.ButtonLilun.setText(_translate("MainWindow", "理论曲线"))
        self.ButtonDaoru.setText(_translate("MainWindow", "导入测量数据"))
        self.ButtonShiji.setText(_translate("MainWindow", "实际曲线"))
        self.ButtonPiancha.setText(_translate("MainWindow", "评定偏差曲线"))
        self.ButtonPinding.setText(_translate("MainWindow", "评定结果"))
        self.ButtonSave.setText(_translate("MainWindow", "保存"))
        self.ButtonQingchu.setText(_translate("MainWindow", "清除"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">评定结果：</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "最大误差值："))
        self.label_8.setText(_translate("MainWindow", "曲线拟合标准差："))
        self.label_9.setText(_translate("MainWindow", "V点和B点距离："))
        self.label_10.setText(_translate("MainWindow", "压力角误差："))
        self.label_11.setText(_translate("MainWindow", "B点增益误差："))
        self.label_12.setText(_translate("MainWindow", "B点滞后误差："))
        self.label_13.setText(_translate("MainWindow", "谷底增益误差："))
        self.label_14.setText(_translate("MainWindow", "谷底滞后误差："))
        self.label_15.setText(_translate("MainWindow", "补偿参数："))
        self.ButtonClose.setText(_translate("MainWindow", "关闭"))

    #################################################################
    def load_data(self):  # 以后万一用得上
        with open('data.json', 'r') as json_file:
            load_dict = json.load(json_file)
            print(load_dict)

    def save_data(self, dic):  # 以后万一用得上
        json_str = json.dumps(dic, indent=4)
        print(json_str)
        with open('data.json', 'w') as json_file:
            load_dict = json.load(json_file)
            print(load_dict)

    def theoretical_curve(self):
        std_z = 40  # 这是啥来的忘了好像用不上
        std_e = 28.5648595796  # 这是啥来的忘了好像用不上
        std_rb = 400  # 样板模拟齿轮的基圆半径
        std_rp = 1.5  # 齿轮测量仪器的测头半径(但是是用户导入的数据，所以暂时用不上)
        std_m = 21.28355545  # 这是啥来的忘了好像用不上
        std_c = 401.583156  # 定心轴和测量中心轴的距离
        std_rc = 105.102  # 检测圆弧半径
        input_rp = self.textEditCetou.text()  # 齿轮测量仪器的测头半径(用户输入)
        input_interval = self.textEditCaiyang.text()  # 采样间隔
        input_rotationAngle = self.textEditXuanzhuan.text()  # 样板的旋转角度ε
        delta_p = Functions.func1(std_rc, input_rp, std_c, std_rb, input_rotationAngle)
    #################################################################


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
