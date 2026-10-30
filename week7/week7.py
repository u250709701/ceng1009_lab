# def sumTo(n):
#     return (n * (n + 1)) / 2
#
# print(sumTo(10))  # 55
import numbers
import turtle


# import turtle
#
# def star(n):
#     if n < 3 or n % 2 == 0:
#         print("n must be an odd number greater than or equal to 3")
#         return
#
#     for i in range(n):
#         turtle.forward(100)
#         turtle.right(180 - 180/n)
#
#     turtle.done()
#
# star(5)
# wn.exitonclick()
# def sumTo(n):
#     total = 0
#
#     for i in range(1, n + 1):
#         total += i
#
#     return total
#
# print(sumTo(10))
# n  = int(sumTo(10))
# print("Sum is", sumTo(n))

# import math
#
# def mySqrt(x):
#     guess = x / 2
#     for i  in range(20):
#         guess = (1/2) * (guess + x / guess)
#     return guess
#
#
# n = int(input("Enter a positive integer: "))
# print("The result is ",mySqrt(n))
# print("The result is ", math.sqrt(n))


# def drawSprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSprite(t, 8, 20)
#         t.forward(size)
#         t.left(90)
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("pink")
# t.pensize(2)
# t.speed(4)
# fancySquare(t, 100)
# wn.exitonclick()

# import turtle
# def drawTip(t, size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size / 2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size / 2)
#     t.right(90)
#     t.end_fill()
# def drawSpriteWithTips(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         drawTip(someturtle, 10)
#         someturtle.backward(length)
#         someturtle.left(angle)
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t,8, 20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(2)
# fancySquare(t, 100)
# wn.exitonclick()

# def checkSign(x):
#     if x > 0:
#         return "positive"
#     elif x < 0:
#         return "negative"
#     else:
#         return "zero"
# num = [-7 , 5, 0]
# for number in num:
#     print(number, "is", checkSign(number))
# n = int(input("Enter a number: "))
# print(checkSign(n))

# import turtle
#
# def drawBar(t, height, label, distance):
#     t.fillcolor("red")
#     t.pencolor("blue")
#
#     t.begin_fill()
#
#     t.left(90)
#     t.forward(height)
#
#     # Write label above the bar
#     t.penup()
#     t.forward(distance)
#     t.pencolor("red")
#     t.write(str(label), align="center", font=("Arial", 8, "normal"))
#
#     t.backward(distance)
#     t.pendown()
#     t.pencolor("blue")
#
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#
#     t.end_fill()
#
#     t.penup()
#     t.forward(0)
#     t.pendown()
#
#
# def barChart(data):
#     t = turtle.Turtle()
#     t.speed(5)
#
#     turtle.bgcolor("lightgreen")
#
#     t.penup()
#     t.goto(-150, -100)
#     t.pendown()
#
#     maxheight = max(data)
#     distance = (maxheight + 10) * 0.03
#
#     for value in data:
#         drawBar(t, value, value, distance)
#
#     turtle.done()
#
#
# data = [48, 117, 200, 240, 160, 260, 220]
#
# barChart(data)