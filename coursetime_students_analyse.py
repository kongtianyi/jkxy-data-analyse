# -*- encoding: utf-8 -*-

# import pymongo
import pandas as pda
import matplotlib.pylab as pyl

'''
探究课程时长与学员数的关系
'''

pyl.rcParams['font.sans-serif'] = ['SimHei']  # 使图像中能显示中文

# 从MongoDB读数据
# client = pymongo.MongoClient("localhost", 27017)
# db = client["spider"]
# coll = db["jkxy"]
# data = pda.DataFrame(list(coll.find()))
# del data["_id"]

# 从csv中读数据
data = pda.read_csv("jkxy.csv", encoding="gbk")
data = data[["course_time", "students"]]

x = data.T.values[0]
y = data.T.values[1]
pyl.title("课程时长-学员数局部散点视图1")
pyl.xlabel("课程时长")
pyl.ylabel("学员数")

# 得到总视图
# pyl.plot(x, y, "o")
# pyl.show()

# 得到局部视图1
# pyl.xlim(0,200)
# pyl.ylim(0, 40000)

pyl.xlim(0,80)
pyl.ylim(0, 10000)
pyl.plot(x, y, "o")
pyl.show()

'''
分析结论：
1.根据总视图看，学员数与课程时长成近似反比关系，即课程时长越长，学员数越少。
2.根据局部视图看，绝大部分课程学员数在2000以上，我们知道极客学院是有VIP机制的，即
很多课程需要有VIP权限才能观看，所以可以判断，
极客学院的活跃VIP保持在2000以上。而学员数较密集的区间是[2000,10000]，可以推断，大约每五个观看过
极客学院视频的学员就有一个购买了VIP，极客学院的课程吸引力不言而喻。
3.在这里尚不能断定课程总时长与学员数的必然联系，比如在总视图中，有一异常点，课程时长1400
分钟，观看人数6万人，在数据库中找到此条记录后发现，这个课程包含79小节，所以，是不是小节
时长对观看人数的影响更为明显，联系更大呢？我们再进行后续分析。
'''


