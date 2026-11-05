import random
from statistics import multimode
start = []
evens = []
odds = []
mode = 0

for i in range(20):
    start.append(random.randint(1,50))
    if start[i] % 2 == 0:
        evens.append(start[i])
    else:
        odds.append(start[i])

mode = multimode(start)

print(f"Full list: {start}")
print(f"Even integers: {evens}")
print(f"Odd integeres: {odds}")
print(f"Mode(s): {mode}")