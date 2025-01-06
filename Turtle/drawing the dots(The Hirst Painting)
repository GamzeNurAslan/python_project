import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(245, 245, 239), (203, 171, 118), (154, 143, 49), (140, 121, 22), (120, 32, 11), (238, 246, 239), (222, 145, 150), (94, 68, 76), (67, 131, 130), 
              (90, 38, 33), (1, 88, 85), (218, 203, 33), (205, 89, 91), (220, 206, 72), (203, 91, 90), (1, 84, 88), (242, 244, 248), (246, 235, 238), (141, 174, 159), 
              (71, 130, 133), (93, 43, 46), (228, 176, 162), (82, 35, 38), (94, 145, 136), (233, 164, 170), (3, 76, 68), (170, 202, 194), (3, 75, 83), (136, 163, 165), (99, 144, 146)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
      tim.dot(20, random.choice(color_list))
      tim.forward(50)

      if dot_count % 10 == 0:
         tim.setheading(90)
         tim.forward(50)
         tim.setheading(180)
         tim.forward(500)
         tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
