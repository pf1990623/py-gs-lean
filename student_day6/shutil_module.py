import os,shutil

"""
#
文件copy,r
"""

shutil.copy(r"D:\py-gs-lean\python练习题\python练习题2.py", r"D:\py-gs-lean\student_day6\a.py")


"""
copy()和copyfile()
copy仅拷贝文件和权限
copy2() 权限和状态都copy
copytree() 拷贝一个目录 相当于linux copy -rp
rmtree() 递归删除，删除一个目录
"""
shutil.copyfile()
shutil.rmtree()
"""

"""
#

shutil.move()
"""
move(src, dst, copy_function=copy2):
src: 源文件或目录
dst: 目标文件或目录

"""

shutil.make_archive()
"""
压缩文件
# make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0,
#                  dry_run=0, owner=None, group=None, logger=None):
#
# basename: 压缩包的文件名，也可以是压缩包的路径，只是文件名时，则保存至当前目录。否则保存到指定目录
# 如：  www  ===>保存到当前目录
# 如：  /var/www ==>保存到var目录下
#
# format:  压缩包的格式，“zip”,"tar","bztar","gztar"
# root_dir = 要压缩的文件路径，默认是当前目录
# owner:  用户，默认当前用户
# group:  组，默认当前组
# logger:  用于记录日志，通常是logging.Loger对象
"""

import zipfile
"""
zip压缩
压缩file
只支持压缩文件
"""
zip_object = zipfile.ZipFile("file", 'r')
zip_object.write("test")  # 写入要压缩到文件
zip_object.write("xxx")   # 写入要压缩的文件名
zip_object.close()    # 关闭文件
# 解压
z = zipfile.ZipFile("xx.zip", 'r')
z.extractall()
z.close()

import tarfile
# tar打包压缩
tar = tarfile.open("your.tar", 'w')
tar.add(r"D:\py-gs-lean\python练习题", arcname="xiaofeng")
tar.close()

# arcname=None
# 默认为空，不写参数，显示的是绝对路径，如果填写，压缩包里查看的名字为arcname定义的名字，可以理解为顶层目录冲命令
