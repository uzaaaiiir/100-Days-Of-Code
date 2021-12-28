from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_number = random.randint(1,6)
        if random_number==6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            y_position = random.randint(-250, 250)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)
                
    
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
        
    def change_speed(self):
        self.car_speed += MOVE_INCREMENT


