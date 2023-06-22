def turn_right():
  turn_left()
  turn_left()
  turn_left()


def four_step():
  move()
  turn_right()
  move()
  turn_right()
  move()


def three_step():
  turn_left()
  move()
  turn_left()


move()
turn_left()
four_step()
three_step()
four_step()
three_step()
four_step()
three_step()
four_step()
three_step()
four_step()
three_step()
four_step()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for step in range(0,6):
    jump()
#count_num = 6