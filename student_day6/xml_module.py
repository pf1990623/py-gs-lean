
"""
xml是实现不同语言或程序之间进行数据交换，跟json差不多，但json使用起来更简单，不过，古时候
在json还没诞生的黑暗年代，大家只能选择用xml，至今很多传统金融航悦的很多系统接口主要还是xml


"""
"""
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

"""
import xml.etree.ElementTree as ET

tree = ET.parse("file")    # 打开文件xml文档
root = tree.getroot()             # 获取root节点，即是顶级标签
print(root.tag)                   # 打印根节点

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print("\t", i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

"""

修改和删除xml文档内容
"""
# import xml.etree.ElementTree as ET

tree = ET.parse("file")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")

tree.write("test.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

