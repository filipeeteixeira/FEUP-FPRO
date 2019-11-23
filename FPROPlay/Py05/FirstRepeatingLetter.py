#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:33:28 2019

@author: filipe
"""

def repeated_letter(s):
    for i in s:
        s=s[:s.index(i)]+s[s.index(i)+1:]
        for k in s:
            if i==k:
                return i
    