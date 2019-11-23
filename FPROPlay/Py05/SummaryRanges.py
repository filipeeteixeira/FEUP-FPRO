#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:20:27 2019

@author: filipe
"""

def summary_ranges(astring):
    alist=astring.split(",")
    range_start = previous_number = alist[0]
    string=""
    for number in alist[1:]: 
        if int(number) == int(previous_number) + 1: 
            previous_number = number
        else:
            string+=str(range_start)+"->"+str(previous_number)+","
            range_start = previous_number = number
    string+=str(range_start)+"->"+str(previous_number)
    return string

print(summary_ranges("0,1,2,3,4,5,7,10,11,20,21"))