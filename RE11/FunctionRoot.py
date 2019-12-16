# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:59:14 2019

@author: filip
"""

def bisect(f,n):
    lower=0
    upper=1
    it=0
    while(it<n):
        mid=(lower+upper)/2
        if f(lower)*f(mid)<0:
            upper=mid
        else:
            lower=mid
        it+=1
    return round(mid,5)