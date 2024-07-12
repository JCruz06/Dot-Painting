import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

raph = Turtle()
raph.hideturtle()
raph.speed('fastest')
raph.pu()

dot_size = 20
spacing = 50
grid_size = 10
start_x = -(spacing * (grid_size - 1)) / 2
start_y = -(spacing * (grid_size - 1)) / 2

# Set the starting position
raph.setpos(start_x, start_y)

# Draw the grid of dots
for space in range(grid_size):
    for dots in range(grid_size):
        raph.dot(dot_size, random.choice(color_list))
        raph.forward(spacing)
    raph.setx(start_x)
    raph.sety(raph.ycor() + spacing)



screen = Screen()
screen.exitonclick()