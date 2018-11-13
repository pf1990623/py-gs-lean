# 输入两个数，比较两个数的大小，先打印最大的数，再打印最小的
# 三元运算符，三木运算符
# 三元表达式
# 样式 真值 if 条件 else 假值
# 样式1
x = int(input("x="))
y = int(input("y="))
if x >y:
    print(x, y)
else:
    print(y,x)
# 样式2
x = int(input("x="))
y = int(input("y="))
print(x, y) if x > y else print(y, x)
