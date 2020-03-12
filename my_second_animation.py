# Author: Corinna Bürger
# Title: My Third Animation

from turtle import *
import math

def start_point(distance):
    start_distance = math.sqrt(distance**2 + distance**2)
    penup()
    left(135)
    fd(start_distance)
    right(135)
    pendown()

def square(distance):
    pensize(0.3)
    pencolor("lime green")
    fd(distance)
    right(90)
    pencolor("red")
    fd(distance)
    right(90)
    pencolor("cyan")
    fd(distance)
    right(90)
    pencolor("yellow")
    fd(distance)
    right(90)

def jump_to_next_square():
    penup()
    fd(3)
    left(90)
    fd(3)
    right(94)
    pendown()

def draw_animation(distance):
    speed(30)
    hideturtle()
    start_point(distance)
    while True:
        square(distance)
        jump_to_next_square()
        distance = distance + 6
    



if __name__ == '__main__':

    bgcolor("black")
    draw_animation(30)

