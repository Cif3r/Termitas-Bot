
from asyncio import sleep
from select import select
from sqlite3 import Time
from turtle import delay
import cv2 as cv
import numpy as np
import pyautogui as au
from PIL import ImageGrab
import time
import keyboard

#Metodo de deteccion
method = cv.TM_CCOEFF_NORMED

#Variables globales control de flujo e inicializ221133|acion.
enemySelect = False
attack = False
limiteAtaques = 0
limiteIntentosRecogida = 0

TemplateEnemy = [  './imgs/IMGseleccion/imgSelec1.png', './imgs/IMGseleccion/imgSelec2.png',
                    './imgs/IMGseleccion/imgSelec3.png', './imgs/IMGseleccion/imgSelec4.png', 
                    './imgs/IMGseleccion/imgSelec5.png', './imgs/IMGseleccion/imgSelec6.png', 
                    './imgs/IMGseleccion/imgSelec7.png', './imgs/IMGseleccion/imgSelec8.png',]


TemplateRecoger = [  './imgs/IMGRecoger/CaidaA.png', './imgs/IMGRecoger/CaidaB.png',
                     './imgs/IMGRecoger/CaidaC.png', './imgs/IMGRecoger/CaidaD.png',
                     './imgs/IMGRecoger/CaidaA1.png','./imgs/IMGRecoger/CaidaB1.png', 
                     './imgs/IMGRecoger/CaidaC1.png', './imgs/IMGRecoger/CaidaD1.png']

TemplateFaro = './imgs/IMGControl/Faro.png'

SenseNPC = 0.86
SeseRecoger = 0.8
lastPoint = -1
recogido = False

def DetectEnemy():
    global enemySelect
    global limiteIntentosRecogida

    while enemySelect != True:
        for n in range(len(TemplateEnemy)):
                    cap_arr = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
                    imgGris = cv.cvtColor(cap_arr, cv.COLOR_BGR2GRAY)

                    template = cv.imread(TemplateEnemy[n],0)
                    w, h =  template.shape[::-1]
                    res = cv.matchTemplate(template,imgGris,method)
                    min_val, max_val, min_loc,max_loc = cv.minMaxLoc(res)
                    top_left = max_loc
                    if np.amax(res) > SenseNPC:
                        au.click((top_left[0] + w )-18,(top_left[1] + h)-16)
                        enemySelect = True
                        print("NPC Seleccionado")
                        limiteIntentosRecogida = 0;


                        cap_arr = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
                        imgGris = cv.cvtColor(cap_arr, cv.COLOR_BGR2GRAY)
                        template = cv.imread(TemplateFaro,0)
                        w, h =  template.shape[::-1]
                        res2 = cv.matchTemplate(template,imgGris,method)
                        min_val, max_val, min_loc,max_loc = cv.minMaxLoc(res2)
                        top_left = max_loc
                        if np.amax(res2) > 0.83:
                            print("Desbloqueando mira")
                            au.click((top_left[0] + w )-38,(top_left[1] + h)-90)
                        break
                    cap_arr = 0

def collect():
    global lastPoint
    global recogido 
    global limiteAtaques
    global limiteIntentosRecogida 
    for n in range(len(TemplateRecoger)):
        ca = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
        imgGris = cv.cvtColor(ca, cv.COLOR_BGR2GRAY)

        template = cv.imread(TemplateRecoger[n],0)
        w, h =  template.shape[::-1]
        rec = cv.matchTemplate(template,imgGris,method)
        min_val, max_val, min_loc,max_loc = cv.minMaxLoc(rec)
        top_left = max_loc

        limiteIntentosRecogida += 1
        if limiteIntentosRecogida >= 360:
            print("Tiempo Cumplido")
            reinciar()
            break

        if np.amax(rec) > SeseRecoger:
            limiteAtaques = 0
            if n == 0 and lastPoint != 0: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-18,(top_left[1] + h)-15)
                time.sleep(2)
                reinciar()
                break
            if n == 1 and lastPoint != 1: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-10,(top_left[1] + h)-30)
                time.sleep(2)
                reinciar()
                break
            if n == 2 and lastPoint != 2: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-50,(top_left[1] + h)-10)
                time.sleep(2)
                reinciar()
                break  
            if n == 3 and lastPoint != 3: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-20,(top_left[1] + h)-10)
                time.sleep(2)
                reinciar()
                break
            if n == 4 and lastPoint != 4: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-20,(top_left[1] + h)-10)
                time.sleep(2)
                reinciar()
                break
            if n == 5 and lastPoint != 5: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-10,(top_left[1] + h)-16)
                time.sleep(2)
                reinciar()
                break
            if n == 6 and lastPoint != 6: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-50,(top_left[1] + h)-10)
                time.sleep(2)
                reinciar()
                break
                
            if n == 7 and lastPoint != 7: 
                recogido = True
                lastPoint = n 
                time.sleep(1.4)
                au.click((top_left[0] + w )-10,(top_left[1] + h)-10)
                time.sleep(2)
                reinciar()
                break
            break

    

def AttackEnemy():
    global recogido
    global limiteAtaques
   #https://pythonbros.com/controlar-el-teclado-con-python/
    if recogido == False:
        if limiteAtaques <= 36:
            keyboard.send("4")
            keyboard.send("4")

            keyboard.send("1")
            keyboard.send("1")

            keyboard.send("3")
            keyboard.send("3")

            keyboard.send("2")
            keyboard.send("2")

            keyboard.send("5")
            keyboard.send("5")
            limiteAtaques += 1

        #Lo repito para que no quede 123seleccionada la habilidad y no pueda recoger el botin

    #intento recoger

def reinciar():
    global enemySelect
    global recogido
    keyboard.send("enter")
    print("Punto de inicio")
    enemySelect = False
    recogido = False
    time.sleep(1)
    cza = np.array(ImageGrab.grab(bbox=(0,0,600,600)))
    imgGris = cv.cvtColor(cza, cv.COLOR_BGR2GRAY)

    template = cv.imread(TemplateFaro,0)
    w, h =  template.shape[::-1]
    rec = cv.matchTemplate(template,imgGris,method)
    min_val, max_val, min_loc,max_loc = cv.minMaxLoc(rec)
    top_left = max_loc

    if np.amax(rec) > 0.80:
        print("Faro encontrado")
        au.click((top_left[0] + w )-16,(top_left[1] + h)-150)
        keyboard.send("enter")

    time.sleep(3)


while True:
    DetectEnemy()
    AttackEnemy()
    collect()
    if cv.waitKey(1) == 27:
       cv.destroyAllWindows()
       break
