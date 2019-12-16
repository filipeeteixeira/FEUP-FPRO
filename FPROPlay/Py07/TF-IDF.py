# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 01:31:57 2019

@author: filip
"""
import math

def numOcc(doc,word):
    counter=0
    for i in doc:
        if word==i:
            counter+=1
    return counter

def numDoc(listt,word):
    n=len(listt)
    for i in listt:
        if i==0:
            n-=1
    return n

def tfidf(documents):
    wordsList=[]
    for i in documents:
        for word in i.split():
            if word.lower() not in wordsList:
                wordsList.append(word.lower())
    print(wordsList)

    manyOccurs={}
    for i in documents:
        for word in wordsList:
            manyOccurs.update({word:[]})
            
    for i in documents:
        for word in wordsList:
            manyOccurs[word].append(numOcc(map(str.lower,i.split()),word))
    
    for i in manyOccurs.keys():
        n=numDoc(manyOccurs[i],i)
        for k in range (0,len(manyOccurs[i])):
            manyOccurs[i][k]=round(manyOccurs[i][k]*math.log(len(documents)/n),3)
    
    return manyOccurs

print(tfidf(['We are what we repeatedly do excellence then is not an act but a habit', 'A wise man gets more use from his enemies than a fool from his friends', 'Do not seek to follow in the footsteps of the men of old seek what they sought', 'All men are frauds The only difference between them is that some admit it I myself deny it']))
            
            
    
        