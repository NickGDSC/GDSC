#dictionaries
print("#1")
d = {"first" : "a", "second" : "b"}
print(d)
print(d["first"])

print("#2")
d = dict(first = "a", second = "b")
print(d)
print(d["second"])

print("#3")
d = dict.fromkeys(["a" , "b" , "c"])
print(d)
print (d["a"])

print("#4")
d = {a : a**2 for a in range(5)}
print(d)