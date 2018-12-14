#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: panfeng
@license: Apache Licence 
@file: re_module.py
@time: 2018/11/29 16:19
"""
import re
"""
'.'     默认匹配\n之外的任意一个字符，若指定flag DORALL，则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags multline,这种也可以匹配（r"^a","\nabc\neee",flag=re.MULTILINE)
'$'     匹配字符结尾，或re.search("foo$","bfoo\nsdsf",lag=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbac") 结果为 ['abb','ab','a']
'+'     匹配一个字符1次或多次，re.findall('ab+',"ab+cd+acc+bba" 结果为 ['ab','abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果['abb','ab','abb']
'|'     匹配|左或|右字符。re.search('abc|ABC',"ABCBabcCD").group() 结果ABC
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c)","abcabca456c").group() 结果：abcabca456c
groups()分组，以 列表方式显示
'\A'  只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的 和 ^效果相同
'\Z'  匹配字符结尾，同$
'\d'  匹配数字0-9
'\D'  匹配非数字
'\w'  匹配[A-Za-z0-9]
'\W'  匹配非[A-Za-z0-9]，只匹配特殊字符
's'   匹配空白字符、\t、\n、\r，re.search("\s+","ab\tc1\n3").group() 结果为"\t"

最长用的匹配语法
    re.match()：从头开始匹配
    re.search()：匹配包含
    re.findall()：把所有匹配的字符放到以列表中的元素返回
    re.split()：以匹配到的字符当作列表分隔符,也可以理解为反响
    re.sub()：匹配字符并替换
        sub(pattern, repl, string, count=0, flags=0):
反斜杠困扰：
    与大多数编程语言相通，正则表达式使用"\"作为转义字符，这就可能造成反斜杠困扰，加入你需要匹配文本中的字符“\”,
    那么使用编程语言表示的正则表达式里将需要4个反斜杠“\\\\”;前两个和后两个分别用于在编程语言里转义反斜杠，转换成
    两个反斜杠后再在正则表达式里转换成一个反斜杠，python里原生字符串很好的解决了这个问题，这个例子中的正则表达式
    可以使用r"\\"表示。同样匹配一个数字的“\\d”,可以写成r"\d",有了原生字符串，再也不用担心是不是漏写了反斜杠，
    写出来的表达式也更直观。
    示例：

"""
print(re.search("\s+", "ab\tc1\n3").group())

# 示例 flags= 参数 re.I, M
# re.I(re.IGNORECASE)  # 忽略大小写（括号内是完整写法，下同）
re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})", "371481199306143242").groupdict("city")
"""

(?P<province>)  定义字典key名称
[0-9]{4}  数字0-9，匹配4次

"""

#re.match()
"""
match(pattern, string, flags=0)
pattern：规则
Try to apply the pattern at the start of the string, returning
a match object, or None if no match was found.

"""
re.search('(\d{1,3}\.){3}\d{1,3}',"inet addr:10.20.45.61  Bcast:10.20.45.255  Mask:255.255.255.0")
re.sub()