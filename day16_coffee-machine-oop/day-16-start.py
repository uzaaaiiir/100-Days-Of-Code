import turtle 
import prettytable 

timmy = turtle.Turtle()

# Prints object and location in memory
print(timmy)

my_screen = turtle.Screen()
print(my_screen.canvheight)

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen.exitonclick()