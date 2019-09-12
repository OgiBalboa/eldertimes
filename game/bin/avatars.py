# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:23:42 2019

@author: fener_000
"""
# AVATAR LIST
from PIL import Image,ImageTk
from ui.resim import resim
try:
    crusade = resim("pics/avatars/crusade.jpg")

    orc = resim ("pics/avatars/orc.jpg")

    arrow = resim("pics/avatars/arrow.jpg")
    
    spartan = resim("pics/avatars/spartan.jpg")
except :
    crusade = resim("bin/pics/avatars/crusade.jpg")

    orc = resim ("bin/pics/avatars/orc.jpg")

    arrow = resim("bin/pics/avatars/arrow.jpg")

    spartan = resim("bin/pics/avatars/spartan.jpg")    
avat=[crusade,orc,arrow,spartan]
boyut = len(avat)

