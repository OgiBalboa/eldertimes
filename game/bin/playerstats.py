# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:35:06 2019

@author: fener_000
"""
import tkinter
class newplayerstat():
    def __init__(self,name,powerstat,agistat,intstat):
        self.name = name
        self.powerstat = powerstat
        self.agistat = agistat
        self.intstat = intstat
        self.statp = 4
        self.tempstatp = 0
        self.avno = 0
    def defaultstat(self):
        self.powerstat = 5
        self.agistat = 5
        self.intstat = 5
        self.statp = 4
    def givestatp(self,statp):
        self.statp = statp
    def avatarno(self,x):
        self.avno = x
    #---------------------------------------------------------POWER----------------------------------------------------------------    
    def powerup(self):
        if self.statp > 0:
            self.statp-=1
            self.tempstatp+=1
            self.powerstat+=1
    def powerdown(self):
        if self.tempstatp != self.statp:
            self.statp +=1
            self.powerstat  -=1
            if self.tempstatp == self.statp:
                self.tempstatp = 0
    #---------------------------------------------------------AGILITY----------------------------------------------------------------
    def agiup(self):
        if self.statp > 0:
                self.statp-=1
                self.tempstatp+=1
                self.agistat+=1
    def agidown(self):
        if self.tempstatp != self.statp:
            self.statp +=1
            self.agistat  -=1
            if self.tempstatp == self.statp:
                self.tempstatp = 0
    #-----------------------------------------------------INTELLIGENCE----------------------------------------------------------------
    def intup(self):
        if self.statp > 0:
            self.statp-=1
            self.tempstatp+=1
            self.intstat+=1


    def intdown(self):
        if self.tempstatp != self.statp:
            self.statp +=1
            self.intstat -=1
            if self.tempstatp == self.statp:
                self.tempstatp = 0