#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Sinus angle
# Feedback script

import ast
import csv
import json
import os
import sys

sys.path.append('/task/static')
from lib import pythia

import math

def sumsinus(a, b):
  a = math.radians(a)
  b = math.radians(b)
  return math.sin(a) * math.cos(b) + math.sin(a) * math.sin(b)

class TaskFeedbackSuite(pythia.FeedbackSuite):
  def __init__(self, config):
    pythia.FeedbackSuite.__init__(self, '/tmp/work/input/data.csv', '/tmp/work/output/data.res', config)

  def teacherCode(self, data):
    return sumsinus(*data)

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
  output['feedback']['score'] = feedback['stats']['succeeded'] / feedback['stats']['total']
  output['status'] = 'success' if verdict else 'failed'

print(json.dumps(output))
