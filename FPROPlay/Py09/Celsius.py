# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:44:04 2019

@author: filip
"""

def to_celsius(t):
    return list(map(lambda x: round((x-32)/1.8,1),t))