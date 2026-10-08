#todo: d6, count total, hit or call, get 21, >21=loss, ==21=win
#krav: minst 1 loop, några If- satser, minst 2 variabler, tydligt

import random
import time
sum = 0
wins = 0
p2call = False
p1call = False
playerturn = 1
p1sum = 0
p2sum = 0
def resetvars():
    sum = 0
    wins = 0
    p2call = False
    p1call = False
    playerturn = 1
    p1sum = 0
    p2sum = 0

while True:
    print("Gamemodes: PVE, PVP")
    print(" ")
    gamemode = str.lower(input("Please select a gamemode: "))
    print(" ")
    resetvars()

    if gamemode == "pve":
        print("")
        print("Welcome to Dice Game PVE!")
        time.sleep(1)
        print(" ")
    
        print("The goal is to get as close to 21 without going over. ")
        time.sleep(3)
        print("If you stop before 21, The House will generate a random number.")
        time.sleep(3)
        print("if you go over it you win. ")
        time.sleep(2.75)
        print("Get as many wins in a row as possible!")
        time.sleep(2.25)
        print("Also you can hit with just 'h'")
        time.sleep(2.75)
        
        print("--------------------------------------------------------------- ")
        
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
                print(" ")
                if re == "Y":
                    sum = 0
                    wins = 0
                elif re == "y":
                    sum = 0
                    wins = 0
                else:
                    print(f"You got ({wins}) wins.")
                    break
                    print("")

    #PVP STARTS HERE
    else:
            print("Welcome to Dice Game PVP!")
            time.sleep(1)
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

            while True:

                if p1sum == 21 or p2sum == 21:
                    if p1sum == 21:
                        p1wins += 1
                        print("")
                        print("PLAYER 1 WIN")
                        print("")
                        playerturn = 1
                        p1sum = 0
                        p2sum = 0
                elif p1sum > 21 or p2sum > 21:
                    #give win to who didnt bust
                elif p1call == True and p2call == True:
                    #compare and choose victor
                elif p1call == True:
                    #p2 turn
                elif p2call == True:
                    #p1 turn
                elif playerturn == 1:
                    #p1 turn
                elif playerturn != 1:




                if playerturn == 1 and p1call == False or playerturn == 0 and p2call == True:
                    print("Player 1's turn. ")
                    print(f"P1 sum: {p1sum} ")
                    print(" ")
                    hitcall = str.lower(input("Hit or call: "))
                    print(" ")
                    if hitcall == "hit" or hitcall == "h":
                        p1sum = p1sum + random.randint(1,6)
                        playerturn = 0
                    else:
                        p1call = True
                        playerturn = 0

                elif playerturn == 0 and p2call == False or playerturn == 1 and p1call == True:
                    print("Player 2's turn. ")
                    print(f"P2 sum: {p2sum} ")
                    print(" ")
                    hitcall = str.lower(input("Hit or call: "))
                    print(" ")
                    if hitcall == "hit" or hitcall == "h":
                        p2sum = p2sum + random.randint(1,6)
                        playerturn = 1
                    else:
                        p1call = True
                        playerturn = 1
                elif p1call == True and p2call == True:
                    if p1sum < p2sum:
                        print("Player 2 Wins!")
                        p2wins += 1
                        print("Current wins:")
                        print(f"P1: {p1wins}")
                        print(f"P2: {p2wins}")
                        print(" ")
                    elif p1sum == p2sum:
                        print("It's a Tie!")
                    else:
                        print("Player 1 Wins!")
                        p1wins += 1
                        print("Current wins:")
                        print(f"P1: {p1wins}")
                        print(f"P2: {p2wins}")
                        print(" ")
                    