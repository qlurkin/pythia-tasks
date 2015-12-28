def init():
    global __data__
    __data__ = {}

def fact(n):
    if n not in __data__:
        __data__[n] = __factrec(n)
    return __data__[n]

def __factrec(n):
    if n == 0:
        return 1
    return n * __factrec(n - 1)

def cache():
    return __data__
