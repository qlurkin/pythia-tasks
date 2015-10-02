#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Hello World
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
        if content == 'Hello\nWorld!':
            output['status'] = 'success'
            output['feedback']['score'] = 1
        # Missing line break
        elif '\n' not in content:
            output['feedback']['message'] = '<p>Vous devez écrire la phrase <code>Hello World!</code> sur deux lignes.</p>'
        # Missing final exclamation mark
        elif content == 'Hello\nWorld':
            output['feedback']['message'] = '<p>Vous avez oublié le point d\'exclamation !</p>'
        else:
            tokens = content.split('\n')
            if len(tokens) == 2 and (tokens[0].lower() == 'hello' or tokens[1].lower().startswith('world')):
                output['feedback']['message'] = '<p>Attention, la différence entre majuscule et minuscule est importante.</p>'
            else:
                output['feedback'] = {'score': 0, 'example': {'expected': 'Hello\nWorld!', 'actual': content}}
                if content == '':
                    output['feedback']['message'] = '<p>Votre programme n\'affiche rien.</p>'

print(json.dumps(output))