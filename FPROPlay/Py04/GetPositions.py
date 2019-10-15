#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 00:01:18 2019

@author: filipe
"""


def get_word1(w):
    for i in w:
        if i==" ":
            index=w.index(i)
    return w[:index]

def get_word2(w):
    for i in w:
        if i==" ":
            index=w.index(i)
    return w[index+1:]

def get_positions(sentence, word_list):
    result=""
    for i in word_list:
        if get_word1(sentence)==i:
            result+= str(word_list.index(i))
            word_list[word_list.index(i)]=""
            break
    if result=="":
        return result
    for k in word_list:
        if get_word2(sentence)==k:
            result+= " " + str(word_list.index(k))
            break
    
    return result
        
print(get_positions('lousy lousy', ['hello', 'lousy', 'lousy']))