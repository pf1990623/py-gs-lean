import sys
import os
# BaseDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(BaseDir)
# """
# os.path.abspath(__file__)   当前的相对路径修改为绝对路径
#
# """
# Basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BaseDir)
# print(os.path.dirname(__file__))   # 打印当前目录
# print(__file__)
# sys.path.append()
# for i in sys.path:
#     print(i)
"""
调用当前目录的下的模块，使用import 函数名称  或者 from  模块名  import  函数名称
如果想调用上级目录下的 模块，直接使用import 或 from方式会报错的
这个时候就得使用  from 上级目录名 import 函数方法
__file__ 是相对路径
os.path.abspath(__file__) #把相对路径修改为绝对路径
python 程序当前目录，是当前执行的py程序所在的目录为程序发起的目录
脚本所在的目录为当前目录
"""

"""
模块使用相对路径方法
使用相对路径

"""
#  此种方法使用绝路径，对python多环境情况下，就会出现问题，不能对环境迁移到别的程序
#
# sys.path.append("D:\python-gs-lean>")
# print(sys.path)
# 使用相对路径方法

print(__file__)
# D:/py-gs-lean/student_day4/模块.py
# 打印当前程序的文件名
print(os.path.dirname(__file__))
# D:/py-gs-lean/student_day4
# 后去当前目录
print(os.path.dirname(os.path.dirname(__file__)))
# 获取到顶级目录
# D:/py-gs-lean
print(sys.path)
print("----------")
# 打印当前目录的上一级目录，os.path.abspath(__file__) 去掉文件名的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))
Basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Basedir)
# 打印当前目录的上一级目录的上一级目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 打印所有可以搜索模块的路径
print(sys.path)
"""
__file__相对路径
os.path.abs.path(__file__)把相对路径变为绝对路径
os.path.dirname()相当于返回上一层
os.path.dirname(os.path.dirname())返回上级的上级
如果想在任何目录下调用任何目录下的函数方法，就需要添加如下：
os.path.dirname()根据需求剥离多少层就调用就可以使用偶数os.path.dirname()层层嵌套的方法
Basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Basedir)
"""
from student_day3 import oldboy2
oldboy2.xiao()

