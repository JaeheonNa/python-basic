fileName = "/Users/jaeheon.na/python_study.csv"
file = open(fileName, 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    line = line.strip()
    words = line.split(",")
    for word in words:
        print("  ", word, end='')
    print()
file.close()