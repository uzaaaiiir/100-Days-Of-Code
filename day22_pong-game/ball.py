from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(0,0)
    
    def move(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor + 0.3, y_cor + 0.2)
