# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:22:47 2019

@author: fener_000
"""
import os
import bin.save.saving as saving
#----------------------------------------------------KARAKTER İMPORT-----------------------------------------
oyuncu1 = saving.player("Dovahkiin",3)
oyuncu2 = saving.player("Ozibalboa",2)
oyuncu3 = saving.player("Ronaldo",1)
oyuncu1.default()
oyuncu2.default()
oyuncu3.default()
def afterwar1():
        os.chdir("bin/save")
        with open("afterwar.txt","r") as  warend:
            file = warend.readlines()[0]
            warend.seek(0)
            filee = str(warend.readlines()[1])
            oyuncu1.DEF = int(file)
            print(oyuncu1.DEF)
            oyuncu1.level()
            print("exp")
            print(oyuncu1.expr)
            os.chdir("..")

    
afterwar1()
