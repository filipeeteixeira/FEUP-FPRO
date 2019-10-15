#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:35:59 2019

@author: filipe
"""

def ugly(n):
    while n%2==0:
        n=n/2
    while n%3==0:
        n=n/3
    while n%5==0:
        n=n/5
    if n==1:
        return True
    else:
        return False