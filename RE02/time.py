#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:52:58 2019

@author: filipe
"""

import datetime

current_time=datetime.datetime.now()

#print(current_time.strftime("%H:%M"))

alarm_h= (current_time.hour+8 + (current_time.minute+30)//60) % 24
alarm_m= (current_time.minute+30)%60

print(str(alarm_h).zfill(2)+":"+str(alarm_m).zfill(2))


