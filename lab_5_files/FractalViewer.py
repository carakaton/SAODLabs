from turtle import *
from math import sqrt
import subprocess


# Определение тёмной/светлой темы системы
def check_appearance():
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])


# Реализация окна просмотра и рисования фрактала
class FractalViewer:

    # Инициализация
    def __init__(self, size=800):
        self.screen = Screen()
        self.screen.title('Кривая Серпинского')
        self.screen_size = size

        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.up()

        # Выбор темы
        turtle_color, screen_bgcolor = ('white', 'black') if check_appearance() else ('black', 'white')
        self.turtle.color(turtle_color)
        self.screen.bgcolor(screen_bgcolor)

    # Открытие окна
    def show(self):
        self.screen.setup(self.screen_size, self.screen_size, 50)

    # Закрытие окна после клика
    def hide(self):
        self.screen.exitonclick()

    # Вывод фрактала
    def display_sierpinski(self, depth, animation=False):
        if animation:
            self.screen.tracer(4 ** depth, 0)
        else:
            self.screen.tracer(0, None)

        # Предварительная настройка черепахи
        size = 2 ** (depth - 1)     # Условный размер фрактала

        self.turtle.clear()
        self.turtle.home()
        self.turtle.pensize(self.screen_size / (15 * size))

        padding = 30                # Размер отступов от краев экрана
        side = 5 * size + size - 1  # Длина стороны фрактала в недиагональных шагах

        move_distance = (self.screen_size - padding * 2) / side  # длина недиагонального шага черепахи

        # Смещение черепахи в верхний левый угол (с учётом отступов)
        offset = self.screen_size // 2 - padding
        self.turtle.goto(-offset + move_distance, offset)
        self.turtle.right(45)

        # Рисование
        self.turtle.down()
        self.draw_sierpinski(depth, move_distance)
        self.turtle.up()

        if not animation:
            self.screen.update()

    # Рисование фрактала
    def draw_sierpinski(self, depth, move_distance=1):

        # Рисование половинки фрактала
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

        for _ in range(2):
            half_sierpinski(depth)

            self.turtle.right(90)
            self.turtle.forward(move_distance * sqrt(2))
            self.turtle.right(90)
