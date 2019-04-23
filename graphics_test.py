from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import cv2
import math
import IO


class MyWindow(object):
    def __init__(self):
        super().__init__()
        #     self.myButton = QtWidgets.QPushButton(self)
        #
        #     self.myButton.clicked.connect(self.msg)
        #
        # def msg(self):
        aaa = QtWidgets.QMessageBox()
        print(3)
        aaa.about(QtWidgets.QMessageBox(), '窗口标题', '提示信息')


if __name__ == "__main__":
    # import sys
    #
    # app = QtWidgets.QApplication(sys.argv)
    # myshow = MyWindow()
    # myshow.show()
    # sys.exit(app.exec_())

    # X_FK = 28.0
    fk_Y_list = [2, 2, 2, 2, 2]
    # fk_list = []
    # for i in DCE_X_list:
    #     print(i)
    #     if i >= 0.0 and i <= 28.0:
    #         fk_list.append(i)
    # print(fk_list)

    # deviation = 0.0
    # for i in fk_Y_list:
    #     deviation = deviation + math.pow(i, 2)
    # deviation = math.sqrt(deviation) / (len(fk_Y_list) - 1)
    # print(deviation)
    x_list = []
    y_list = []
    with open('1.txt', 'r') as f:
        for line in f.readlines():
            sign = True
            # print(line)
            line = str(line.strip())  # 把末尾的'\n'删掉
            # print(line)
            # print(line.split(','))
            # print(list(line))
            x_list.append(line.split(',')[0])
            y_list.append(line.split(',')[1])

            # print(x, y)
            # print(11111111111111111)
            # for i in list(str):
            #     print('i={}'.format(i))
            #     if i == ',':
            #         print(000)
            #         sign = True  # True是横坐标，False是纵坐标
            #         continue
            #     if sign == True:
            #         x_list.append(i)
            #         sign = False
            #         print(222)
            #     else:
            #         y_list.append(i)
            #         sign = True
            #         print(333)

    print(x_list)
    print(y_list)
