# -*- encoding: utf-8 -*-

# import pymongo
import numpy as npy
import pandas as pda
import matplotlib.pylab as pyl

'''
探究课程小节平均时长与学员数的关系
'''

pyl.rcParams['font.sans-serif'] = ['SimHei']  # 使图像中能显示中文

# 从csv中读数据
data = pda.read_csv("jkxy.csv", encoding="gbk")

course_times = data["course_time"].T
course_nums = data["course_num"].T
course_times_avg = []
for course_time, course_num in zip(course_times, course_nums):
    course_times_avg.append(course_time/course_num)
x = pda.Series(course_times_avg)
y = data["students"].T
pyl.title("小节平均时长-学员数局部散点视图")
pyl.xlabel("小节平均时长")
pyl.ylabel("学员数")

# 得到总视图
# pyl.plot(x, y, "o")
# pyl.show()

# 得到局部视图
pyl.xlim(0, 40)
pyl.ylim(2000, 40000)

pyl.plot(x, y, "o")
pyl.show()


'''
分析结论：
1.从总视图来看，大趋势比课程时长-学员数更为清晰，并且可以说，没有出乎意料的数据出现
2.从局部视图来看，密集区域更接近正态分布，而正态分布的期望约是7分钟。
所以说，我们可以推断出，在课程质量相近的前提下，网络课将时间定在每小节7分钟更能吸引学员，
让学员有耐心听完。
'''


