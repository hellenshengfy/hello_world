import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)

#读数据
gas=pd.read_csv('gas_prices.csv')
#print(gas)

plt.figure(figsize=(10,6))
for country in gas.columns[1:]:
    #print(country)
    plt.plot(gas['Year'],gas[country],marker='.',label=country)
#一个一个画：
 # plt.plot(gas['Year'],gas['USA'],'b.-',label='USA',) #'b.-’对应蓝色，数据点为点，线段为线条
 # # 也可以写成：plt.plot(gas.Year,gas.USA)
 # plt.plot(gas['Year'],gas['Canada'],'r.-',label='Canada')
 # plt.plot(gas['Year'],gas['South Korea'],'g.-',label='South Korea')
 # plt.plot(gas['Year'],gas['Australia'],'y.-',label='Australia')

plt.title('Gas Prices over Time(in USD)',fontdict={'fontweight':'bold','size':18})
plt.xlabel('Year')
plt.ylabel('US dollars')
plt.xticks(gas['Year'][::3].tolist()+[2010]) #每三年取一个值作为X数轴数,并增加2019年
plt.legend(loc='upper left',ncol=3)
#bbox...是把图例位置进行左右上下微调，也可以直接写plt.legend()自动找位置
plt.show()
plt.savefig('Gas_Price_figure.png',dpi=300)
