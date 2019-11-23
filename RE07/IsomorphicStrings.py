#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:14:28 2019

@author: filipe
"""

def findKey(dic,k):
    for i in dic.keys():
        if i ==k:
            return True
    return False

def findValue(dic,v):
    for i in dic.values():
        if i ==v:
            return True
    return False

def getKey(dic,k):
    for i in dic.keys():
        if i ==k:
            return i

def isomorphic(astring1,astring2):
    dictionary={}
    indx_astring2=0
    verify=True
    alist=[]
    for i in astring1:
        if (findKey(dictionary,i)):
            if dictionary[i]==astring2[indx_astring2]:
                indx_astring2+=1
                continue
            else:
                verify=False
                break
        if (findValue(dictionary,astring2[indx_astring2])):
            if getKey(dictionary,astring2[indx_astring2])==i:
                indx_astring2+=1
                continue
            else:
                verify=False
                break
        else:
            dictionary.update({i:astring2[indx_astring2]})
        indx_astring2+=1
        
    for j in dictionary.keys():
        alist.append((j,dictionary[j]))
    if (verify ==True):
        return "'{0}' and '{1}' are isomorphic because we can map: ".format(astring1,astring2) + str(alist)
    else:
        return "'{0}' and '{1}' are not isomorphic".format(astring1,astring2)

print(isomorphic('turtle', 'tletur'))
    

