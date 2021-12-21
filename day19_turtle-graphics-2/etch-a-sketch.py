import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    '''(None)->None
    Moves turtle forward by 10
    '''
    tim.forward(10)

def move_backward():
    '''(None)->None
    Moves turtle backward by 10
    '''
    tim.backward(10)

def move_right():
    '''(None)->None
    Changes turtle angle right by 10 degrees
    '''
    tim.right(10)

def move_left():
    '''(None)->None
    Changes turtle angle left by 10 degrees
    '''
    tim.left(10)

def clear():
    '''(None)->None
    Clears the screen
    '''
    screen.resetscreen()

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(clear, "c")


screen.exitonclick()