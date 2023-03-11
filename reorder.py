#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Easy reading for handicapped people - get from scanner an speak the text 
# remove some parts of the scanned text that disturb the text-to-speech 
# V 0.1
# Author Thomas Glaser
# Copyright 2022-2023
# Released under the GPL version 3 or later license.
# 
# 
from curses import KEY_DOWN
import re
import os
from subprocess import call
from multiprocessing import Process
#
text = open('tmp/rawText.txt').readlines()
# 
# load all in one string
t2 = ""
for line in text:
    t2 = t2 + str(line)
# 
# cleanup this string
#
t2 = t2.replace("\n\n", "\n")
t2 = t2.replace("\n", " ")
t2 = t2.replace("  ", " ")
t2 = t2.replace("*", "")
t2 = re.sub(r",(\w)", r", \g<1>", t2)
t2 = re.sub(r"\. ", r".\n", t2)
#print(t2)
t3 = t2.split("\n") 
outText = open('tmp/readText.txt', 'w')
outText.write(t2) 