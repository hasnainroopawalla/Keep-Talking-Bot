import numpy as np

def examine(wires, batteries, serial):
    cut=0
    print(wires)
    numwires=6-wires.count('E')
    if(numwires==3):
        for i in range(5,-1,-1):
            if(wires[i]!='E' and wires[i]=='BL'):
                cut=i+1
                break
            
        if(wires.count('R')==0):
            cut=2
 
        elif(wires.count('B')>1):
            for i in range(5,-1,-1):
                if(wires[i]=='B'):
                    cut=i+1
                    break
        else:
            # Cut last wire
            print('efs')
            for i in range(5,-1,-1):
                print(wires[i])
                if(wires[i]!='E'):
                    
                    cut=i+1
                    break
                    
    elif(numwires==4):
        if(wires.count('R')>1 and int(serial[-1])%2!=0):

            for i in range(5,-1,-1):
                if(wires[i]=='R'):
                    cut=i+1
                    break
        elif(wires[5]=='Y' and wires.count('R')==0):  # Cut first wire
            for i in range(0,6):    
                if(wires[i]!='E'):
                    cut=i+1
                    break
        elif(wires.count('B')==1):
            for i in range(0,6):
                if(wires[i]!='E'):
                    cut=i+1
                    break
        elif(wires.count('Y')>1):
            for i in range(0,6):    
                if(wires[i]!='E'):
                    cut=i+1
                    break
        else:
            f = 0
            for i in range(0,6):
                if(wires[i]!='E'):
                    if(f==1):
                        cut=i+1
                        break
                    else:
                        f=1
                        
    elif(numwires==5):
        for i in range(5,-1,-1):
            if(wires[i]!='E' and wires[i]=='BL' and int(serial[-1])%2!=0):      # Cut fourth wire
                f = 0
                for i in range(0,6):
                    if(wires[i]!='E'):
                        if(f==3):
                            cut=i+1
                            break
                        else:
                            f+=1
                            
        if(wires.count('R')==1 and wires.count('Y')>1):
            print('2')
            for i in range(0,6):    
                if(wires[i]!='E'):
                    cut=i+1
                    break
        elif(wires.count('BL')==0):      # Cut second wire
            f = 0
            print('3')
            for i in range(0,6):
                if(wires[i]!='E'):
                    if(f==1):     
                        cut=i+1
                        break
                    else:
                        f+=1
        else:
            for i in range(0,6):    
                if(wires[i]!='E'):
                    cut=i+1
                    break

    elif(numwires==6):     
        if(wires.count('Y')==0 and int(serial[-1])%2!=0):      # Cut third wire
            f = 0
            for i in range(0,6):
                if(wires[i]!='E'):
                    if(f==2):     
                        cut=i+1
                        break
                    else:
                        f+=1

        elif(wires.count('Y')==1 and wires.count('W')>1):
            f = 0
            for i in range(0,6):
                if(wires[i]!='E'):
                    if(f==3):
                        cut=i+1
                        break
                    else:
                        f+=1          
        
        elif(wires.count('R')==0):
            for i in range(5,-1,-1):    
                if(wires[i]!='E'):
                    cut=i+1
                    break
        
        else:
            f = 0
            for i in range(0,6):
                if(wires[i]!='E'):
                    if(f==3):
                        cut=i+1
                        break
                    else:
                        f+=1

    print('cut: wire at position',cut)
                
    
def getwirecolors():
    wires = []

    #Speech to Text here

    wires.append(input('Wire 1:'))
    wires.append(input('Wire 2:'))
    wires.append(input('Wire 3:'))
    wires.append(input('Wire 4:'))
    wires.append(input('Wire 5:'))
    wires.append(input('Wire 6:'))
    return wires


def solve(batteries, serial):
    wires = getwirecolors()
    examine(wires, batteries, serial)