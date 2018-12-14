#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: subpress_module.py
@time: 2018/12/11 17:11
"""
import os
import subprocess
# res = os.system("dir")
# res_1 = os.popen("dir").read()
# print(res_1)
"""
os.system() 输出命令结果到屏幕，返回命令执行状态
res结果为0
判断当前目录是否存在，0为真，非0为假

os.popen("dir") 相当于打开一个文件，返回值是内存对象，read()用来读取内存对象内容
subpress

os.popen("dir").read()  将命令结果存下来，而不会返回状态

又想要状态，又想要执行结果
py.2.7
commands模块
commans.getstatusoutput("dir")

又想要状态，又想要执行结果
python3 方法
    subpress模块

"""
"""
subpress 替换 os.system() os.spwn()


"""
# print(subprocess.run(["df", "-h"]))
# 涉及到管道过滤
# print(subprocess.run("df -h |grep sda1", shell=True))
"""
subprocess.call()  相当于os.system
subprocess.check_call()   # 过程中出错，直接报错
subprocess.getstatusoutput()   # 相当于commans.getstatusoutput，最常用，返回一个元组
subprocess.check_output()   # 返回结果都是byes格式

"""

"""
Popen拿到返回结果

"""
# res = subprocess.Popen("ifconfig |grep 192", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# res.stderr.read()
# res.stdout.read()
#
# res.poll()  # 耗时较长的命令，使用poll()方法查看是否完成
# res.wait()  # 一直等待输出结果
# res.terminate()  # 命令执行一半，发现有问题，在半路终结正在执行的程序
# res.communicate()  # 在执行的过程中，再传数据，基本不长用

"""
Popen（）可用参数
args: shell命令，可用是字符串或者序列类型（如：list ,元组）
bufszie: 指定缓存，0无缓冲，1行缓存个，其他缓冲区大小，负值，系统缓冲
stdout,stderr,stdin: 分别表示程序的标准输出，错误，输入
preexec_fn=None：只在unix平台有效，用于指定一个可执行对象，它将在子进程之前被调用
close_fds=_PLATFORM_DEFAULT_CLOSE_FDS ： 在windows平台下，如果close_fds被设置为True,则新创建的子进程将不会集成父进程的输入输出错误管道
    所以不能讲close_fds设置为True同时重定向子进程的标注输入、输出、错误（stdin，stdout、stderr）
shell：同上
cwd: 用于设置子进程的当前目录
env: 用于执行子进程的环境变量，如果env = none,子进程的环境变量将从父进程中继承
universal_newlines： 不通操作系统的换行符不同，True-->同意使用\n
startupinfo、creationflags只在windows下有效，将被传递给底层的CreateProcess()函数，用于设置子进程的一些
    属性，如：主窗口的外观，进程的优先级等等。

终端输入的命令分两种：
    输入即可得到输出，如ifconfig
    输入进入某环境，依赖再再输入，如：python
"""

# 需要交互的命令示例
import subprocess
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write(b'print(1)')
obj.stdin.write(b'print(2)')
obj.stdin.write(b'print(3)')
obj.stdin.write(b'print(4)')
obj.stdin.closed

out_err_list = obj.communicate(timeout=10)
print(out_err_list)
# 实现sudo自动输入密码
