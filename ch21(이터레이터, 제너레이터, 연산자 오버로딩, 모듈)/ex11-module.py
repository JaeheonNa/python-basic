import module.fibo as fibo
fibo.fib_num(1000)
print(fibo.fib_list(1000))
print("--" * 10)

from module.fibo import fib_num
from module.fibo import fib_list
fib_num(1000)
print(fib_list(1000))
print("--" * 10)

from module.fibo import *
fib_num(1000)
print(fib_list(1000))
print("--" * 10)

