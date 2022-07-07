import turtle
import random
print("""To move, use the buttons: ")
w - move up
s - move down
d - move right
a - move left
e - invisibility
g - Change color to selected (0,1,2,3,4)
f - To change the color of the turtle to random """)
t = turtle.Turtle()
t.shape('turtle')
t.screen.setup(1000, 1000)
while True:
    q = str(input())
    if q == "g":                                             # смена цвета
        a = random.randint(0, 5)
        if a == 1:
            color = str("green")
        elif a == 2:
            color = str("orange")
        elif a == 3:
            color = str("magenta")
        elif a == 0:
            color = str("pink")
        else:
            color = str("blue")
        t.color(color)
    if q == "f":
        a = random.randint(0, 5)
        if a == 1:
            color = str("green")
        elif a == 2:
            color = str("orange")
        elif a == 3:
            color = str("magenta")
        elif a == 0:
            color = str("pink")
        else:
            color = str("blue")
        t.color(color)
    if q == "w":
        print('move 50 pixels forward')
        t.forward(50)
    if q == "s":
        print('move 50 pixels back')
        t.backward(50)
    if q == "d":
        print('turn right 45°')
        t.right(45)
    if q == "a":
        print('turn left 45°')
        t.left(45)
    else:
        print("This action is not yet written")
turtle.exitonclick()