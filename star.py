from turtle import colormode, pencolor, bgcolor, hideturtle, pensize, speed, pendown, right, fd, penup, home
import random

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colormode(255)        
    pencolor(r, g, b)

def draw_turtle_draw():
    bgcolor("black")
    hideturtle()

    while True:
        r_pensize = random.randint(1, 3)
        r_speed = random.randint(30, 50)
        r_distance = random.randint(0, 500)
        r_angle = random.randint(0, 360)

        change_color()
        pensize(r_pensize)
        speed(r_speed)

        #draws one ray:
        pendown()
        right(r_angle)
        fd(r_distance)

        # sends turtle back home
        penup()
        home()

if __name__ == '__main__':

    draw_turtle_draw()


