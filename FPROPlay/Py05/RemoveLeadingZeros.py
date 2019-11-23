#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:58:45 2019

@author: filipe
"""

def remove_leading(ip):
    alist=ip.split(".")
    klist=[]
    for i in alist:
        klist.append(str(int(i)))
    return ".".join(klist)
