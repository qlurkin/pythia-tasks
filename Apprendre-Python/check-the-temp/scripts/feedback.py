#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Surveillance de la température
# Feedback script

import ast
import csv
import json
import os
import sys

sys.path.append('/task/static')
from lib import pythia

import math

def checktemp(temperature, thermostat):
    outlimits = False
    if temperature <= 13 or temperature >= 27:
        outlimits = True
        thermostat += temperature - 15
    return (outlimits, thermostat)

class TaskFeedbackSuite(pythia.FeedbackSuite):
    def __init__(self, config):
        pythia.FeedbackSuite.__init__(self, '/tmp/work/output/stderr', None, '/tmp/work/input/data.csv', '/tmp/work/output/data.res', config)

    def teacherCode(self, data):
        return checktemp(*data)

    def parseTestData(self, data):
        return tuple(int(x) for x in data)

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
