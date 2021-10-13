import matplotlib.pyplot as plt
import pandas as pd

# 添加文件名即可，最多九个
name = ['full_wave.csv',
        'cor_wavelength.csv',
        'wave_noclass.csv',
        'wave_2class.csv',
        'wave_3class.csv']


sign = ['+', 'x', '*', 'o', 'v', '^', '_', 'h', '.']  # 符号
gap = 5  # 间隔

plt.figure(figsize=(9, 3.5))
ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
for i in range(len(name)):
    y = pd.read_csv(name[i])
    y = y.values.T[0]
    y = y[::gap]
    plt.scatter([i + 1000 for i in y], [i+1] * len(y), marker=sign[i], s=30, label=name[i][:-4])

plt.scatter([1000]*605, [len(name)+1]*605, alpha=0)
plt.scatter([1000]*605, [len(name)+2]*605, alpha=0)
plt.scatter([1000]*605, [0]*605, alpha=0)
# plt.legend()
plt.legend( loc = "upper center",ncol=5)    #生成legend
# plt.legend(ncol=5)
plt.yticks([])
plt.show()
