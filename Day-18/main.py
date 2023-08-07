from turtle import Turtle, Screen
import random

# timmy_the_turtle = Turtle()
#
# timmy_the_turtle.shape("circle")
#
# timmy_the_turtle.color("sea green")

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# Draw a Square

# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)

# def size(number_side):
#     color = ["red", "green", "blue", "purple"]
#     angle = 360 / number_side
#     for _ in range(number_side):
#         timmy_the_turtle.forward(90)
#         timmy_the_turtle.right(angle)
#     timmy_the_turtle.color(random.choice(color))
#
#
# for num in range(3,10):
#     size(num)
#
# import random
# from turtle import Turtle,Screen
# from random import Random
#
# import heroes
#
dagi = Turtle()
#
# dagi.shape("turtle")
# dagi.color("green")
# I can do with for loop
# Draw Rectangle
# for _ in range(4):
#     dagi.forward(100)
#     dagi.left(90)
#
# Draw line Exercise
#
# for _ in range(15):
#
#     dagi.pendown()
#     dagi.forward(10)
#     dagi.penup()
#     dagi.forward(10)

# Draw Different angle from rectangle to decagone
# triangle = 3
# angle = 360 / triangle
#
# for _ in range(triangle):
#     dagi.forward(100)
#     dagi.left(angle)
#
# rectangle = 4
# angle = 360 / rectangle
#
# for _ in range(rectangle):
#     dagi.forward(100)
#     dagi.left(angle)
# hexagon = 5
# angle = 360 / hexagon
#
# for _ in range(hexagon):
#     dagi.forward(100)
#     dagi.left(angle)
# def draw_shape(number_side):
color = ["blue", "aquamarine", "chocolate", "magenta", "blue violet", "orange"]
direction = [0, 90, 180, 270]
for _ in range(200):
    dagi.pensize(3)
    dagi.forward(30)
    dagi.setheading(random.choice(direction))
    dagi.color(random.choice(color))
    dagi.speed(10)

#     angle = 360 / number_side
#     for _ in range(number_side):
#         dagi.forward(100)
#         dagi.left(angle)
#     dagi.color(random.choice(color))
# for num in range(3,10):
#     draw_shape(num)

# draw random line
# this is the junk step to complet the challange
# dagi.forward(100)
# dagi.left(90)
# dagi.forward(100)
# dagi.left(90)
# dagi.forward(100)
# dagi.left(90)
# dagi.forward(100)
# dagi.left(90)
#
#
# dagi.left(90)
# dagi.left(90)
# dagi.back(100)
# dagi.left(90)
# dagi.left(90)
# dagi.left(90)
# dagi.forward(100)

screen = Screen()

screen.exitonclick()