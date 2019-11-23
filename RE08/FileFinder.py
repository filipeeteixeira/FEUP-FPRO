#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:39:01 2019

@author: filipe
"""


def file_finder(dirs,file_name):
    vec = []
    for i in range(1,len(dirs)):
        if type(dirs[i])==list:
            ret=file_finder(dirs[i],file_name)
            if ret != None:
                for j in ret:
                    vec.append(dirs[0]+"/"+j)
        elif file_name == dirs[i]:
            vec.append(dirs[0]+"/"+dirs[i])
    if len(vec)==0:
        return None
    else:
        return vec


print(file_finder(['user', ['Torrents', ['Movies', ["asdf",'incredibles.mp4', 'mile22.mp4']], ['Books', "mile22.mp4",'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'mile22.mp4'))     