import random

words = ["Python", "C", "C++", "C#", "Java", "Javascript", "Typescript", "Go"]
for _ in range(3):
    print(words.pop(random.randint(1, len(words)) - 1), end=" ")
print()
for _ in range(3):
    print(random.choice(words), end=" ")
print()
print("--" * 10)

selectedLine = ""
while len(selectedLine) <= 10:
    selectedAlpha = chr(random.randrange(ord('a'), ord('z') + 1))
    if selectedAlpha not in selectedLine:
        selectedLine += selectedAlpha
print(selectedLine)
print("--" * 10)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
selectedLine = ""
while len(selectedLine) <= 10:
    selectedAlpha = random.choice(alphabet)
    if selectedAlpha not in selectedLine:
        selectedLine += selectedAlpha
print(selectedLine)
print("--" * 10)

for _ in range(5):
    print(random.randrange(100, 201, 2), end=" ")
print()
print("--" * 10)

print([random.randrange(100, 201, 2) for _ in range(5)])
print("--" * 10)

print(random.sample([i for i in range(100, 201) if i % 2 == 0], 5))