li1 = [10, 20, "안녕"]
li2 = [10, 20, "안녕"]
print("li1 == li2", li1 == li2) # True

li3 = [1, 2, 3]
li4 = [1, 2, 4]
print("li3 < li4", li3 < li4) # True

li5 = [1, 2, 3]
li6 = [1, 2]
print("li5 > li6", li5 > li6) # True

li7 = ["a", "b", "c"]
li8 = ["a", "b", "d"]
print("li7 < li8", li7 < li8) # True
print("ord(\"c\")", ord("c"))
print("ord(\"d\")", ord("d"))
print("chr(99)", chr(99))
print("chr(100)", chr(100))

li = [80, 90, 100, -70, -50]
li.sort()
print("li.sort()", li)

li = [80, 90, 100, -70, -50]
sortedLi = sorted(li)
print("li", li)
print("sortedLi", sortedLi)

li = [80, 90, 100, -70, -50]
li.reverse() # 역순정렬이 아니라 순서를 뒤집는 매서드
print("li.reverse()", li)

li = [80, 90, 100, -70, -50]
sortedLi = sorted(li, reverse=True) # 역순 정렬
print("li", li)
print("sortedLi", sortedLi)

li = ["다시마", "나루", "마사지", "라디오", "가나"]
sortedLi = sorted(li)
print("li", li)
print("sortedLi", sortedLi)

statement = "나는 한국에서 살고 있는 개발자입니다. 만나서 반갑습니다."
statementList = statement.split()
print("statementList", statementList)

statementList = statement.split(".")
print("statementList", statementList)
