import numpy as np
import speak as speak
import pyttsx3

engine = pyttsx3.init()

def examine(color, serial):
    if(color=='blue'):
        return 'red'
    elif(color=='yellow'):
        return 'green'
    elif(color=='red'):
        return 'blue'
    elif(color=='green'):
        return 'yellow'

    
    
    
def getscene(serial):
    ans = []

    ans.append(examine(speak.gettext('1st Color?',4), serial))
    print(ans)
    for i in ans:
        engine.say(i) 
        engine.runAndWait()

    ans.append(examine(speak.gettext('2nd Color?',4), serial))
    print(ans)
    for i in ans:
        engine.say(i) 
        engine.runAndWait()

    ans.append(examine(speak.gettext('3rd Color?',4), serial))
    print(ans)
    for i in ans:
        engine.say(i) 
        engine.runAndWait()

    ans.append(examine(speak.gettext('4th Color?',4), serial))
    print(ans)
    for i in ans:
        engine.say(i) 
        engine.runAndWait()

    
def solve(serial):
    getscene(serial)
