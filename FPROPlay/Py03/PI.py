#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:58:57 2019

@author: filipe
"""

import math

somat=0
for i in range(0,50):
    somat+=(math.factorial(4*i)*(1103+26390*i))/((math.factorial(i)**4)*396**(4*i))
result=round(1/(((2*math.sqrt(2))/9801)*somat),8)

print(result)


