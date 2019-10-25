import numpy as np

def release(color, text):
    strip = input('Strip Color: ')
    if(strip=='B'):
        print('Timer 4')
    elif(strip=='W'):
        print('Timer 1')
    elif(strip=='Y'):
        print('Timer 5')
    else:
        print('Timer 1')

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