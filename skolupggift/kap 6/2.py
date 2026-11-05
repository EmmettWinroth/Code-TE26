inp = input("Enter numbers seperated by space: ")
lst = inp.split()
negs = 0
for i in range(len(lst)):
    if int(lst[i]) < 0:
        negs += 1
print(f"There are {negs} negative numbers.")