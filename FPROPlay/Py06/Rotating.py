#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:05:56 2019

@author: filipe
"""

def rotate_list(l):
    resultlist=l[3:]
    resultlist=resultlist+l[0:3]
    return resultlist