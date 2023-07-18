# from turtle import Turtle,Screen
# # import another_module
# #
# # print(another_module.another_variable)
#
# dagi = Turtle()
# print(dagi)
# dagi.shape("turtle")
# dagi.color("red")
# dagi.position()
# dagi.forward(300)
# dagi.speed(10)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from  prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pockman Name", ["Pickacu", "Squity", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align="r"
print(table)


