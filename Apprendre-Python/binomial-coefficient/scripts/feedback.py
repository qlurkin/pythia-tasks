#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Coefficient binomial
# Feedback script

import ast
import csv
import json
import os
import sys

sys.path.append('/task/static')
from lib import pythia

import math
import utils

def binom(n, k):
    return utils.fact(n) // (utils.fact(k) * utils.fact(n - k))

class TaskFeedbackSuite(pythia.FeedbackSuite):
    def __init__(self, config):
        pythia.FeedbackSuite.__init__(self, '/tmp/work/output/stderr', None, '/tmp/work/input/data.csv', '/tmp/work/output/data.res', config)
        self.__postprocess = open('/tmp/work/output/postprocess.fdk', 'w', encoding='utf-8')

    def teacherCode(self, data):
        utils.init()
        coeff = binom(*data)
        self.__postprocess.write('{}\n'.format(len(utils.cache())))
        return coeff

    def parseTestData(self, data):
        return tuple(int(x) for x in data)

    def __del__(self):
        self.__postprocess.close()

# Retrieve task id
with open('/tmp/work/tid', 'r', encoding='utf-8') as file:
    tid = file.read()
output = {'tid': tid, 'status': 'failed', 'feedback': {'score': 0}}

# Read test configuration
config = []
with open('/task/config/test.json', 'r', encoding='utf-8') as file:
    content = file.read()
    config = json.loads(content)
    config = config['predefined']
(verdict, feedback) = TaskFeedbackSuite(config).generate()
output['feedback'] = feedback
output['status'] = 'success' if verdict else 'failed'

print(json.dumps(output))
