#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:43:20 2019

@author: filipe
"""

def count_chars(astring):
    countInt=0
    countStr=0
    countChr=0
    for i in astring:
        if (ord(i)<58 and ord(i)>47):
            countInt+=1
        elif (ord(i.upper())>64 and ord(i.upper())<91):
            countStr+=1
        else:
            countChr+=1
    return (countStr,countInt,countChr)
