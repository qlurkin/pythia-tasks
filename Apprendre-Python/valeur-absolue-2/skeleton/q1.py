# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Valeur absolue (2)

import sys

sys.path.append('/task/static')
from lib import pythia

def absval(x):
    result = @@f1@@
    if type(result) != int:
        raise pythia.BadTypeException('result', type(result), int)
    return result
