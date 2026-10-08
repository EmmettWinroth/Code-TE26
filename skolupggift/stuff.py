a = "561231-4913"
double = True
b = []
digits = ["1","2","3","4","4","5","6","7","8","9","0"]
for i in range(len(a)):
    b.append(a[i])
for j in range(len(a)):
    if b[j] in digits:
        if double == True:
            b[j] = int(b[j])
            b[j] = b[j]*2
            double = False
            b[j] = str(b[j])
        else:
            double = True
control = b[-1]
del b[-1]
b = "".join(b)
b = b.replace("-","")
c = 0
for l in range(len(b)):
    c = c+int(b[l])

c //= 10

if c != control:
    print("this is valid")
else:
    print("this isnt valid")