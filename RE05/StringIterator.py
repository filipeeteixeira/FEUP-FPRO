#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:40:28 2019

@author: filipe
"""

def rm_letter_rev(l,astr):
    newstr=""
    for i in astr:
        if i!=l:
            newstr+=i
        else:
            continue
    newstr=newstr[::-1]
    return newstr

            