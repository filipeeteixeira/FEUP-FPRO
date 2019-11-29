#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:00:41 2019

@author: filipe
"""

def nth_lowest(lnum,n):
    lnum.sort()
    return lnum[n-1]

print(nth_lowest([42, 234, 135, 21, 232, 12312, -2343], 2))