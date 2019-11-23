#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:30:20 2019

@author: filipe
"""


def manipulator(l,cmds):
    string=""
    for i in cmds:
        if i.find("insert")!=-1:
            tmp = i.split(" ")
            l.insert(int(tmp[1]),int(tmp[2]))
        elif i.find("print")!=-1:
            string+=str(l)+" "
        elif i.find("remove")!=-1:
            tmp = i.split(" ")
            l.remove(int(tmp[1]))
        elif i.find("append")!=-1:
            tmp = i.split(" ")
            l.append(int(tmp[1]))
        elif i.find("sort")!=-1:
            l.sort()
        elif i.find("pop")!=-1:
            l.pop()
        elif i.find("reverse")!=-1:
            l.reverse()
    return string
          
print(manipulator([], ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']))