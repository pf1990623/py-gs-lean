#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: sock_client.py
@time: 2018/12/26 17:10
"""
import socket
import os
import json
client = socket.socket()
client.connect(("localhost",8000))

while True:
    choice = input(">>>").strip()
    if len(choice) == 0:continue

    cmd_list = choice.split()
    if cmd_list[0] == "put":
        if len(cmd_list[1]) == 1:
            print("no filename follows after put cmd")
            continue
        filename = cmd_list[1]
        if os.path.isfile(filename):
            file_obj = open(filename, 'rb')
            base_filename = filename.split("/")[-1]
            print(file_obj.name, os.path.getsize(filename))
            data_header = {
                "action": "put",
                "filename": base_filename,
                "size": os.path.getsize(filename)
            }
            client.send(json.dumps(data_header).encode())
            for line in file_obj:
                client.send(line)
            print("send file done")
        else:
            print("file is not valid")
            continue
    elif cmd_list[0] == "get":
        pass
