# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Valeur absolue

import sys

sys.path.append('/task/static')
from lib import pythia

def absval(x):
@    @f1@@
    if 'x' not in locals():
        raise pythia.UndeclaredException('x')
    if type(x) != int:
        raise pythia.BadTypeException('x', type(x), int)
    return x
