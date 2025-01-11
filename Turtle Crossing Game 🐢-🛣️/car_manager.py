import random
import time
from turtle import Turtle, Screen


COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "gold", "lightBlue", "brown", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
screen = Screen()

class CarManager:
    def __init__(self):
        self.arabalar = []
        self.create_car_interval = 6
        self.counter = 0
        self.car_speed = STARTING_MOVE_DISTANCE

    def araba_olustur(self):
        araba = Turtle()
        araba.shape("square")
        araba.shapesize(stretch_wid=1, stretch_len=2)
        araba.color(random.choice(COLORS))
        araba.penup()

        y_pos = random.randint(-250 + 50, 250 - 50)
        araba.goto(300, y_pos)
        self.arabalar.append(araba)

    def hareket_et(self):
        for araba in self.arabalar:
            araba.setx(araba.xcor() - self.car_speed)
            if araba.xcor() < -300:
                araba.goto(300, random.randint(-250 + 50, 250 - 50))

    def oyun_dongusu(self):
        self.counter += 1
        if self.counter % self.create_car_interval == 0:
            self.araba_olustur()
        self.hareket_et()

    def kontrol_et(self, player):
        for araba in self.arabalar:
            if araba.distance(player.kaplumbaga) < 20:
                return True
        return False

    def hiz_arttir(self):
        self.car_speed += MOVE_INCREMENT
