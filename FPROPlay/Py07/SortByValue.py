#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:34:43 2019

@author: filipe
"""


def sort_rule(item):
    return int(item[1][1:], 16)

def sort_by_value(dictt):
    temp = sorted(dictt.items(),key=sort_rule,reverse=False)
    return temp

print(sort_by_value({'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}))
