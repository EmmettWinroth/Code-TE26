import turtle
turtle.colormode(255)
turtle.speed(0)
turtle.penup()
turtle.right(90)
turtle.backward(640)
turtle.left(90)
turtle.backward(640)
turtle.right(90)
turtle.pendown()
r=155
g=0
b=155
for i in range(7):
    for j in range(107):
        turtle.forward(1080)
        turtle.left(90)
        turtle.forward(1)
        turtle.left(90)
        turtle.forward(1080)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
        turtle.color(r,g,b)
    if r==155 and b==155 and g==0:
        #if purple make blue
        r=0
        b=255
    elif r==00 and g==0 and b==255:
        #if blue make green
        r=0
        b=0
        g=255
    elif r==0 and g==255 and b==0:
        #if green make yellow
        g=255
        r=255
    elif r==255 and g==255 and b==0:
        #if yellow make orange
         g=155
    elif r==255 and g==155 and b==0:
        #if orange make red
        g=0
    turtle.color(r,g,b)

turtle.exitonclick()
