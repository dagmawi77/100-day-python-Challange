from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("circle")

timmy_the_turtle.color("sea green")

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

def size(number_side):
    color = ["red", "green", "blue", "purple"]
    angle = 360 / number_side
    for _ in range(number_side):
        timmy_the_turtle.forward(90)
        timmy_the_turtle.right(angle)
    timmy_the_turtle.color(random.choice(color))


for num in range(3,10):
    size(num)




screen = Screen()

screen.exitonclick()