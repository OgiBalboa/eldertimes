# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:10:15 2019

@author: ogibalboa
"""
import tkinter
from tkinter import *
from PIL import Image,ImageTk
from ui.resim import resim
import pygame
import os
import time

Mainmenu = Tk()
Mainmenu.title("ELDER TIMES")
Mainmenu.geometry("1366x681")
Mainmenu.maxsize(1210,681)
Mainmenu.minsize(1210,681)
# FONKSİYONLAR

def newgame():
    os.chdir('bin')
    Mainmenu.destroy()
    os.system('python newgame.py')    
def cikis():
    Mainmenu.destroy()
def seskapa():
    pygame.mixer.music.stop()

emblem = resim("pics/mainmenu.png",)
Label(Mainmenu,image=emblem.render).place(x=0,y=0)
Label(Mainmenu,text = "ogibalboa was here").place(x=10,y=1000)
#Label(Mainmenu, text = " HOZEVREK", font=("Arial",36), bg ="black",fg = "yellow").place(x=0,y=0)
newgm = Button(Mainmenu, text = "YENİ OYUN", command = newgame,font=("Arial",18),bg ="black",fg = "yellow").place(x=1050,y=490)
mute = resim("pics/mute.jpg")
ext= Button(Mainmenu,text=" ÇIKIŞ", command = cikis,font=("Arial",18),bg ="black",fg = "yellow").place(x=1050,y=540)
Button(Mainmenu,image = mute.render, command = seskapa).place(x=1150,y=0)


pygame.init()

pygame.mixer.music.load("sounds/mainmenu.mp3")

pygame.mixer.music.play()

#time.sleep(10)
Mainmenu.mainloop()
