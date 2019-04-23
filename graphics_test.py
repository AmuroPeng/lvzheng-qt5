from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator = MultipleLocator(20)  # 将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%1.1f')  # 设置x轴标签文本的格式
xminorLocator = MultipleLocator(5)  # 将x轴次刻度标签设置为5的倍数

ymajorLocator = MultipleLocator(0.5)  # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
yminorLocator = MultipleLocator(0.1)  # 将此y轴次刻度标签设置为0.1的倍数

t = [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,
     10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0,
     29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0]
s = [-1.56, -1.19, -0.87, -0.62, -0.4, -0.26, -0.14, -0.066, -0.019, 0.0055, 0.01, 0.0011, -0.017, -0.044, -0.074,
     -0.11, -0.13, -0.13, -0.15, -0.18, -0.19, -0.19, -0.18, -0.15, -0.13, -0.11, -0.078, -0.052, -0.026, -0.006,
     0.0038, -0.000122, -0.022, -0.066, -0.14, -0.22, -0.41, -0.59, -0.84, -1.15, -1.51, -1.91, -2.49, -3.09, -3.81,
     -4.69, -5.55, -6.66, -7.94, -9.33, -10.9]

ax = subplot(111)  # 注意:一般都在ax中设置,不再plot中设置
plot(t, s, '--b*')

# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

# 显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

# ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
# ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

show()
savefig("./1.jpg")
