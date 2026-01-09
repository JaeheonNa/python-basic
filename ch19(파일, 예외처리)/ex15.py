import re

fileName = "text/uscons.txt"
file = open(fileName, "r")
for line in file.readlines():
    line = line.rstrip()
    if re.search("^[0-9]+", line):
        print(line)

text = """101 COM     Python Program
102 MAT     LinearAlgebra
103 ENG     Computer"""

s = re.findall('\d+', text)
print(s)

