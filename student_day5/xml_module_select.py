#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: xml_module_select.py
@time: 2018/11/27 18:25
"""
import xml.etree.ElementTree as ET
"""

tag，即标签，用于标识该元素表示哪种数据，即APP_KEY
attrib，即属性，用Dictionary形式保存，即{'channel' = 'CSDN'}
text，文本字符串，可以用来存储一些数据，即hello123456789

"""

# 1.先加载文档到内存里，形成一个倒桩的树结构
tree = ET.parse("test.xml")

# 2. 获取根节点
root = tree.getroot()
print('tag:', root.tag, 'attrib:', root.attrib, 'text:', root.text)
print(root.tag)

# 遍历根几点
for ele in root:
    print('tag:', ele.tag, 'attrib:', ele.attrib, ele.attrib['name'])
    """
    country
        属性名：name
        属性name的值：ele.attrib['name']
    """
    print("-" * 50)
    for e in ele:
        print('tag:', e.tag, 'attrib:', e.attrib, 'text', e.text)
        """
        e.tag: rank
        e.tag: 
        e.tag: gdppc
        e.tag: neighbor
        e.tag: neighbor
        e.attrib: 属性名，没有返回空
        text: e.text返回rank文本值：4
        ext: e.text返回year文本值：2008
        """

# 更加明了的显示方法

test = {}
tree = ET.parse("test.xml")
root = tree.getroot()

for ele in root:
    value = []
    for e in ele:
        if e.text is None:       # ==>判断e.text是空
            value.append(e.attrib)
        else:
            value.append({e.tag: e.text})   # ===> e.tag = rank e.text = 4 ,将字典添加到列表
    test[ele.attrib['name']] = value
    """
    test: 字典
    ele.attrib['name']：属性name的值
    类似 test['liechtnexxx'] = 'ran'
    
    """
print(test)

"""
查找指定的子节点：
当XML文件较大或者其中的子节点tag非常多的时候，一个一个获取是比较麻烦的而且有很多不是我们需要的，
这样我们可以通过find('nodeName')或者findall('nodeName')方法来查找指定tag的节点。

find('nodeName')：表示在该节点下，查找其中第一个tag为nodeName的节点。
findall('nodeName')：表示在该节点下，查找其中所有tag为nodeName的节点。
https://blog.csdn.net/lqian1993/article/details/80490982
"""
