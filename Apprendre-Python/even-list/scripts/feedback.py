#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Even List
# Feedback script

import json
import sys

sys.path.append('/task/static')
from lib import pythia

def even(liste):
    res = []
    for i in range(0, len(liste), 2):
        res.append(liste[i])
    return res

class TaskFeedbackSuite(pythia.FeedbackSuite):
    def __init__(self, config):
        pythia.FeedbackSuite.__init__(self, '/tmp/work/output/stderr', None, '/tmp/work/input/data.csv', '/tmp/work/output/data.res', config)

    def teacherCode(self, data):
        return even(data)

    def parseTestData(self, data):
        return data[0]

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
