#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: sock_server.py
@time: 2018/12/26 17:03
"""
import socket
import json
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8000))
s.listen(5)
print("------start------server------")
while True:
    conn,client_addr = s.accept()
    print("got a new conn：" %client_addr)

    while True:
        data = conn.recv(1024)
        print("recv data:",data)
        data = json.loads(data.decode())

        if data.get("action") is not None:
            if data["action"] == "put":
                # client sends file to server
                file_obj = open(data["filename"],"wb")
                recevied_size = 0
                while recevied_size < data["size"]:
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    recevied_size += len(recv_data)
                    print(data["size",recevied_size])
                else:
                    file_obj.close()
                    print("successfully recevoed file [%s]---" %data["filename"])
            elif data["action"] == "get":
                # client download file from server
                pass

