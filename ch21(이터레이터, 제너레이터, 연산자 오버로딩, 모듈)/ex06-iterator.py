from MyEnumerate import *

if __name__ == '__main__':
    myEnumerate = MyEnumerate("abc")
    for index, item in myEnumerate:
        print(index, ":", item)