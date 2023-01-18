# Hirst painting
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()


color_list = [(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47),
              (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164),
              (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10), (18, 18, 43),
              (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168), (81, 234, 202),
              (61, 233, 241), (5, 67, 42)]

timmy.penup()
timmy.setpos(-200, -300)
for i in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.setpos(-200, timmy.ycor() + 50)


screen = Screen()
screen.exitonclick()
