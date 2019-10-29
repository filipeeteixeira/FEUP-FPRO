#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:44:47 2019

@author: filipe
"""

def is_palindrome(string):
    print(string)
    if len(string)==1 or string=="":
        return False
    stringInv=string[::-1]
    for i in range(0,len(string)-1):
        if stringInv[i]==string[i]:
            continue
        else:
            return False
    
    return True
        

def palindrome(astring):
    numPalindromes=0
    for i in range(0,len(astring)-1):
        for k in range(i,len(astring)):
            if is_palindrome(astring[i:k+1]):
                numPalindromes+=1
            else:
                continue
    return "The string '{0}' contains {1} palindrome substrings.".format(astring,numPalindromes)

        