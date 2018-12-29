#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: client.py
@time: 2018/12/25 14:13
"""
import socket

client = socket.socket()            # 定义socker客户端
client.connect(("192.168.56.133", 8000))
"""
client.connect(("localhost",8000))
    localhost 指定服务端的地址，8000服务器端端口
    connect：客户端链接

"""
while True:
    msg = input(">>>").strip()
    if len(msg) == 0: continue  # msg是否为None,如果为None,则重新输入
    client.send(msg.encode())   # 客户端发送消息
    print("发送信息：%s" % msg)       # 打印发送消息
    data = client.recv(1024) # 1024代表客户端接收的大小
    print(data)
    total_len = int(data.decode())
    reveived_size = 0
    res = b''
    while reveived_size < total_len:
        d = client.recv(1024)
        res += d
        reveived_size += len(d)
    print("recevief from server:", res.decode()) # 打印接收信息

