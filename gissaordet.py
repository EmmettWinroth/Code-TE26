import time
time.sleep(0.2)
guessed = ""
wrongs = 6
exit = False
check = 1
correct = str(input("Enter a word to be guessed: "))
time.sleep(1)
correct.strip()
correct = correct.lower()
g1 = " "
g2 = " "
g3 = " "
g4 = " "
g5 = " "
g6 = " "
c = []
b = []

for i in range(20):
    print("")

for j in range(len(correct)):
    b.append(correct[j])
    c.append("_")

while exit != True:
    guess = input("Enter guess: ")
    guess = guess[0].lower()
    if guessed.find(guess[0]) != -1: 
        print("already guessed.")
    elif guess in correct:
        print("Correct!")
        guessed = guessed + guess[0].lower()
        for l in range(len(correct)):
            if b[l] == guess:
                del c[l]
                c.insert(l,guess)
    else:
        print("Wrong!")
        guessed = guessed + guess[0].lower()
        wrongs -= 1
        print(f"guesses left: {wrongs}")
    if wrongs ==5:
        g1 = "(: P)"
    elif wrongs ==4:
        g2 = "I"
    elif wrongs ==3:
        g3 = "\\"
    elif wrongs ==2:
        g4 = "/"
    elif wrongs ==1:
        g5 = "/"
    elif wrongs ==0:
        g6 = "\\"
    print("\n", guessed,"                               "
        "\n", c, "                                    "
        "\n" "       ____________                     "
        "\n" "      /            \\                   "
        "\n" "     I           ",g1,"                 "
        "\n" "     I          ",g4,"",g2,"",g3,"   "
        "\n" "     I         ",g4," ",g2," ",g3,"  "
        "\n" " /][][][][\\      ",g5," ",g6,"        " 
        "\n" "/][][][][][\\    ",g5,"   ",g6          )
    d = "".join(c)
    
    if d == correct:
        exit = True
    if wrongs <= 0:
        exit = True
if wrongs <= 0:
    print("You lost.")
else:
    print("You win!")
print(f"The word was: {correct}")