# 输入三个整数x,y,z，请把这三个数由小到大输出。
# 分析：我们想办法把最小的数放到x上，先将x与y进行比较，
# 如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
# 如果x>z则将x与z的值进行交换，这样能使x最小。
list = []

for i in range(3):
    x = input('int:\n')
    if x.isdigit():
        x = int(x)
        list.append(x)

    else:
        print('please input int')

else:
    print("输入的三个数，其中有部分不是整数")

list.sort()
print(list)

#  此题有bug,如果输入三个非整数，就会报错，留待后期完善
