import datetime

print("Hello World!")
print("Jag heter Emmett.")
namn = input("Vad heter du? ")
if namn == "Emmett":
    print("Vi har samma namn!")
else:
    print(f"Hej, {namn}!")

Q = input("Vad vill du veta? ")

if Q == "datum":
    date = datetime.date.today()
    print(f"Dagens datum är: {date}")
elif Q == "tid":
    time = datetime.datetime.now().time()
    print(f"Dagens tid är: {time}")
