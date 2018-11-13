matrix = [[1,2,3],[4,5,6]]
tm = []
count = 0
for row in matrix:
    for i, col in enumerate(row):
        if len(tm) < i + 1:
            tm.append([])

        tm[i].append(col)
        count +=1
        print(tm)
print(matrix)
print(tm)