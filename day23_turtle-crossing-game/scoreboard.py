from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0 
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-260,260)
        self.write(f"Level: {self.level}", align="left", font=(FONT))

    def update_score(self):
        self.level+=1
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align='center', font=FONT)
