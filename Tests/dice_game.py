import random
import time

sum = 0
wins = 0
p2call = False
p1call = False
p1turn = True
p1sum = 0
p2sum = 0

print("Welcome to Dice Game PVP!")
time.sleep(1.25)
print(" ")
print("The goal is to get as close to 21 without going over. ")
time.sleep(3)
print("You can either hit or call, you and your opponent take turns. ")
time.sleep(3)
print("Hitting rolls a d6 and adds it to your sum. ")
time.sleep(2.5)
print("Calling locks your sum in, once the opponent calls, the person with higher wins.")
time.sleep(3.5)
print("Also you can hit with just 'h'")
time.sleep(2.75)
print("--------------------------------------------------------------- ")
if 1 == 1:
    while True:
        if p1sum > 21 or p2sum > 21:
            if p1sum > 21:
                print("")
                print("Player 2 Wins!")
                p2wins += 1
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True
            else:
                print(" ")
                print("Player 1 Wins!")
                p1wins += 1
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True
    
        elif p1sum == 21 or p2sum == 21:
            if p1sum == 21:
                print(" ")
                print("Player 1 Wins!")
                p1wins += 1
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True
            else:
                print(" ")
                print("Player 2 Wins!")
                p2wins += 1
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True

        elif p1call == True and p2call == True:
            if p1sum > p2sum:
                print(" ")
                print("Player 1 Wins!")
                p1wins += 1
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True
            elif p1sum == p2sum:
                print(" ")
                print("Its a tie!")
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True
            else:
                print(" ")
                print("Player 2 Wins!")
                p2wins += 1
                p1sum = 0
                p2sum = 0
                p1call = False
                p2call = False
                p1turn = True


        elif p1call == True:
            print("p2s turn")
        elif p2call == True:
            print("p1s turn")
        elif p1turn == True:
            print("p1s turn")
        else:
            print("p2s turn")-