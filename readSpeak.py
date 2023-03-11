#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Easy reading for handicapped people - get from scanner an speak the text 
# Main proramm file readSpeak.py 
# V 0.1
# Author Thomas Glaser
# Copyright 2022-2023
# Released under the GPL version 3 or later license.
# 
#
# import essential modules - dont't change 
from threading import Thread
from readchar import key, readkey
import re
import os
from subprocess import call
import time

# import individual modules - change it for your requirements
# Language and individuel messages for speaked messages 
import messagesDE as m
import configuration as c

#known_keys = {v: k for k, v in reversed(vars(key).items()) if not k.startswith("__")}


def keylogger():
    global running
    global ctlKey
    global ctlState
    global ctlRun
    global volume
    print("starting keylogger...")
    while running:
        try:
            data = readkey()
        except KeyboardInterrupt:
            running = False
            break
        if data == key.DOWN:
            ctlKey = "Down"
            volume = volume - 2
            setVolume(volume)
        if data == key.UP:
            ctlKey = "Up"
            volume = volume + 2
            setVolume(volume)
        if data == key.RIGHT:
            ctlKey = "Forward" 
        if data == key.LEFT:
            ctlKey = "Backward"
        if data == "+":
            if ctlRun == "Start":
                ctlRun = "Stop"
            else:
                ctlRun = "Start"
            print(ctlRun)    
        if data == "-":
            if ctlState == "StartScan":
                ctlState = ""
            else:
                ctlState = "StartScan"                                        
            
        print(f"{data} - key was pressed")

    print("stopping keylogger...")

def setVolume(volume):
    if volume < 80 :
        volume = 80
    if volume > 100 :
        volume = 100     
    v = str(volume) + "%"
    r = call(['amixer', '-c', '3', 'sset', 'Speaker','0', v,',',v])
    print(v)

def openFile():
    t2 = ""
    try:
        #txtFile = open('tmp/rawText.txt','r')
        text = open('tmp/readText.txt').readlines()
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
        #print(t2)
        t3 = t2.split("\n") 
    return(t3)    

def speakTextPerLine(text):
    global ctlKey, ctlRun
    i = 0
    
    while i < len(text):
        r = call(['espeak-ng', '-vmb-de6', '-b1', '-s140', text[i]])   
        ctlKey = ""
        print(i)
    
        while ctlKey == "" and ctlRun == "Start": 
            time.sleep(1)
        if ctlKey == "Forward":
            i = i + 1
            ctlKey = ""
        if ctlRun == "Stop":
            i = len(text)
            r = call(['espeak-ng', '-vmb-de5', '-b1', '-s140', m.stopReading])
            return()        
    
    r = call(['espeak-ng', '-vmb-de5', '-b1', '-s140', m.EndOfText ])   
    print(r)
    return()                
    
def speakAllText(text):    
    global ctlKey
    i= 0
    while i < len(text):
        r = call(['espeak-ng', c.voice, '-b1', '-s140', text[i]])   
        print(i) 
        i = i + 1  
        if ctlRun == "Stop":
            i = len(text)
            r = call(['espeak-ng', c.messageVoice, '-b1', '-s140', m.stopReading])   
            return()
    print(r)
    r = call(['espeak-ng', c.messageVoice, '-b1', '-s140', m.EndOfText ])   
    return(r)

def speakMessage(message):
    r = r = call(['espeak-ng', c.messageVoice, '-b1', '-s140', message ])
    return(r)    

#
## Ask for mode the text should speaked
#@Todo remove?
#
def askForMode():
    global ctlState, ctlRun
    
    ctlRun = "Stop"
    ctlKey = ""
    
    while ctlRun == "Stop":
        
        if ctlState == "Lines":
            speakMessage(m.askForModeLines)
        #    
        if ctlState == "All":
            speakMessage(m.askForModeAll)
        
        speakMessage(m.askForModeStart)
        wt = 0
        wt = wt + 1
        if ctlKey == "Start" or wt > c.waitTime:
                ctlRun = "Start"
        time.sleep(5)        
    return()
            
def askForRepeat():
    global ctlState, ctlRun
    
    ctlRun = "Stop"
    ctlRepeat = 2
    
    while ctlRepeat == 2:
        
        speakMessage(m.askForRepeat)
        speakMessage(m.askForNext)  
        #    
        time.sleep(10)
        if ctlState == "StartScan":
            ctlRepeat = 0
        if ctlRun == "Start":
            ctlRepeat = 1    
    
        print(ctlRepeat, ctlState)
        
              
    return(ctlRepeat)



# Setup Global Variables
running = 1
ctlKey = ""
ctlState = "All"
ctlRun = "" 
ctlScanned = ""
volume = 85
setVolume(volume)
speakMessage(m.greeting)
#


# Main funktion
def main():
    global ctlState, ctlRun, ctlScanned  
    while running:
        print(f"LOG: current time is {time.time()} --- {ctlKey}")
        ##
        ## Start and scan code 
        ##
        if ctlScanned == "":
            speakMessage(m.readyToScan)
        #
        while ctlScanned == "":
            print("21", ctlState) 
            if ctlState == "StartScan":
                speakMessage(m.waitPlease)
                r = call(['./scan2text.sh'])
                ctlScanned = "yes"     
            time.sleep(5)
        # 
        # 
        #askForMode()
        
        if ctlState == "StartScan":
            text = openFile()
            ctlRun = "Start" 
            speakAllText(text)
            ctlRun = "Stop"
            ctlState = ""
        
        # left key    
        if ctlState == "Lines":
            ctlRun = "Start"
            text = openFile()
            speakTextPerLine(text)
            ctlRun = "Stop"
            ctlState = ""
        
        if askForRepeat() == 0:
            ctlScanned = ""
            ctlState = "" 
        else:
            ctlScanned = "yes"
            ctlState = "StartScan"    
        #
        
        print(ctlState, ctlScanned)        
            
    #speakTextPerLine(text)
    time.sleep(5)
    


# Start  Threads and main
if __name__ == '__main__':
#
    Thread(name="keyreader", target=keylogger).start()
    main()
    
        
        