#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Typception
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
        return q1.containstype(data)

    def parseTestData(self, data):
        if data[0] == 'int':
            return int(data[1])
        elif data[0] == 'float':
            return float(data[1])
        elif data[0] == 'bool':
            return data[1] == 'True'
        elif data[0] == 'type':
            if data[1] == 'bool':
                return bool
            else:
                return int
        else:
            return data[1]

TaskTestSuite().run('/tmp/work/output', 'data.res')
