# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: T'es trop swap !

import sys

sys.path.append('/task/static')
from lib import pythia

def swap(x, y):
@    @f1@@
    if 'x' not in locals():
        raise pythia.UndeclaredException('x')
    if 'y' not in locals():
        raise pythia.UndeclaredException('y')
    if type(x) != int:
        raise pythia.BadTypeException('x', type(x), int)
    if type(y) != int:
        raise pythia.BadTypeException('y', type(y), int)
    return (x, y)
