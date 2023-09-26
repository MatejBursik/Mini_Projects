import turtle

def sideLength(length):
    return (length**2/2)**0.5

def curve(length, direction, n):
    if n == 0:
        turtle.forward(length)
        return
    
    if direction == "right":
        turtle.right(45)
    else:
        turtle.left(45)

    curve(sideLength(length), "right", n-1)

    if direction == "right":
        turtle.right(90)
    else:
        turtle.left(90)

    curve(sideLength(length), "left", n-1)

    if direction == "right":
        turtle.right(45)
    else:
        turtle.left(45)

turtle.speed(0)
curve(300,"right",10)
input("press enter to end")
