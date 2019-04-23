# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def one_line(x, y, title='Curve', save_path='line.jpg'):
    print(">>>>>>>>> Draw >>> one_line >>>>>>>>>>")
    # X轴，Y轴数据
    # x = [0, 1, 2, 3, 4, 5, 6]
    # y = [0.3, 0.4, 2, 5, 3, 4.5, 4]
    plt.figure(figsize=(6, 4))  # 创建绘图对象
    plt.plot(x, y, "b--", linewidth=1)  # 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
    plt.xlabel("Rotation Angle(deg)")  # X轴标签
    plt.ylabel('Deviation(μm)')  # Y轴标签
    plt.title(title)  # 图标题

    # ax = subplot(111)  # 注意:一般都在ax中设置,不再plot中设置
    # xmajorLocator = MultipleLocator(5)  # 将x主刻度标签设置为20的倍数
    # xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
    # xminorLocator = MultipleLocator(2.5)  # 将x轴次刻度标签设置为5的倍数
    #
    # ymajorLocator = MultipleLocator(2)  # 将y轴主刻度标签设置为0.5的倍数
    # ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
    # yminorLocator = MultipleLocator(1)  # 将此y轴次刻度标签设置为0.1的倍数
    # # 设置主刻度标签的位置,标签文本的格式
    # ax.xaxis.set_major_locator(xmajorLocator)
    # ax.xaxis.set_major_formatter(xmajorFormatter)
    #
    # ax.yaxis.set_major_locator(ymajorLocator)
    # ax.yaxis.set_major_formatter(ymajorFormatter)
    #
    # # 显示次刻度标签的位置,没有标签文本
    # ax.xaxis.set_minor_locator(xminorLocator)
    # ax.yaxis.set_minor_locator(yminorLocator)

    # plt.show()  # 显示图
    plt.savefig(save_path)  # 保存图
    print("<<<<<<<<< Draw <<< one_line <<<<<<<<<<")


def two_lines(x, y_the, y_act, title='Curve', save_path='line.jpg'):
    print(">>>>>>>>> Draw >>> one_line >>>>>>>>>>")

    # migtime = [16.6, 16.5, 16.9, 17.1, 17.2, 18.1, 18.2, 18.4, 19.4, 19.3, 20.4, 20.3, 22, 21.7, 22]
    # delay = [108, 98, 92, 83, 87, 77, 85, 48, 31, 58, 35, 43, 36, 31, 19]

    plt.figure(figsize=(6, 4))  # 创建绘图对象
    fig, ax = plt.subplots()

    plt.xlabel("Rotation Angle(deg)")  # X轴标签
    plt.ylabel('Deviation(μm)')  # Y轴标签

    """set interval for y label"""
    yticks = range(10, 110, 10)
    ax.set_yticks(yticks)

    # """set min and max value for axes"""
    # ax.set_ylim([10, 110])
    # ax.set_xlim([58, 42])

    # x = [57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43]
    plt.plot(x, y_act, "x-", label="Actual Curve")
    plt.plot(x, y_the, "+-", label="Theoretical Curve")

    """open the grid"""
    # plt.grid(True)

    plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
    plt.title(title)  # 图标题

    # plt.show()
    plt.savefig(save_path)  # 保存图
    print("<<<<<<<<< Draw <<< one_line <<<<<<<<<<")

if __name__ == "__main__":
    two_lines(1,1,1)
    # one_line([-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,
    #  10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0,
    #  29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0], [-1.56, -1.19, -0.87, -0.62, -0.4, -0.26, -0.14, -0.066, -0.019, 0.0055, 0.01, 0.0011, -0.017, -0.044, -0.074,
    #  -0.11, -0.13, -0.13, -0.15, -0.18, -0.19, -0.19, -0.18, -0.15, -0.13, -0.11, -0.078, -0.052, -0.026, -0.006,
    #  0.0038, -0.000122, -0.022, -0.066, -0.14, -0.22, -0.41, -0.59, -0.84, -1.15, -1.51, -1.91, -2.49, -3.09, -3.81,
    #  -4.69, -5.55, -6.66, -7.94, -9.33, -10.9], title='Image', save_path=r'./检测结果/理论图像.jpg')  # 绘制图片
