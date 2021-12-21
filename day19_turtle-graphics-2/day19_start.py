from turtle import Turtle, Screen

def move_forward():
    tim.forward(10)

tim = Turtle()

screen = Screen()
screen.listen()
screen.onkey(move_forward, "space") 
# When we use a function as an argument, don't add the parantheses
    # Only want to trigger the function when the space is pressed 
screen.exitonclick()