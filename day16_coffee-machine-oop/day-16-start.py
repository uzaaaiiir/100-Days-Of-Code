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

table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pickachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

table.align = "l"
print(table)