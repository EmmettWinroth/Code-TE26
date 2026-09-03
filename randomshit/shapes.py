import turtle as turtle
turtle.hideturtle() 
turtle.penup()
turtle.backward(320)
turtle.pendown()
def scooch():
    turtle.left(179.9)
    turtle.forward(150)
    turtle.right(179.9)
    turtle.forward(150)
    
R = 255
G = 0
B = 0
turtle.speed(0)
turtle.colormode(255)
turtle.color((R,G,B))
turtle.right(90)
for i in range(255):
    scooch()
    scooch()
    R -= 1
    G += 1
    turtle.color((R,G,B))

for i in range(255):
    scooch()
    scooch()
    G -= 1
    B += 1
    turtle.color((R,G,B))
turtle.speed(1)
while True:
    turtle.left(1)