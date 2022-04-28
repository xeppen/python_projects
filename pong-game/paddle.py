from turtle import Turtle

class Paddle(Turtle):

    def __int__(self):
        super().__init__()
        self.shape("square")
        self.color("white")