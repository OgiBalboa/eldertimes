# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:54:52 2019

@author: fener_000
"""

import tkinter
from tkinter import *
from tkinter import Label
#from tkinter import TopLevel
from PIL import Image,ImageTk
from ui.resim import resim
import threading
import time
import random
import os
print("resim yükleniyor")

print("yüklendi")   

       
class monstercard():
    def __init__(self,name,ATK,DEF,picture,pname,patk,pdef,pcrit,ppic,exp,gold):
        self.name = name
        self.ATK = ATK
        self.DEF = DEF
        self.EXP = exp
        self.GOLD = gold
        self.card = tkinter.Toplevel()
        self.card.title(self.name)
        self.card.geometry("1000x700")
        from bin.avatars import avat
        self.pic = resim(picture)
        self.PNAME = pname
        self.PATK = patk
        self.PDEF = pdef
        self.PCRIT = pcrit
        self.ppic = avat[ppic]
        self.vs = resim("pics/mapicons/vs.png")
        self.backgr = resim("pics/start.jpg")
        
        Label(self.card,image = self.backgr.render).place(x = 0,y = 0)
        Label(self.card,text =self.name, font=("Algerian",16)).place(x= 10,y = 10)
        Label(self.card,image = self.pic.render).place(x = 10,y = 50)
        Label(self.card,text =str(self.PNAME), font=("Algerian",16)).place(x= 800,y = 10)
        Label(self.card,image = self.ppic.render).place(x = 740, y = 50)
        Label(self.card,image = self.vs.render).place(x = 400, y = 100)                             
        Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(DEF), font=("Algerian",16)).place(x= 10,y = 230)
        Label(self.card,text ="ATK  :" + str(self.PATK), font=("Algerian",16)).place(x= 680,y = 230)    
        Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
        Label(self.card,text ="KRİTİK :" + str(self.PCRIT), font=("Algerian",16)).place(x= 880,y = 230)
        Button(self.card,text = "FIGHT ! ",command = self.startzar).place(x = 400, y = 170)
        
        self.card.mainloop()
                
    def getplayer(self,patk,pdef,pcrit):
        pass
        #Label(self.card,image = self.pic.render).place(x = 0,y = 0)        
        #Button(self.card,text = "Basalayani belirlemek icin zar at !",command = self.startzar,font=("Algerian",10)).place(x= 300,y = 500)
#---------------------------------------------------------START-------------------------------------------------        
 
    def startzar(self,):
        self.star = random.randint(1,6)
        if self.star > 3:
            Label(self.card,text ="Atılan zar : " + str(self.star) + "   "+ str(self.PNAME) + " başlayacak",font=("Algerian",16),fg = "black").place(x = 250,y = 400)
            
        else : 
            
            Label(self.card,text ="Atılan zar : " + str(self.star) + "   "+ str(self.name) + " başlayacak",font=("Algerian",16),fg = "black").place(x = 250,y = 400)
        Button(self.card,text = "OK",command = self.nextturn,font=("Algerian",10)).place(x=410,y = 210) 
#---------------------------------------------------------CAN PUANLARI-------------------------------------------------        
    def playerhealth(self,status,count):
        if status == "none":
            Label(self.card,text = "                   ",font=("Algerian",16),fg="black").place(x = 780,y = 230)
            Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
        if status == "damage":
            self.PDEF  -= count
            Label(self.card,text = "                   ",font=("Algerian",16),fg="black").place(x = 780,y = 230)
            Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
    def monsterhealth(self,status,count):
        if status == "none":
            Label(self.card,text = "                               ",font=("Algerian",16),fg="black").place(x = 10,y = 230)
            Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(self.DEF), font=("Algerian",16)).place(x= 10,y = 230)
        if status == "damage":
            self.DEF  -= count
            Label(self.card,text = " "*50,font=("Algerian",16),fg="black").place(x = 10,y = 230)
            Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(self.DEF), font=("Algerian",16)).place(x= 10,y = 230)
#---------------------------------------------------------SALDIRI PROTOKOLLERİ-------------------------------------------------        
                   
    def playerattack(self,):
        self.zarat()
        self.crit()
        Label(self.card,text = "Atılan Zar :" + str(self.zar),font=("Algerian",16)).place(x= 250,y = 400)
        self.pdamage = self.PATK + self.critic
        Label(self.card,text = "Verilen Hasar :" + str(self.pdamage),font=("Algerian",16)).place(x= 450,y = 400)
        self.DEF -=self.pdamage
        self.monsterhealth("damage",self.pdamage)
        if self.DEF < 1 :
            res = self.name + " ÖLDÜRÜLDÜ !"
            result = self.infowindow("KAZANDIN",res) 
            Label(self.root,image = self.ppic.render).pack()
            Label(self.root,text ="Kazanılan EXP  :" + str(self.EXP) ,font=("Algerian",16)).pack()
            Label(self.root,text ="Kazanılan PARA  :" + str(self.GOLD)+" AKÇE" ,font=("Algerian",16)).pack()

                
        #Button(self.card,text = "OK",command = self.nextturn,font=("Algerian",10)).place(x=400,y = 650)
        
    def monsterattack(self,):
        self.PDEF -=self.ATK
        self.playerhealth("damage",self.ATK)
        Label(self.card,text = "Alınan Hasar :" + str(self.ATK),font=("Algerian",16)).place(x= 370,y = 500)
        if self.PDEF <1:
            res =  "GEÇMİŞ OLSUN BIRADER ÖLDÜN"
            result = self.infowindow("GEBERDİN !",res)   
            Label(self.root,image = self.pic.render).pack()        
        #Button(self.card,text = "OK",command = self.nextturn,font=("Algerian",10)).place(x=400,y = 650)
    def zarat(self,):
        self.zar = random.randint(1,6)
    def crit(self,):
        self.critic = int(self.zar * self.PCRIT / 100) + int(self.zar/2) 
    def infowindow(self,tit,info):
        self.root = tkinter.Toplevel()
        self.root.title(tit)
        self.root.geometry("300x300")
        Label(self.root, text = info, font=("Algerian",16)).pack()
        Button(self.root,text = "ÇIK",command = self.end,font=("Algerian",16)).pack()
    def end(self,):
        self.root.destroy()
        os.chdir("bin/save")
        warend = open("afterwar.txt","w+")
        info = str(self.PDEF)+ "\n" + str(self.EXP) +"\n" + str(self.GOLD) 
        warend.write(info)
        os.chdir("..")
        os.chdir("..")
        self.card.destroy()
    def nextturn(self,):
        Label(self.card,image = self.backgr.render).place(x = 0,y = 0)
        Label(self.card,text =self.name, font=("Algerian",16)).place(x= 10,y = 10)
        Label(self.card,image = self.pic.render).place(x = 10,y = 50)
        Label(self.card,text =str(self.PNAME), font=("Algerian",16)).place(x= 800,y = 10)
        Label(self.card,image = self.ppic.render).place(x = 740, y = 50)                             
        Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(self.DEF), font=("Algerian",16)).place(x= 10,y = 230)
        Label(self.card,text ="ATK  :" + str(self.PATK), font=("Algerian",16)).place(x= 680,y = 230)    
        #Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
        Label(self.card,text ="KRİTİK :" + str(self.PCRIT), font=("Algerian",16)).place(x= 880,y = 230)
        Label(self.card,image = self.vs.render).place(x = 400, y = 100)                                     
        self.playerhealth("none",0)
        self.monsterhealth("none",0)
        Button(self.card,text = "Saldır !",command = self.monsterattack,font=("Algerian",16)).place(x=40,y = 300)
        Button(self.card,text = "Saldır !",command = self.playerattack,font=("Algerian",16)).place(x=800,y = 300)
#ork = monstercard("orc",1,15,"pics/cards/orc.jpg","Dovahkiin",1,15,20,3,25)
#--------------------------------------------------VS KART---------------------------------------------------
class vskart():
    def __init__(self,name,ATK,DEF,picture,pname,patk,pdef,pcrit,ppic,exp,gold):
        self.name = name
        self.ATK = ATK
        self.DEF = DEF
        self.EXP = exp
        self.GOLD = gold
        self.card = tkinter.Toplevel()
        self.card.title(self.name)
        self.card.geometry("1000x700")
        from bin.avatars import avat
        self.pic = resim(picture)
        self.PNAME = pname
        self.PATK = patk
        self.PDEF = pdef
        self.PCRIT = pcrit
        self.ppic = avat[ppic]
        self.vs = resim("pics/mapicons/vs.png")
        self.backgr = resim("pics/start.jpg")
        
        Label(self.card,image = self.backgr.render).place(x = 0,y = 0)
        Label(self.card,text =self.name, font=("Algerian",16)).place(x= 10,y = 10)
        Label(self.card,image = self.pic.render).place(x = 10,y = 50)
        Label(self.card,text =str(self.PNAME), font=("Algerian",16)).place(x= 800,y = 10)
        Label(self.card,image = self.ppic.render).place(x = 740, y = 50)
        Label(self.card,image = self.vs.render).place(x = 450, y = 100)                             
        Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(DEF), font=("Algerian",16)).place(x= 10,y = 230)
        Label(self.card,text ="ATK  :" + str(self.PATK), font=("Algerian",16)).place(x= 680,y = 230)    
        Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
        Label(self.card,text ="KRİTİK :" + str(self.PCRIT), font=("Algerian",16)).place(x= 880,y = 230)
        Button(self.card,text = "FIGHT ! ",command = self.startzar).place(x = 400, y = 170)
        
        self.card.mainloop()
                
    def getplayer(self,patk,pdef,pcrit):
        pass
        #Label(self.card,image = self.pic.render).place(x = 0,y = 0)        
        #Button(self.card,text = "Basalayani belirlemek icin zar at !",command = self.startzar,font=("Algerian",10)).place(x= 300,y = 500)
#---------------------------------------------------------START-------------------------------------------------        
 
    def startzar(self,):
        self.star = random.randint(1,6)
        if self.star > 3:
            Label(self.card,text ="Atılan zar : " + str(self.star) + "   "+ str(self.PNAME) + " başlayacak",font=("Algerian",16),fg = "black").place(x = 250,y = 400)
            
        else : 
            
            Label(self.card,text ="Atılan zar : " + str(self.star) + "   "+ str(self.name) + " başlayacak",font=("Algerian",16),fg = "black").place(x = 250,y = 400)
        Button(self.card,text = "OK",command = self.nextturn,font=("Algerian",10)).place(x=410,y = 210) 
#---------------------------------------------------------CAN PUANLARI-------------------------------------------------        
    def playerhealth(self,status,count):
        if status == "none":
            Label(self.card,text = "                   ",font=("Algerian",16),fg="black").place(x = 780,y = 230)
            Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
        if status == "damage":
            self.PDEF  -= count
            Label(self.card,text = "                   ",font=("Algerian",16),fg="black").place(x = 780,y = 230)
            Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
    def monsterhealth(self,status,count):
        if status == "none":
            Label(self.card,text = "                                 ",font=("Algerian",16),fg="black").place(x = 10,y = 230)
            Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(self.DEF), font=("Algerian",16)).place(x= 10,y = 230)
        if status == "damage":
            self.DEF  -= count
            Label(self.card,text = "                                                                 ",font=("Algerian",8),fg="black").place(x = 10,y = 230)
            Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(self.DEF), font=("Algerian",16)).place(x= 10,y = 230)
#---------------------------------------------------------SALDIRI PROTOKOLLERİ-------------------------------------------------        
                   
    def playerattack(self,):
        self.zarat()
        self.crit()
        Label(self.card,text = "Atılan Zar :" + str(self.zar),font=("Algerian",16)).place(x= 250,y = 400)
        self.pdamage = self.PATK + self.critic
        Label(self.card,text = "Verilen Hasar :" + str(self.pdamage),font=("Algerian",16)).place(x= 450,y = 400)
        self.DEF -=self.pdamage
        self.monsterhealth("damage",self.pdamage)
        if self.DEF < 1 :
            res = self.name + " ÖLDÜRÜLDÜ !"
            result = self.infowindow("KAZANDIN",res) 
            Label(self.root,image = self.ppic.render).pack()
        #Button(self.card,text = "OK",command = self.nextturn,font=("Algerian",10)).place(x=400,y = 650)
        
    def monsterattack(self,):
        self.PDEF -=self.ATK
        self.playerhealth("damage",self.ATK)
        Label(self.card,text = "Alınan Hasar :" + str(self.ATK),font=("Algerian",16)).place(x= 370,y = 500)
        if self.PDEF <1:
            res =  "GEÇMİŞ OLSUN BIRADER ÖLDÜN"
            result = self.infowindow("GEBERDİN !",res)   
            Label(self.root,image = self.pic.render).pack()        
        #Button(self.card,text = "OK",command = self.nextturn,font=("Algerian",10)).place(x=400,y = 650)
    def zarat(self,):
        self.zar = random.randint(1,6)
    def crit(self,):
        self.critic = int(self.zar * self.PCRIT / 100) + int(self.zar/2) 
    def infowindow(self,tit,info):
        self.root = tkinter.Toplevel()
        self.root.title(tit)
        self.root.geometry("300x300")
        Label(self.root, text = info, font=("Algerian",16)).pack()
        Button(self.root,text = "ÇIK",command = self.end,font=("Algerian",16)).pack()
    def end(self,):
        self.root.destroy()
        os.chdir("bin/save")
        warend = open("afterwar.txt","w+")
        info = str(self.PDEF)+ "\n" + str(self.EXP) +"\n" + str(self.GOLD) 
        warend.write(info)
        os.chdir("..")
        os.chdir("..")
        self.card.destroy()
    def nextturn(self,):
        Label(self.card,image = self.backgr.render).place(x = 0,y = 0)
        Label(self.card,text =self.name, font=("Algerian",16)).place(x= 10,y = 10)
        Label(self.card,image = self.pic.render).place(x = 10,y = 50)
        Label(self.card,text =str(self.PNAME), font=("Algerian",16)).place(x= 800,y = 10)
        Label(self.card,image = self.ppic.render).place(x = 740, y = 50)                             
        Label(self.card,text = "ATK :" + str(self.ATK) + "    DEF :" + str(self.DEF), font=("Algerian",16)).place(x= 10,y = 230)
        Label(self.card,text ="ATK  :" + str(self.PATK), font=("Algerian",16)).place(x= 680,y = 230)    
        #Label(self.card,text ="DEF   :" + str(self.PDEF), font=("Algerian",16)).place(x= 780,y = 230)
        Label(self.card,text ="KRİTİK :" + str(self.PCRIT), font=("Algerian",16)).place(x= 880,y = 230)
        Label(self.card,image = self.vs.render).place(x = 450, y = 100)                                     
        self.playerhealth("none",0)
        self.monsterhealth("none",0)
        Button(self.card,text = "Saldır !",command = self.monsterattack,font=("Algerian",16)).place(x=40,y = 300)
        Button(self.card,text = "Saldır !",command = self.playerattack,font=("Algerian",16)).place(x=800,y = 300)
#ork = monstercard("orc",1,15,"pics/cards/orc.jpg","Dovahkiin",1,15,20,3,25)


