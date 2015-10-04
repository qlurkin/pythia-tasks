#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Lunch pack
# Feedback script

import ast
import csv
import json
import os
import sys

sys.path.append('/task/static')
from lib import pythia

def sum(sandwich, beverage, dessert):
  return 17 * (sandwich + 2 * beverage + dessert)

class TaskFeedbackSuite(pythia.FeedbackSuite):
  def __init__(self, config):
    pythia.FeedbackSuite.__init__(self, '/tmp/work/input/data.csv', '/tmp/work/output/data.res', config)

  def teacherCode(self, data):
    return sum(*data)

  def parseTestData(self, data):
    return tuple(int(x) for x in data)

# Retrieve task id
with open('/tmp/work/tid', 'r', encoding='utf-8') as file:
    tid = file.read()
output = {'tid': tid, 'status': 'failed', 'feedback': {'score': 0}}

# Check stderr
hasError = False
stderr = '/tmp/work/output/stderr'
if os.path.exists(stderr):
    with open(stderr, 'r') as file:
        content = file.read().strip()
        if content != '':
            output['feedback'] = {'score': 0, 'message': '<p>Une erreur s\'est produite lors de l\'exécution de votre programme :</p><pre>' + content + '</pre>'}
            hasError = True

if not hasError:
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
