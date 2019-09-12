# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:00:47 2019

@author: fener_000
"""
import random
#----------------------------MONSTERS----------------------------
class goblin():
    def __init__(self,x):
        self.level = x
        if x == 1: # Level 1 golin
            self.name = "Goblin Hırsızı"
            self.ATK = 1
            self.DEF = 7
        
        if x == 2:
            self.name = "Goblin Haydutları"
            self.ATK = 2
            self.DEF = 14
            
        if x ==3: 
            self.name = "Goblin Şefi "
            self.ATK = 6
            self.DEF = 16


class hayvan():
    def __init__(self,x):
        self.level = x
        if x == 1: # Level 1 kurt
            self.name = "Kurt"
            self.ATK = random.randint(1,4)
            self.DEF = random.randint(3,9)
        if x == 2: # Level 1 kurt
            self.name = " Zırhlı Domuz "
            self.ATK = 4
            self.DEF = 16

class mage():
    def __init__(self,x):
        self.level = x
        if x == 1: # Level 1 mage
            self.name = "Şaman"
            self.ATK = random.randint(3,6)
            self.DEF = 8
        
        if x == 2:
            self.name = "SOON"
            self.ATK = 12
            self.DEF = 12
class orc():
    def __init__(self,x):
        self.level = x
        if x == 1: # Level 1 orc
            self.name = "Yabani Orc"
            self.ATK = random.randint(1,7)
            self.DEF = 7
        
        if x == 2:
            self.name = " Orc Kabile Lideri"
            self.ATK = 7
            self.DEF = 26

class haydut():
    def __init__(self,x):
        self.level = x
        if x == 1: # Level 1 haydut
            self.name = "Orman Avcısı"
            self.ATK = random.randint(3,4)
            self.DEF = 4
        
        if x == 2:
            self.name = "Goblin Haydutları"
            self.ATK = 12
            self.DEF = 12

