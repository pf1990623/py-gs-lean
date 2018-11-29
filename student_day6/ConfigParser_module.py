#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: ConfigParser_module.py
@time: 2018/11/29 11:53
"""
"""
修改配置文件ini类型文件
类似于


"""
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9' }
config['bitbucker.org'] = {}
config['bitbucker.org']['User'] = 'hg'
config['topseceret.server.com'] = {}

topsecret = config['topseceret.server.com']
topsecret['Host Port'] = '5000'
topsecret['Forwardx11'] = 'no'
topsecret['enabled'] = 'yes'
config['DEFAULT']['Forwardx11'] = 'yes'
with open('config.ini', 'w') as configfile:
    config.write(configfile)

"""
读取

"""
config = configparser.ConfigParser()

# 读取文件
config.read("config.ini")
print(config.sections())    # 只打印[]内容，默认DEFAULT不显示
"""
运行结果：
    ['bitbucker.org', 'topseceret.server.com']

"""
print(config.default_section)
"""
运行结果：
    DEFAULT

"""

#  获取host port端口
find_node = config['topseceret.server.com']['host port']
print(find_node)

#
section_name = config.sections()[1]
print(section_name)

for k, v in config[section_name].items():
    print(k,v)


sec_name = config.sections()[1]
print(sec_name)
for k in config[sec_name]:
    print(k)

