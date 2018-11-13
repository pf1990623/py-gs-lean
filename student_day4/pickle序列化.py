import pickle

data = {
    'name': "xiaofeng",
    "age": 22,
    "Sex": "M"

}

f = open("data.pkl", 'wb')
f.write(pickle.dumps(data))
f.close()

"""
json和pickle区别
json只能序列化普通的数据类型，属于全部语言通用型的
pickle只能用于python里面，能序列化和发序列化的东西更多

"""
