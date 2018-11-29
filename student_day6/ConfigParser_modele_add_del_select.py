#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: ConfigParser_modele_add_del_select.py
@time: 2018/11/29 14:07
"""
import configparser
config = configparser.ConfigParser()
# config["section1"]={}
# config['section1']['k1'] = 'v1'
# config['section1']['k2'] = 'v2'
#
# config['section2'] = {}
# config['section2']['k1'] = 'v1'
#
# with open('i.cfg','w') as f:
#     config.write(f)
config.read('config.ini')

section_name = config.sections()[1]    # section_nam
print(config.options(section_name))
"""
options() 打印默认DEFAULT和当前topseceret.server.com的key
运行结果：
   ['host port', 'forwardx11', 'enabled', 'serveraliveinterval', 'compression', 'compressionlevel']
 

"""
print(config.items(section_name))
"""
items()生成key和value的形式，显示效果列表套元组的形式

运行结果“”：
[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), 
('forwardx11', 'no'), ('host port', '5000'), ('enabled', 'yes')]

"""

# 获取值的方法
#  获取topsecret.server.com，'forwardx11' key的值
print(config.get(section_name,'forwardx11'))

"""
[topseceret.server.com]  topseceret.server.com是section
host port = 5000         host port 是 topseceret.server.com的key
forwardx11 = no          forwardx11 是 topseceret.server.com的key
enabled = yes

remove_option(self, section, option):
section的名字
    前面已经定义：section_name = topsecret.server.com
option：
    定义是topsecret.server.com下的key

"""
# 产出选项forwardx11
config.remove_option(section_name, 'forwardx11')

"""

set(self, section, option, value=None):
section = section_name = topseceret.server.com
option = host port = 8000

"""
# 修改host port为8000
config.set(section_name, 'host port', '8000')

# 删除完成后写入到新的文件
config.write(open('config1.ini', 'w'))
