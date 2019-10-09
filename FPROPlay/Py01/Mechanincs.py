#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:37:06 2019

@author: filipe
"""

import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

#lançamento obliquo
result= (2*cos_angle*sin_angle*(18**2))/(10)

print(round(result))
