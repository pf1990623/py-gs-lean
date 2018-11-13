# 列表的复制
a = [1,2,3,4]
# 方法1：
# b = a
# print(b)
# # 方法2：
# b = a.copy()
# print(b)

#方法3：使用for循环实现
b=[]
for i in a:
    b.append(i)
print(b)