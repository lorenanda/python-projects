import random

class Dice:
    def roll(self):
        res = random.randrange(0, 7)
        return res

dice = Dice()
print("Result:", dice.roll())