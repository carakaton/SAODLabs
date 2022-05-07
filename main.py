from view import View
from lab_1_files import lab_1_tasks
from lab_2_files import lab_2_tasks
from lab_3_files import lab_3_tasks
from lab_4_files import lab_4_tasks
from lab_5_files import lab_5_tasks

if __name__ == '__main__':
    start_screen = View("Все работы по САОД")

    lab_1 = View("Лабораторная работа №1 — Алгоритмы сортировки", lab_1_tasks.task_3)

    lab_2 = View("Лабораторная работа №2 — Поиск и Шахматы")
    lab_2_task_1 = View("Задание №1 — Алгоритмы поиска", lab_2_tasks.task_1)
    lab_2_task_2 = View("Задание №2 — Поиск хешированием", lab_2_tasks.task_2)
    lab_2_task_3 = View("Задание №3 — Шахматы", lab_2_tasks.task_three)
    lab_2.add_children([lab_2_task_1, lab_2_task_2, lab_2_task_3])

    lab_3 = View("Лабораторная работа №3 — Подстроки и Пятнашки")
    lab_3_task_1 = View("Задание №1 — Поиск подстроки", lab_3_tasks.task_1)
    lab_3_task_2 = View("Задание №2 — Пятнашки", lab_3_tasks.task_2)
    lab_3.add_children([lab_3_task_1, lab_3_task_2])

    lab_4 = View("Лабораторная работа №4 — Стеки-Деки")
    lab_4_task_1 = View("Задание №1 — Cортировка названий книг", lab_4_tasks.task_1)
    lab_4_task_2 = View("Задание №2 — Расшифровка", lab_4_tasks.task_2)
    lab_4_task_3 = View("Задание №3 — Пирамидки", lab_4_tasks.task_3)
    lab_4_task_4 = View("Задание №4 — Проверка круглых скобок", lab_4_tasks.task_4)
    lab_4_task_5 = View("Задание №5 — Проверка квадратных скобок", lab_4_tasks.task_5)
    lab_4_task_6 = View("Задание №6 — Разделение на цифры, буквы и другое", lab_4_tasks.task_6)
    lab_4_task_7 = View("Задание №7 — Сначала отрицательные, потом положительные", lab_4_tasks.task_7)
    lab_4_task_8 = View("Задание №8 — Строки в обратном порядке", lab_4_tasks.task_8)
    lab_4.add_children([lab_4_task_1, lab_4_task_2, lab_4_task_3, lab_4_task_4, lab_4_task_5, lab_4_task_6, lab_4_task_7, lab_4_task_8])

    lab_5 = View("Лабораторная работа №5 — Построение фрактала", lab_5_tasks.task_1)

    start_screen.add_children([lab_1, lab_2, lab_3, lab_4, lab_5])

    View.load_save(start_view=start_screen)