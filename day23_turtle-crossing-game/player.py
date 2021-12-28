from turtle import Turtle 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        '''(Player)->None
        Initializes the turtle player
        '''
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.reset_position()
    
    def move(self): 
        '''(Player)->None
        Moves the turtle player forward
        '''
        self.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        '''(Player)->None
        Moves the turtle player to the starting position
        '''
        self.goto(STARTING_POSITION)
    
    def is_at_finish(self):
        '''(Player)->bool
        Function returns True if the turtle player is at the finish line.
        Otherwise returns False.
        '''
        return self.ycor() > FINISH_LINE_Y
    
