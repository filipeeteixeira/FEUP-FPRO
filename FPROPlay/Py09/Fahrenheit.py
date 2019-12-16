# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:52:47 2019

@author: filip
"""

def to_fahrenheit(t):
    return list(map(lambda x: round(x*(9/5)+32,2),t))