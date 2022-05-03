from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
            f.close();
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def clear_score(self):
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.reset()
