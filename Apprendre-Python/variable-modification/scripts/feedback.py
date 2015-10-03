#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Variable modification
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
            output['feedback'] = {'score': 0, 'message': '<p>Une erreur s\'est produite lors de l\'exécution de votre programme :</p><pre>' + content + '</pre>'}
            hasError = True

# Check stdout, if no error
stdout = '/tmp/work/output/stdout'
if (not hasError) and os.path.exists(stdout):
    with open(stdout, 'r') as file:
        content = file.read().rstrip()
        # Good answer
        if content == '42':
            output['status'] = 'success'
            output['feedback']['score'] = 1
        # Undeclared variable
        elif content == 'exception:deleted':
            output['feedback']['message'] = '<p>Vous avez supprimé la variable <code>x</code>.</p>'
        # Bad type
        elif content == 'exception:badtype':
            output['feedback']['message'] = '<p>La variable <code>x</code> doit contenir le <b>nombre entier</b> 42.</p>'
        # Variable unchanged
        elif content == '10':
            output['feedback']['message'] = '<p>La valeur de la variable <code>x</code> n\'a pas été modifiée !</p>'
        else:
            output['feedback'] = {'score': 0, 'example': {'expected': '42', 'actual': content}}

print(json.dumps(output))