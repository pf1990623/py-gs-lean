lst0 = list(range(4))
lst2 = list(range(4))
print(lst0 == lst2)
lst1 = lst0
lst1[2] = 10
print(lst0)
print(lst0 == lst2)

# ===============
print('----------------')
lst0 = list(range(4))
lst5 = lst0.copy()
print(lst5 == lst0)
lst5[2] = 10
print(lst0)
print(lst5)
# lst0和lst5一样吗？   答案是不一样的，原因是lst0和lst5指定的不是同一个内存地址
# -------------------------
print("----------------------")
lst0 = [1,[2,3,4],5]
lst5 = lst0.copy()
print(lst5)
print(lst5 == lst0)
lst5[2] = 10
print(lst5)
print(lst5 == lst0)
lst5[2] = 5
lst5[1][1] = 20
print(lst5,lst0,sep= '\n')
print(lst5 == lst0)

n = 100
lst = [2]
for n in range(3,n):
    for i in lst:
        if n % i ==0:
            break
    else:
        lst.append(n)
print(lst)

# 杨辉三角型
triangle = [[1], [1,1]]
n = 6
for i in range(2,n):
    pre = triangle[i-1]
    cur = [1]
    for j in range(0,i-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)

# 方法1变体
triangle = []
n = 6
for i in range(6):
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(i-1):
        row.append(triangle[i-1][j]+triangle[i-1][j+1])
    row.append(1)
print(triangle)

# 升级方法
n = 6
oldline = []
newline = [1]
length = 0
print(newline)
for i in range(1,n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1]+oldline[j])
    print(newline)
