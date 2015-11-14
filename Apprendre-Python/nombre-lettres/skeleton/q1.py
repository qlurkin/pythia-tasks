# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Nombre de lettres

import sys

sys.path.append('/task/static')
from lib import pythia

def nbletters(word):
    s = '''@@f1@@'''
    if 'while' in s or 'for' in s:
        raise Exception('Vous ne pouvez pas utiliser de boucle while ou for')
    del(s)
@@f1@@
