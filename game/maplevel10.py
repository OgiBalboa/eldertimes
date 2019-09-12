# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:18:08 2019

@author: fener_000
"""

#-------------------------------LEVEL 10 MAP -------------------------------
import tkinter
from tkinter import *
from PIL import Image,ImageTk
from ui.resim import resim
import threading
from threading import Thread
import time
import os
import bin.playerstats
import random

game = Tk()
game.title("ELDER TIMES - LEVEL 10")
game.minsize(1366,1000)
maplevel10 = resim("pics/maplevel10.jpg")
import bin.avatars
def reload():
    Label(game, image = maplevel10.render).place(x=0,y=0)
    
class hareket():
    def __init__(self,avno):
        self.avno = avno
        self.dimx = 10
        self.dimy = 10
    def ileri():
        pass
    def yerles(self,):
        reload()
        Label(game,text =str(self.avno),font=("Arial",16),bg = "black",fg="yellow").place(x=self.dimx, y = self.dimy)        
     
oyuncu1 = hareket("X") 
oyuncu1.yerles()

oyuncu2 = hareket("O")
oyuncu2.yerles()

def go():
    oyuncu1.ileri(1)
def go2():
    oyuncu2.ileri(1)    
def zar():
    sayi = random.randint(1,6)
    Label(game,text =str(sayi),font=("Arial",16),bg = "black",fg="yellow").place(x = 230, y = 550)
    
Label(game, image = maplevel10.render).place(x=0,y=0)
Button(game,text="Oyuncu 1 İlerle",command = go,font=("Arial",16),bg = "black",fg="yellow").place(x = 0, y = 500)
#Button(game,image=goblin.render,command = goblin).place(x = 20, y = 20)

Button(game,text="Oyuncu 2 İlerle",command = go2,font=("Arial",16),bg = "black",fg="yellow").place(x = 0, y = 600)
Button(game,text="Zar At",command = zar,font=("Arial",16),bg = "black",fg="yellow").place(x = 200, y = 500)
game.mainloop()