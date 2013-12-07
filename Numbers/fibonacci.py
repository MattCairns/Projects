import time
def fib(n):
    """Returns a list of the fibonacci numbers up to n"""

    fib0 = 0
    fib1 = 1
    count = 0
    yield fib0
    yield fib1

    while count < n:
        fib0, fib1 = fib1, fib0+fib1
        yield fib1
        count += 1


for i in fib(100):
    print i



