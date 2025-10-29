dic1 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dic1)

dic2 = {1:"사과", (2,):"토마토", "과일":"오렌지"}
print(dic2)

dic3 = {}
print(dic3)

dic4 = {1:"사과", 2:"토마토", 3:"오렌지"}
print("dic4의 키 1의 값은: ", dic4[1])
print("dic4의 키 1의 값은: ", dic4.get(1))
print("dic4의 키 5의 값은: ", dic4.get(5))
# print("dic4의 키 5의 값은: ", dic4[5]) 에러
print("dic4의 키 5의 값은: ", dic4.get(5, "파인애플"))

print(1 in dic4)
print(1 not in dic4)
print(5 in dic4)
print(5 not in dic4)

dic5 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dic5)
print("dic5의 요소 추가 전 id: ", id(dic5))
dic5[4] = "키위"
print(dic5)
print("dic5의 요소 추가 후 id: ", id(dic5))


dic6 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dic6)
print("dic6의 요소 삭제 전 id: ", id(dic6))
dic6.pop(2)
print(dic6)
print("dic6의 요소 삭제 후 id: ", id(dic6))

dic7 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dic7)
print("dic7의 요소 삭제 전 id: ", id(dic7))
del dic7[3]
print(dic7)
print("dic7의 요소 삭제 후 id: ", id(dic7))
dic7.clear()
print(dic7)