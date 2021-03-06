def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n):
    """ Calculating n! recursively as n! = n * (n-1)!"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """ F(n) = F(n-1) + F(n-1)"""
    """ Recursive function - takes a long time to run"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    """ Iterative approach"""
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = result
        for n in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result




for i in range(20):
    # print(i, fact(i))
    # print(i, factorial(i))
    print(i, fib(i))

