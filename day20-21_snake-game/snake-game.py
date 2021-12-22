import turtle 
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = turtle.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake.append(new_segment)
    
    def move(self):
        for seg in range(len(self.snake) -1, 0, -1):
                new_x = self.snake[seg- 1].xcor()
                new_y = self.snake[seg- 1].ycor()
                self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

# Main
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
screen.exitonclick()