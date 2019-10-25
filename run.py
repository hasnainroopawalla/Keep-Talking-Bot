import numpy as np
import cv2
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
import bounding_box as bb
import ocr as ocr
import wire as wire
imgs=[]

# Manual Region select
##def grabimg():
##    im = np.array(ImageGrab.grab(bbox=(0, 40, 802, 635)))    #FULL
##    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
##    fromCenter = False
##    r = cv2.selectROI(im, fromCenter)                        
##    img = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
##    imgs.append(img)
##    rects=bb.gettext(img)
##    for i in rects:
##        x = i[0]
##        w = i[2]
##        y = i[1]
##        h = i[3]
##        roi = img[y-20:h+20, x-20:w+20]
##        roi = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
##        print(ocr.get_string(roi))
##        cv2.destroyAllWindows()


def staticgrabimg():
    im = np.array(ImageGrab.grab(bbox=(320, 240, 503, 420)))
    im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    wire.solve(im)
    
def on_press(key):
    if(key=='b'):
        print('ffff')
        
def on_release(key):
    if key==Key.enter:
        print('ok')
    elif key.char=='b':
        staticgrabimg()
    elif key.char=='p':
        print()
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



