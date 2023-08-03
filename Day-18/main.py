from turtle import Turtle,Screen

dagi = Turtle()

dagi.shape("turtle")
dagi.color("green")
# I can do with for loop

for _ in range(4):
    dagi.forward(100)
    dagi.left(90)

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