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

# Update score with quality constraint
with open('/tmp/work/output/postprocess.res', 'r', encoding='utf-8') as resfile,\
     open('/tmp/work/output/postprocess.fdk', 'r', encoding='utf-8') as fdkfile:
    results = [int(x.strip()) for x in resfile.readlines()]
    feedbacks = [int(x.strip()) for x in fdkfile.readlines()]
    if len(results) == len(feedbacks):
        nocall = 0
        morecalls = 0
        i = 0
        while i < len(results):
            if results[i] == 0:
                nocall += 1
            elif results[i] > feedbacks[i]:
                morecalls += 1
            i += 1
        if nocall > 0:
            output['feedback']['quality'] = {'weight': (len(results) - nocall) / len(results), 'message': '<p>Vous n\'appelez pas toujours la fonction <code>fact</code>.</p>'}
        elif morecalls > 0:
            output['feedback']['quality'] = {'weight': (len(results) - morecalls) / len(results), 'message': '<p>Vous calculez la factorielle de certains nombres inutilement.</p>'}
    else:
        output['feedback']['quality'] = {'weight': 0, 'message': '<p>Erreur lors du comptage des appels à la fonction <code>fact</code>.</p>'}

print(json.dumps(output))
