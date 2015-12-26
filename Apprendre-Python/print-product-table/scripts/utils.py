def init():
    global __data__
    __data__ = []

def printmultiply(i, n):
    __data__.append('{} x {} = {}'.format(i, n, i * n))

def result():
    return '\n'.join(__data__)
