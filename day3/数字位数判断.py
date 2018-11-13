num = int(input("输入1-99999范围的整数:"))
print(len(num))
if 1 <= num <= 9:
    print("1位数")
elif 10 <= num <= 99:
    print("2位数")
elif 100 <= num <= 999:
    print("3位数")
elif 1000 <= num <= 9999:
    print("4位数")
elif 10000 <= num <= 99999:
    print("5位数")
else:
    print("输入的数错误，请重新输入")


