# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:14:31 2019

@author: filip
"""

import statistics as s

def batch_norm(alist,batch_size):
    lists=[alist[x:x+batch_size] for x in range(0,len(alist),batch_size)]
    nlists=[]
    for k in range(0,len(lists)):
        nlists.append(list(map(lambda i: i-(s.median(lists[k])),lists[k])))
    for j in nlists:
        yield j

print(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5))