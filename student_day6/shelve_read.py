import shelve
f = shelve.open("shelve_test")
print(f["test"])
print(f["func"])