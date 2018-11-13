#   27、查找列表li中的元素，移除每个元素的空格，并找出以
#       "A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中, 最后循环打印这个新列表。
#       li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
ls1 = []
for i in li:
    i = i.strip()
    print(i)
    if i.startswith('A') or i.startswith('a') and i.endswith('c'):
        ls1.append(i)
for j in ls1:
    print(j)