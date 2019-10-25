import numpy as np
import wire as wire
import button as button
imgs=[]

def bombconfig():
    batteries = int(input('Batteries: '))
    serial = input('Serial No.: ')
    label = input('Label: ')
    return batteries, serial, label

batteries, serial, label = bombconfig()

while(True):
    
    print('\n\n1- Wires')
    print('2- Button')
    print('0- Exit')
    ch = int(input('Choose module: '))
    print()
    if(ch==1):
        wire.solve(batteries, serial)
    elif(ch==2):
        button.solve(batteries, serial, label)
    elif(ch==0):
        break
        


