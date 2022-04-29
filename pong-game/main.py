from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_running = True
while game_is_running:
    time.sleep(ball.move_speed)
    ball.move()

    # Bounce on Y
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce on r_ paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    # Bounce on l_ paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Right ball out
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # Right ball out
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

    screen.update()

screen.exitonclick()