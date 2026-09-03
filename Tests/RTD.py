from math import *
import random
#RTD stands for Roll The Dice
numd = input("How many dice to roll: ")
numd = int(numd)
dnum = input("What kind of die to roll: ")
dnum = int(dnum)

for i in range(numd):
    randomint = random.randint(1, dnum)
    print(randomint)