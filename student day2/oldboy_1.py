name = " aleX leNb "
#   1、有变量name = "aleX leNb"
#       完成如下操作：
#       1)  移除name变量对应的值两边的空格, 并输出处理结果
print(name.strip())
#       2)  移除name变量左边的"al"并输出处理结果
print(name.lstrip('al'))
#       3)  移除name变量右面的"Nb", 并输出处理结果
print(name.rstrip('Nb'))
#       4)  移除name变量开头的a"与最后的"b",并输出处理结果
print(name.rstrip('b').lstrip('a'))
#       5)  判断name变量是否以"al"开头, 并输出结果
print(name.startswith('al'))
#       6)  判断name变量是否以"Nb"结尾, 并输出结果
print(name.endswith('Nb'))
#       7)  将name变量对应的值中的所有的"l"替换为"p", 并输出结果
print(name.replace('l', 'p'))
#       8)  将name变量对应的值中的第一个"l"替换成"p", 并输出结果
print(name.replace('l', 'p', 1))
#       9)  将name变量对应的值根据所有的"l"分割, 并输出结果。
print(name.split('l'))
#       10) 将name变量对应的值根据第一个"l"分割, 并输出结果。
print(name.split('l', 1))
#       11) 将name变量对应的值变大写, 并输出结果
print(name.upper())
#       12) 将name变量对应的值变小写, 并输出结果
print(name.lower())
#       13) 将name变量对应的值首字母"a"大写, 并输出结果
print(name.capitalize())
#       14) 判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count('l'))
#       15) 如果判断name变量对应的值前四位"l"出现几次, 并输出结果
print(name.count('l', 0, 5))
#       16) 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
print(name.index("N"))
#       17) 从name变量对应的值中找到"N"对应的索引(如果找不到则返回 - 1)输出结果】
print(name.find("N"))
#       18) 从name变量对应的值中找到"X le"对应的索引, 并输出结果
print(name.find("X le"))
#       19) 请输出name变量对应的值的第2个字符?
print(name[0:2])
#       20) 请输出name变量对应的值的前3个字符?
print(name[0:3])
#       21) 请输出name变量对应的值的后2个字符?
print(name[-3:-1])
#       22) 请输出name变量对应的值中"e"所在索引位置?
print(name.find("e"))
