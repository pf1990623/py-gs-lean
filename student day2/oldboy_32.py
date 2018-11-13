#   32、有字符串
#           "k:1|k1:2|k2:3|k3:4"
#       处理成字典
#           {'k': 1, 'k1': 2....}
a = "k:1|k1:2|k2:3|k3:4".split('|')
b = {}
for x in a:
    k, v = x.split(":")
    b[k] = v
print(b)