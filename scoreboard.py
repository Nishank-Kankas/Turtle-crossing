from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 40, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("pink")
        self.level = 1
        self.show_score()


    def level_complete(self):
        self.level += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, 225)
        self.write(arg=f"Level: {self.level}", align=ALIGN, font=FONT)
