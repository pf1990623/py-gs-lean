
# username = open('username','r',encoding='utf-8')
# a=username.readlines()
# print(type(a))
#
# for i in a:
#     b = i.split(':')
#     print(b[0])
# print(range(10))
# for i in range(3):
#     print(i)
# oldboy_age = 39
# for i in range(3):
#     guess_age = int(input("age:"))
#     if guess_age == oldboy_age:
#         print("猜对了")
#         break
#     elif guess_age > oldboy_age:
#         print("bigger")
#         continue
#     else:
#         print("smaller")
#         continue
# else:  #如果for循环正常结束，就执行else下面的语句，即没有被break
#     exit("too many attempts....")
# print("welcome enter to the second level...")

# count = 0
# oldboy_age = 39
# while count < 3:
#     guess_age = input("age:")
#     if guess_age.isdigit():
#         guess_age = int(guess_age)
#     else:
#         continue
#     if guess_age == oldboy_age:
#         print("猜对了")
#         break
#     elif guess_age > oldboy_age:
#         print("bigger")
#     else:
#         print("smaller")
#
#     count += 1
# for i in range(10):
#     for j in range(5):
#         print(i,j)
#         if j > 5:
#             break

# for i in range(10):
#     for j in range(10):
#         if j < 5:
#             continue
#         print(i,j)
# count = 0
# while True:
#     print("你是风儿我是沙",count)
#     count+=1
# a = 1
# for i in range(1,11):
#     print(i)
#     a *= i
#     print(a)
# print(a)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
