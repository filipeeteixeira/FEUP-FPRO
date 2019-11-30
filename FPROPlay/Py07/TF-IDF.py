# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 01:31:57 2019

@author: filip
"""

def tfidf(documents):
    wordsList=[]
    for i in documents:
        for word in i:
            if word not in wordsList:
                wordsList.append(word)
    