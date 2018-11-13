# 暂停一秒输出，并格式化当前时间。
# print(ord("A"))
# print(chr(66))
# print(chr(25991))
# print('abc'.encode('ascii'))
# print('中文'.encode('utf-8'))
#
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#
# print(len('abc'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
#
# sum = 0
# for i in range(1,10001):
#     sum +=i
# print(sum)
# print(list(range(1,11)))
# dict = {'key1':'a','key2':'b'}
# if 'key1' in dict:
#     print("存在")
# else:
#     print("不存在")
# print(dict.get('key3'))
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
def my_abs(x):
    if x >=0:
        return x
    else:
        return -x
print(my_abs(-1))

sum = 1
for i in range(1,20):
    sum *= i
    continue
print(sum)