import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed(0)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(5,360,5):
    tim.color(randomColor())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)

screen = turtle.Screen()
screen.exitonclick()