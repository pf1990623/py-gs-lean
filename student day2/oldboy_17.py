#   17、等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输⼊”，并允许⽤户重新输⼊并打印。
#   敏感字符：“⼩粉嫩”、“⼤铁锤”
s = "⼩粉嫩⼤铁锤"
while True:
    i = input(">>>")
    if i in s:
        print("存在敏感字符请重新输⼊")
        continue
else:
    print("完成")

lst = ['⼩粉嫩', '⼤铁锤']
while True:
    i = input(">>>").strip()
    for n in lst:
        if n.find(i) >= 0:
            print("存在敏感字符请重新输⼊")
            break
    else:
        print("完成")