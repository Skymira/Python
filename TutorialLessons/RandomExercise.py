import random

class Dice:
    num = 0
    def roll(self):
        fnum = random.randint(1,6)
        snum = random.randint(1,6)
        return fnum, snum


dice1 = Dice()
print(dice1.roll())



