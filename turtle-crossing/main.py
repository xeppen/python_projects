from turtle import Screen
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

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_running = True
while game_is_running:
    time.sleep(0.1)

    # # Bounce on Y
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #     ball.bounce_y()
    #
    # # Bounce on r_ paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
    #     ball.bounce_x()
    #
    # # Bounce on l_ paddle
    # if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
    #     ball.bounce_x()
    #
    # # Right ball out
    # if ball.xcor() > 380:
    #     ball.reset_position()
    #     scoreboard.r_point()
    #
    # # Right ball out
    # if ball.xcor() < -380:
    #     ball.reset_position()
    #     scoreboard.l_point()

    screen.update()

screen.exitonclick()