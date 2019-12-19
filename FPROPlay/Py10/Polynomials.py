# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:01:44 2019

@author: filip
"""


def evaluate(a, x):
    listt=[p*x**a.index(p) for p in a]
    return sum(listt)
    