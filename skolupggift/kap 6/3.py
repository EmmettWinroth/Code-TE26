import random
work = [0]
work[0] = random.randint(1,1000)
mem = 0
for i in range(99):
    work.append(random.randint(1,1000))
mn = min(work)
mx = max(work)
for j in range(100):
    mem = mem + work.pop()
mem = mem/100
print("Lowest # is: ", mn)
print("Highest # is: ", mx)
print("Average # is: ", mem)
