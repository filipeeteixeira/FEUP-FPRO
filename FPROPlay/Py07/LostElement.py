#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:32:05 2019

@author: filipe
"""

def lost_element(s1,s2):
    for i in s1:
        if i not in s2:
            return i
    for j in s2:
        if j not in s1:
            return j