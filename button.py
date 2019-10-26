import speak as speak
import numpy as np
import pyttsx3
import time

engine = pyttsx3.init()

def release(color, text):
    
    print()
    strip = speak.gettext('Press and hold, what is the Strip Color?')
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
        print('\nPress and release immediately')
    
    elif(color=='W' and label=='car'):
        release(color, label)
    
    elif(batteries>2 and label=='frk'):
        print('\nPress and release immediately')
    
    elif(color=='Y'):
        release(color, text)

    elif(color=='R' and text=='hold'):
        print('\nPress and release immediately')
    
    else:
        release(color, text)
                
    
def getscene():

    #Speech to Text here
    color_map = {'blue':'B','red':'R','yellow':'Y','black':'BL','white':'W','nothing':'E'}

    color = speak.gettext('Button Color?')
    text = speak.gettext('Button Text?')
    color = color_map[color]   
    return color, text


def solve(batteries, serial, label):
    color, text = getscene()
    examine(color, text, batteries, serial, label)