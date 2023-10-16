COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
import turtle
from scoreboard import Scoreboard
from turtle import Turtle
from player import Player


class CarManager(Scoreboard):
    def __init__(self, screen):
        super().__init__(screen)
        self.car = turtle.Turtle()
        self.car.speed(0)
        self.car.shape("square")
        self.car.shapesize(1, 2)
        self.car.color("blue")
        self.car.penup()
        self.car.goto(450, random.randint(-280, 280))

        self.player_at_finish_line = Player.player_at_finish_line

        self.screen = screen
        self.cars = []

        self.morecars = 1
        

    def is_collision(self, t1, t2):
        distance = t1.distance(t2)
        distance2 = t2.distance(t1)
        return distance < 10 or distance2 < 20
    
    def spawn_car(self, create_random_cars, random_time, cars, number_of_cars):
        # print("spawn_car", len(cars), "number_of_cars", self.morecars)

        if len(cars) < self.morecars:
            self.screen.ontimer(create_random_cars, random_time)

        if len(cars) > self.morecars:
            cars.pop(0)



    def move_car(self, player):
        car = turtle.Turtle()
        car.speed(0)
        car.shape("square")
        car.shapesize(1, 2)
        car.color("blue")
        car.penup()
        car.goto(450, random.randint(-240, 240))

        def update_car():
            x = car.xcor()
            x -= random.randint(4, 6)
            car.setx(x)
            if car.xcor() < -300:
                randomY = random.randint(-240, 240)
                car.goto(280, randomY)
            

            if self.is_collision(player, car):
                player.goto(0, -280)
                player.reset_player()
                self.reset_score()
                self.morecars = 1

            if self.player_at_finish_line(player):
                self.increase_score()
                self.morecars += 1
                print("self.morecars", self.morecars)
                


            self.screen.update()
            self.screen.ontimer(update_car, 20)

        self.cars.append(car)
        update_car()
    
    def get_car(self):
        return self.car

    
