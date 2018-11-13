#   26、利用for循环和range，将1 - 30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成 *。
lst = list(range(1, 30))
for i in lst:
    if i % 3 == 0:
        lst[lst.index(i)]="*"
print(lst)

#   26、利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
ls1 = list(range(100, 10, -2))
ls2 = []
for j in ls1:
    if j % 4 !=0:
        continue
    else:
        ls2.append(j)
print(ls2)
