from turtle import *
from math import sqrt
import subprocess


def check_appearance():
    """Checks DARK/LIGHT mode of macOS."""
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])


class FractalViewer:

    def __init__(self, size=800):
        self.screen = Screen()
        self.screen_size = size

        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.up()

        turtle_color, screen_bgcolor = ("white", "black") if check_appearance() else ("black", "white")
        self.turtle.color(turtle_color)
        self.screen.bgcolor(screen_bgcolor)

    def show(self):
        self.screen.setup(self.screen_size, self.screen_size)

    def hide(self):
        self.screen.exitonclick()

    def display_sierpinski(self, depth, animation=False):
        if animation:
            self.screen.tracer(4 ** depth, 0)
        else:
            self.screen.tracer(0, None)

        count = 2 ** (depth - 1)

        self.turtle.clear()
        self.turtle.home()
        self.turtle.pensize(self.screen_size / (15 * count))

        # Рассчет длины недиаганального шага черепахи
        padding = 30
        cat_ears = 5 * count
        connector = count - 1
        move_distance = (self.screen_size - padding * 2) / (cat_ears + connector)

        # Смещение черепахи в верхний левый угол (с учетом отступов)
        offset = self.screen_size // 2 - padding
        self.turtle.goto(-offset + move_distance, offset)

        # Отрисовка
        self.turtle.down()
        self.draw_sierpinski(depth, move_distance)
        self.turtle.up()

        if not animation:
            self.screen.update()

    def draw_sierpinski(self, depth, move_distance=1):
        def half_sierpinski(level):
            if level > 0:
                half_sierpinski(level - 1)
                self.turtle.left(45)
                self.turtle.forward(move_distance)
                self.turtle.left(45)
                half_sierpinski(level - 1)

                self.turtle.right(90)
                self.turtle.forward(move_distance * sqrt(2))
                self.turtle.right(90)

                half_sierpinski(level - 1)
                self.turtle.left(45)
                self.turtle.forward(move_distance)
                self.turtle.left(45)
                half_sierpinski(level - 1)

            else:
                self.turtle.forward(move_distance * sqrt(2))

        self.turtle.right(45)
        for _ in range(2):
            half_sierpinski(depth)

            self.turtle.right(90)
            self.turtle.forward(move_distance * sqrt(2))
            self.turtle.right(90)

