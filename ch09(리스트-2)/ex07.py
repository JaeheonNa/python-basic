num = [1, 5, -9, 100]
print("최소값:", min(num))
print("최대값:", max(num))
print("="*10)

prices = [10000, 3000, 500, 10000, 20000, 700]
lowPrice = prices[0]
for price in prices:
    if price < lowPrice:
        lowPrice = price
print("가장 싼 가격:", lowPrice)
print("="*10)

animals = ["dog", "cat", "horse", "lion", "tiger", "elephant", "bi"]
shortest_animals = []
shortest_word = animals[0]
shortest_animals.append(shortest_word)
for i in range(1, len(animals)):
    animal = animals[i]
    if len(shortest_word) >= len(animal):
        if len(shortest_word) > len(animal):
            shortest_word = animal
            shortest_animals.clear()
        shortest_animals.append(animal)

print("가장 짧은 단어들:", shortest_animals)