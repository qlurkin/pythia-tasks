# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Dis moi la vérité !

import sys

sys.path.append('/task/static')
from lib import pythia

def truthvalue(a, b, c):
    result = @@f1@@
    if type(result) != bool:
        raise pythia.BadTypeException('result', type(result), bool)
    return result
