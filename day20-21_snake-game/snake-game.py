import turtle 
import random

def move_forward():
    tim.forward(10)

def move_left():
    tim.left(90)

def move_right():
    tim.right(90)


tim = turtle.Turtle(shape="square")
tim.turtlesize(stretch_len=3, stretch_wid=0.5)
tim.penup()
screen = turtle.Screen()

screen.bgcolor("black")
tim.color("white")

screen.listen()
screen.onkeypress(fun = move_forward, key = "Up")
screen.onkeypress(fun = move_left, key = "Left")
screen.onkeypress(fun = move_right, key = "Right")
screen.onkeyrelease(fun = move_forward, key = "Up")

screen.exitonclick()