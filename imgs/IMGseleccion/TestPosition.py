from tracemalloc import start
import cv2 as cv
import numpy as np
import pyautogui as au
from PIL import ImageGrab
import time
templateBolsa = cv.imread('imgSelec8.png',0)


method = cv.TM_CCOEFF_NORMED

clickedEnemi = False

threshold = 0.6

recoger1 = False;

def buscarFigura(template, imgGris):
        w, h = template.shape[::-1]
        res = cv.matchTemplate(template,imgGris,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        return res, max_loc, top_left, bottom_right, w, h

""" def countdown(num_of_secs):
    while num_of_secs:
        time.sleep(1)
        num_of_secs -= 1
        print(num_of_secs)
        
    print('Countdown finished.') """
    


while True:
    cap =  ImageGrab.grab(bbox=(0,0,600,600))
    cap_arr = np.array(cap)
    imgGRIS = cv.cvtColor(cap_arr, cv.COLOR_BGR2GRAY)


    """ CLickear enemigo """
    if clickedEnemi == False:
        objec = buscarFigura(templateBolsa, imgGRIS)
        print(np.amax(objec[0]))
        if np.amax(objec[0]) > threshold:
            cv.rectangle(imgGRIS,objec[2], objec[3], (0,0,255), 2)
            au.click((objec[2][0] + objec[4] )-18,(objec[2][1] + objec[5])-16)
            clickedEnemi = True
            # countdown(5)
            print("clickeado")

    cv.imshow("",imgGRIS)
    
 
    

    if cv.waitKey(1) == 27:
        cv.destroyAllWindows()
        break
