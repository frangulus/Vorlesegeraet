#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 
from curses import KEY_DOWN
import re
import os
from subprocess import call
from multiprocessing import Process
#import getch

#def readKey():
#    while 1:
#        key = getch.getch()
#        print(key)




#txtFile = open('tmp/rawText.txt','r')
#for line in txtFile:
#    print(line)
#txtFile.close()
text = open('tmp/rawText.txt').readlines()
#print(text)  
#print("___________________________________________________________")
t2 = ""
for line in text:
    t2 = t2 + str(line)
#print(t2)
t2 = t2.replace("\n\n", "\n")
t2 = t2.replace("\n", " ")
t2 = t2.replace("  ", " ")
t2 = t2.replace("*", "")
t2 = re.sub(r",(\w)", r", \g<1>", t2)
t2 = re.sub(r"\. ", r".\n", t2)
#print(t2)
t3 = t2.split("\n") 

#print(t3)

i=0
#
#event = keyboard.read_event()
#while i < len(t3):
#    r = call(['espeak-ng', '-vmb-de6', '-b1', '-s140', t3[i]])
#    print(r)
#    key = getch.getch()
#    print(key)
        
    #cont = input()
#    i = i + 1
    

#for line in t3:
#    outFile= "tmp/text2read" + str(i) + ".txt"
#    outText = open(outFile, 'w')
#    call(['espeak-ng', '-vmb-de6', '-b1', '-s140', line])
    #
#    cont = input()
    
#    i = i + 1
    
    
#text.close()
outText = open('tmp/readText.txt', 'w')
outText.write(t2) 