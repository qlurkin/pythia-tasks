#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Length String
# Execution script

import inspect
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
        find = [f for (n, f) in inspect.getmembers(q1, inspect.isfunction) if n == 'lengths']
        if len(find) != 1:
            raise pythia.UndeclaredException('lengths')
        if not callable(find[0]):
            raise pythia.BadTypeException('lengths', type(find[0]), 'function')
        spec = inspect.getargspec(find[0])
        if len(spec.args) != 1:
            raise pythia.WrongParameterNumberException('lengths', len(spec.args), 1)
        return q1.lengths(data)

    def parseTestData(self, data):
        return data[0]

TaskTestSuite().run('/tmp/work/output', 'data.res')
