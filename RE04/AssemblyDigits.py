#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:54:16 2019

@author: filipe
"""

def adigits(a,b,c):
    s=[int(a),int(b),int(c)]
    s.sort(reverse=True)
    return s[0]*100+s[1]*10+s[2]
            
            
        