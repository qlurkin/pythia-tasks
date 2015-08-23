#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Feedback script

import json
import os

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
            output['feedback'] = {'score': 0, 'message': '<p>An error occurred.</p><pre>' + content + '</pre>'}
            hasError = True

# Check stdout, if no error
stdout = '/tmp/work/output/stdout'
if (not hasError) and os.path.exists(stdout):
    with open(stdout, 'r') as file:
        content = file.read().rstrip()
        if content == 'Hello World!':
            output['status'] = 'success'
            output['feedback']['score'] = 1
        else:
            output['feedback'] = {'score': 0, 'example': {'expected': 'Hello World!', 'actual': content}}
            if content == '':
                output['feedback']['message'] = '<p>Your program do not print anything.</p>'

print(json.dumps(output))