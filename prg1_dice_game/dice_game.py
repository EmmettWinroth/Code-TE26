#todo: d6, count total, hit or call, get 21, >21=loss, ==21=win
#krav: minst 1 loop, några If- satser, minst 2 variabler, tydligt

import random
import time

print("Welcome to Dice Game!")
time.sleep(1)
print(" ")
time.sleep(1)
print("The goal is to get as close to 21 without going over. ")
time.sleep(1)
print("If you stop before 21, The House will generate a random number.")
time.sleep(1)
print("if you go over it you win. ")
time.sleep(1)
print("Get as many wins in a row as possible!")
time.sleep(1)
print("Also you can hit with just 'h'")

print("--------------------------------------------------------------- ")

sum = 0
wins = 0
while True:
    print(" ")
    print(f"Current sum is: {sum}")
    print(" ")
    if sum < 21:
        action = str(input("Hit or Call? "))
        if action == "Hit":
            sum = sum+random.randint(1,6)
            action = ""
        elif action == "hit":
            sum = sum + random.randint(1,6)
            action = ""
        elif action == "h":
            sum = sum + random.randint(1,6)
            action = ""
        else:
            if sum > random.randint(1,21):
                print(" ")
                print("You beat the house!")
                print(" ")
                quit = input("Quit now? Y/N ")
                if quit == "N":
                    sum = 0
                    wins = wins + 1
                    print(" ")
                    print(f"Current wins: {wins}")
                elif quit == "n":
                    sum = 0
                    wins = wins + 1
                    print(" ")
                    print(f"Current wins: {wins}")
                else:
                    print(f"You got ({wins}) wins.")
                    wins = 0
                    sum = 0
                    break
            elif sum == 21:
                print("You got exactly 21!")
                print(" ")
                wins == wins + 1
                sum = 0
                quittt = input("Quit now? Y/N ")
                if quittt == "N":
                    sum = 0
                    print(" ")
                    print(f"Current wins: {wins}")
                elif quittt == "n":
                    sum = 0
                    print(" ")
                    print(f"Current wins: {wins}")
                else:
                    print(f"You got ({wins}) wins.")
                    break                  
            else:
                print("The house had higher than you.")
                sum = 0
                print(" ")
                reshart = input("Restart now? (Y/N) ")
                if reshart == "Y":
                    sum = 0
                    wins = 0
                    print(" ")
                if reshart == "y":
                    sum = 0
                    wins = 0
                    print(" ")
                else:
                    print(f"You got ({wins}) wins.")
                    wins = 0
                    sum = 0
                    break
    elif sum == 21:
        print("You got exactly 21!")
        wins = wins + 1
        sum = 0
        quitt = input("Quit now? (Y/N)")
        if quitt == "N":
            sum = 0
            print(" ")
            print(f"Current wins: {wins}")
        elif quitt == "n":
            sum = 0
            print(" ")
            print(f"Current wins: {wins}")
        else:
            print(f"You got ({wins}) wins.")
            break
    else:
        re = input("Oops! You went over 21! restart? (Y/N)")
        if re == "Y":
            sum = 0
            wins = 0
        elif re == "y":
            sum = 0
            wins = 0
        else:
            print(f"You got ({wins}) wins.")
            break