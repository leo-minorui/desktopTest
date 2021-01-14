# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# some simple data
x = [1,2,3,4]
y = [5,4,3,2]
#create new figure
#激活图表 接下来的绘图都在该图表上进行
plt.figure()
#divide subplots into 2*3 grid
#and select#1
plt.subplot(231) #plt.subplot(2,3,1)
#第一个表示行数，第二个表示列数，第三个表示图形标号
plt.plot(x,y)
#select #2
#bar()垂直柱状图
plt.subplot(232)
plt.bar(x, y)
#barh()水平柱状图
plt.subplot(233)
plt.barh(x,y)
#堆叠柱状图
plt.subplot(234)
plt.bar(x, y)
y1 = [7,8,5,3]
plt.bar(x, y1, bottom=y, color= 'r')
#箱线图
plt.subplot(235)
plt.boxplot(x)
#散点图
plt.subplot(236)
plt.scatter(x,y)
plt.show()