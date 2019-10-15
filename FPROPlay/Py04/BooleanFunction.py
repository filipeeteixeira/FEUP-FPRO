#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:14:02 2019

@author: filipe
"""

def validate(x):
    while ((type(x)==float or type(x)== int) and x >= 0 and x <= 100):
        return True
    return False