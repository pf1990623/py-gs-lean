import time
import datetime

print(time.clock())
print(time.process_time())   # 返回处理器时间
print(time.altzone)  # 返回与utc的时间差，以秒计算，格林威治时间
print(time.asctime())  # 返回时间格式
print(time.localtime())  # 返回本地时间的struct time对象格式，也可以进行时间计算
t = time.localtime()
print(t.tm_year, t.tm_mday)
print(time.time()/(3600*24*365))  # 时间戳，从unix诞生到现在多少年
print(time.gmtime())     # utc Time
print(time.gmtime(time.time()-800000))  # 返回utc时间的struct时间对象格式,时间戳,做时间运算


print(time.ctime())  # ctime()方法和localtime打印方法一样
print(time.asctime(time.localtime()))  # 和楼上的方法一样
