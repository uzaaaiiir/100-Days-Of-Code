import turtle 
import pandas

# Create a screen writer turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Creating screen with gif image 
tim = turtle.Turtle()
screen = turtle.Screen()
screen.title("US States Game")
# screen.setup(width=725, height=491)
screen.addshape("blank_states_img.gif")
tim.shape("blank_states_img.gif")

# Reading State Data
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

count = 0
total = 50

while count < 50:
    user_input = screen.textinput(title=f"States {count}/{total}", prompt="Enter a State:").title()
    
    if user_input == "Exit":
        # States to learn .csv 
        states = pandas.DataFrame(states)
        states.to_csv("US_states.csv")
        break

    if user_input in states:
        states.remove(user_input)
        state = data[data.state==user_input]
        writer.goto(int(state.x), int(state.y))
        writer.write(user_input)
        count+=1



screen.exitonclick()
