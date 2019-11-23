#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:59:18 2019

@author: filipe
"""

def get_sum_num(num):
    somaa=0
    for m in num:
        somaa+=ord(m)
    return somaa

def get_sum_tuple(atuple):
    soma=0
    for k in atuple:
        if type(k)==tuple:
            soma+=get_sum_tuple(k)
        else:
            soma+=get_sum_num(k)
    return soma


def greatest_member(atuple):
    larger=0
    newValue=0
    greatestMemb=""
    if atuple == ():
        return ()
    for i in atuple:
        if type(i)==tuple:
            newValue=get_sum_tuple(i)
            print(newValue)
            if (newValue > larger):
                larger=newValue
                greatestMemb=i
        else:
            newValue=get_sum_num(i)
            print(newValue)
            if(newValue>larger):
                larger=newValue
                greatestMemb=i
    return greatestMemb

print(greatest_member(('a', 'z', ('1', ('6', '2'), '9'), ('1', ('2',), '4'))))