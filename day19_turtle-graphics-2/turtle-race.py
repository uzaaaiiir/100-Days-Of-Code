import turtle
import random

# Creating screen
is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)

# User input
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

# Colors and turtles list
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []

# Creates turtles and adds it to a list
for i in range(len(colors)):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    n = 33.3
    new_turtle.goto(x = -230, y = -100 + i*n)
    turtles.append(new_turtle)

# The race begins 
if user_bet:
    is_race_on = True

# Runs the race 
while is_race_on:

    # Each turtle moves forward 
    for each_turtle in turtles:

        # When turtle reaches end, check if it wins 
        if each_turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        # Moving each turtle forward by random distance
        random_distance = random.randint(0,10)
        each_turtle.forward(random_distance)

# Closing screen when clicked
screen.exitonclick()
