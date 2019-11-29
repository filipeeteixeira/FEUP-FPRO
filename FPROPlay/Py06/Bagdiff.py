#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:18:42 2019

@author: filipe
"""

def bagdiff(xs,ys):
    for i in xs:
        if i in ys:
            xs.remove(i)
            ys.remove(i)
    return xs

print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))