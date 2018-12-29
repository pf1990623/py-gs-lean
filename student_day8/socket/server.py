#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence
@file: server.py
@time: 2018/12/25 14:11
"""
import socket
import os
import subprocess
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
"""
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.AF_INET: IPV4
    socket.SOCK_STREAM： TCP协议

"""
server.bind(("0.0.0.0", 8000))
"""
server.bind:
    0.0.0.0: 服务端IP地址
    8000：  服务端端口
    
"""
server.listen(5)
"""
sk.listen(backlog)

　　开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。

      backlog等于5，表示内核已经接到的连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
      这个值不能无限大，因为要在内核中维护连接队列
      def listen(self, backlog: int) -> None: ...
    # TODO the return value may be BinaryIO or TextIO, depending on mode
"""
while True:
    conn, client_addr = server.accept()
    print("--------start-- server---------")
    print(conn, client_addr)
    while True:
        try:
            data = conn.recv(1024)   # 1024字节  # 接收消息
            print("recv form client %s" % data)
            resdata = subprocess.Popen(data,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            res = resdata.stdout.read()
            conn.send(str(len(res)).encode())
            conn.send(res)

        except ConnectionRefusedError as e:
            print(e)
            break
"""
　　接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。

　　接收TCP 客户的连接（阻塞式）等待连接的到来
"""

