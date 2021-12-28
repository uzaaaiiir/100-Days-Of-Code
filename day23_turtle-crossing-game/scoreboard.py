from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        '''(Scoreboard)->None
        Initializes the scoreboard.
        '''
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1 
        self.update_scoreboard()

    def update_scoreboard(self):
        '''(Scoreboard)->None
        Writes the scoreboard to the screen with the current level.
        '''
        self.clear()
        self.goto(-260,260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        '''(Scoreboard)->None
        Updates the level attribute of Scoreboard object.
        '''
        self.level+=1
    
    def game_over(self):
        '''(Scoreboard)->None
        Writes "Game Over" to the screen if turtle player collides with a car.
        '''
        self.goto(0,0)
        self.write("Game Over", align='center', font=FONT)
