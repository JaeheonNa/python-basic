import copy

li1 = [1, 2, 3, 4, 5]

print("="*10, "list()", "="*10)
li2 = list(li1)
print()

print("="*10, "copy()", "="*10)
li3 = li1.copy()
print()

print("="*10, "copy.deepcopy()", "="*10)
li4 = copy.deepcopy(li1)
print()

print("="*10, "copy.copy()", "="*10)
li5 = copy.copy(li1)
print()

print("="*10, "[:]", "="*10)
li6 = li1[:]
print()

li1.append(6)

print("li1:", li1)
print("li1의 id:", id(li1))
print()

print("="*10, "list()", "="*10)
print("li2:", li2)
print("li2의 id:", id(li2))
print()

print("="*10, "copy()", "="*10)
print("li3:", li3)
print("li3의 id:", id(li3))
print()

print("="*10, "copy.deepcopy()", "="*10)
print("li4:", li4)
print("li4의 id:", id(li4))
print()


print("="*10, "copy.copy()", "="*10)
print("li5:", li5)
print("li5의 id:", id(li5))
print()

print("="*10, "[:]", "="*10)
print("li6:", li6)
print("li6의 id:", id(li6))
print()