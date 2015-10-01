#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: L'as de la programmation
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
        if content == 'Je suis un as de la programmation.':
            output['status'] = 'success'
            output['feedback']['score'] = 1
        elif content == 'Je suis un as de la programmation':
            output['feedback']['message'] = '<p>Vous avez oublié le point en fin de phrase.</p>'
        else:
            output['feedback'] = {'score': 0, 'example': {'expected': 'Je suis un as de la programmation.', 'actual': content}}
            if content == '':
                output['feedback']['message'] = '<p>Votre programme n\'affiche rien.</p>'

print(json.dumps(output))