from turtle import *
from math import sqrt
import lab_5_files


class Fractaler:

    def __init__(self, size=800):
        self.deepness = 0
        self.move_distance = 0
        self.screen_size = size

        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.colormode(255)
        self.screen.setup(size, size)

    def draw_sierpinski(self, depth):
        self.deepness = depth
        count = 2 ** (depth - 1)

        self.screen.tracer(4 ** self.deepness, 0)
        self.turtle.pensize(self.screen_size / (15 * count))

        padding = 30

        # Рассчет длины недиаганального шага черепахи
        cat_ears = 5 * count
        connector = count - 1
        self.move_distance = (self.screen_size - padding * 2) / (cat_ears + connector)

        # Смещение черепахи в верхний левый угол (с учетом отступов)
        offset = self.screen_size // 2 - padding
        self.turtle.up()
        self.turtle.goto(-offset + self.move_distance, offset)
        self.turtle.down()

        # Рисование фрактала
        self.turtle.right(45)
        for _ in range(2):
            self.half_sierpinski(depth)

            self.turtle.right(90)
            self.draw_line(depth, self.move_distance * sqrt(2))
            self.turtle.right(90)

    def draw_line(self, level, move_distance):
        if level > 0:
            shadow = 255 // self.deepness
            rgb = (255 - level * shadow, 255 - level * shadow, 220)
            self.turtle.pencolor(rgb)
        self.turtle.forward(move_distance)

    def half_sierpinski(self, level):
        if level > 0:
            self.half_sierpinski(level - 1)
            self.turtle.left(45)
            self.draw_line(level, self.move_distance)
            self.turtle.left(45)
            self.half_sierpinski(level - 1)

            self.turtle.right(90)
            self.draw_line(level, self.move_distance * sqrt(2))
            self.turtle.right(90)

            self.half_sierpinski(level - 1)
            self.turtle.left(45)
            self.draw_line(level, self.move_distance)
            self.turtle.left(45)
            self.half_sierpinski(level - 1)

        else:
            self.draw_line(level, self.move_distance * sqrt(2))
