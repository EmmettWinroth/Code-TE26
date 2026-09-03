import turtle
turtle.speed(0)
turtle.colormode(255)

def cool_circle (str):
    facing = float(0)
    waypoint = 0
    turtle.position(waypoint)
    turtle.
    print(str)
    ang = int(45)
    leng = float(0.5)
    R = 0
    G = 0
    B = 255
    for i in range(600):
        turtle.color(R,G,B)
        turtle.forward(leng)
        turtle.right(ang)
        ang -= 0.01
        leng += 0.05
        if R == 255:
            G = 255
            R = 0
        elif G == 255:
            B=255
            G=0
        elif B == 255:
            R=255
            B=0
    turtle.goto(waypoint)
    return()
turtle.pendown
coolcircles = int(input("yo how many broski: "))
print("aight i gotchu brochacho B)")
angle = 360/coolcircles
lengthy = 1000/coolcircles

for j in range (coolcircles):
    turtle.left(angle)
    turtle.forward(lengthy)
    cool_circle("here my man")