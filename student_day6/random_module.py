import random
import string
#  返回一个随机的小数
print(random.random())


"""
random.randint(1, 5) 包含1和5

"""
print(random.randint(1, 5))

"""
random.randrange()前包后不包
random.randrange(1, 10) 不包换10

"""
print(random.randrange(1, 10))

"""


"""
print(random.sample(range(100), 5))
print(random.sample('abcde', 5))
str_source = string.ascii_letters + string.digits
print(random.sample(str_source, 5))
x = ''.join(random.sample(str_source, 5))
print(x)
print(string.ascii_letters)
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

"""
随机验证码
方法1：6位随机验证码生成,其中字母是大写

"""
checkcode = ''
for i in range(0, 6):
    current = random.randint(0, 6)
    if current != i:
        tmp = chr(random.randint(65, 90))          # ASCII码 大写A-Z
    else:
        tmp = random.randint(0, 9)       # 如果随机数当好等于循环数，则重新给随机数赋值
    checkcode += str(tmp)                # 循环累计添加4次
print(checkcode)

"""
随机验证码
方法2: 6位随机验证码

"""
checkcode = ''.join(random.sample(string.ascii_letters, 6))
print(checkcode)