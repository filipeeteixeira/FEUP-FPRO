# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:52:33 2019

@author: filip
"""

def to_celsius(t):
    return [round((i-32)/1.8,1) for i in t]