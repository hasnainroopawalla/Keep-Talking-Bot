import numpy as np
import wire as wire
imgs=[]

def bombconfig():
    batteries = input('Batteries: ')
    serial = input('Serial No.: ')
    return batteries, serial

def staticgrabimg():
    wire.solve()

batteries, serial = bombconfig()

while(True):
    
    print('\n\n1- Wires')
    print('2- Button')
    print('0- Exit')
    ch = int(input('Choose module: '))
    print()
    if(ch==1):
        wire.solve(batteries,serial)
    elif(ch==2):
        print('2')
        #button.solve()
    elif(ch==0):
        break
        


