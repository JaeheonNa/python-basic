import os

dir = os.getcwd()
print("현재 디렉토리:", dir)
print("--" * 10)

print("현재 디렉토리 내 모든 파일:", end=" ")
for filename in os.listdir(dir):
    print(filename, end=", ")
print()
print("--" * 10)

print("현재 디렉토리 내 파일:", end=" ")
for filename in os.listdir(dir):
    if os.path.isfile(filename):
        print(filename, end=", ")
print()
print("--" * 10)

print("현재 디렉토리 내 디렉토리:", end=" ")
for filename in os.listdir(dir):
    if os.path.isdir(filename):
        print(filename, end=", ")
print()
print("--" * 10)

print("현재 디렉토리 내 .py파일:", end=" ")
for filename in os.listdir(dir):
    if os.path.isfile(filename):
        if filename.endswith(".py"):
            print(filename, end=", ")
print()
print("--" * 10)

