#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:24:57 2019

@author: filipe
"""

def fetch_middle(llists):
    result=[]
    for i in llists:
        if len(i)%2!=0:
            result.append(i[len(i)//2])
        else:
            result.append((i[len(i)//2]+i[len(i)//2-1])/2)
    return result