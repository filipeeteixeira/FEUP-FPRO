# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:11:10 2019

@author: filip
"""

def rearrange(l):
    list1=[i*1 for i in l if i<=0]
    list2=[i*1 for i in l if i>0]
    return list1+list2