#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 01:01:07 2019

@author: filipe
"""

import math

sides= int(input())

hypot = math.sqrt(sides**2+sides**2)

print(round(hypot,2))