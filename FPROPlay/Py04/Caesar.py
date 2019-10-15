#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:05:35 2019

@author: filipe
"""

import math

def fibb(index_letra):
    fn=((1+math.sqrt(5))**index_letra-(1-math.sqrt(5))**index_letra)/(2**index_letra*math.sqrt(5))
    return int(fn)

def encrypted_letter(letra,index_letra):
    abec="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in abec:
        if (i==letra):
            newLetter=abec[(abec.index(i)-fibb(index_letra))%26]
            return newLetter
    return letra
        
def caesar(message):
    EncryptedMessage=""
    for i in message:
        print(i)
        EncryptedMessage+=encrypted_letter(i,message.index(i))
        message=message[:message.index(i)]+" "+message[message.index(i)+1:]
    return EncryptedMessage

print(caesar("HELLO WORLD!"))
    