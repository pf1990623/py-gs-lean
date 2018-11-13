import json

f = open("data.txt")
data = json.loads(f.read())
print(data)
