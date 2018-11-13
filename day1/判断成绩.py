score = int(input("输入你的成绩："))
if score > 100:
    print("滚")
elif score == 100:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("C-")
else:
    print("D")