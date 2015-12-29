def init():
    global __data__
    __data__ = {}
    __data__[0] = 1

def fact(n):
    if n not in __data__:
        __data__[n] = __factrec(n)
    return __data__[n]

def __factrec(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def cache():
    return __data__
