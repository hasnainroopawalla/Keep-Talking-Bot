import numpy as np
import wire as wire
imgs=[]


def staticgrabimg():
    # im = np.array(ImageGrab.grab(bbox=(320, 240, 503, 420)))
    # im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    wire.solve()
    
# def on_press(key):
#     if(key=='b'):
#         print('ffff')
        
# def on_release(key):
#     if key==Key.enter:
#         print('ok')
#         staticgrabimg()
#     elif key.char=='p':
#         print()
#     if key == Key.esc:
#         return False

# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
staticgrabimg()


