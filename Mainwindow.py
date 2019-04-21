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
import cv2


###############################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(220, 90, 541, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 170, 110))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textEditCetou = QtWidgets.QDoubleSpinBox(self.groupBox)
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
        self.groupBox_3.setGeometry(QtCore.QRect(790, 120, 261, 441))
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
        self.textEditBuchang_2 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.textEditBuchang_2.setObjectName("textEditBuchang_2")
        self.horizontalLayout_12.addWidget(self.textEditBuchang_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 390, 82, 271))
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
        # MainWindow.setCentralWidget(self.centralwidget)
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
        self.groupBox.setTitle(_translate("MainWindow", "参数设置："))
        self.label_2.setText(_translate("MainWindow", "测头半径："))
        self.textEditCetou.setSuffix(_translate("MainWindow", "mm"))
        self.label_3.setText(_translate("MainWindow", "采样间隔："))
        self.textEditCaiyang.setSuffix(_translate("MainWindow", "deg"))
        self.label_4.setText(_translate("MainWindow", "样板旋转角度："))
        self.textEditXuanzhuan.setSuffix(_translate("MainWindow", "deg"))
        self.groupBox_2.setTitle(_translate("MainWindow", "测量数据："))
        self.groupBox_3.setTitle(_translate("MainWindow", "评定结果："))
        self.label_7.setText(_translate("MainWindow", "最大误差值："))
        self.textEditWucha.setSuffix(_translate("MainWindow", "um"))
        self.label_8.setText(_translate("MainWindow", "曲线拟合标准差："))
        self.textEditBiaozhuncha.setSuffix(_translate("MainWindow", "um"))
        self.label_9.setText(_translate("MainWindow", "V点和B点距离："))
        self.textEditJuli.setSuffix(_translate("MainWindow", "deg"))
        self.label_10.setText(_translate("MainWindow", "压力角误差："))
        self.textEditYalijiao.setSuffix(_translate("MainWindow", "um/deg"))
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
        print(">>>>>>>>>>>>>>>>>>>>theoretical_curve>>>>>>>>>>>>>>>>>>>")
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
        input_rp = float(self.textEditCetou.value())  # 齿轮测量仪器的测头半径
        if input_rp == 0.0:
            input_rp = 1.5  # default
        input_interval = float(self.textEditCaiyang.value())  # 采样间隔
        if input_interval == 0.0:
            input_interval = 0.001  # default
        input_rotationAngle = float(self.textEditXuanzhuan.value())  # 样板的旋转角度ε
        if input_rotationAngle == 0.0:
            input_rotationAngle = 28.0  # default
        X_list = []
        Y_list = []
        list_num = int(input_rotationAngle / input_interval)
        print(list_num)
        for i in range(-10, list_num+1):
            print(i)
            current_rotationAngle = input_rotationAngle * (i + 1) / list_num
            X_list.append(current_rotationAngle)
            Y_result = Functions.func1(std_rc, input_rp, std_c, std_rb, current_rotationAngle)
            Y_list.append(Y_result)
        print(X_list)
        print(Y_list)
        Draw.one_line(X_list, Y_list)  # 绘制图片
        # 加载图片
        img = cv2.imread("line.jpg")  # 读取图像
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

        print("<<<<<<<<<<<<<<<theoretical_curve<<<<<<<<<<<<<<<<<<<<")

    def actual_curve(self):  # 实际曲线
        input_rp = self.textEditCetou.value()  # 齿轮测量仪器的测头半径(用户输入)
        input_interval = float(self.textEditCaiyang.value())  # 采样间隔
        input_rotationAngle = float(self.textEditXuanzhuan.value())  # 样板的旋转角度ε
        # todo: 用实际导入数据计算

    def DCE(self):  # 评定偏差曲线：DCE = 实际曲线 - 理论曲线
        theoretical_list = IO.load_cache('theoretical_list')
        actual_list = IO.load_cache('actual_list')
        # todo:偏差曲线

    def evaluation(self):
        DCE_list = IO.load_cache('DCE_list')
        # todo:所有评定结果的计算

    def save(self):  # 清除所有数据和曲线
        a = 1  # todo:保存按钮

    def close_window(self):  # 关闭程序
        a = 1  # todo:关闭程序


#################################################################


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
