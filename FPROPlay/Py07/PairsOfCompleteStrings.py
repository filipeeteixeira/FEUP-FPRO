# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 01:08:39 2019

@author: filip
"""

def containsAlphabet(s1):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s1:
            return False
    return True

def complete_pairs(s1,s2):
    result=set()
    for i in s1:
        for j in s2:
            if containsAlphabet(i+j):
                result.add(i+j)
    return result

print(complete_pairs({'yesbg', 'graby'}, {'atqswrlxhikeczfnpjdvmou'}))