import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player, cars, scoreboard
turtle_player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Move player forward using Up key
screen.listen()
screen.onkeypress(fun=turtle_player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Create and move cars 
    cars.create_car()
    cars.move_cars()

    # Detect collissions with cars
    for car in cars.all_cars: 
        if turtle_player.distance(car) < 20:
            game_is_on = False 
            scoreboard.game_over()
    

    # When player reaches the end, reset position, update score, change car speed
    if turtle_player.is_at_finish():
        turtle_player.reset_position()
        cars.change_speed()

        # Update Score and scoreboard
        scoreboard.update_score()
        scoreboard.update_scoreboard()


screen.exitonclick()