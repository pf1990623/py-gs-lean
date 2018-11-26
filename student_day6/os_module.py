import os
"""
os 模块，俗称系统模块，显
  在自动化测试中，经常需要查找操作文件，
  比如说查找配置文件（从而读取配置文件的信息），
  查找测试报告（从而发送测试报告邮件），
  经常要对大量文件和大量路径进行操作，
  这就依赖于os模块，所以今天整理下比较常用的几个方法。
  网上这方面资料也很多，
  每次整理，只是对自己所学的知识进行梳理，从而加深对某个模块的使用。
"""
"""
os.getcwd() 获取当前文件所在目录，返回字符串类型
#返回当前工作目录
"""
os_module = os.getcwd()
print(type(os_module))
print(os_module)
"""
os.listdir(os.getcwd())
返回当前目录下的所有文件，
并以列表的形式显示

"""
os_module = os.listdir(os.getcwd())
print(os_module)
print(type(os_module))

"""
返回当前目录的绝对路径

"""
os_module = os.path.abspath(".")
print(os_module)
"""
返回当前目录的上一级目录的绝对路径
"""
os_module = os.path.abspath("..")
print(os_module)

"""
path()

"""
print(os.path)
"""
查看路径的文件夹部分和文件名部分
"""
# print(os.path.dirname("."))
for i in os.path.dirname("."):
    print(i)

"""
os.path.basename(os.getcwd())
返回当前文件所在的目录名
"""
print(os.path.basename(os.getcwd()))

"""
查看文件时间
 os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
 os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。
 os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数。
"""
print(os.path.getatime("os_module.py"))
print(os.path.getctime("os_module.py"))
print(os.path.getmtime("os_module.py"))
"""
查看文件的大小，文件名需要带文件类型
"""
print(os.path.getsize("os_module.py"))

"""
判断文件是否存在
os.path.exists(path):文件或文件夹是否存在，返回True 或 False。
"""
print(os.path.exists("os_module.py"))
"""
os中定义了一组文件、路径在不同操作系统中的表现形式参数，如：

>>> os.sep()
'\\'
>>> os.extsep()
'.'
>>> os.pathsep()
';'
>>> os.linesep()
'\r\n'

"""

"""
返回当前系统平台
windows用nt表示，linux用posix表示
"""
print(os.name)
os.system("cmd")
os.system("ls")
"""
创建目录
"""
os.mkdir("path")  # 创建path目录(只能创建一级目录，如'F:\XXX\WWW'）,在XXX目录下创建WWW目录
os.makedirs("path")  # 创建多级目录（如'F:\XXX\SSS'），在F盘下创建XXX目录，继续在XXX目录下创建SSS目录

"""
删除文件或目录
"""
os.remove("file")  # 只能文件，必须是文件
os.rmdir("path")  # 删除path目录(只能删除一级目录，如'F:\XXX\SSS'),只删除SSS目录
os.removedirs("path")  # #删除多级目录（如'F:\XXX\SSS'）,必须为空目录，删除SSS、FFF目录

"""
更改路径
"""
os.chdir("path")  # 将当前工作目录更改为指定路径path

"""
查看文件
"""
os.path.exists("file")  # 判断file是否存在，存在返回True,不存在返回False
os.path.isfile("file")  # 判断file是否是文件，是返回True,不是返回False
os.path.isdir("path")  # 判断path是否是目录，是返回True,不是返回False

"""
获取文件和目录
"""
os.walk("path")  # 递归返回path下的目录(包含path)、子目录、文件名的三元组

"""
获取shell命令返回值
"""
fp = os.popen("cmd")  # 打开命令cmd,打开管道，返回值是链接管道的文件对象
rlt = fp.read()  # 读取结果
rlt = fp.readline()  # 读取结果


