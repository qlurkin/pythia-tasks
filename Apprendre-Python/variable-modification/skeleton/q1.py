# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Variable modification

import sys

sys.path.append('/task/static')
from lib import pythia

def getvalue():
    x = 10
@    @f1@@
    if not 'x' in locals():
        raise pythia.UndeclaredException('deleted')
    elif not type(x) == int:
        raise pythia.BadTypeException('badtype')
    return x
