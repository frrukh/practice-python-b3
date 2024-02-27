import random
class Dice:
    def roll(self):
        val1=random.randint(1,6)
        val2=random.randint(1,6)
        return val1,val2


dice=Dice()
print(dice.roll())