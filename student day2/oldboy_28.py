#   28、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
#       敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
#       则将用户输入的内容中的敏感词汇替换成等长度的 *（苍老师就替换 ** *），
#       并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
pl = []
while True:
    pinglun = input(">>输入评论内容(退出q)：")
    if pinglun == 'q':
        break
    for i in range(len(li)):
        pass
    else:
        pl.append(pinglun)
        continue
print(pl)