#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:02:30 2019

@author: filipe
"""

def roman_to_integer(astring):
    dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result=0
    for i in range(0,len(astring)-1):
        if dict1[astring[i]]>=dict1[astring[i+1]]:
            result+=dict1[astring[i]]
        else:
            result-=dict1[astring[i]]
    result+=dict1[astring[len(astring)-1]]
    return result

print(roman_to_integer('XV'))