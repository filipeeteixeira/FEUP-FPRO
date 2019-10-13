#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:26:13 2019

@author: filipe
"""

import math

def time_until_lost_connection(direction_A, direction_B):
    inside_angle = math.radians(direction_A-direction_B)
    
    distance_walked=math.sqrt(35**2/(2-2*math.cos(inside_angle)))
    
    hours_walked=distance_walked/5
    
    minutes_walked=hours_walked*60
    
    return round(minutes_walked,3)

print(time_until_lost_connection(0, 200))