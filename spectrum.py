# coding = utf-8
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import matplotlib.font_manager as mpt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 导入数据
file = '1400_30_spectrum.txt'
a = np.loadtxt(file)

plt.ion()           # 开启一个画图的窗口进入交互模式，用于实时更新数据
for i in range(60):
    plt.cla()                   # 清除刷新前的图表，防止数据量过大消耗内存
    x = np.arange(0, 800, 1)    # 取第二列数据
    y = a[i * 800:(i + 1) * 800]  # 取第第一个800点数据
    plt.plot(x, y, ls="--", lw=2, c="b", label='spectrum figure')
    plt.legend(loc='upper right')
    plt.xlabel('FFT点数:0-800')
    plt.ylabel('电平值 : dBuv * 100')
    plt.title('单频测量频谱图')

    # plt.show()
    plt.pause(0.2)              # 设置暂停时间，太快图表无法正常显示\
    
plt.ioff()       # 关闭画图的窗口，即关闭交互模式
plt.show()       # 显示图片，防止闪退
