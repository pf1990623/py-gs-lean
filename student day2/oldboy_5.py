#   5、使用for循环对s = "abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb, ...gsb。
s = "abcdefg"
for i in s:
    print(i+'sb')
#   6、使用for循环对s = "321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s = "321"
for i in s:
    print("倒计时%s秒" % i)
for i in s:
    print("倒计时{}秒".format(i))