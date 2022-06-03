from view import View
from lab_1_files import lab_1_tasks as lab_1
from lab_2_files import lab_2_tasks as lab_2
from lab_3_files import lab_3_tasks as lab_3
from lab_4_files import lab_4_tasks as lab_4
from lab_5_files import lab_5_tasks as lab_5
from lab_6_files import lab_6_tasks as lab_6
from olympiad_files import olympiad_tasks as olympiad
from final_files import final_tasks as final


def main():
    start_view = View('Все работы по СиАОД')

    lab_1_view = View('Лабораторная работа №1 — Алгоритмы сортировки', lab_1.task_3)

    lab_2_view = View('Лабораторная работа №2 — Поиск и Шахматы')
    lab_2_view.add_children(
        View('Задание №1 — Алгоритмы поиска', lab_2.task_1),
        View('Задание №2 — Поиск хешированием', lab_2.task_2),
        View('Задание №3 — Шахматы', lab_2.task_3))

    lab_3_view = View('Лабораторная работа №3 — Подстроки и Пятнашки')
    lab_3_view.add_children(
        View('Задание №1 — Поиск подстроки', lab_3.task_1),
        View('Задание №2 — Пятнашки', lab_3.task_2))

    lab_4_view = View('Лабораторная работа №4 — Стеки-Деки')
    lab_4_view.add_children(
        View('Задание №1 — Сортировка названий книг', lab_4.task_1),
        View('Задание №2 — Расшифровка', lab_4.task_2),
        View('Задание №3 — Пирамидки', lab_4.task_3),
        View('Задание №4 — Баланс круглых скобок', lab_4.task_4),
        View('Задание №5 — Баланс квадратных скобок', lab_4.task_5),
        View('Задание №6 — Разделение на цифры, буквы и другое', lab_4.task_6),
        View('Задание №7 — Сначала отрицательные, потом положительные', lab_4.task_7),
        View('Задание №8 — Строки в обратном порядке', lab_4.task_8))

    lab_5_view = View('Лабораторная работа №5 — Построение фрактала', lab_5.task_1)

    lab_6_view = View('Лабораторная работа №6 — Алгоритмы поиска путей', lab_6.task_1)

    olympiad_view = View('Олимпиадные задачи')
    olympiad_view.add_children(
        View('Задача №1 — Поиск наибольшего периметра', olympiad.task_1),
        View('Задача №2 — Создать максимальное число', olympiad.task_2),
        View('Задача №3 — Сортировка диагоналей', olympiad.task_3))

    final_view = View('Курсовая работа')
    final_view.add_children(
        View('Задача №1 — WTF?', final.task_1),
        View('Задача №2 — Это зебра?', final.task_2),
        View('Задача №3 — Файловая система BerOS', final.task_3))

    start_view.add_children(lab_1_view, lab_2_view, lab_3_view, lab_4_view,
                            lab_5_view, lab_6_view, olympiad_view, final_view)

    View.load_save(start_view=start_view)


if __name__ == '__main__':
    main()
