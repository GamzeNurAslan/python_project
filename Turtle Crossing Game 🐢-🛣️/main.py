import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.yukari_git, "Up")
screen.listen()


def oyun_dongusu():
    car_manager.oyun_dongusu()
    if car_manager.kontrol_et(player):
        scoreboard.game_over()
        return


    if player.finish_line():
        car_manager.hiz_arttir()
        scoreboard.increase_level()


    screen.update()
    screen.ontimer(oyun_dongusu, 100)


oyun_dongusu()
screen.mainloop()

