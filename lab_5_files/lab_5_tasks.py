from lab_5_files.FractalViewer import FractalViewer
from compare import time_of, wait


def task_1():
    depth = int(input("Введите желаемую глубину фрактала: "))
    viewer = FractalViewer()
    viewer.show()
    viewer.display_sierpinski(depth)

    print("\nТаблица зависимости\nглубина | время отрисовки")
    times = [0] * depth
    for i in range(depth):
        time = round(time_of(viewer.draw_sierpinski, i, 1), 2)
        times[i] = time
        print(f"      {i+1} : {time:.2f}")
        wait()

    summa = 0
    for i in range(1, depth):
        step = times[i] / times[i-1]
        summa += step

    print(f"Шаг геометрической прогрессии: ~{summa / (depth - 1):.1f}")

    viewer.hide()
