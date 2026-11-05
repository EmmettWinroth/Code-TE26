reps = int(input("Enter how many numbers you'd like: "))
print("")
k = 3
mem = 2
out = [2]
for i in range(reps):
    out.append(mem*k)
    mem = mem*k
print(out)
print("")