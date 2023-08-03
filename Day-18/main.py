from turtle import Turtle,Screen

import heroes

dagi = Turtle()

dagi.shape("turtle")
dagi.color("green")
# I can do with for loop
# Draw Rectangle
# for _ in range(4):
#     dagi.forward(100)
#     dagi.left(90)
#
# Draw line Exercise

for _ in range(15):

    dagi.pendown()
    dagi.forward(10)
    dagi.penup()
    dagi.forward(10)



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