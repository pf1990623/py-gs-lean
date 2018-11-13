import json
data = {
    'name': "xiaofeng",
    "age": 22,
    "Sex":"M"

}
f = open("data.txt", 'w')
f.write(json.dumps(data))
f.close()