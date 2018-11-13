print("Hello world!")
print("Hello world!")
'''
print("Hello world!")
print("Hello world!")
'''
print("Hello world!")


'''
python注释：
    单行注释：
        #号是代表单行注释 或者 ctrl+?
    多行注释：
        三个单引号或者3个双引号
        
    python中单引号和双引号作用是一样的。
    特殊用途：字符串中有单引号。
      例子：I'm is alber,这种用双引号引起来
           "I'm is alber"
    三个单引号和三个多信号同时代表一个段落
'''
'''
intro = """
My name is alber
I am 22 years old,
I like big baojian.
"""
print(intro)
'''

#python中的输入 input, crtl+d代表复制
#python3中使用input(),python2中使用的是rawinput()
name = input("name:")
age = input("age:")
job = input("job:")
hobby = input("hobby:")
print('my name is:', name, 'I am age:',age, "years old,\n"
        ,"my job is", job, "my hobby is ",hobby)
'''
定义格式：
----info of alber -----
name: alber
Age: 22
job: IT
Hobby: baojian
----end of -----------
'''
# 占位符
info = '''
------info of %s------
Name: %s
Age: %s
Job: %s
Hobby: %s
----------end-------
''' %(name, name, age, job,hobby)
print(info)

#-----------------------------------------------------------------
username = input("username:")
password = input("password:")

if username == "alber" and password == "abcd1234":
    print("welcome to ", username)
else:
    print("wrong username or password")
