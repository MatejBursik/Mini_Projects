"""
At a white square, turn 90° clockwise, flip the color of the square, move forward one unit 
At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit
Black = 1, White = 0
orintation of the ant = pos[2] right=+x; up=-y; left=-x; down=+y
"""
import random

def clockwise(pos):
    if pos[2] == "up":
        pos[2] = "right"
    elif pos[2] == "right":
        pos[2] = "down"
    elif pos[2] == "down":
        pos[2] = "left"
    elif pos[2] == "left":
        pos[2] = "up"
    return pos

def counterclockwise(pos):
    if pos[2] == "up":
        pos[2] = "left"
    elif pos[2] == "right":
        pos[2] = "up"
    elif pos[2] == "down":
        pos[2] = "right"
    elif pos[2] == "left":
        pos[2] = "down"
    return pos


def move(pos,grid):
    if grid[pos[1]][pos[0]] == "0":

        grid[pos[1]][pos[0]] = "1" #change color
        pos = clockwise(pos) #change orientation of ant

        if pos[2] == "up":
            pos[1] -= 1
        elif pos[2] == "right":
            pos[0] +=1
        elif pos[2] == "down":
            pos[1] += 1
        elif pos[2] == "left":
            pos[0] -= 1

    elif grid[pos[1]][pos[0]] == "1":
        grid[pos[1]][pos[0]] = "0" #change color
        pos = counterclockwise(pos) #change orientation of ant

        if pos[2] == "up":
            pos[1] -= 1
        elif pos[2] == "right":
            pos[0] +=1
        elif pos[2] == "down":
            pos[1] += 1
        elif pos[2] == "left":
            pos[0] -= 1
    return([pos,grid])

def CalcOrientation(prevOrientation,currentOrientation):
    if prevOrientation == "up":
        if currentOrientation == "right":
            num = -90
        elif currentOrientation == "left":
            num = 90

    elif prevOrientation == "right":
        if currentOrientation == "down":
            num = -90
        elif currentOrientation == "up":
            num = 90

    elif prevOrientation == "down":
        if currentOrientation == "left":
            num = -90
        elif currentOrientation == "right":
            num = 90

    elif prevOrientation == "left":
        if currentOrientation == "up":
            num = -90
        elif currentOrientation == "down":
            num = 90
    
    return num


def RandomGen():
    zeroORone = random.randint(0,100)
    if zeroORone == 8:
        return "1"
    else:
        return "0"
