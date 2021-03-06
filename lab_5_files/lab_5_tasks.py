from lab_5_files.FractalViewer import FractalViewer
from compare import time_of, wait


def task_1():
    # Ввод глубины и рисование фрактала
    depth = int(input('Введите желаемую глубину фрактала: '))
    viewer = FractalViewer()
    viewer.show()
    viewer.display_sierpinski(depth)

    # Вывод таблицы
    print('\nТаблица зависимости\nглубина | время отрисовки')
    times = [0] * depth
    for i in range(depth):
        time, _ = time_of(viewer.draw_sierpinski, i)
        time = round(time, 2)
        times[i] = time
        print(f'      {i+1} : {time:.2f}')
        wait()

    # Подсчёт шага геометрической прогрессии
    summa = 0
    for i in range(1, depth):
        step = times[i] / times[i-1]
        summa += step

    result = summa / (depth - 1) if depth > 1 else summa
    print(f'Шаг геометрической прогрессии: ~{result:.1f}')

    viewer.hide()
