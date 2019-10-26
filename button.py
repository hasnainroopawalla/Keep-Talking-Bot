import listen as listen
import numpy as np
import pyttsx3
import time

engine = pyttsx3.init()

def release(color, text):
    time.sleep(5)
    strip = listen.gettext()
    if(strip=='blue'):
        timer = '4'
    elif(strip=='white'):
        timer = '1'
    elif(strip=='yellow'):
        timer = '5'
    else:
        timer = '1'
    engine.say(timer) 
    engine.runAndWait() 

def examine(color, text, batteries, serial, label):
    
    if (color=='B' and text=='abort'):
        release(color, text)

    elif(batteries>1 and text=='detonate'):
        print('Press and release immediately')
    
    elif(color=='W' and label=='car'):
        release(color, label)
    
    elif(batteries>2 and label=='frk'):
        print('Press and release immediately')
    
    elif(color=='Y'):
        release(color, text)

    elif(color=='R' and text=='hold'):
        print('Press and release immediately')
    
    else:
        release(color, text)
                
    
def getscene():

    #Speech to Text here

    color = input('Button Color: ')
    text = input('Button Text: ')   
    return color, text


def solve(batteries, serial, label):
    color, text = getscene()
    examine(color, text, batteries, serial, label)