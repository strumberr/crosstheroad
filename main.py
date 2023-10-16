import turtle
import random


from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []

player = Player(screen)
player_speed = player.playerSpeed()

carManager = CarManager(screen)

def create_random_cars():
    print("create_random_cars")
    

    carManager.move_car(player)
        
    carManager.get_car()

    interval = random.randint(1000, 2000) // carManager.morecars
    carManager.spawn_car(create_random_cars, interval, cars, number_of_cars=5)


    

move_up = player.move_up
move_down = player.move_down

screen.listen()
screen.onkeypress(move_up, "w")



create_random_cars()

screen.mainloop()