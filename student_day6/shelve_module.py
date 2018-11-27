import shelve
"""
shelve模块是一个简单的k,v将内存的数据文件持久化到模块，可以持久化任何pickle可支持的python数据文件格式


"""

d = shelve.open('shelve_test')  # 打开一个文件

def stu_data(name, age):
    print("register stu", name, age)

name = ['xiaofeng', 'chenjun', 'xxx']

d["test"] = name
d['fun'] = stu_data

