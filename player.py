from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("turtle")
        self.shapesize(1)
        self.color("blue")
        self.penup()
        self.goto(0, -250)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def go_back(self):
        self.goto(0, -250)

    def die(self):
        self.hideturtle()
        self.goto(self.xcor() - 10, self.ycor() - 15)
        self.write(arg="x", font=("Courier", 40, "normal"), align="left")

