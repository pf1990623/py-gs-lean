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
print("==" * 50)
tree = ET.parse("test.xml")
root = tree.getroot()
animNode = root.find('country')  # 查找root节点下第一个tag为country的节点
print(animNode.tag, animNode.attrib, animNode.text)


"""
删除指定的节点以及保存
在合并MainFest文件的时候，可能有一些重复的权限，那么怎么删除呢？ 删除指定节点可以通过remove(node)方法，移除指定的节点
代码示例，比如我们想三处attribute中name为Liechtenstein的节点

"""
# 加载文档为内存里，形成一个倒树形结构
tree = ET.parse("test.xml")
# 获取根节点
root = tree.getroot()
# 查找root节点下第一个tag为country的节点
node = root.find('country')
# 查找root节点下第一个tag为country的所有节点
nodes = root.findall('country')

for node in nodes:
    if node.attrib['name'] == 'Liechtenstein':
        root.remove(node)   # 移除country中name的属性
        break
# 写入到新的文件
tree.write('test1.xml')
print("删除成功")

"""
python标准库提供了一组极少使用但有用的接口来处理xml。两个最基本和最广泛使用搞砸xnl数据的API是SAX 和DOM接口
    SAX：简单的xml（API  SAX） 在这里，当文档较大或内存限制时，此功能非常有用，它会从文件读取文件时解析文件，
    并且整个文件不会存储在内存中
    DOM：文档对象模型，它将整个文件读入到存储器中并以分层（基于树）的形式存储，以表示xml文档的所有功能
"""