#猜对
#猜小
#猜大
oldboy_age = 39

guess_age = int(input("age:"))
#查看数据类型type()函数
print(type(guess_age))
if guess_age == oldboy_age:
    print("猜对了")
elif guess_age > oldboy_age:
    print("try smaller...")
else:
    print("try bigger...")
