#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import json
import os
import sys

sys.path.append('/task/static')
from lib import pythia

# Read test configuration and generate test data
with open('/task/config/test.json', 'r', encoding='utf-8') as file:
  content = file.read()
  config = json.loads(content)
  pythia.generateTestData('/tmp/work/input', 'data.csv', config)
