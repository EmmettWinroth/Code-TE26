inp = str(input("enter text: "))
skip = ["å","ö","ä","u","o","i","e","a","\t"," "]
work = []

for i in range(len(inp)):
    work.append(inp[i])

for j in range(len(inp)):
    if work[j] not in skip:
        work[j] = work[j]+"o"+work[j]

out = "".join(work)

print(out)