import numpy as np
import cv2
import bounding_box as bb
import ocr as ocr

serial='7H5ZW1'
def examine(wires):
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
        print('1')
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
            print('sdsd')
            for i in range(0,6):    
                if(wires[i]!='E'):
                    cut=i+1
                    break
                
    print('cut: wire',cut)
                
    
def getwirecolors(img):
    w1 = img[30,45]
    w2 = img[53,46]
    w3 = img[74,46]
    w4 = img[96,46]
    w5 = img[118,46]
    w6 = img[141,46]
    w1[0],w1[2]=w1[2],w1[0]
    w2[0],w2[2]=w2[2],w2[0]
    w3[0],w3[2]=w3[2],w3[0]
    w4[0],w4[2]=w4[2],w4[0]
    w5[0],w5[2]=w5[2],w5[0]
    w6[0],w6[2]=w6[2],w6[0]
    w=[]
    w.append(w1)
    w.append(w2)
    w.append(w3)
    w.append(w4)
    w.append(w5)
    w.append(w6)
    print(w1,w2,w3,w4,w5,w6)

    a=img.copy()
    a[30,45] = (0,255,0)
    a[53,46] = (0,255,0)
    a[74,46] = (0,255,0)
    a[96,46] = (0,255,0)
    a[118,46] = (0,255,0)
    a[141,46] = (0,255,0)
    
    cv2.imshow('a',a)
    cv2.waitKey(0)
    wires=[]
    white_start = (168, 163, 163)
    white_end = (255, 255, 255)
    blue_start = (41, 65, 204)
    blue_end = ( 55  ,78 ,207)
    yellow_start = (255, 236, 5)
    yellow_end = (255, 255, 61)
    black_start = (0, 0, 0)
    black_end = (61, 61, 61)
    red_start = (255, 0, 0)
    red_end = (255, 113, 61)

    for i in w:
        if all(s <= c <= e for c, s, e in zip(i, white_start, white_end)):
            wires.append('W')
        elif all(s <= c <= e for c, s, e in zip(i, blue_start, blue_end)):
            wires.append('B')
        elif all(s <= c <= e for c, s, e in zip(i, yellow_start, yellow_end)):
            wires.append('Y')
        elif all(s <= c <= e for c, s, e in zip(i, red_start, red_end)):
            wires.append('R')
        elif i[0]>=22 and i[0]<=39 and i[1]>=22 and i[1]<=39 and i[2]>=22 and i[2]<=39:
            wires.append('E')
        elif all(s <= c <= e for c, s, e in zip(i, black_start, black_end)):
            wires.append('BL')
        else:
            wires.append('B')
        
##    print(wires)
    examine(wires)


def solve(img):
    getwirecolors(img)
