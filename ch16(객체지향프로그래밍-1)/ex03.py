from Person import *

if __name__ == '__main__':
    iu = Person()
    print("IU의 name:", iu.getName())
    print("IU의 age:", iu.age)
    print("IU의 height:", iu.height)
    print("IU의 weight:", iu.weight)
    print("IU의 address:", iu.address)

    print("--" * 10)

    ezSilver = Person()
    ezSilver.setName("이지은")
    print("EzSilver의 name:", ezSilver.getName())
    print("EzSilver의 age:", ezSilver.age)
    print("EzSilver의 height:", ezSilver.height)
    print("EzSilver의 weight:", ezSilver.weight)
    print("EzSilver의 address:", ezSilver.address)