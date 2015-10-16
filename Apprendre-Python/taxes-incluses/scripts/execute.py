#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Taxes incluses
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
    return q1.taxincluded(*data)

  def parseTestData(self, data):
    return (float(data[0]), int(data[1]))

TaskTestSuite().run('/tmp/work/output', 'data.res')
