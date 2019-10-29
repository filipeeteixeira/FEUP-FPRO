#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:30:48 2019

@author: filipe
"""

def find_dtype(atuple,data_type):
    newtuple=()
    for i in atuple:
        if (type(i).__name__==data_type):
            newtuple+=(i,)
    return newtuple

