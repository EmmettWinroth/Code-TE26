import turtle
#making vals and importing turt

linesPerColor = int(0)

R = int(0)
G = int(0)
B = int(0)
turtle.colormode(255)
#rgb time

#placing the turt
turtle.speed(0)
turtle.penup()
turtle.right(90)
turtle.backward(640)
turtle.left(90)
turtle.backward(640)
turtle.right(90)
turtle.pendown()
#it is now in top right of the window

color_List = list()
#more vals
stripeNum = int(input("How many stripes?: "))
for i in range (stripeNum):
    color_List.append(str(input(f"Enter color number {i+1}: ")))
#get a list of colors and amount of stripes

def setColor(col,R,G,B):
    #colors to add: purple,red,blue,yellow,green,orange,black,white
    if col == "red":
        R = 255
        G = 0
        B = 0
        return R,G,B
    elif col == "blue":
        R = 0
        G = 0
        B = 255
        return R,G,B        
    elif col == "green":
        R = 0
        G = 255
        B = 0
        return R,G,B
    elif col == "yellow":
        R = 255
        G = 255
        B = 0
        return R,G,B
    elif col == "purple":
        R = 155
        G = 0
        B = 155
        return R,G,B
    elif col == "orange":
        R = 255
        G = 155
        B = 0
        return R,G,B
    elif col == "black":
        R = 0
        G = 0
        B = 0
        return R,G,B
#gives rgbs for respective colors inputted earlier
for j in range(stripeNum):
    R,G,B = setColor(color_List[j],R,G,B)
    print(R)
    print(G)
    print(B)


#time for filling shi-stuff.
linesPerColor = 640/stripeNum
print(int(linesPerColor))
for n in range(stripeNum):
    R,G,B = setColor(color_List[n],R,G,B)
    turtle.color(R,G,B)
    for m in range(int(linesPerColor)):
        turtle.forward(1080)
        turtle.left(90)
        turtle.forward(1)
        turtle.left(90)
        turtle.forward(1080)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
#wait dont end instantly i need to flex my nerdiness
turtle.exitonclick()