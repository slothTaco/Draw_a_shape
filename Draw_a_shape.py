#Draw a shape

from turtle import *
length = 10

#change amount of sides, angle to alter shape

sides = 3


angle = 360 / sides

for number in range(1,5):
    for side in range(1,sides+1):
        forward (number * length)
        left (angle)

    # Move to next shape
    penup()
    forward(length*4)
    pendown()
