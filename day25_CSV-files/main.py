import turtle 
import pandas

FONT = ("Courier", 5, "bold")

def write_to_screen(x,y, state):
    writer.penup()
    writer.goto(x,y)
    writer.write(state, align="left", font=FONT)

writer = turtle.Turtle()
writer.hideturtle()
tim = turtle.Turtle()
screen = turtle.Screen()
screen.title("US States Game")
# screen.setup(width=725, height=491)
screen.addshape("blank_states_img.gif")
tim.shape("blank_states_img.gif")


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
print(states)

count = 0
total = 50

while count <= 50:
    user_input = screen.textinput(title=f"States {count}/{total}", prompt="Enter a State:")
    
    if user_input.title() in states:
        states.remove(user_input.title())
        state = data[data.state==user_input.title()]
        print(state)
        x = state.x
        y = state.y
        write_to_screen(int(x), int(y), user_input.title())
        count+=1
    


turtle.mainloop()
