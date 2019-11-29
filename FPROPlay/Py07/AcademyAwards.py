#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 21:22:57 2019

@author: filipe
"""

def academy_awards(alist):
    resultDict={}
    for i in alist:
        if i[1] not in resultDict:
            resultDict.update({i[1]:1})
        else:
            resultDict[i[1]]+=1
    return resultDict

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]))