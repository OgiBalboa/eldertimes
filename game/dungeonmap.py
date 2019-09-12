# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:35:18 2019

@author: fener_000
"""

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
game.title("ELDER TIMES - BAŞLANGIÇ")
game.minsize(1210,681)
dungeon = resim("pics/dungeonmap.jpg")
arup = resim("pics/mapicons/up.png")
arleft = resim("pics/mapicons/left.png")
arright = resim("pics/mapicons/right.png")
ardown = resim("pics/mapicons/down.png")
import bin.avatars
from bin.movement import hareketlvl1
#----------------------------------------İLERLEME KODLARI-----------------------------------------------------------
def reload():
    Label(game, image = dungeon.render).place(x=200,y=0)


#----------------------------------------PANEL FONKSİYONLAR-----------------------------------------------------------
#------------------------------------------OYUNCU 1-----------------------------------------------------------------
p1 = hareketlvl1()
def kordinat():
    while 1:
        cor = str(p1.dimx) + " " + str(p1.dimy)
        Label(game,text = cor ).place(x = 700,y = 0)
        time.sleep(1)
        
def p1ileri():
    p1.ileri()
    reload()
    yerlestir()
    
def p1geri():
    p1.geri() 
    yerlestir()
    
def p1yukari():
    p1.yukari()
    yerlestir()
    
def p1asagi():
    p1.asagi()
    yerlestir()
#------------------------------------------OYUNCU 2--------------------------------------------------------------
p2 = hareketlvl1()
def p2ileri():
    p2.ileri()
    reload()
    yerlestir()
    
def p2geri():
    p2.geri() 
    yerlestir()
    
def p2yukari():
    p2.yukari()
    yerlestir()
    
def p2asagi():
    p2.asagi()
    yerlestir()
#------------------------------------------OYUNCU 3-------------------------------------------------------------- 
p3 = hareketlvl1()
def p3ileri():
    p3.ileri()
    yerlestir()
    
def p3geri():
    p3.geri() 
    yerlestir()
    
def p3yukari():
    p3.yukari()
    yerlestir()
    
def p3asagi():
    p3.asagi() 
    yerlestir()
 
def zar():
    sayi = random.randint(1,6)
    Label(game,text =str(sayi),font=("Arial",16),bg = "black",fg="yellow").place(x = 230, y = 550)
def nextlevel():
    #game.destroy()
    #os.system("python maplevel5.py")
    pass
   
#----------------------------------------PANEL-----------------------------------------------------------     
Label(game, image = dungeon.render).place(x=200,y=0)

Label(game,text="OYUNCU 1",font=("Arial",16),bg = "black",fg="yellow").place(x = 0, y = 490)
Button(game,image= arup.render,command = p1yukari).place(x = 40, y = 520)
Button(game,image= arleft.render,command = p1geri).place(x = 10, y = 540)
Button(game,image= arright.render,command = p1ileri).place(x = 70, y = 540)
Button(game,image= ardown.render,command = p1asagi).place(x = 40, y = 560)

Label(game,text="OYUNCU 2",font=("Arial",16),bg = "black",fg="yellow").place(x = 140, y = 490)
Button(game,image= arup.render,command = p2yukari).place(x = 180, y = 520)
Button(game,image= arleft.render,command = p2geri).place(x = 150, y = 540)
Button(game,image= arright.render,command = p2ileri).place(x = 210, y = 540)
Button(game,image= ardown.render,command = p2asagi).place(x = 180, y = 560)

Label(game,text="OYUNCU 3",font=("Arial",16),bg = "black",fg="yellow").place(x = 280, y = 490)
Button(game,image= arup.render,command = p3yukari).place(x = 320, y = 520)
Button(game,image= arleft.render,command = p3geri).place(x = 290, y = 540)
Button(game,image= arright.render,command = p3ileri).place(x = 350, y = 540)
Button(game,image= ardown.render,command = p3asagi).place(x = 320, y = 560)

#------------------------------------------OYUN KARELERİ ------------------------------------------------
dal = Thread(target = kordinat)
dal.start()

def yerlestir():
    reload()
    Label(game,text ="P1",font=("Arial",12),bg = "blue",fg="yellow").place(x=p1.dimx, y = p1.dimy)
    Label(game,text ="P2",font=("Arial",12),bg = "red",fg="yellow").place(x=p2.dimx+20, y = p2.dimy)
    Label(game,text ="P3",font=("Arial",12),bg = "green",fg="yellow").place(x=p3.dimx+40, y = p3.dimy)
yerlestir() 

#Button(game,text="Oyuncu 2 İlerle",command = go2,font=("Arial",16),bg = "black",fg="yellow").place(x = 0, y = 600)
Button(game,text="Zar At",command = zar,font=("Arial",16),bg = "black",fg="yellow").place(x = 600, y = 500)
Button(game,text="LEVEL 5",command = nextlevel,font=("Arial",16),bg = "black",fg="yellow").place(x = 800, y = 500)
game.mainloop()
