#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Quel jour sommes-nous ?
# Preprocessing script

import json
import sys

sys.path.append('/task/static')
from lib import pythia

# Setup working directory
pythia.setupWorkingDirectory('/tmp/work')

# Read input data and fill skeleton files
data = sys.stdin.read().rstrip('\0')
input = json.loads(data)

class TaskPreprocessor(pythia.Preprocessor):
    def __init__(self):
        pythia.Preprocessor.__init__(self, input['fields'])

    def preprocess(self, fields):
        return '\n'.join(['{}:{}'.format(op, fields['f1'].count(op)) for op in ('if', 'else', 'elif')])

TaskPreprocessor().run('/tmp/work/output', 'preprocess.res')

pythia.fillSkeletons('/task/skeleton', '/tmp/work', input['fields'])

# Save task id
with open('/tmp/work/tid', 'w', encoding='utf-8') as file:
	file.write(input['tid'])
