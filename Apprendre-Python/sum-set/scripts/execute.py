#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Somme d'un ensemble
# Execution script

import sys

sys.path.append('/task/static')
from lib import pythia

# Redirect stdout and stderr
sys.stdout = open('/tmp/work/output/stdout', 'w')
sys.stderr = open('/tmp/work/output/stderr', 'w')

# Try to import student's code
sys.path.append('/tmp/work')
try:
    import q1
except Exception as e:
    print(e, file=sys.stderr)
    sys.exit(0)

class TaskTestSuite(pythia.TestSuite):
    def __init__(self):
        pythia.TestSuite.__init__(self, '/tmp/work/input/data.csv')

    def studentCode(self, data):
        return q1.setsum(data)

    def parseTestData(self, data):
        return {int(x) for x in data[0][1:len(data[0]) - 1].split(',')}

TaskTestSuite().run('/tmp/work/output', 'data.res')
