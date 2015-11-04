# -*- coding: utf-8 -*-
# Course: Apprendre Python
# Problem: Surveillance de la température

import sys

sys.path.append('/task/static')
from lib import pythia

def checktemp(temperature, thermostat):
@    @f1@@
    if 'outlimits' not in locals():
        raise pythia.UndeclaredException('outlimits')
    if 'thermostat' not in locals():
        raise pythia.UndeclaredException('thermostat')
    if type(outlimits) != bool:
        raise pythia.BadTypeException('outlimits', type(outlimits), bool)
    if type(thermostat) != int:
        raise pythia.BadTypeException('thermostat', type(thermostat), int)
    return (outlimits, thermostat)
