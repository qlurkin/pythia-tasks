#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Hello World (2)
# Execution script

import inspect
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
    find = [f for (n, f) in inspect.getmembers(q1, inspect.isfunction) if n == 'printhelloworld']
    if len(find) != 1:
        raise pythia.UndeclaredException('printhelloworld')
    if not callable(find[0]):
        raise pythia.BadTypeException('printhelloworld', type(find[0]), 'function')
    spec = inspect.getargspec(find[0])
    if len(spec.args) != 0:
        raise pythia.WrongParameterNumberException('printhelloworld', len(spec.args), 0)
    q1.printhelloworld()
except pythia.UndeclaredException as e:
    print('exception:undeclared:{}'.format(e.name), file=sys.stderr)
except pythia.BadTypeException as e:
    print('exception:badtype:{}:{}:{}'.format(e.name, e.actualtype, e.expectedtype), file=sys.stderr)
except pythia.WrongParameterNumberException as e:
    print('exception:wrongparameterexception:{}:{}:{}'.format(e.name, e.actualnumber, e.expectednumber), file=sys.stderr)
except Exception as e:
    print('exception:{}'.format(e), file=sys.stderr)
