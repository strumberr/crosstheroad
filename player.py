STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

import turtle


class Player(turtle.Turtle):
    def __init__(self, screen):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, -280)

        self.screen = screen

        self.player_speed = 15
    
    def playerSpeed(self):
        return self.player_speed
    
    def move_up(self):
        y = self.ycor()
        y += self.player_speed
        if y > 280:
            y = 280
        self.sety(y)


    def move_down(self):
        y = self.ycor()
        y -= self.player_speed
        if y < -280:
            y = -280
        self.sety(y)

    def reset_player(self):
        self.goto(STARTING_POSITION)


    def player_at_finish_line(self):
        if self.ycor() > 260:

            self.reset_player()

            return True
        else:
            return False

   
