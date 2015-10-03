#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Variable modification
# Execution script

import sys

sys.path.append('/task/static')
from lib import pythia

# Redirect stdout and stderr
sys.stdout = open('/tmp/work/output/stdout', 'w')
sys.stderr = open('/tmp/work/output/stderr', 'w')

# Try to import student's code
sys.path.append('/tmp/work')
try:
    import q1
except Exception as e:
    print(e, file=sys.stderr)
    sys.exit(0)

# Execute student's code
try:
    print(q1.getvalue())
except pythia.UndeclaredException:
    print('exception:deleted')
except pythia.BadTypeException:
    print('exception:badtype')
except Exception as e:
    print(e, file=sys.stderr)
