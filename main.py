from re import L
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

# Change to discord tab u want to use.
wincap = WindowCapture('#incense・3 | Pokémon HQ - Discord')

loop_time = time()
while(True):
    
    # get an updated image of the screen
    screenshot = wincap.get_screenshot()
    
    cv.imshow('Discord Bot', screenshot)
    
    # debug to loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    
    # pres 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    
print('Done.')