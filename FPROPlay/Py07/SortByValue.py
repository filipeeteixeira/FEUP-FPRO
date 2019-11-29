#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:34:43 2019

@author: filipe
"""


def sort_by_value(dictt):
    ToSort = []
    for i in dictt.values():
        number = int(i[1:], 16)
        ToSort.append(number)
    ToSort.sort()
    for i in ToSort:
        
    
    return finalresult


print(sort_by_value({'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}))
