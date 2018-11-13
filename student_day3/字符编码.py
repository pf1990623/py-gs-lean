f = open("test1", encoding='utf8').read()
# open() 打开文件
# read()一次性读取所有到内存
# readline()一次性读取一行
f = open("test1", encoding='utf8')

# 读取前5行
for i in range(6):
    print(f.readline().strip())

line_count = 0
for line in f:
    if line_count< 5:
        print(line.strip())
        line_count += 1
    else:
        break



print(f.readline().strip())
print("-".center(50,"-"))
f = open("myfile", "w", encoding='utf8')  # w=write,创建写模式，覆盖了
f.write("wo 爱填满\n")
f.write("ni xxx\n")
f.close()

f = open("myfile1", "a", encoding='utf8')  # w=write,创建写模式，追加，a=append
f.write("wo 爱填满\n")
f.write("ni xxx\n")
f.close()

#  文件的混合模式，r+  读写模式，w+ 写读，会先清空文件，然后写入， a+ 追加写

f.closed  #  判断文件是否关闭
print(f.encoding)  # f.encoding 打印文件编码格式
# print(f.fileno())   # 应用程序打开文件，实际是python程序调用系统程序打开的
f.flush()    # 将内存中的文件，写入到内存
f.isatty()   # 文件终端，很少用到
f.seek() # 寻找，即移动光标
f.tell()  # 打印光标所在的位置
f.truncate() # 截断，从0开始，截断，并打印截断之前的内容，对于文件作用不大，对二进制文件有用



