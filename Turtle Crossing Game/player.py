from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.kaplumbaga = Turtle()
        self.kaplumbaga.shape("turtle")
        self.kaplumbaga.color("white")
        self.kaplumbaga.penup()
        self.kaplumbaga.goto(STARTING_POSITION)
        self.kaplumbaga.setheading(90)

    def yukari_git(self):
        self.kaplumbaga.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.kaplumbaga.ycor() >= FINISH_LINE_Y:
            self.kaplumbaga.goto(STARTING_POSITION)
            return True
        return False
