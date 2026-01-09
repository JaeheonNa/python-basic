



if __name__ == "__main__":
    import fibo

    fibo.fib(40)
    print()
    print(fibo.sum(10))

    print("==" * 10)

    from fibo import *

    fib(40)
    print()
    print(sum(10))

    print(fibo.__name__)
    print(__name__)