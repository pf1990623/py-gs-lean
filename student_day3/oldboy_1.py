import copy
# 1、 文件a1.txt内容
#       序号      部门   人数    平均年龄 备注
#       1       python   30     26    单身狗
#       2       Linux    26     30    没对象
#       3       运营部    20     24    女生多
#       .......
#       通过代码，将其构建成这种数据类型：
#           [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'},......]备注':'单身狗'


# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'}]
# 方法1
f = open("a1", encoding="utf8")
line = f.readline().strip().split()
dic = dict.fromkeys(line)
ln = []
x = 0
for i in f:
    lines = i.strip().split()
    dic1 = {}
    x = 0
    count = 0
    for k in dic.keys():
        count = 0
        for j in range(x, len(lines)):
            if count < 1:
                dic[k] = lines[j]
                x += 1
                count += 1
            else:
                break
    dic1.clear()
    dic1 = dic
    ln.append(copy.deepcopy(dic1))
f.close()
print(ln)
# 方法2 升级版
f = open("a1", 'r', encoding="utf-8")

line = f.readline().strip().split()

ln = []

dict1 = {}

for lines in f:
    lines = lines.split()
    for k in range(len(line)):
        key = line[k]
        dict1[key] = lines[k]
    ln.append(copy.deepcopy(dict1))
f.close()

print(ln)

# 方法3:再优化
with open('a1',encoding="utf-8") as f:
    line = f.readline().strip().split()

    ln = []

    dict1 = {}

    for lines in f:
        lines = lines.split()
        for k in range(len(line)):
            key = line[k]
            dict1[key] = lines[k]
        ln.append(copy.deepcopy(dict1))
    f.close()

print(ln)
