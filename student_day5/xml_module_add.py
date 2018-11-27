import xml.etree.ElementTree as ET

# 1、先加载文档到内存，形成一个倒桩的树结构
tree = ET.parse("test.xml")
# 2、获取到根节点
root = tree.getroot()
print('tag:', root.tag, 'attrib', root.attrib, 'text', root.text)