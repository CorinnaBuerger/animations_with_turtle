# Author: Corinna Bürger
# Title: My Third Animation

from turtle import *
import math
from random import randint

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

def draw_animation(distance):
    speed(30)
    hideturtle()
    pensize(0.3)
    start_point(distance)
    while True:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        pencolor(r,g,b)
        fd(distance)
        right(90.911)
        distance = distance + 1   



if __name__ == '__main__':

    bgcolor("black")
    draw_animation(30)

