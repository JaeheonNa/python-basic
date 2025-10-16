print("=" * 10, "insert", "=" * 10)
li = [1, 2, 4, 5]
li.insert(2, 3)
print(li)
print()

print("=" * 10, "index", "=" * 10)
heros = ["SpiderMan", "IronMan", "Hulk", "SuperMan", "BatMan", "BatMan"]
if "SuperMan" in heros:
    print("SuperMan 이 존재합니다.")
    superManIndex = heros.index("SuperMan")
    print(heros[superManIndex], "의 인덱스:", superManIndex)
else:
    print("SuperMan 이 존재하지 않습니다.")

if "BlackWidow" in heros:
    print("BlackWidow 가 존재합니다.")
    blackWidowIndex = heros.index("BlackWidow")
    print(heros[blackWidowIndex], "의 인덱스:", blackWidowIndex)
else:
    print("BlackWidow 가 존재하지 않습니다.")
print()

print("=" * 10, "pop", "=" * 10)
popedHero = heros.pop(2)
print("Heros: ", heros)
print(popedHero)
print()

print("=" * 10, "remove", "=" * 10)
while True:
    if "BatMan" in heros:
        heros.remove("BatMan")
    else:
        break
print("Heros: ", heros)
print()

print("=" * 10, "del", "=" * 10)
del heros[2]
print("Heros: ", heros)
del heros[:]
print("Heros: ", heros)
print()

print("=" * 10, "clear", "=" * 10)
heros = ["SpiderMan", "IronMan", "Hulk", "SuperMan", "BatMan", "BatMan"]
print("Heros: ", heros)
heros.clear()
print("Heros: ", heros)
print()

print("=" * 10, "count", "=" * 10)
heros = ["SpiderMan", "IronMan", "Hulk", "SuperMan", "BatMan", "BatMan"]
batManCnt = heros.count("BatMan")
spiderManCnt = heros.count("SpiderMan")
print("BatMan Cnt:",  batManCnt)
print("SpiderMan Cnt:", spiderManCnt)
print()

print("=" * 10, "extend", "=" * 10)
li1 = [1, 2, 3]
li2 = [4, 5, 6]
li1.extend(li2)
print(li1)

