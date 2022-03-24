from turtle import Turtle
import random


INITIAL_SPEED = 20
INC_IN_SPEED = 5
ANIMATION_SPEED = 0


def random_start_point():
    x_coor = random.randint(-450, 450)
    y_coor = random.randint(-200, 200)
    return x_coor, y_coor


def reset_point():
    x_coor = 450
    y_coor = random.randint(-200, 200)
    return x_coor, y_coor


def random_colour():
    return random.randint(1, 255)/255, random.randint(1, 255)/255, random.randint(1, 255)/255



class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = INITIAL_SPEED
        self.speed(0)
        self.shape("square")
        self.color(random_colour())
        self.penup()
        self.shapesize(1, 3)
        self.setheading(180)
        self.goto(random_start_point())
        self.speed(ANIMATION_SPEED)

    def move(self):
        self.forward(self.move_speed)

    def go_back(self):
        self.speed(0)
        self.goto(reset_point())
        self.speed(ANIMATION_SPEED)

    def inc_speed(self):
        self.move_speed += INC_IN_SPEED
