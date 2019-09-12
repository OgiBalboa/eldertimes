# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:18:49 2019

@author: fener_000
"""
import random

#-----------------------------------------MAP İCONLAR ------------------------------------------------
class clan():
    def __init__(self,x):
        if x == "orc":
            self.name = x
            self.taraf = "tarafsız"
            self.bilgi = """Orc Klanınamı geldin yabancı !! 
            Ork degilsen kaderin şansına kaldı zar at, 
            3 ve aşagısını atarsan kestim seni !
            Eğer Orksan  istersen klanımıza katılabilirsin.
             """
        if x == "oduncu":
            self.name = x
            self.taraf = "tarafsız"
            self.bilgi = """ Orman Birligine hoşgeldin !
            Gel bi çay içek. Ekibimize katıl ve hayvanların dostu ol.
            Ancak lanet bir orcsan kestik seni !
            Oduncuysan asla karanlık tarafa geçemezsin.
            Eğer karanlık tarafa geçmek istiyorsan Troll Kellesi ayini yapman gerek !
            """

class sandık():
    def __init__ (self,x):
        if x == 1:
            self.name = "Gümüş Sandık "
            self.bilgi = """ Gümüş sandığa ulaştın !
            Ancak açmak için gümüş anahtara ihtiyacın var ! 
            """
 
        if x == 2:
            self.name = "Altın Sandık "
            self.bilgi = """ Altın sandığa ulaştın !
            Ancak açmak için gümüş anahtara ihtiyacın var ! 
            """           
class canbas():
    def __init__(self,x):
        if x == 1:
            self.name = " CANBAS !!!!! "
            self.bilgi = " Hoş geldin yaar ! Şimdi zar at. Şansına göre caniin basacım !"
            self.level = 1
        if x == 2:
            self.name = " CANBAS !!!!! "
            self.bilgi = " Hoş geldin yaar ! Şimdi zar at. Şansına göre caniin basacım !"
            self.level = 2  
        if x == 3:
            self.name = " CANBAS !!!!! "
            self.bilgi = " Hoş geldin yaar ! Şimdi zar at. Şansına göre caniin basacım !"
            self.level = 3

class canyak():
    def __init__(self,x):
        if x == 1:
            self.name = " CANYAK !!!!! "
            self.bilgi = " Hoş geldin yaar ! Şimdi zar at. Şansına göre caniin yakacım !"
            self.level = 1
        if x == 2:
            self.name = " CANBAS !!!!! "
            self.bilgi = " Hoş geldin yaar ! Şimdi zar at. Şansına göre caniin yakacım !"
            self.level = 2  
        if x == 3:
            self.name = " CANBAS !!!!! "
            self.bilgi = " Hoş geldin yaar ! Şimdi zar at. Şansına göre caniin yakacım !"
            self.level = 3

class teleport():
    def __init__(self,x):
        self.name = "Teleport"
        self.bilgi = " HAHAHAH TELEPOORT !! Şimdi seni işinliyacım hahahahahhah "
        if x==1:
            self.sayi = random.randint(1,34)
        if x == 2:
            self.sayi = random.randint(1,34)
        if x == 3:
            self.sayi = random.randint(1,40)

class versus():
    def __init__(self,):
        self.name = "KILIÇLAR ÇEKİLE !"
        self.bilgi = " Şimdi rastgele bir rakip seç ve kapışın. Kazanan rakibin rastgele bir itemini alacak "
class key():
    def __init__(self,x):
        if x == 1:
            self.name = "Gümüş Anahtar"
            self.bilgi = "ULAA HAYIRLI OLSUN GÜMÜŞ ANAHTARIN OLDU ! "
        if x == 1:
            self.name = "Altın Anahtar"
            self.bilgi = "ULAA HAYIRLI OLSUN ALTIN ANAHTARIN OLDU ! "            














