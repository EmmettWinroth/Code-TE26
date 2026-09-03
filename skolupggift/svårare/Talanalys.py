Inp = list()
for i in range (5):
    Inp.append(int(input(f"ge heltal {i+1}: ")))
print("")
print(f"Dina svar: {Inp}")
print("")
def oddoreven(input):
    raw = int(input)
    test = raw % 2
    if test == 1:
        return("Odd")
    else:
        return("Even")

odds = 0
evens = 0
for j in range(5):
    if oddoreven(Inp[j]) == "Odd":
        odds = odds + 1
    else:
        evens = evens + 1
print(f"{odds} tal är udda, {evens} tal är jämna.")
medel = (Inp[0] + Inp[1] + Inp[2] + Inp[3] + Inp[4]) / 5
print(f"Medelvärdet är lika med: {medel}")
largest = max(Inp)
smallest = min(Inp)
print(f"Största talet är: {largest}, minsta talet är: {smallest}")