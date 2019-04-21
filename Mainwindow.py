# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
###############################################################
from PyQt5.QtGui import QImage, QPixmap
import Functions
import Draw
import math
import json
import IO
import cv2
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QCoreApplication
import cv2
import numpy as np


###############################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(220, 90, 671, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 201, 110))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textEditCetou = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.textEditCetou.setSuffix("")
        self.textEditCetou.setDecimals(3)
        self.textEditCetou.setObjectName("textEditCetou")
        self.horizontalLayout.addWidget(self.textEditCetou)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textEditCaiyang = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.textEditCaiyang.setSuffix("")
        self.textEditCaiyang.setDecimals(3)
        self.textEditCaiyang.setObjectName("textEditCaiyang")
        self.horizontalLayout_2.addWidget(self.textEditCaiyang)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.textEditXuanzhuan = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.textEditXuanzhuan.setSuffix("")
        self.textEditXuanzhuan.setDecimals(3)
        self.textEditXuanzhuan.setObjectName("textEditXuanzhuan")
        self.horizontalLayout_3.addWidget(self.textEditXuanzhuan)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 181, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEditCeliangshuju = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEditCeliangshuju.setGeometry(QtCore.QRect(10, 20, 161, 161))
        self.textEditCeliangshuju.setObjectName("textEditCeliangshuju")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(900, 120, 211, 441))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.textEditWucha = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditWucha.setEnabled(False)
        self.textEditWucha.setSuffix("")
        self.textEditWucha.setDecimals(3)
        self.textEditWucha.setObjectName("textEditWucha")
        self.horizontalLayout_4.addWidget(self.textEditWucha)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.textEditBiaozhuncha = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditBiaozhuncha.setEnabled(False)
        self.textEditBiaozhuncha.setSuffix("")
        self.textEditBiaozhuncha.setDecimals(3)
        self.textEditBiaozhuncha.setObjectName("textEditBiaozhuncha")
        self.horizontalLayout_5.addWidget(self.textEditBiaozhuncha)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.textEditJuli = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditJuli.setEnabled(False)
        self.textEditJuli.setSuffix("")
        self.textEditJuli.setDecimals(3)
        self.textEditJuli.setObjectName("textEditJuli")
        self.horizontalLayout_6.addWidget(self.textEditJuli)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.textEditYalijiao = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditYalijiao.setEnabled(False)
        self.textEditYalijiao.setSuffix("")
        self.textEditYalijiao.setDecimals(3)
        self.textEditYalijiao.setObjectName("textEditYalijiao")
        self.horizontalLayout_7.addWidget(self.textEditYalijiao)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.textEditBzengyi = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditBzengyi.setEnabled(False)
        self.textEditBzengyi.setObjectName("textEditBzengyi")
        self.horizontalLayout_8.addWidget(self.textEditBzengyi)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.textEditBzhihou = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditBzhihou.setEnabled(False)
        self.textEditBzhihou.setObjectName("textEditBzhihou")
        self.horizontalLayout_9.addWidget(self.textEditBzhihou)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.textEditGuzengyi = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditGuzengyi.setEnabled(False)
        self.textEditGuzengyi.setObjectName("textEditGuzengyi")
        self.horizontalLayout_10.addWidget(self.textEditGuzengyi)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.textEditGuzhihou = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditGuzhihou.setEnabled(False)
        self.textEditGuzhihou.setObjectName("textEditGuzhihou")
        self.horizontalLayout_11.addWidget(self.textEditGuzhihou)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.textEditBuchang = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditBuchang.setEnabled(False)
        self.textEditBuchang.setObjectName("textEditBuchang")
        self.horizontalLayout_12.addWidget(self.textEditBuchang)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 390, 82, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ButtonLilun = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonLilun.setObjectName("ButtonLilun")
        self.verticalLayout_2.addWidget(self.ButtonLilun)
        self.ButtonDaoru = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonDaoru.setObjectName("ButtonDaoru")
        self.verticalLayout_2.addWidget(self.ButtonDaoru)
        self.ButtonShiji = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonShiji.setObjectName("ButtonShiji")
        self.verticalLayout_2.addWidget(self.ButtonShiji)
        self.ButtonPiancha = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonPiancha.setObjectName("ButtonPiancha")
        self.verticalLayout_2.addWidget(self.ButtonPiancha)
        self.ButtonPinding = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonPinding.setObjectName("ButtonPinding")
        self.verticalLayout_2.addWidget(self.ButtonPinding)
        self.ButtonSave = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonSave.setObjectName("ButtonSave")
        self.verticalLayout_2.addWidget(self.ButtonSave)
        self.ButtonQingchu = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonQingchu.setObjectName("ButtonQingchu")
        self.verticalLayout_2.addWidget(self.ButtonQingchu)
        self.ButtonClose = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonClose.setObjectName("ButtonClose")
        self.verticalLayout_2.addWidget(self.ButtonClose)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #################################################################
        self.ButtonLilun.clicked.connect(lambda: self.theoretical_curve())
        self.ButtonDaoru.clicked.connect(lambda: self.load_data())
        self.ButtonShiji.clicked.connect(lambda: self.actual_curve())
        self.ButtonPiancha.clicked.connect(lambda: self.DCE())
        self.ButtonPinding.clicked.connect(lambda: self.evaluation())
        self.ButtonQingchu.clicked.connect(lambda: self.clear())
        self.ButtonSave.clicked.connect(lambda: self.save())
        self.ButtonClose.clicked.connect(lambda: QCoreApplication.quit())

        #################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "参数设置："))
        self.label_2.setText(_translate("MainWindow", "测头半径(mm)："))
        self.label_3.setText(_translate("MainWindow", "采样间隔(deg)："))
        self.label_4.setText(_translate("MainWindow", "样板旋转角度(deg)："))
        self.groupBox_2.setTitle(_translate("MainWindow", "测量数据："))
        self.groupBox_3.setTitle(_translate("MainWindow", "评定结果："))
        self.label_7.setText(_translate("MainWindow", "最大误差值(um)："))
        self.label_8.setText(_translate("MainWindow", "曲线拟合标准差(um)："))
        self.label_9.setText(_translate("MainWindow", "V点和B点距离(um)："))
        self.label_10.setText(_translate("MainWindow", "压力角误差(um/deg)："))
        self.label_11.setText(_translate("MainWindow", "B点增益误差："))
        self.label_12.setText(_translate("MainWindow", "B点滞后误差："))
        self.label_13.setText(_translate("MainWindow", "谷底增益误差："))
        self.label_14.setText(_translate("MainWindow", "谷底滞后误差："))
        self.label_15.setText(_translate("MainWindow", "补偿参数："))
        self.ButtonLilun.setText(_translate("MainWindow", "理论曲线"))
        self.ButtonDaoru.setText(_translate("MainWindow", "导入测量数据"))
        self.ButtonShiji.setText(_translate("MainWindow", "实际曲线"))
        self.ButtonPiancha.setText(_translate("MainWindow", "评定偏差曲线"))
        self.ButtonPinding.setText(_translate("MainWindow", "评定结果"))
        self.ButtonSave.setText(_translate("MainWindow", "保存"))
        self.ButtonQingchu.setText(_translate("MainWindow", "清除"))
        self.ButtonClose.setText(_translate("MainWindow", "关闭"))

    #################################################################

    def theoretical_curve(self):
        print(">>>>>>>>>>>>>>>>>>>> theoretical_curve >>>>>>>>>>>>>>>>>>>>>>>>>")
        # 将所有数据都float化！！！
        std_z = 40.0  # 这是啥来的忘了好像用不上
        std_e = 28.5648595796  # 这是啥来的忘了好像用不上
        std_rb = 400.0  # 样板模拟齿轮的基圆半径
        std_rp = 1.5  # 齿轮测量仪器的测头半径(但是是用户导入的数据，所以暂时用不上)
        std_m = 21.28355545  # 这是啥来的忘了好像用不上
        std_c = 401.583156  # 定心轴和测量中心轴的距离
        std_rc = 105.102  # 检测圆弧半径
        # if (str(input_rp).split(".")[0]).isdigit() or str(input_rp).isdigit() or (str(input_rp).split('-')[-1]).split(".")[
        #     -1].isdigit():
        #     pass
        # else:
        #     QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), '错误', '请输入正确的测头半径')
        #     return 0
        input_rp = float(self.textEditCetou.value())  # 齿轮测量仪器的测头半径(用户输入)
        if input_rp == 0.0:
            input_rp = 1.5  # default
        input_interval = float(self.textEditCaiyang.value())  # 采样间隔
        if input_interval == 0.0:
            input_interval = 0.001  # default
        input_rotationAngle = float(self.textEditXuanzhuan.value())  # 样板的旋转角度ε
        if input_rotationAngle == 0.0:
            input_rotationAngle = 28.0  # default
        self.theoretical_X_list, self.theoretical_Y_list = Functions.culculate_curve(std_rc, input_rp, std_c, std_rb,
                                                                                     input_rotationAngle,
                                                                                     input_interval)
        Draw.one_line(self.theoretical_X_list, self.theoretical_Y_list, title='Theoretical Image',
                      save_path=r'./检测结果/理论图像.jpg')  # 绘制图片
        self.show_pic(save_path=r'./检测结果/理论图像.jpg')  # 加载图片

        print("<<<<<<<<<<<<<<<<<<<< theoretical_curve <<<<<<<<<<<<<<<<<<<<<<<<<")

    def load_data(self):
        print(">>>>>>>>>>>>>>>>>>>> load_data >>>>>>>>>>>>>>>>>>>>>>>>>")
        self.data_dict = IO.load_data()
        data_str = ''
        for key, value in self.data_dict.items():
            data_str = data_str + str(key) + ':' + str(value) + '\n'
        self.textEditCeliangshuju.setText(data_str)
        print("<<<<<<<<<<<<<<<<<<<< load_data <<<<<<<<<<<<<<<<<<<<<<<<<")

    def actual_curve(self):  # 实际曲线
        print(">>>>>>>>>>>>>>>>>>>> actual_curve >>>>>>>>>>>>>>>>>>>>>>>>>")
        input_rp = float(self.textEditCetou.value())  # 齿轮测量仪器的测头半径(用户输入)
        if input_rp == 0.0:
            input_rp = 1.5  # default
        input_interval = float(self.textEditCaiyang.value())  # 采样间隔
        if input_interval == 0.0:
            input_interval = 0.001  # default
        input_rotationAngle = float(self.textEditXuanzhuan.value())  # 样板的旋转角度ε
        if input_rotationAngle == 0.0:
            input_rotationAngle = 28.0  # default
        print(input_rotationAngle)
        self.actual_X_list, self.actual_Y_list = Functions.culculate_curve(self.data_dict['rc'], input_rp,
                                                                           self.data_dict['C'],
                                                                           self.data_dict['rb'], input_rotationAngle,
                                                                           input_interval)
        Draw.one_line(self.actual_X_list, self.actual_Y_list, title='Actual Image',
                      save_path=r'./检测结果/实际图像.jpg')  # 绘制图片
        self.show_pic(save_path=r'./检测结果/实际图像.jpg')  # 加载图片
        print("<<<<<<<<<<<<<<<<<<<< actual_curve <<<<<<<<<<<<<<<<<<<<<<<<<")

    def DCE(self):  # 评定偏差曲线：DCE = 实际曲线 - 理论曲线
        print(">>>>>>>>>>>>>>>>>>>> DCE >>>>>>>>>>>>>>>>>>>>>>>>>")
        self.DCE_X_list = self.theoretical_X_list
        self.DCE_Y_list = []
        for i in range(len(self.DCE_X_list)):
            print(i)
            self.DCE_Y_list.append(self.actual_Y_list[i] - self.theoretical_Y_list[i])
        Draw.one_line(self.DCE_X_list, self.DCE_Y_list, title='DCE Image',
                      save_path=r'./检测结果/平定偏差图像.jpg')  # 绘制图片
        self.show_pic(save_path=r'./检测结果/平定偏差图像.jpg')  # 加载图片
        print("<<<<<<<<<<<<<<<<<<<< DCE <<<<<<<<<<<<<<<<<<<<<<<<<")

    def evaluation(self):
        print(">>>>>>>>>>>>>>>>>>>> evaluation >>>>>>>>>>>>>>>>>>>>>>>>>")
        # V：理论驼峰曲线谷底的点
        # B：理论驼峰曲线第二个峰值点
        Y_B, X_B, Y_V, X_V = Functions.culculate_V_B(self.theoretical_X_list, self.theoretical_Y_list)
        print("谷底的点({},{}),第二个峰值点({},{})".format(X_V, Y_V, X_B, Y_B))
        # 最大误差值
        fk_X_list, fk_Y_list = Functions.culculate_fafk(self.DCE_X_list, self.DCE_Y_list)
        min_y = min(fk_Y_list)
        min_x = fk_X_list[fk_Y_list.index(min_y)]
        max_y = max(fk_Y_list)
        max_x = fk_X_list[fk_Y_list.index(max_y)]
        print("Fafk范围内最小值({},{}),最大值({},{})".format(min_x, min_y, max_x, max_y))
        self.textEditWucha.setValue((max_y - min_y) * 1000)  # 转换单位
        # 曲线拟合标准差
        deviation = 0.0
        for i in fk_Y_list:
            deviation = deviation + math.pow(i, 2)
        deviation = math.sqrt(deviation) * 1000 / (len(fk_Y_list) - 1)
        print("曲线拟合标准差 {}".format(deviation))
        self.textEditBiaozhuncha.setValue(deviation)
        # V点和B点距离
        V_index = self.DCE_X_list.index(X_V)
        B_index = self.DCE_X_list.index(X_B)
        distance = abs(self.DCE_Y_list[V_index] - self.DCE_Y_list[B_index]) * 1000
        print('V点和B点距离 {}'.format(distance))
        self.textEditJuli.setValue(distance)
        # 压力角误差
        yalijiao = distance * 1000 / (X_B - X_V)
        print('压力角误差 {}'.format(yalijiao))
        self.textEditYalijiao.setValue(yalijiao)
        print("<<<<<<<<<<<<<<<<<<<< evaluation <<<<<<<<<<<<<<<<<<<<<<<<<")

    def save(self):
        print(">>>>>>>>>>>>>>>>>>>> save >>>>>>>>>>>>>>>>>>>>>>>>>")
        save_data = {
            '测头半径(mm)：': self.textEditCetou.value(),
            '采样间隔(deg)：': self.textEditCaiyang.value(),
            '样板旋转角度(deg)：': self.textEditXuanzhuan.value(),
            '最大误差值(um)：': self.textEditWucha.value(),
            '曲线拟合标准差(um)：': self.textEditBiaozhuncha.value(),
            'V点和B点距离(um)：': self.textEditJuli.value(),
            '压力角误差(um/deg)：': self.textEditYalijiao.value()
        }
        print('保存数据 {}'.format(save_data))
        print("<<<<<<<<<<<<<<<<<<<< save <<<<<<<<<<<<<<<<<<<<<<<<<")

    def clear(self):  # 清除所有数据和曲线
        print(">>>>>>>>>>>>>>>>>>>> clear >>>>>>>>>>>>>>>>>>>>>>>>>")
        self.textEditCetou.clear()
        self.textEditCaiyang.clear()
        self.textEditXuanzhuan.clear()
        self.textEditWucha.clear()
        self.textEditBiaozhuncha.clear()
        self.textEditJuli.clear()
        self.textEditYalijiao.clear()
        self.textEditCeliangshuju.clear()
        print("<<<<<<<<<<<<<<<<<<<< clear <<<<<<<<<<<<<<<<<<<<<<<<<")

    # def close_window(self):  # 关闭程序
    #     self.

    def show_pic(self, save_path='line.jpg'):
        print(">>>>>>>>>>>>>>>>>>>> show_pic >>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(save_path)
        img = cv2.imdecode(np.fromfile(save_path, dtype=np.uint8), -1)  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        # self.zoomscale = 1  # 图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)  # 将场景添加至视图
        print("<<<<<<<<<<<<<<<<<<<< show_pic <<<<<<<<<<<<<<<<<<<<<<<<<")


#################################################################


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
