# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:22:02 2019

@author: fener_000
"""
import tkinter
from tkinter import *
from tkinter import Label
from PIL import Image,ImageTk
from ui.resim import resim
import threading
from threading import Thread
import time
import os
import bin.playerstats
import random     
import bin.monsters 
from bin.monsters import *
import bin.mapicons
import cards
from tkinter import messagebox
from tkinter import filedialog
#def starting():
    #os.chdir("bin/save")
    #filename = filedialog.askopenfilename()  
    #fname = os.path.split(filename)
import bin.save.saving as saving
#----------------------------------------------------KARAKTER İMPORT-----------------------------------------
oyuncu1 = saving.player("Ogibalboa",3)
oyuncu2 = saving.player("Böcük",2)
oyuncu3 = saving.player("Bayramleydi",0)
oyuncu4 = saving.player("Babaleydi",0)
oyuncu1.default()
oyuncu2.default()
oyuncu3.default()
oyuncu4.default()
game = Tk()
game.title("ELDER TIMES - BAŞLANGIÇ")
game.minsize(1300,681)
mainmap = resim("pics/mainmap.jpg")
arup = resim("pics/mapicons/up.png")
arleft = resim("pics/mapicons/left.png")
arright = resim("pics/mapicons/right.png")
ardown = resim("pics/mapicons/down.png")
p1avatar = resim("pics/avatar/kunkka.png")
backg = resim("pics/start.jpg")
import bin.avatars
from bin.movement import hareketlvl1
game.configure(background = "#00004d") # red 330000
#----------------------------------------İLERLEME KODLARI-----------------------------------------------------------
def reload():
    #Label ( game,image = backg.render).place ( x= 0, y = 0)
    Label(game, image = mainmap.render).place(x=0,y=0)
def reload2():
    Label(game, text = "  " , height = "150" , width = "200").place(x = 700 , y = 0)

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
#------------------------------------------OYUNCU 4-------------------------------------------------------------- 

p4 = hareketlvl1()
def p4ileri():
    p4.ileri()
    yerlestir()
    
def p4geri():
    p4.geri() 
    yerlestir()
    
def p4yukari():
    p4.yukari()
    yerlestir()
    
def p4asagi():
    p4.asagi() 
    yerlestir()
 
def zar():
    sayi = random.randint(1,6)
    Label(game,text =str(sayi),font=("Algerian",16),bg = "black",fg="yellow").place(x = 605, y = 550)
def nextlevel():
    game.destroy()
    os.system("python maplevel5.py")

#------------------------------------------KOORDİNATLAR ------------------------------------------------
def afterwar1():
    try :
        os.chdir("bin/save")
        with open("afterwar.txt","r") as  warend:
            file = warend.readlines()[0]
            warend.seek(0)
            file2 = warend.readlines()[1]
            warend.seek(0)
            oyuncu1.DEF = int(file)
            oyuncu1.levell(int(file2))
            file3 = warend.readlines()[2]            
            oyuncu1.GOLD += int(file3)
            yerlestir()
            os.chdir("..")
            os.chdir("..")
    except: 
        os.chdir("..")
        os.chdir("..")
def afterwar2():
    try :
        os.chdir("bin/save")
        with open("afterwar.txt","r") as  warend:
            file = warend.readlines()[0]
            warend.seek(0)
            file2 = warend.readlines()[1]
            warend.seek(0)            
            oyuncu2.DEF = int(file)
            oyuncu2.levell(int(file2))
            file3 = warend.readlines()[2]            
            oyuncu2.GOLD += int(file3)
            yerlestir()
            os.chdir("..")
            os.chdir("..")
    except: 
        os.chdir("..")
        os.chdir("..")
def afterwar3():
    try :
        os.chdir("bin/save")
        with open("afterwar.txt","r") as  warend:
            file = warend.readlines()[0]
            warend.seek(0)
            file2 = warend.readlines()[1]
            oyuncu3.DEF = int(file)
            oyuncu3.levell(int(file2))
            warend.seek(0)
            file3 = warend.readlines()[2]            
            oyuncu3.GOLD += int(file3)
            yerlestir()
            os.chdir("..")
            os.chdir("..")
    except: 
        os.chdir("..")
        os.chdir("..")
def afterwar4():
    try :
        os.chdir("bin/save")
        with open("afterwar.txt","r") as  warend:
            file = warend.readlines()[0]
            warend.seek(0)
            file2 = warend.readlines()[1]
            oyuncu4.DEF = int(file)
            oyuncu4.levell(int(file2))
            warend.seek(0)
            file3 = warend.readlines()[2]            
            oyuncu4.GOLD += int(file3)
            yerlestir()
            os.chdir("..")
            os.chdir("..")
    except: 
        os.chdir("..")
        os.chdir("..")
def p1kor():
    kareler(p1.dimx,p1.dimy,oyuncu1.name,oyuncu1.ATK,oyuncu1.DEF,oyuncu1.CRIT,oyuncu1.avno)
def p2kor():
    kareler(p2.dimx,p2.dimy,oyuncu2.name,oyuncu2.ATK,oyuncu2.DEF,oyuncu2.CRIT,oyuncu2.avno)
def p3kor():
    kareler(p3.dimx,p3.dimy,oyuncu3.name,oyuncu3.ATK,oyuncu3.DEF,oyuncu3.CRIT,oyuncu3.avno)
def p4kor():
    kareler(p4.dimx,p4.dimy,oyuncu4.name,oyuncu4.ATK,oyuncu4.DEF,oyuncu4.CRIT,oyuncu4.avno)
    
def kareler(x,y,pname,patk,pdef,pcrit,avno):
    from cards import monstercard
    if x >10 and x < 80 and y >10 and y < 31:
        name =""" 
        Hos Geldiniz Savaşçılar ! 
        Atıldığınız bu macerada yolu en az zararla
        ve en çok kazançla tamamlamanın yolunu arayın.
        İlk hedefiniz olabildiğince çok savaşmak olmalı.
        Çünkü ileride savaştan kaçmanın yollarını arayacaksınız.
        Haadi kolay gele !
              """
        tkinter.messagebox.showinfo("Merhaba",name)
    elif x >10 and x < 80 and y >10 and y < 96:
        name = bin.monsters.goblin(1).name
        ATK = bin.monsters.goblin(1).ATK
        DEF = bin.monsters.goblin(1).DEF
        exp = random.randint(1,5)
        gold = random.randint(20,25)
        monstercard(name,ATK,DEF,"pics/cards/goblinwarrior.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
        #afterwar1()
    elif x >10 and x < 80 and y >10 and y < 161:
        name = bin.monsters.hayvan(1).name
        ATK = bin.monsters.hayvan(1).ATK
        DEF = bin.monsters.hayvan(1).DEF
        exp = random.randint(15,30)
        monstercard(name,ATK,DEF,"pics/cards/warwolf.jpg",pname,patk,pdef,pcrit,avno,exp,0)
    elif x >10 and x < 80 and y >10 and y < 226:
        name = bin.monsters.mage(1).name
        ATK = bin.monsters.mage(1).ATK
        DEF = bin.monsters.mage(1).DEF
        exp = random.randint(5,15)
        gold = random.randint(5,15)
        monstercard(name,ATK,DEF,"pics/cards/mage.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x >10 and x < 80 and y >10 and y < 291:
        name = bin.monsters.hayvan(1).name
        ATK = bin.monsters.hayvan(1).ATK
        DEF = bin.monsters.hayvan(1).DEF
        exp = random.randint(15,30)
        monstercard(name,ATK,DEF,"pics/cards/warwolf.jpg",pname,patk,pdef,pcrit,avno,exp,0)
    elif x >10 and x < 80 and y >10 and y < 366:
        name = bin.mapicons.clan("orc").name
        clan = tkinter.Toplevel(game)
        clan.title("ORC CLANI")        
        Label(clan,text = "ORC CLANINA HOS GELDIN ", font=("Algerian",16)).pack()
        info = bin.mapicons.clan("orc").bilgi
        orcpic = resim("pics/mapicons/orc.jpg")
        #Label(clan,image = orcpic.render).pack()
        Label(clan,text = info, font=("Algerian",16),justify= LEFT).pack()  
        Button(clan,text = "EXIT",command = clan.destroy).pack()
        
    elif x >10 and x < 80 and y >10 and y < 421:
        name = bin.monsters.goblin(2).name
        ATK = bin.monsters.goblin(2).ATK
        DEF = bin.monsters.goblin(2).DEF
        exp = random.randint(5,8)
        gold = random.randint(40,55)
        monstercard(name,ATK,DEF,"pics/cards/goblinarmy.png",pname,patk,pdef,pcrit,avno,exp,gold)
    if x >94 and x <140 and y == 420:
        name = bin.monsters.orc(1).name
        ATK = bin.monsters.orc(1).ATK
        DEF = bin.monsters.orc(1).DEF
        exp = random.randint(15,35)
        gold = random.randint(5,15)
        monstercard(name,ATK,DEF,"pics/cards/orcchaos.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    if x >159 and x <201 and y == 420:
        canbas(pname,10,20)
    elif  x >159 and x <201 and y == 355 : 
        sandik(pname)                    
    elif  x >159 and x <201 and y == 290 :       
        name = bin.monsters.haydut(1).name
        ATK = bin.monsters.haydut(1).ATK
        DEF = bin.monsters.haydut(1).DEF
        exp = random.randint(60,100)
        gold = random.randint(90,110)
        monstercard(name,ATK,DEF,"pics/cards/banditarcher.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif  x >159 and x <201 and y ==225:       
        name = bin.mapicons.clan("orc").name
        clan = tkinter.Toplevel(game)
        clan.title("ODUNCU CLANI")        
        Label(clan,text = "ODUNCU CLANINA HOS GELDIN ", font=("Algerian",16)).pack()
        info = bin.mapicons.clan("oduncu").bilgi
        #orcpic = resim("pics/mapicons/orc.jpg")
        Label(clan,image = orcpic.render).pack()
        Label(clan,text = info, font=("Algerian",16),justify= LEFT).pack() 
        Button(clan,text = "EXIT",command = clan.destroy).pack()
    elif  x >159 and x <201 and y ==160:       
        name = bin.monsters.hayvan(1).name
        ATK = bin.monsters.hayvan(1).ATK
        DEF = bin.monsters.hayvan(1).DEF
        exp = random.randint(15,30)
        monstercard(name,ATK,DEF,"pics/cards/warwolf.jpg",pname,patk,pdef,pcrit,avno,exp,0)
    elif  x >159 and x <201 and y == 95:       
        canbas(pname,10,30)
#--------------------------------------------------2. SERİ--------------------------------------------------------- 
    elif  x >159 and x <201 and y == 30:       
        teleport(pname)
    elif  x > 224 and x < 264 and y == 30:
        name = bin.monsters.haydut(1).name
        ATK = bin.monsters.haydut(1).ATK
        DEF = bin.monsters.haydut(1).DEF
        exp = random.randint(60,100)
        gold = random.randint(90,120)
        monstercard(name,ATK,DEF,"pics/cards/banditarcher.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif  x >289 and x < 329 and y == 30:
        sandik(pname)
    elif x > 289 and x < 329 and y == 95:
        name = bin.monsters.mage(1).name
        ATK = bin.monsters.mage(1).ATK
        DEF = bin.monsters.mage(1).DEF
        exp = random.randint(45,60)
        gold = random.randint(25,55)
        monstercard(name,ATK,DEF,"pics/cards/mage.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 289 and x < 329 and y == 160:
        name = bin.monsters.hayvan(1).name
        ATK = bin.monsters.hayvan(1).ATK
        DEF = bin.monsters.hayvan(1).DEF
        exp = random.randint(70,140)
        monstercard(name,ATK,DEF,"pics/cards/warwolf.jpg",pname,patk,pdef,pcrit,avno,exp,0)
    elif x > 289 and x < 329 and y == 225:  
        name = bin.monsters.orc(1).name
        ATK = bin.monsters.orc(1).ATK
        DEF = bin.monsters.orc(1).DEF
        exp = random.randint(25,35)
        gold = random.randint(15,20)
        monstercard(name,ATK,DEF,"pics/cards/orcchaos.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 289 and x < 329 and y == 295:  
        name = bin.monsters.goblin(2).name
        ATK = bin.monsters.goblin(2).ATK
        DEF = bin.monsters.goblin(2).DEF
        exp = random.randint(40,58)
        gold = random.randint(140,240)
        monstercard(name,ATK,DEF,"pics/cards/goblinarmy.png",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 289 and x < 329 and y == 355: 
        canbas(pname,10,50)
    elif x > 289 and x < 329 and y == 420: 
        canyak(pname,5,10)
    elif x > 353 and x < 395 and y == 420:  
        name = bin.mapicons.clan("orc").name
        clan = tkinter.Toplevel(game)
        clan.title("MADENCI CLANI")        
        Label(clan,text = "MADENCI CLANINA HOS GELDIN ", font=("Algerian",16)).place(x= 200,y = 0)
        info = bin.mapicons.clan("orc").bilgi
        orcpic = resim("pics/mapicons/orc.jpg")
        Label(clan,image = orcpic.render).place(x= 0,y = 20)
        Label(clan,text = info, font=("Algerian",8),justify= LEFT).place(x= 0,y = 150)  
        Button(clan,text = "EXIT",command = clan.destroy).place( x = 200, y = 400)
    elif x > 419 and x < 451 and y == 420:
        sandik(pname)   
        
    elif x > 419 and x < 451 and y == 355:
        pass # VS
    elif x > 419 and x < 451 and y == 290:
        name = bin.monsters.orc(1).name
        ATK = bin.monsters.orc(1).ATK
        DEF = bin.monsters.orc(1).DEF
        exp = random.randint(60,100)
        gold = random.randint(30,55)
        monstercard(name,ATK,DEF,"pics/cards/orcchaos.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 419 and x < 451 and y == 225:
        name = bin.monsters.goblin(2).name
        ATK = bin.monsters.goblin(2).ATK
        DEF = bin.monsters.goblin(2).DEF
        exp = random.randint(40,58)
        gold = random.randint(140,240)
        monstercard(name,ATK,DEF,"pics/cards/goblinarmy.png",pname,patk,pdef,pcrit,avno,exp,gold)
        
    elif x > 419 and x < 451 and y == 160:
        name = bin.monsters.hayvan(1).name
        ATK = bin.monsters.hayvan(1).ATK
        DEF = bin.monsters.hayvan(1).DEF
        exp = random.randint(100,140)
        monstercard(name,ATK,DEF,"pics/cards/warwolf.jpg",pname,patk,pdef,pcrit,avno,exp,0)
    elif x > 419 and x < 451 and y == 95:
        name = bin.monsters.mage(1).name
        ATK = bin.monsters.mage(1).ATK
        DEF = bin.monsters.mage(1).DEF
        exp = random.randint(70,90)
        gold = random.randint(25,55)
        monstercard(name,ATK,DEF,"pics/cards/mage.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 419 and x < 451 and y == 30:
        name = bin.mapicons.canyak(1).name # canyak
        cards.title(name)
        Label(cards,text = name, font=("Algerian",16)).place(x= 120,y = 0)
        info = bin.mapicons.canyak(1).bilgi
        Label(cards,text = info, font=("Algerian",12)).place(x= 120,y = 150)   
    elif x > 484 and x < 514 and y == 30:
        name = bin.mapicons.canbas(1).name # canbas
        cards.title(name)
        Label(cards,text = name, font=("Algerian",16)).place(x= 120,y = 0)
        info = bin.mapicons.canbas(1).bilgi
        Label(cards,text = info, font=("Algerian",12)).place(x= 120,y = 150)   
    elif x > 549 and x < 600 and y == 30:
        name = bin.monsters.orc(1).name
        ATK = bin.monsters.orc(1).ATK
        DEF = bin.monsters.orc(1).DEF
        exp = random.randint(300,400)
        gold = random.randint(40,55)
        monstercard(name,ATK,DEF,"pics/cards/orcchaos.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 549 and x < 600 and y == 95:
        sandik() # ANAHTAR
    elif x > 549 and x < 600 and y == 160:
        name = bin.monsters.hayvan(2).name
        ATK = bin.monsters.hayvan(2).ATK
        DEF = bin.monsters.hayvan(2).DEF
        exp = random.randint(2000,2500)
        monstercard(name,ATK,DEF,"pics/cards/wolfwarrior.jpg",pname,patk,pdef,pcrit,avno,exp,0)
    elif x > 549 and x < 600 and y == 225:
        name = bin.monsters.orc(2).name
        ATK = bin.monsters.orc(2).ATK
        DEF = bin.monsters.orc(2).DEF
        exp = random.randint(1300,1400)
        gold = random.randint(700,1000)
        monstercard(name,ATK,DEF,"pics/cards/orcchief.jpg",pname,patk,pdef,pcrit,avno,exp,gold)
    elif x > 549 and x < 600 and y == 290:
        name = bin.monsters.goblin(3).name
        ATK = bin.monsters.goblin(3).ATK
        DEF = bin.monsters.goblin(3).DEF
        exp = random.randint(600,900)
        gold = random.randint(2000,3000)
        monstercard(name,ATK,DEF,"pics/cards/goblin.jpg",pname,patk,pdef,pcrit,avno,exp,gold)     
    elif x > 549 and x < 600 and y == 355:
        teleport(pname)
    elif x > 549 and x < 600 and y == 420:
        pass # FINISH
#----------------------------------------PANEL-----------------------------------------------------------     
Label(game, image = mainmap.render).place(x=0,y=0)

Label(game,text="OYUNCU 1",font=("Algerian",16),bg = "#00004d" ,fg="white").place(x = 10, y = 490)
Button(game,image= arup.render,command = p1yukari).place(x = 40, y = 520)
Button(game,image= arleft.render,command = p1geri).place(x = 10, y = 540)
Button(game,image= arright.render,command = p1ileri).place(x = 70, y = 540)
Button(game,image= ardown.render,command = p1asagi).place(x = 40, y = 560)

Label(game,text="OYUNCU 2",font=("Algerian",16),bg = "#00004d" ,fg="white").place(x = 150, y = 490)
Button(game,image= arup.render,command = p2yukari).place(x = 180, y = 520)
Button(game,image= arleft.render,command = p2geri).place(x = 150, y = 540)
Button(game,image= arright.render,command = p2ileri).place(x = 210, y = 540)
Button(game,image= ardown.render,command = p2asagi).place(x = 180, y = 560)

Label(game,text="OYUNCU 3",font=("Algerian",16),bg = "#00004d" ,fg="white").place(x = 290, y = 490)
Button(game,image= arup.render,command = p3yukari).place(x = 320, y = 520)
Button(game,image= arleft.render,command = p3geri).place(x = 290, y = 540)
Button(game,image= arright.render,command = p3ileri).place(x = 350, y = 540)
Button(game,image= ardown.render,command = p3asagi).place(x = 320, y = 560)

Label(game,text="OYUNCU 4",font=("Algerian",16),bg = "#00004d" ,fg="white").place(x = 450, y = 490)
Button(game,image= arup.render,command = p4yukari).place(x = 480, y = 520)
Button(game,image= arleft.render,command = p4geri).place(x = 450, y = 540)
Button(game,image= arright.render,command = p4ileri).place(x = 510, y = 540)
Button(game,image= ardown.render,command = p4asagi).place(x = 480, y = 560)

#--------------------------------------------------OYUNCU BİLGİLERİ---------------------------------------------
def oyuncu1info():  
    Label(game,text =oyuncu1.name,font=("Algerian",16),bg = "#00004d" ,fg="white").place(x=750, y = 30)
    oyuncualani(700,55)      
    hp = oyuncu1.DEF
    p1atk = oyuncu1.ATK
    p1crit = oyuncu1.CRIT
    p1lvl = oyuncu1.LEVEL
    p1exp = oyuncu1.EXPR
    p1gold = oyuncu1.GOLD
    def check():
        def atkup():
            oyuncu1.ATK += 2
            yerlestir()
            lvl.destroy()
        def defup():
            oyuncu1.DEF += 20
            yerlestir()
            lvl.destroy()
        def cup():
            oyuncu1.CRIT += 5
            yerlestir()
            lvl.destroy()
        if oyuncu1.nextlevel == True:
            lvl = tkinter.Toplevel(game)
            tit= str(oyuncu1.name) + ", LEVEL ATLADIN ! "
            lvl.title(tit)
            Label(lvl,text = "Yükseltmek istediğin özelliği seç ",font=("Algerian",12)).pack()
            Button(lvl,text = "ATAK GÜCÜ",font=("Algerian",12),command = atkup).pack()
            Button(lvl,text = "DEFANS DAYANIKLILIĞI",font=("Algerian",12),command = defup).pack()
            Button(lvl,text = "KRİTİK HASAR",font=("Algerian",12),command = cup).pack()
            oyuncu1.nextlevel = False
            #lvl.mainloop()
    #--------------------------------------MANUEL GİRDİLER-------------------------------------------------
    def manuel1():
        def don ():
            oyuncu1.ATK = int(str(atken.get()))   
            oyuncu1.DEF = int(str(defen.get()))
            oyuncu1.CRIT = int(str(crten.get()))
            oyuncu1.GOLD = int(str(golden.get()))
            manual.destroy()
        manual = tkinter.Toplevel(game)
        manual.title("YENİ DEGERLERİ GİRİNİZ")
        manual.geometry("500x500")
        Label(manual,text = "ATK ",font=("Algerian",12)).pack()
        atken= Entry(manual,width = '5')
        atken.pack()

        Label(manual,text = "DEF ",font=("Algerian",12)).pack()
        defen= Entry(manual,width = '5')
        defen.pack()
        Label(manual,text = "KRİTİK ",font=("Algerian",12)).pack()

        crten= Entry(manual,width = '5')
        crten.pack()
        Label(manual,text = "PARA ",font=("Algerian",12)).pack()

        golden= Entry(manual,width = '5')
        golden.pack()


        Button(manual,text = "OKAY ",font=("Algerian",12),command = don ).pack()


    check()
    Button(game,text="Manuel",command = manuel1,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x= 752, y= 185)      
    p1info = "Can Puani : " + str(hp) + "\nATK      : " + str(p1atk) + "\nKRITIK    : " + str(p1crit) + "\nLEVEL    :" + str(p1lvl) +" | EXP    : " + str(p1exp) + "\nPARA   :" + str(p1gold) + " Akçe" 
    Label(game,text =p1info,font=("Algerian",16),bg = "#ffff00" ,fg="#00004d",justify = "left").place(x=702, y = 57)
    Button(game,text="OK",command = afterwar1,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x = 702, y = 185)
    Button(game,text="Envanter",command = p1envanter,font=("Algerian",10),bg = "black",fg="yellow").place(x = 702, y = 210)
def oyuncu2info():  
    Label(game,text =oyuncu2.name,font=("Algerian",16),bg = "#00004d" ,fg="white").place(x=1052, y = 30)
    oyuncualani(1000,55)      
    hp = oyuncu2.DEF
    p2atk = oyuncu2.ATK
    p2crit = oyuncu2.CRIT
    p2exp = oyuncu2.EXPR
    p2lvl = oyuncu2.LEVEL
    p2gold = oyuncu2.GOLD
    
    def check():
        def atkup():
            oyuncu2.ATK += 2
            yerlestir()
            lvl.destroy()
        def defup():
            oyuncu2.DEF += 20
            yerlestir()
            lvl.destroy()
        def cup():
            oyuncu2.CRIT += 5
            yerlestir()
            lvl.destroy()
        if oyuncu2.nextlevel == True:
            lvl = tkinter.Toplevel(game)
            tit= str(oyuncu2.name) + ", LEVEL ATLADIN ! "
            lvl.title(tit)
            Label(lvl,text = "Yükseltmek istediğin özelliği seç ",font=("Algerian",12)).pack()
            Button(lvl,text = "ATAK GÜCÜ",font=("Algerian",12),command = atkup).pack()
            Button(lvl,text = "DEFANS DAYANIKLILIĞI",font=("Algerian",12),command = defup).pack()
            Button(lvl,text = "KRİTİK HASAR",font=("Algerian",12),command = cup).pack()
            oyuncu2.nextlevel = False
    #--------------------------------------MANUEL GİRDİLER-------------------------------------------------

    def manuel2():
        def don ():
            oyuncu2.ATK = int(str(atken.get()))   
            oyuncu2.DEF = int(str(defen.get()))
            oyuncu2.CRIT = int(str(crten.get()))
            oyuncu2.GOLD = int(str(golden.get()))
            manual.destroy()
        manual = tkinter.Toplevel(game)
        manual.title("YENİ DEGERLERİ GİRİNİZ")
        manual.geometry("300x300")
        Label(manual,text = "ATK ",font=("Algerian",12)).pack()
        atken= Entry(manual,width = '5')
        atken.pack()

        Label(manual,text = "DEF ",font=("Algerian",12)).pack()
        defen= Entry(manual,width = '5')
        defen.pack()
        Label(manual,text = "KRİTİK ",font=("Algerian",12)).pack()

        crten= Entry(manual,width = '5')
        crten.pack()
        Label(manual,text = "PARA ",font=("Algerian",12)).pack()

        golden= Entry(manual,width = '5')
        golden.pack()


        Button(manual,text = "OKAY ",font=("Algerian",12),command = don ).pack()


    check()  
    Button(game,text="Manuel",command = manuel2,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x= 1052, y= 185)      
    Button(game,text="OK",command = afterwar2,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x = 1002, y = 185)    
    p2info = "Can Puani : " + str(hp) + "\nATK        : " + str(p2atk) + "\nKRITIK    : " + str(p2crit)+ "\nLEVEL    :" + str(p2lvl) + " | EXP      : " + str(p2exp) + "\nPARA   :" + str(p2gold) + " Akçe" 
    Label(game,text =p2info,font=("Algerian",16),bg = "#ffff00" ,fg="#00004d",justify = "left").place(x=1002, y = 57)
    Button(game,text="Envanter",command = p1envanter,font=("Algerian",10),bg = "black",fg="yellow").place(x = 1002, y = 210)
#----------------------------------------------OYUNCU 4 İNFO----------------------------------------------
def oyuncu3info():  
    Label(game,text =oyuncu3.name,font=("Algerian",16),bg = "#00004d" ,fg="white").place(x=750, y = 240)
    oyuncualani(700,275)      
    hp = oyuncu3.DEF
    p3atk = oyuncu3.ATK
    p3crit = oyuncu3.CRIT
    p3exp = oyuncu3.EXPR
    p3lvl = oyuncu3.LEVEL
    p3gold = oyuncu3.GOLD
    
    def check():
        def atkup():
            oyuncu3.ATK += 2
            yerlestir()
            lvl.destroy()
        def defup():
            oyuncu3.DEF += 20
            yerlestir()
            lvl.destroy()
        def cup():
            oyuncu3.CRIT += 5
            yerlestir()
            lvl.destroy()
        if oyuncu3.nextlevel == True:
            lvl = tkinter.Toplevel(game)
            tit= str(oyuncu3.name) + ", LEVEL ATLADIN ! "
            lvl.title(tit)
            Label(lvl,text = "Yükseltmek istediğin özelliği seç ",font=("Algerian",12)).pack()
            Button(lvl,text = "ATAK GÜCÜ",font=("Algerian",12),command = atkup).pack()
            Button(lvl,text = "DEFANS DAYANIKLILIĞI",font=("Algerian",12),command = defup).pack()
            Button(lvl,text = "KRİTİK HASAR",font=("Algerian",12),command = cup).pack()
            oyuncu3.nextlevel = False
    #--------------------------------------MANUEL GİRDİLER-------------------------------------------------

    def manuel3():
        def don ():
            oyuncu3.ATK = int(str(atken.get()))   
            oyuncu3.DEF = int(str(defen.get()))
            oyuncu3.CRIT = int(str(crten.get()))
            oyuncu3.GOLD = int(str(golden.get()))
            manual.destroy()
        manual = tkinter.Toplevel(game)
        manual.title("YENİ DEGERLERİ GİRİNİZ")
        manual.geometry("300x300")
        Label(manual,text = "ATK ",font=("Algerian",12)).pack()
        atken= Entry(manual,width = '5')
        atken.pack()

        Label(manual,text = "DEF ",font=("Algerian",12)).pack()
        defen= Entry(manual,width = '5')
        defen.pack()
        Label(manual,text = "KRİTİK ",font=("Algerian",12)).pack()

        crten= Entry(manual,width = '5')
        crten.pack()
        Label(manual,text = "PARA ",font=("Algerian",12)).pack()

        golden= Entry(manual,width = '5')
        golden.pack()


        Button(manual,text = "OKAY ",font=("Algerian",12),command = don ).pack()


    check()  
    Button(game,text="Manuel",command = manuel3,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x= 752, y= 405)      
    Button(game,text="OK",command = afterwar3,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x = 702, y = 405)    
    p3info = "Can Puani : " + str(hp) + "\nATK        : " + str(p3atk) + "\nKRITIK    : " + str(p3crit)+ "\nLEVEL    :" + str(p3lvl) + " | EXP      : " + str(p3exp) + "\nPARA   :" + str(p3gold) + " Akçe" 
    Label(game,text =p3info,font=("Algerian",16),bg = "#ffff00" ,fg="#00004d",justify = "left").place(x=702, y = 277)
    Button(game,text="Envanter",command = p3envanter,font=("Algerian",10),bg = "black",fg="yellow").place(x = 702, y = 430)
#-----------------------------------------------------OYUNCU 4--------------------------------------
def oyuncu4info():  
    Label(game,text =oyuncu4.name,font=("Algerian",12),bg = "#00004d" ,fg="white").place(x=1052, y = 30)
    oyuncualani(1000,355)      
    hp = oyuncu4.DEF
    p4atk = oyuncu4.ATK
    p4crit = oyuncu4.CRIT
    p4exp = oyuncu4.EXPR
    p4lvl = oyuncu4.LEVEL
    p4gold = oyuncu4.GOLD
    
    def check():
        def atkup():
            oyuncu4.ATK += 2
            yerlestir()
            lvl.destroy()
        def defup():
            oyuncu4.DEF += 20
            yerlestir()
            lvl.destroy()
        def cup():
            oyuncu4.CRIT += 5
            yerlestir()
            lvl.destroy()
        if oyuncu4.nextlevel == True:
            lvl = tkinter.Toplevel(game)
            tit= str(oyuncu4.name) + ", LEVEL ATLADIN ! "
            lvl.title(tit)
            Label(lvl,text = "Yükseltmek istediğin özelliği seç ",font=("Algerian",12)).pack()
            Button(lvl,text = "ATAK GÜCÜ",font=("Algerian",12),command = atkup).pack()
            Button(lvl,text = "DEFANS DAYANIKLILIĞI",font=("Algerian",12),command = defup).pack()
            Button(lvl,text = "KRİTİK HASAR",font=("Algerian",12),command = cup).pack()
            oyuncu4.nextlevel = False
    #--------------------------------------MANUEL GİRDİLER-------------------------------------------------

    def manuel4():
        def don ():
            oyuncu4.ATK = int(str(atken.get()))   
            oyuncu4.DEF = int(str(defen.get()))
            oyuncu4.CRIT = int(str(crten.get()))
            oyuncu4.GOLD = int(str(golden.get()))
            manual.destroy()
        manual = tkinter.Toplevel(game)
        manual.title("YENİ DEGERLERİ GİRİNİZ")
        manual.geometry("300x300")
        Label(manual,text = "ATK ",font=("Algerian",12)).pack()
        atken= Entry(manual,width = '5')
        atken.pack()

        Label(manual,text = "DEF ",font=("Algerian",12)).pack()
        defen= Entry(manual,width = '5')
        defen.pack()
        Label(manual,text = "KRİTİK ",font=("Algerian",12)).pack()

        crten= Entry(manual,width = '5')
        crten.pack()
        Label(manual,text = "PARA ",font=("Algerian",12)).pack()

        golden= Entry(manual,width = '5')
        golden.pack()


        Button(manual,text = "OKAY ",font=("Algerian",12),command = don ).pack()


    check()  
    Button(game,text="Manuel",command = manuel4,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x= 1052, y= 185)      
    Button(game,text="OK",command = afterwar4,font=("Algerian",10),bg = "#00004d",fg="yellow").place(x = 1002, y = 185)    
    p4info = "Can Puani : " + str(hp) + "\nATK        : " + str(p4atk) + "\nKRITIK    : " + str(p4crit)+ "\nLEVEL    :" + str(p4lvl) + " | EXP      : " + str(p4exp) + "\nPARA   :" + str(p4gold) + " Akçe" 
    Label(game,text =p4info,font=("Algerian",16),bg = "#ffff00" ,fg="#00004d",justify = "left").place(x=1002, y = 57)
    Button(game,text="Envanter",command = p4envanter,font=("Algerian",10),bg = "black",fg="yellow").place(x = 1002, y = 210)


    
#------------------------------------------OYUN KARELERİ ------------------------------------------------
dal = Thread(target = kordinat)
dal.start()
def p1envanter():
    pass
def p3envanter():
    pass
def p4envanter():
    pass
def oyuncualani(a,b):
    satir = " "*80 + "\n"
    Label(game,text = satir*10, bg = "#ffff00",borderwidth = 7).place( x = a, y = b)
def yerlestir():
    reload()
    oyuncu1info()
    oyuncu2info()
    oyuncu3info()
    Label(game,image =p1avatar.render).place(x=p1.dimx, y = p1.dimy)
    Label(game,text ="P2",font=("Algerian",12),bg = "red",fg="yellow").place(x=p2.dimx+20, y = p2.dimy)
    Label(game,text ="P3",font=("Algerian",12),bg = "green",fg="yellow").place(x=p3.dimx+30, y = p3.dimy)
    Label(game,text ="P4",font=("Algerian",12),bg = "blue",fg="yellow").place(x=p4.dimx+40, y = p4.dimy)
yerlestir() 
Button(game,text="OK",command = p1kor,font=("Algerian",10),bg = "#00004d" , fg="yellow").place(x = 40, y = 620)
Button(game,text="OK",command = p2kor,font=("Algerian",10),bg = "#00004d" ,fg="yellow").place(x = 180, y = 620)
Button(game,text="OK",command = p3kor,font=("Algerian",10),bg = "#00004d" ,fg="yellow").place(x = 320, y = 620)
Button(game,text="OK",command = p4kor,font=("Algerian",10),bg = "#00004d" ,fg="yellow").place(x = 490, y = 620)

#Button(game,text="Oyuncu 2 İlerle",command = go2,font=("Arial",16),bg = "black",fg="yellow").place(x = 0, y = 600)
Button(game,text="Zar At",command = zar,font=("Algerian",16),bg = "black",fg="yellow").place(x = 600, y = 500)
Button(game,text="LEVEL 5",command = nextlevel,font=("Algerian",16),bg = "black",fg="yellow").place(x = 800, y = 500)
#-----------------------------------------OYUNCU BİLGİLERİ-------------------------------------------------------
oyuncu1info()
oyuncu2info()
oyuncu3info()
def sandik(pname):
        if pname ==oyuncu1.name :
            i = random.randint(1,3)
            a = random.randint(100,350)
            if i ==1:              
                oyuncu1.EXP += a
                c = "EXP"
            elif i == 2:
                oyuncu1.GOLD += a
                c = "GOLD"
        elif pname ==oyuncu2.name :
            i = random.randint(1,3)
            a = random.randint(100,350)
            if i ==1:              
                oyuncu2.EXP += a
                c = "EXP"
                
            elif i == 2:
                oyuncu2.GOLD += a
        elif pname ==oyuncu3.name :
            i = random.randint(1,3)
            a = random.randint(100,350)
            if i ==1:   
                c = "EXP"
                oyuncu3.EXP += a
            elif i == 2:
                c = "GOLD"
                oyuncu3.GOLD += a
        elif pname ==oyuncu4.name :
            i = random.randint(1,3)
            a = random.randint(100,350)
            if i ==1:  
                c = "EXP"
                oyuncu4.EXP += a
            elif i == 2:
                oyuncu4.GOLD += a
                c = "GOLD"
        sandik = tkinter.Toplevel(game)
        sandik.title("Tebrikler !")
        Label(sandik, text = "Helal len " + str(pname) +" , " + str(a) + " " +str(c) +" Kazandın.").pack()
        Button(sandik, text = "OK.", command = sandik.destroy).pack()

def canbas(pname,x,y):
        if pname == oyuncu1.name :
            a = random.randint(x,y)
            oyuncu1.DEF += a
        if pname == oyuncu2.name :
            a = random.randint(x,y)
            oyuncu2.DEF += a
        if pname == oyuncu3.name :
            a = random.randint(x,y)
            oyuncu3.DEF += a
        if pname == oyuncu4.name :
            a = random.randint(x,y)
            oyuncu4.DEF += a
        canbas = tkinter.Toplevel(game)
        canbas.title("CANBAAAS !")
        Label(canbas, text = "Helal len " + str(pname) +"  ," + str(a) + " DEFANS Kazandın").pack()
        Button(canbas, text = "OK.", command = canbas.destroy).pack()

def canyak(pname,x,y):
        if pname == oyuncu1.name :
            a = random.randint(x,y)
            oyuncu1.DEF -= a
        if pname == oyuncu2.name :
            a = random.randint(x,y)
            oyuncu2.DEF -= a
        if pname == oyuncu3.name :
            a = random.randint(x,y)
            oyuncu3.DEF -= a
        if pname == oyuncu4.name :
            a = random.randint(x,y)
            oyuncu4.DEF -= a
        canbas = tkinter.Toplevel(game)
        canbas.title("CANBAAAS !")
        Label(canyak, text = "HAHAHAHHAH " + str(pname) +" ," + str(a) + " CANIN GETTİ").pack()
        Button(canyak, text = "OK.", command = canbas.destroy).pack()

def teleport (pname):
        a = random.randint(5,25)
        teleport = tkinter.Toplevel(game)
        teleport.title("TELEPOORT !")
        Label(teleport, text = "HAHAHAHHAH " + str(pname) +" ," + str(a) + ". KAREYE GİT " ).pack()
        Button(teleport, text = "OK.", command = canbas.destroy).pack()
                
game.mainloop()

