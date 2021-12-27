import turtle
import random

tim = turtle.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "red", "magenta", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.penup()
tim.goto(-100,100)
tim.pendown()

# Makes all Polygons from 3 sides to 10 sides
for i in range(3,25):
    tim.color(random.choice(colours))
    for j in range(i):
        tim.forward(100)
        tim.right(360/i)

screen = turtle.Screen()
screen.exitonclick()