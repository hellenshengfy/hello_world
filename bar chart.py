import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#数据输入
labels=['A','B','C']
values=[1,4,2]
#画布大小、清晰度设定
plt.figure(figsize=(5,3),dpi=200)
#作图
bars=plt.bar(labels,values)
#给每一个画不同的符号
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
#上面3条语句相当于下面3条语句，当条数很多的时候可以用
# patterns=['/','o','*']
# for bar in bars:
#     bar.set_hatch(patterns.pop(0))

plt.title('My_bar_graph',fontdict={'fontname': 'Times New Roman', 'weight': 'normal', 'size': 15})
plt.xlabel('x-axis',fontdict={'fontname':'Arial'})
plt.ylabel('y-axis',fontdict={'fontname':'Arial'})

plt.show()