list1 = ["bee", "moth"]
list3 = ["bee", "moth", "ant"]

#Functions.
print(list1)

print(len(list1))

print(max(list1))

print(max(list1, list3))

print(min(list1))

print(min(list1, list3))

print(list(range(10)))
print(list(range(1,11)))
print(list(range(51,56)))
print(list(range(1,11,2)))

#Methods
list1.append("ant")
print(list1)

list1.extend(["ant", "fly"])
print(list1)

list1.insert(0, "ant")
print(list1)
list1.insert(2, "fly")
print(list1)

list1.remove("moth")
print(list1)

list1.pop(1)
print(list1)

print(list1.index("ant"))
print(list1.index("ant", 2))

print(list1.count("bee"))
print(list1.count("ant"))
print(list1.count(""))

list1.sort(reverse=True)
print(list1)

list1.sort()
print(list1)

list1.sort(key=len)
print(list1)

list1.sort(key=len, reverse=True)
print(list1)

list1.reverse()
print(list1)

list2 = list1
list2.append("ant")
print(list1)
print(list2)

list2 = list1.copy()
list2.append("ant")
print(list1)
print(list2)

list1.clear()
print(list1)

