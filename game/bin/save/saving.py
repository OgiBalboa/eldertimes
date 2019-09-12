
class player():
        def __init__(self,name,avno):                           
            self.name = name
            self.avno = avno
        def default(self,):
            self.LEVEL = 1
            self.EXP = 0
            self.ATK = 1
            self.DEF = 15
            self.CRIT = 5  
            self.EXPR = 0
            self.nextlevel = False
            self.GOLD = 10
        def manuel(self,atk,DEF,crit,level,exp,gold):
               self.LEVEL = level
               self.EXP = exp
               self.ATK = atk
               self.DEF = DEF
               self.CRIT = crit
               self.GOLD = gold
        def levell(self,exp):
            self.EXP += exp
            self.NLVL = 5**self.LEVEL
            if self.EXP >= self.NLVL:
               self.LEVEL+=1
               self.nextlevel = True
               self.NLVL = 5**self.LEVEL
               self.EXP= 0
            self.EXPR = self.EXP*100/self.NLVL   

            """
oyuncu1 = player("Dovahkiin",3)
oyuncu1.default()
oyuncu1.manuel(1,22,22,1,50)
oyuncu1.levell(5)
print(oyuncu1.EXP)"""