#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:00:35 2019

@author: filipe
"""
def andOp(x,y):
    toreturn=set()
    for i in x:
        for k in y:
            if(i==k):
                toreturn.add(i)
    return toreturn

def orOp(x,y):
    toreturn=x
    for i in y:
        toreturn.add(i)
    return toreturn

def xorOp(x,y):
    return x^y

def notOp(x,y):
    for i in x:
        if i in y:
            y.remove(i)
    return y

def logic(s, operations):
    result=s.copy()
    for key in operations.keys():
        if key == 'and':
            result = andOp(result,operations[key])
        elif key == 'xor':
            result = xorOp(result,operations[key])
        elif key == 'not':
            result= notOp(result,operations[key])
        elif key == 'or':
            result= orOp(result,operations[key])
    return result

def logic2(s, operations):
    s1 = s.copy()
    for akey in operations:
        if akey == 'and':
            s1 = s1.intersection(operations[akey])
        if akey == 'not':
            s1 = s1.symmetric_difference(operations[akey])
        if akey == 'or':
            s1.update(operations[akey])
        if akey == 'xor':
            s1.symmetric_difference_update(operations[akey])
            
    return s1
    
print(logic2({'Bernardo', 'Eduardo', 'Diana', 'Carlos'}, {'and': {'Goncalo', 'Eduardo', 'Diana', 'Filipe'}, 'or': {'Ana', 'Filipe'}}))
    