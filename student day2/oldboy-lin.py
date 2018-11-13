# msg = "hello world"
# print(msg[4])
# print(msg.capitalize())
# print(msg.center(20, '#'))
# print(msg.count('l', 4, -1))
# print(msg.endswith('l'))
# msg1 = 'a\tb'    # 使用table
# print(msg1.expandtabs(10))  # 定义table的长度
# print(msg.find('d'))  # 返回d的索引，如果不存在返回-1
#
# msg2 = "if2"
# print(msg2.isidentifier()) # 判定一个单词是否含有关键字，切记一个单词

msg = "my name is panfeng"
table = str.maketrans('panfeng','zhiqian')
print(msg.translate(table))

print(msg.zfill(20))  # 默认采用右对齐


