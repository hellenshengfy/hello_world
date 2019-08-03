import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fifa=pd.read_csv('FIFA_data.csv')
#柱状图
# # pd.set_option('display.max_columns', None)
# # pd.set_option('display.max_row', None)
# # print(fifa)
# bins=np.arange(40,110,10)
# #print(bins)
# plt.hist(fifa['Overall'],bins=bins,color='#33CC66') #颜色自已去网上搜色板，一点就有号码
#
# plt.ylabel('Number of Players')
# plt.xlabel('Skill level')
#
# plt.title('Distribution of Player Skills in FIFA 2018',fontdict={'fontweight':'bold','size':14})
# #plt.show()

# ####饼状图
# left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
# right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
# #print(left)
# #print(right)
#
# # labels=['Left','Right']
# # colors=['red','blue']
# # plt.pie([left,right],labels=labels,colors=colors,autopct='%.2f%%')
# # plt.title('Foot Preference in FIFA Players 2018', fontdict={'fontweight': 'bold', 'size': 14})
# # plt.show()
#
# ###
# #print(fifa.Weight)
# #去掉单位的影响
# fifa.Weight=[int(x.strip('lbs')) if type(x)==str else x for x in  fifa.Weight]
# #print(fifa.Weight)
# light=fifa.loc[fifa.Weight<125].count()[0] #light=fifa.loc[fifa.Weight<125].count()能够根据体重筛选数据，且把所有列的计数都显示出来，都是重复的，故【0】这里任意挑选第一个
# light_medium=fifa.loc[(fifa.Weight>=125) & (fifa.Weight<150)].count()[0]
# medium=fifa.loc[(fifa.Weight>=150) & (fifa.Weight<175)].count()[0]
# medium_heavy=fifa.loc[(fifa.Weight>=175) & (fifa.Weight<200)].count()[0]
# heavy=fifa.loc[fifa.Weight>200].count()[0]
#
# plt.style.use('ggplot')
# weight=[light,light_medium,medium,medium_heavy,heavy]
# labels=['Under 125','125-150','150-175','175-200','Over 200']
# explode=(.2,.1,0,.03,.3)
# plt.pie(weight,labels=labels,autopct='%.2f%%',pctdistance=0.8,explode=explode)
# plt.title('Weight Distribution of Player in FIFA 2018', fontdict={'fontweight': 'bold', 'size': 14})
# plt.legend(loc='lower left')
# plt.show()
plt.figure(figsize=(5,8))
barcelona=fifa.loc[fifa.Club=='FC Barcelona']['Overall']
print(barcelona)
madrid=fifa.loc[fifa.Club=='Real Madrid']['Overall']
revs=fifa.loc[fifa.Club=='New England Revolution']['Overall']
labels=['Barcelona','Madrid','NE Revolution']
boxes=plt.boxplot([barcelona,madrid,revs],labels=labels,medianprops={'linewidth':3},patch_artist=True) #patch_artist是为了后面设置填充色而写的
for box in boxes['boxes']: #改变box的颜色等设定
    box.set(linewidth=2,facecolor='red')
plt.title('Professional Football Team Comparison', fontdict={'fontweight': 'bold', 'size': 14})
plt.ylabel('FIFA overall rating')

plt.show()