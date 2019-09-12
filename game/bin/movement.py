# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:42:28 2019

@author: fener_000
"""

class hareketlvl1():
    def __init__(self,):
        self.dimx = 30
        self.dimy = 30
        self.x = 65
    def ileri(self,):
        if self.dimx <600:
          self.dimx += self.x

    def geri (self,):
        if self.dimx > 30:
          self.dimx -= self.x
          
    def yukari (self,):
        if self.dimy > 30:
            self.dimy -= self.x
            
    def asagi (self,):
        if self.dimy <400:
            self.dimy += self.x

class hareketlvl5():
    def __init__(self,avno):
        self.avno = avno
        self.dimx = 10
        self.dimy = 10
        self.yerles()       
    def ileri(self,x):
          for i in range (0,x):
            if self.dimx < 600 and self.dimy <60:                
                self.dimx+=60
            elif self.dimx >600 and self.dimy <360:
                self.dimy+=60
                
            elif self.dimx > 60 and self.dimy > 359:
                self.dimx -= 60
                
            elif self.dimx <61 and self.dimy > 59 :
                self.dimy -=60

class hareketlvl10():
    def __init__(self,avno):
        self.avno = avno
        self.dimx = 10
        self.dimy = 10
        self.yerles()       
    def ileri(self,x):
          for i in range (0,x):
            if self.dimx < 600 and self.dimy <60:                
                self.dimx+=60
            elif self.dimx >600 and self.dimy <360:
                self.dimy+=60
                
            elif self.dimx > 60 and self.dimy > 359:
                self.dimx -= 60
                
            elif self.dimx <61 and self.dimy > 59 :
                self.dimy -=60
