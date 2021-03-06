#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Coefficient binomial
# Execution script

import sys

sys.path.append('/task/static')
from lib import pythia

import utils

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
        self.__postprocess = open('/tmp/work/output/postprocess.res', 'w', encoding='utf-8')

    def studentCode(self, data):
        utils.init()
        coeff = q1.binom(*data)
        self.__postprocess.write('{}\n'.format(len(utils.cache())))
        return coeff

    def parseTestData(self, data):
        return tuple(int(x) for x in data)

    def __del__(self):
        self.__postprocess.close()

TaskTestSuite().run('/tmp/work/output', 'data.res')
