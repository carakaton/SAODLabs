from lab_5_files.fractal import Fractaler
from compare import time_of


def task_1():
    fractaler = Fractaler()
    depth = int(input("Размерность фрактала: "))
    fractaler.draw_sierpinski(depth)