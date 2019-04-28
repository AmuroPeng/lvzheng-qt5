# -*- coding: utf-8 -*-
import math
import csv
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import scipy.signal as signal


# 老需求：导入参数计算
def culculate_curve(std_rc, input_rp, std_c, std_rb, input_rotationAngle, input_interval):
    print(">>>>>>>>> Function >>> culculate_curve >>>>>>>>>>")
    X_list = []
    Y_list = []
    list_start = int(-10.0 / input_interval)
    list_end = int(input_rotationAngle / input_interval)
    # print(list_end)
    for i in range(list_start, list_end + 1):
        # print(i)
        current_rotationAngle = input_rotationAngle * i / list_end
        # print(current_rotationAngle)
        X_list.append(current_rotationAngle)
        # print(X_list)
        Y_result = func1(std_rc, input_rp, std_c, std_rb, current_rotationAngle)
        Y_list.append(Y_result)
    return X_list, Y_list
    print("<<<<<<<<<< Function <<< culculate_curve <<<<<<<<<")


# 新需求：直接导入点坐标
def culculate_curve_via_X(std_rc, input_rp, std_c, std_rb, input_rotationAngle, X_list):
    print(">>>>>>>>> Function >>> culculate_curve >>>>>>>>>>")
    Y_list = []
    # print(list_end)
    for i in X_list:
        Y_result = func1(std_rc, input_rp, std_c, std_rb, i)
        Y_list.append(Y_result)
    return X_list, Y_list
    print("<<<<<<<<<< Function <<< culculate_curve <<<<<<<<<")


def culculate_V_B(X_list, Y_list):
    print(">>>>>>>>> Function >>> culculate_curve >>>>>>>>>>")
    x = np.array(Y_list, dtype=float)  # , dtype = int
    Y_B = x[signal.argrelextrema(x, np.greater)][1]  # 极大值（纵坐标）
    X_B_temp = (signal.argrelextrema(x, np.greater))[0][1]  # 极大值所对的横坐标的索引
    X_B = X_list[X_B_temp]  # 对应的横坐标
    x = np.array(Y_list, dtype=float)  # , dtype = int
    Y_A = x[signal.argrelextrema(x, np.greater)][0]  # 极大值（纵坐标）
    X_A_temp = (signal.argrelextrema(x, np.greater))[0][0]  # 极大值所对的横坐标的索引
    X_A = X_list[X_A_temp]  # 对应的横坐标
    Y_V = (x[signal.argrelextrema(x, np.less)])[0]  # 极小值（纵坐标）
    X_V_temp = (signal.argrelextrema(x, np.less))[0][0]  # 极小值所对的横坐标的索引
    X_V = X_list[X_V_temp]  # 对应的横坐标
    return Y_B, X_B, Y_V, X_V, Y_A, X_A
    # for x,y in zip(X_list,Y_list):
    #     if y>Y_V:
    print("<<<<<<<<<< Function <<< culculate_curve <<<<<<<<<")


def func1(std_rc, input_rp, std_c, std_rb, input_rotationAngle):
    # print("进入Functions.func1")
    temp1 = math.pow(std_rc + input_rp, 2)
    temp5 = (math.pow(std_rb, 2) + math.pow(std_c, 2) - math.pow(std_rc, 2)) / (2 * std_rb * std_c)
    temp6 = input_rotationAngle * math.pi / 180.0
    temp4 = temp6 - math.acos(temp5)
    temp2 = math.pow(std_c * math.cos(temp4) - std_rb, 2)
    temp3 = std_c * math.sin(temp4)
    result = math.sqrt(temp1 - temp2) + temp3 - input_rp - std_rb * temp6
    # print("结束Functions.func1")
    return result


def culculate_fafk(DCE_X_list, DCE_Y_list, FK_start=11.93, FK_end=20.3344):  # 计算最大误差值
    # default FK：11.93°~20.3344°
    fk_X_list = []
    fk_Y_list = []
    for x, y in zip(DCE_X_list, DCE_Y_list):
        if x >= FK_start and x <= FK_end:
            fk_X_list.append(x)
            fk_Y_list.append(y)
    return fk_X_list, fk_Y_list


if __name__ == "__main__":
    std_z = 40.0  # 这是啥来的忘了好像用不上
    std_e = 28.5648595796  # 这是啥来的忘了好像用不上
    std_rb = 400.0  # 样板模拟齿轮的基圆半径
    std_rp = 1.5  # 齿轮测量仪器的测头半径(但是是用户导入的数据，所以暂时用不上)
    std_m = 21.28355545  # 这是啥来的忘了好像用不上
    std_c = 401.583156  # 定心轴和测量中心轴的距离
    std_rc = 105.102  # 检测圆弧半径
    input_rp = 1.5
    input_rotationAngle = 40.0
    input_interval = 0.1
    # print(func1(std_rc, input_rp, std_c, std_rb, 20.0))
    culculate_V_B([1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1])
