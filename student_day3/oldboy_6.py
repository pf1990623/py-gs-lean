# 6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
#       四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个文件中。student_msg

def fun6(name, sex, age, education):
    ls = str([name, sex, age, education])
    fx = open("student_msg", "a+", encoding="utf8")
    fx.write(ls)
    fx.write("\n")
    # fx.write(name)
    # fx.write(sex)
    # fx.write(age)
    # fx.write(education)
    fx.close()
    fx.closed
    # pass

fun6("zhangsan", "男", "22", "大专")
