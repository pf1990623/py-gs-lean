"""
创建xml文件

"""
from xml.etree.ElementTree import fromstring,ElementTree
import xml.etree.ElementTree as ET



new_xml = ET.Element("namelist")          # 根节点名字
name = ET.SubElement(new_xml, 'name', attrib={"enrolled": "yes"})   # name为名字 attrib={'xxx':'yyy'}属性定义
name.text = "panfeng"
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'

name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
name2.text = "chenjun"
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.Element("namelist")
et.write("test3.xml", encoding="utf8", xml_declaration=True)

# ET.dump("namelist")  # 打印生成格式