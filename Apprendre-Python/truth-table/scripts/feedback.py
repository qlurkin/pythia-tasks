#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Dis moi la vérité !
# Feedback script

import ast
import csv
import json
import os
import sys

sys.path.append('/task/static')
from lib import pythia

import math

def truthvalue(a, b, c):
    return b or (a and c)

class TaskFeedbackSuite(pythia.FeedbackSuite):
    def __init__(self, config):
        pythia.FeedbackSuite.__init__(self, '/tmp/work/output/stderr', None, '/tmp/work/input/data.csv', '/tmp/work/output/data.res', config)

    def teacherCode(self, data):
        return truthvalue(*data)

    def parseTestData(self, data):
        return tuple(x == 'True' for x in data)

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
with open('/tmp/work/output/preprocess.res', 'r', encoding='utf-8') as file:
    total = 0
    for line in file:
        total += int(line.rstrip().split(':')[1])
    output['feedback']['quality'] = {'weight': 2.0 / total if total != 0 else 0}
    if total > 2:
        output['feedback']['quality']['message'] = "<p>Vous pouvez utiliser moins d'opérateurs logiques.</p>"

print(json.dumps(output))
