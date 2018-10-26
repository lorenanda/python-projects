import random

class Coin:
    def toss(self):
        res = random.uniform(0, 1)
        return res

coin = Coin()
heads = 0
tails = 0
for i in range(100):
    if coin.toss() < 0.5:
        heads += 1
    else:
        tails += 1

print("Heads count: ", heads)
print("Tails count: ", tails)