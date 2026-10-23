import turtle
from operator import length_hint

# -- setup --
s = turtle.Screen()
s.bgcolor("lightgreen")
t = turtle.Turtle()

# -- functions --

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in  range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)

def drawSpirel(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size = size + 2
def drawEquilatriangle(someturtle, somesize):
    drawPoly(someturtle,3,somesize)

def drawStar(someturtle,size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

def drawSprite(someturtle, length, legs):
    angle = 360 / legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)




# Exercise 1
# t.pencolor("hotpink")
# t.pensize(3)
# drawPoly(t, 8, 50)

# Exercise 2
# t.pencolor("darkblue")
# t.speed(100)
# t.pensize(2)
# for i in range(20):
#     drawPoly(t, 4, 100)
#     t.left(18)

# # Exercise 3
# t.penup()
# t.goto(-150,0)
# t.pendown()
# t.pencolor("darkblue")
# t.pensize(2)
# t.speed(20)
# drawSpirel(t, 90)
# t.penup()
# t.goto(150,0)
# t.pendown()
# drawSpirel(t, 89)

# Exercise 4
# drawEquilatriangle(t, 100)

# Exercise 5
# t.color("hotpink")
# t.pensize(4)
#
# for i in range(5):
#     drawStar(t, 50)
#     t.penup()
#     t.forward(350)
#     t.right(144)
#     t.pendown()
# Exercise 6
drawSprite(t, 120, 15)



# -- finish --
s.exitonclick()