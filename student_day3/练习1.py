import copy
# dic = {'key1':None,'key2':None, 'key3':None}
# ls = [1, 2, 3]
#
# # dic = {'key1':1,...}
# i = 0
# for j in range(len(ls)):
#     for k in dic.keys():
#         # print(k)
#         count = 0
#         for j in range(i, len(ls)):
#             if count < 1:
#                 j = ls[j]
#                 dic[k] = j
#                 count += 1
#                 i += 1
#             else:
#                 break
# print(dic)
#
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
