# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def one_line(x, y, title='Curve', save_path='line.jpg'):
    print(">>>>>>>>> Draw >>> one_line >>>>>>>>>>")
    # X轴，Y轴数据
    # x = [0, 1, 2, 3, 4, 5, 6]
    # y = [0.3, 0.4, 2, 5, 3, 4.5, 4]
    plt.figure(figsize=(8, 4))  # 创建绘图对象
    plt.plot(x, y, "b--", linewidth=1)  # 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
    plt.xlabel("Rotation Angle(deg)")  # X轴标签
    plt.ylabel('Deviation(μm)')  # Y轴标签
    plt.title(title)  # 图标题
    # plt.show()  # 显示图
    plt.savefig(save_path)  # 保存图
    print("<<<<<<<<< Draw <<< one_line <<<<<<<<<<")


if __name__ == "__main__":
    one_line([1,2,3], [1,2,3], title='理论图像', save_path=r'./检测结果/理论图像.jpg')  # 绘制图片
