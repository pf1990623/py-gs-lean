import pickle

f = open("data.pkl", 'rb')
data = pickle.loads(f.read())
print(data)