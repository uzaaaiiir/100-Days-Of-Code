import turtle
import random

tim = turtle.Turtle()
directions = [0,90,180,270]
tim.pensize(15)
tim.speed(0)
turtle.colormode(255)


for _ in range(200):
    tim.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()