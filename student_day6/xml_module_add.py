#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: xml_module_add.py
@time: 2018/11/27 18:22
"""
import xml.etree.ElementTree as ET
tree = ET.parse("file")    # 打开文件xml文档
root = tree.getroot()             # 获取root节点，即是顶级标签
print(root.tag)