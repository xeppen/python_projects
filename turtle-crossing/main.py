from turtle import Screen

from car_manager import CarManager
from player import Player
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Pong")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_running = True
while game_is_running:
    time.sleep(0.1)
    manager.generate_car()

    # # Bounce on Y
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #     ball.bounce_y()

    manager.move()

    screen.update()

screen.exitonclick()