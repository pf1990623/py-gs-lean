# 暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。
# -*- coding:UTF-8 -*-
import time

for key in range(1,10):
    time.sleep(2)
    print(key)