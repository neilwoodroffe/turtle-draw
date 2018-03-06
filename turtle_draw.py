#Turtle draw game
import turtle
import random
#import os
import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values

#set up the screen
turtle.setup(1000, 800)
turtle.delay(delay=None)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Draw")
colours = ["cyan", "gray", "purple", "brown", "red", "blue", "yellow", "orange", "green", "pink", "white", "darkgreen", "darkcyan", "crimson", "darkblue", "gold", "darkred", "lime", "darkorange", "deeppink", "dimgray", "olive", "maroon"]

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Heading
heading = turtle.Turtle()
heading.speed(0)
heading.penup()
heading.setposition(0, 315)
heading.pendown()
heading.color("orange")
heading.write("Turtle Draw", align="center",font=("Arial", 16, "normal"))
heading.hideturtle()

#Info
info = turtle.Turtle()
info.hideturtle()
info.speed(0)
info.penup()
info.setposition(-485, 290)
info.pendown()
info.color("light blue")
info.write("Arrow keys = N,S,E,W", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 270)
info.pendown()
info.color("light blue")
info.write("W = forward", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 250)
info.pendown()
info.color("light blue")
info.write("Q = flash forward", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 230)
info.pendown()
info.color("light blue")
info.write("A = turn left", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 210)
info.pendown()
info.color("light blue")
info.write("D = turn right", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 190)
info.pendown()
info.color("light blue")
info.write("C = draw circle", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 170)
info.pendown()
info.color("light blue")
info.write("T = draw Triangle", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 150)
info.pendown()
info.color("light blue")
info.write("S = draw star", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 130)
info.pendown()
info.color("light blue")
info.write("B = draw square", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 110)
info.pendown()
info.color("light blue")
info.write("R = draw rectangle", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 90)
info.pendown()
info.color("light blue")
info.write("H = draw hexagon", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 70)
info.pendown()
info.color("light blue")
info.write("F = draw flower", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 50)
info.pendown()
info.color("light blue")
info.write("Space = random colour", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 30)
info.pendown()
info.color("light blue")
info.write("P = penup", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, 10)
info.pendown()
info.color("light blue")
info.write("L = pendown", font=("Arial", 10, "normal"))
info.penup()
info.setposition(-485, -10)
info.pendown()
info.color("light blue")
info.write("1-4 = line thickness", font=("Arial", 10, "normal"))

#Create the player turtle
player = turtle.Turtle()
player.color("green")
player.shape("turtle")
player.speed(0)
player.setheading(90)

playerspeed = 5


#Move the player
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    player.setheading(180)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    player.setheading(0)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    player.sety(y)
    player.setheading(90)
    
def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)
    player.setheading(270)

#change color
def change_colour():
    player.color(random.choice(colours))

#Turtle circle
def player_circle():
    player.circle(25)

#Turtle star
def player_star():
    for i in range(5):
        player.forward(50)
        player.right(144)

#Turtle square
def player_box():
    for i in range(4):
        player.forward(50)
        player.right(90)

#Turtle triangle
def player_triangle():
    for i in range(3):
        player.forward(50)
        player.right(120)

#Turtle rectangle
def player_rectangle():
    for i in range(2):
        player.forward(50)
        player.right(90)
        player.forward(100)
        player.right(90)

#Turtle hexagon
def player_hexagon():
    num_sides = 6
    side_length = 30
    angle = 360.0 / num_sides 

    for i in range(num_sides):
        player.forward(side_length)
        player.right(angle)

#Turtle flower
def player_flower():
    for i in range(50):
        player.forward(50)
        player.left(123)

#Turtle forward
def player_forward():
    player.forward(5)
    x = player.xcor()
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)
    y = player.ycor()
    if y < -280:
        y = -280
    if y > 280:
        y = 280
    player.sety(y)

#Turtle color forward
def player_flash():
    player.forward(5)
    x = player.xcor()
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)
    y = player.ycor()
    if y < -280:
        y = -280
    if y > 280:
        y = 280
    player.sety(y)
    player.color(random.choice(colours))

#Turtle turn
def player_right():
    player.right(5)

#Turtle turn
def player_left():
    player.left(5)
    
#Turtle pen up
def player_penup():
    player.penup()

#Turtle pen down
def player_pendown():
    player.pendown()

#Turtle pensize1
def player_pensize1():
    player.pensize(1)
    
#Turtle pensize2
def player_pensize2():
    player.pensize(5)
    
#Turtle pensize3
def player_pensize3():
    player.pensize(10)

#Turtle pensize4
def player_pensize4():
    player.pensize(20)


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(change_colour, "space")
turtle.onkey(player_circle, "c")
turtle.onkey(player_star, "s")
turtle.onkey(player_box, "b")
turtle.onkey(player_triangle, "t")
turtle.onkey(player_forward, "w")
turtle.onkey(player_right, "d")
turtle.onkey(player_left, "a")
turtle.onkey(player_flash, "q")
turtle.onkey(player_penup, "p")
turtle.onkey(player_pendown, "l")
turtle.onkey(player_rectangle, "r")
turtle.onkey(player_hexagon, "h")
turtle.onkey(player_flower, "f")
turtle.onkey(player_pensize1, "1")
turtle.onkey(player_pensize2, "2")
turtle.onkey(player_pensize3, "3")
turtle.onkey(player_pensize4, "4")

turtle.done()
