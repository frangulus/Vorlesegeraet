#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 
from ast import Global
from curses import KEY_DOWN
from multiprocessing.connection import wait
from threading import Thread
from readchar import key, readkey
import re
import os
from subprocess import call
#from multiprocessing import Process, Value
#import getch
import time
from py import process

inKey = ""

#known_keys = {v: k for k, v in reversed(vars(key).items()) if not k.startswith("__")}


def keylogger():
    global running
    global state
    print("starting keylogger...")
    while running:
        try:
            data = readkey()
        except KeyboardInterrupt:
            running = False
            break
        if data == key.DOWN:
            state = "Down"
        if data == key.UP:
            state = "Up"    
            
        print(f"{data} - key was pressed")

    print("stopping keylogger...")

def openFile():
    t2 = ""
    try:
        #txtFile = open('tmp/rawText.txt','r')
        text = open('tmp/rawText.txt').readlines()
    except:
        running = False
        return("E1")
    for line in text:
        t2 = t2 + str(line)
        t2 = t2.replace("\n\n", "\n")
        t2 = t2.replace("\n", " ")
        t2 = t2.replace("  ", " ")
        t2 = re.sub(r",(\w)", r", \g<1>", t2)
        t2 = re.sub(r"\. ", r".\n", t2)
        print(t2)
        t3 = t2.split("\n") 
    return(t3)    

def speakTextPerLine(text):
    global state
    i = 0
    
    while i < len(text):
        r = call(['espeak-ng', '-vmb-de6', '-b1', '-s140', text[i]])   
        state = ""
        print(r)
    #   k = readkey()
    #    if k == key.DOWN:
    #        i = i + 1
        while state == "":
            time.sleep(1)
        if state == "Down":
            i = i + 1
            state = ""    
    
    r = call(['espeak-ng', '-vmb-de6', '-b1', '-s140', "Ende des Textes"])   
    print(r)                
    
def speakAllText(text):    
    i= 0
    while i < len(text):
        r = call(['espeak-ng', '-vmb-de6', '-b1', '-s140', text[i]])   
        print(r)   
    if state == "Down":
        i = len(text)
    
# Global Varaibles
running = 1
state = "" 
#
# Main funktion
def main():
    # while running:
    print(f"LOG: current time is {time.time()} --- {state}")
    text = openFile()
    speakTextPerLine(text)
    time.sleep(1)


# Start  Threads and main
if __name__ == '__main__':
#
    Thread(name="keyreader", target=keylogger).start()
    main()
    
        
        