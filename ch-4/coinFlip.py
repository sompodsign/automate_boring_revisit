import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    coinFlip = []
    # Code that creates a list of 100 heads or tails values.
    for i in range(100):
        coinFlip.append(random.randint(0,1))
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(1, len(coinFlip)):
        if coinFlip[i:i+6] == [0,0,0,0,0,0]:
            numberOfStreaks += 1
        elif coinFlip[i:i+6] == [1,1,1,1,1,1]:
            numberOfStreaks += 1
            
            
print('Chance of streak: %s%%' % (numberOfStreaks/10000))
