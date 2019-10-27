import numpy as np
import speak as speak
import pyttsx3

engine = pyttsx3.init()

def examine(wires, batteries, serial):
    cut=0
    print(wires)
    numwires=6-wires.count('E')
    if(numwires==3):
        for i in range(5,-1,-1):
            if(wires[i]!='E' and wires[i]=='BL'):
                cut=i+1
                break
            
        if(wires.count('R')==0):   # Cut second wire
            f = 0
            for i in range(0,6):
                if(wires[i]!='E'):
                    if(f==1):     
                        cut=i+1
                        break
                    else:
                        f+=1
 
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

    engine.say('Cut wire at position '+str(cut)) 
    engine.runAndWait() 
    
                
    
def getscene():
    wires = []
    color_map = {'blue':'B','red':'R','yellow':'Y','black':'BL','white':'W','nothing':'E'}

    print()
    w1 = speak.gettext('Wire 1?', 1)
    print()
    w2 = speak.gettext('Wire 2?', 1)
    print()
    w3 = speak.gettext('Wire 3?', 1)
    print()
    w4 = speak.gettext('Wire 4?', 1)
    print()
    w5 = speak.gettext('Wire 5?', 1)
    print()
    w6 = speak.gettext('Wire 6?', 1)

    wires.append(color_map[w1])
    wires.append(color_map[w2])
    wires.append(color_map[w3])
    wires.append(color_map[w4])
    wires.append(color_map[w5])
    wires.append(color_map[w6])
    return wires


def solve(batteries, serial):
    wires = getscene()
    examine(wires, batteries, serial)