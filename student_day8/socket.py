#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: socket.py
@time: 2018/12/25 11:08
"""

"""
1、socker 地址簇
    ipv4\ipv6
2、socker type
    Tcp\udp\
3、socker方法

sk.bind(addr)
sk.listen(backlog) 
    backlog默认是5个


服务器端
server = socket.socket(AF_INRT,Sock_stream)
server.bind('0.0.0.0,8000)
server.listen(5)
server.accept()
    conn,client_addr = server,accept()
conn.send('xxx')
conn.recv('xxx')
server.close()

客户端：
client = sockert.socket()
client.connect('')
client
"""
import socket
server = socket.socket()
