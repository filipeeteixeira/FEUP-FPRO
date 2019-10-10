#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:44:59 2019

@author: filipe
"""

import datetime

hour= int(input())
minutes= int(input())

hour = (hour + 6 + ((minutes + 51)//60)) % 24
minutes = (minutes + 51)%60

x=datetime.time(hour,minutes)

print(x.strftime("%H:%M"))