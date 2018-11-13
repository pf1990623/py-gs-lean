# msg='hello world'
# print(msg.capitalize())
# #
# #capitalize()首字母大写
# print(msg.capitalize())
#
# #center(20)将字符串按20的长度进行居住显示
# print(msg.center(20,'*'))
# # count(self, sub, start=None, end=None)
# # count() 统计某一个字符串出现的次数
# # 顾头不顾尾，从4开始，到6结束
# print(msg.count('l',0,7))
# print(msg.count('l',4,-1))
#
# #endswith('d')判断字符串是否以d结尾，如果是以指定的字符串结尾返回true,反之flase
# print(msg.endswith('d'))
#
msg1='a\tb'
# expandtabs(10)执行table键的长度
# print(msg1.expandtabs(10))



#
# # find(str,start=,end=none)  #查找字符串，并打印索引的值，索引是从0开始算，空格也算
# # 如果不存在，返回-1
# # 只要找到的第一个的索引，即使后面还有该字符，也不会打印索引值
# print(msg.find('l',0,-1))
#
# # format()格式化字符串
# # 方式1
# print('{0}{1},{0}'.format('name','age'))
# # 方式2
# print('{name}'.format(name='alber'))
# # 方式3
# print('{}{}'.format('name','age'))
# # format_map()应用于监控
#
# #index() #只取找到的第一个的索引
# print(msg.index('e'))
#
# #isalnum()函数判断是字母和数字的组合或分开
# meg3='a123'
# print(msg.isalnum()) #如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
#
# ##isalpha()判断是否是字母
# print(meg3.isalpha()) #如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
#
# print(msg.isdigit())  #判断是否是整型数字
# print(msg.isdecimal())  #判断是否是10进制
# print(msg.isidentifier())  #判断单词是否包含python中的关键字，如if,while
# print(msg.islower())      #判断是否全部是小写
# print(msg.isprintable())
# print(msg.isspace())#判断是否是空格
# print(msg.istitle())  #判断单词首字母是否是大写
# print(msg.isnumeric()) 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# print(msg.isupper()) #判断是否全部是大写
#
# # msg.join()
# #ljust(self, width, fillchar=None) width指定宽度，fillchar填充字符
# print(msg.ljust()  )      #左对齐
# # rjust(self, width, fillchar=None):
# print(msg.rjust())         #右对齐
# # lower(self)
# print(msg.lower()) #大写转换小写
# # upper(self)
# print(msg.upper())      #小写转换大写
#
# print(msg.replace())  #
# print(msg.rfind())    #
# print(msg.rindex())   #
# print(msg.rpartition())  #
# print(msg.rsplit())    #
#
#
# print(msg.rstrip())    #去掉右边空格
# print(msg.lstrip())    #去掉左边空格
# print(msg.split())     #去掉首尾空格
#
# print(msg.splitlines())  #
# print(msg.startswith())  #以
# print(msg.swapcase())  #将字符串中大写转换为小写，小写转换为大写
#
# print(msg.title())     #以什么开头
# print(msg.translate()) #
# print(msg.zfill(20,))     #

# msg16="my name is abcde"
# table=str.maketrans('abcde','alber')
# print(msg16.translate(table))
# msg17='abc'
# print(msg17.zfill(20))
# msg17.isnumeric()
# print(max(msg17))


# 字符串总结
# 1、移除空白
# msg19='  123456sss'
# print(msg19.strip())

# 字符串切片
# mess='nihao 123'
# print(mess[4:6])
# print(mess[0:3]) # 0 1 2
# print(mess[0:])  # 整体
# print(mess[0:-1]) #从开始到-2
# print(mess[:])  #整体
# print(mess[0::2]) #步长2，默认步长为1
# print(mess[0:7:2])

#round()函数在2.x版本中是四舍五入
#round()函数在3.x版本中是5舍6入
x='ahellobcpab'
if (len(x) % 2) == 1:
    a = round(len(x) / 2)

    print(a)
    print(x[a])
else:
    print("没有中间值")

name='abc'
age = 'a'
if age in name:
    print("age在namezhong")


