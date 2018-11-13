# python_list =['alex','lhf','sijiayong','panfeng']
# linux_list=['xiaoming','laowang','alex','lhf']
#
# both=[]
# for name in linux_list:
#     if name in python_list:
#        both.append(name)
# print(both)

# 集合中的交集
# 集合中的并集
# 集合中的差级
'''
s1={'a',1,2,3,4,5,3,3,5}
print(s1)

python_set= {'alex','lhf','sijiayong','panfeng'}
linux_set= {'xiaoming','laowang','alex','lhf'}
# print(python_set)

print(python_set.intersection(linux_set))    #交集
print(python_set&linux_set)

# 并集
print(python_set|linux_set)
print(python_set.union(linux_set))

# 差集
print(python_set-linux_set)    #
print(linux_set-python_set)

# 对称差集
print(python_set^linux_set)

# 子集 (即包含的关系)
print(python_set>=linux_set)

# 父级
print(python_set <= linux_set)
'''


# 集合的内置方法
# 更新,通常连个集合update
s1={1,2,3}
s1.update('e')
print(s1)
s1.update((1,2,3,4))
print(s1)
s2={'h','e'}
s1.update(s2)
print(s1)
s1.update('hell')
print(s1)

# 增加
s1.add('hello')
print(s1)

# 删除,随机删除
s1.pop()
print(s1)

# 指定删除,如果不存在。remove就报错
# s1.remove('a')
print(s1)

s1.discard('w')
print(s1)


#字符编码
# 1、内存固定使用  unicode编码，硬盘编码（即你可以修改的编码）
# 2、使用什么编码往硬盘写，就用什么编码去读
# 3、程序运行分两阶段：1、从硬盘读到内存2、python解释器运行已经读到内存的代码
# 4、针对test.py文件来说python与nodpad++\vim的区别就是多了第二个步骤
# 5、conding只是表示从硬盘读取到内存用什么方法
