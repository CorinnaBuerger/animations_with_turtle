# Author: Corinna Bürger
# Title: My First Animation

from turtle import *
import math

def start_point(distance):
    start_distance = math.sqrt(distance**2 + distance**2)
    penup()
    left(45)
    fd(start_distance)
    right(135)
    pendown()

def square(distance):
    pensize(2)
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

def draw_animation(distance):
    speed(30)
    hideturtle()
    start_point(distance)
    while True:
        square(distance)
        right(10)
        distance = distance + 5


if __name__ == '__main__':

    bgcolor("black")
    draw_animation(50)

