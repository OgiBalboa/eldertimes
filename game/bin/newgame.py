# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 01:00:11 2019

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

start = Tk()
start.title("ELDER TIMES     CHARACTER SCREEN")
start.geometry("1366x681")
start.maxsize(1210,681)
start.minsize(1210,681)
# GLOBALLER
global count
count = 0 
# FONKSİYONLAR
import avatars
try :
    bg = resim("pics/start.jpg")
    ltarrow = resim("pics/leftarrow.png")
    rtarrow = resim("pics/rightarrow.png")
    mainstats = resim("pics/mainstats.jpg")
    plus = resim("pics/plus.jpg")
except : 
    bg = resim("bin/pics/start.jpg")
    ltarrow = resim("bin/pics/leftarrow.png")
    rtarrow = resim("bin/pics/rightarrow.png")
    plus = resim("bin/pics/plus.jpg")
    


def reload():
    re = Label(start, image = bg.render).place(x=0,y=0) #BACKGROUND REFRESH
    
def check():     #DENETLEYİCİ
    global count
    global oyuncu_sayisi
    global flag
    global player_list
    flag = False
    while 1:

        if count == oyuncu_sayisi:
            status = True
            reload()
            break
        time.sleep(1)
import playerstats
players = [] 
def onay():
    global count
    players[count-1].avatarno(avno)
    entername()
def newplayer(): 
    reload()
    #denetle = Thread(target = check)
    #denetle.start()
    global avno
    global count
    def getentry():
        if count ==1 : 
            os.chdir("save")
            os.mkdir(str(players[0].name))
            os.chdir(str(players[0].name))
            save1 = open("info.py","w+")
            info1 = """
class player():
   def __init__(self):
                        """
            save1.write(info1)
            info = "\n    self.name = " + " \'" + str(players[0].name) + "\'" + " \n    self.ATK = 1\n    self.DEF = 15 \n    self.CRIT = 10"
            save1.write(info)
            os.chdir("..")
    avno = 0
    txt1= "Hoş Geldin " + str(players[count-1].name) + " , Maceraya hazırsan tanıt kendini !"
    Label(start, text = txt1 ,font=("Algerian",15), bg = "black",fg="yellow").place(x=350,y=10) # WILKOMMEN    
    atkentry = Entry(start,width = "5")
    atkentry.place(x = 300, y = 50)    
    Label (start,text = "ATK    DEF    CRIT " ).place ( x= 295, y = 10)
    defentry = Entry(start,width = "5")
    defentry.place(x = 300, y = 50)  
    critentry = Entry(start,width = "5")
    critentry.place(x = 300, y = 50) 
    Button(start,text = "OK",command = getentry, font = ("Algerian",12)).place(x = 320, y = 80)
    def left():
        global avno
        avno-=1
        if avno<0:
            avno = avatars.boyut
            avno-=1
        Label(start,image = avatars.avat[avno].render).place(x = 40, y =200)
        
    def right():
        global avno
        avno+=1
        
        if avno == avatars.boyut:
            avno = 0
        Label(start,image = avatars.avat[avno].render).place(x = 40, y =200)
    def powerup():
         players[count-1].powerup()
         Label(start,text=str(players[count-1].powerstat),font=("Arial",12) , bg = "brown",fg="black").place(x = 100, y = 420)
         Label(start,text="Kalan özellik puanları : " + str(players[count-1].statp),font=("Arial",12),  bg = "brown",fg="white").place(x = 10, y = 520)
    def agiup():
         players[count-1].agiup()
         Label(start,text=str(players[count-1].agistat),font=("Arial",12), bg = "brown",fg="black").place(x = 100, y = 455)
         Label(start,text="Kalan özellik puanları : " + str(players[count-1].statp),font=("Arial",12),  bg = "brown",fg="white").place(x = 10, y = 520)
    def intup():
         players[count-1].intup()
         Label(start,text=str(players[count-1].intstat),font=("Arial",12),  bg = "brown",fg="black").place(x = 100, y = 487)
         Label(start,text="Kalan özellik puanları : " + str(players[count-1].statp),font=("Arial",12),  bg = "brown",fg="white").place(x = 10, y = 520)
    #----------------------------------AVATAR-------------------------------------------------------------    
    LEFT = Button(start,image = ltarrow.render,command = left).place(x= 10, y = 200)
    Label(start,text="Avatar Seç",font=("Arial",12), bg = "black",fg="yellow").place(x=100,y = 160)
    Label(start,image = avatars.avat[avno].render).place(x = 40, y =200)
    RIGHT = Button(start,image = rtarrow.render,command = right).place(x= 255, y = 200)
    #----------------------------------MAIN STATS-------------------------------------------------------------   
    #Label(start,text="ANA ÖZELLİKLER",font=("Arial",12), bg = "black",fg="yellow").place(x=10,y = 380)
    #Label(start,text = " GÜÇ",font=("Arial",12), bg = "yellow",fg="black").place(x=10,y = 410)
    Label(start,image = mainstats.render,highlightcolor="black",highlightthickness = 0 ).place(x=10, y = 380)
    #-----------------------------------------------------STAT UP DOWN----------------------------------------------------------------
    Button(start,image = plus.render,command= powerup,highlightbackground="black",highlightthickness = 0).place(x = 175, y = 420)
    Label(start,text=str(players[count-1].powerstat),font=("Arial",12) , bg = "brown",fg="black").place(x = 100, y = 420)
    Button(start,image = plus.render,command = agiup,highlightthickness = 0).place(x = 175, y = 455)
    Label(start,text=str(players[count-1].agistat),font=("Arial",12),  bg = "brown",fg="black").place(x = 100, y = 455)
    Button(start,image = plus.render,command = intup,highlightthickness = 0).place(x = 175, y = 487)
    Label(start,text=str(players[count-1].intstat),font=("Arial",12),  bg = "brown",fg="black").place(x = 100, y = 487)
    Label(start,text="Kalan özellik puanları : " + str(players[count-1].statp),font=("Arial",12),  bg = "brown",fg="white").place(x = 10, y = 520)
    


    Button(start, text = "TAMAM",command = onay,font=("Arial",16), bg = "black",fg="yellow",highlightbackground="white",highlightthickness = 0 ).place(x=400,y=500) #ONAY
def listall():
    def goo():   
            os.chdir("..")        
            start.destroy()
            os.system("python rungame.py")
    reload()
    z=0
    Label(start,text="MACERACILAR",font=("Arial",16),bg = "black",fg="yellow").place(x = 500, y = 100)
    for i in range (0,count,1): 
        if z < 2:
            Label(start,text=str(players[i].name),font=("Arial",16),bg = "black",fg="yellow").place(x = 100, y = 200 + z*215)
            Label(start, image =avatars.avat[players[i].avno].render).place(x = 100, y = 250 + z*200)
            z+=1
        elif z>=2:
            Label(start,text=str(players[i].name),font=("Arial",16),bg = "black",fg="yellow").place(x = 400, y = 200 + (z-2)*215)
            Label(start, image =avatars.avat[players[i].avno].render).place(x = 400, y = 250 + (z-2)*200)
            z+=1
    Button(start,text="İLERLE",command = goo,font = ("Arial",16),bg = "black", fg = "yellow").place(x = 300, y = 600)
def entername():
  reload()
  global players
  global count
  pcount = int(pcout.get())
  if count == pcount:
        listall()
  else:
    #----------------------------------OYUNCU ADI----------------------------------------------------------    
    txt = "Hey Savaşçı ! Adın nedir ?"
    Label(start, text = txt ,font=("Arial",36), bg = "black",fg="yellow").place(x=300,y=10) #OYUNCU NO
    pname = Entry(start,width = 12)
    pname.place(x = 500, y = 105)
    def nameselect():
        global playername 
        playername = str(pname.get())
        continuee()
    def continuee():
        global count
        players.append(playername)
        players[count] = playerstats.newplayerstat(playername,5,5,5)
        count +=1
        newplayer()
    playerno = str(pcout.get()) 
    Button(start, text = "ONAY",command = nameselect,font=("Arial",16), bg = "black",fg="yellow").place(x = 500, y = 140)
    

reload()
Label(start,text = " Kac Kisi oynayi ?",font=("Arial",36), bg = "black",fg="yellow").place(x=350,y=10)
pcout= Entry(start,width = 12)
pcout.place(x=480,y=90) 
Button(start,text = "Onayla",command = entername,font=("Arial",22), bg = "black",fg = "yellow").place(x=460,y=122)

start.mainloop()