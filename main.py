import time
from turtle import Screen
from car import Car
from player import Player
from scoreboard import ScoreBoard

REFRESH_RATE = 0.0001
CAR_NUMBER = 10
screen = Screen()
screen.setup(height=600, width=900)
screen.title("Turtle crossing")
screen.bgcolor("white")
player = Player()
scoreboard = ScoreBoard()
car_list = []
for i in range(CAR_NUMBER):
    car = Car()
    car_list.append(car)

screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(REFRESH_RATE)
    screen.update()
    for car in car_list:
        if max(car.ycor(),player.ycor()) - min(car.ycor(),player.ycor()) < 20 and max(car.xcor(), player.xcor()) - min(car.xcor(), player.xcor()) < 50:
            game_is_on = False
            player.die()


        if car.xcor() < -500:
            car.go_back()
        car.move()
    screen.onkeypress(player.move, "w")

    if player.ycor() > 250:
        scoreboard.level_complete()
        player.go_back()
        for car in car_list:
            car.inc_speed()



screen.exitonclick()