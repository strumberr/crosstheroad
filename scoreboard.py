FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard():
    def __init__(self, screen):

        self.screen = screen

        self.score_text = Turtle()
        self.score = 0
        self.score_text.penup()
        self.score_text.goto(-280, 250)
        self.score_text.hideturtle()
        self.score_text.color("black")

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score_text.clear()
        self.score_text.write(f"Level: {self.score}", align="left", font=FONT)
