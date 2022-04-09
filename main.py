from display import View
from lab_1_files import lab_1_tasks
from lab_2_files import lab_2_tasks
from lab_3_files import lab_3_tasks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_screen = View("Все работы по САОД")

    lab_1 = View("Лабораторная работа №1", lab_1_tasks.task_3)

    lab_2 = View("Лабораторная работа №2")
    lab_2_task_1 = View("Задание №1", lab_2_tasks.task_1)
    lab_2_task_2 = View("Задание №2", lab_2_tasks.task_2)
    lab_2_task_3 = View("Задание №3", lab_2_tasks.task_three)
    lab_2.add_children([lab_2_task_1, lab_2_task_2, lab_2_task_3])

    lab_3 = View("Лабораторная работа №3")
    lab_3_task_1 = View("Задание №1", lab_3_tasks.task_1)
    lab_3_task_2 = View("Задание №2", lab_3_tasks.task_2)
    lab_3.add_children([lab_3_task_1, lab_3_task_2])

    start_screen.add_children([lab_1, lab_2, lab_3])

    start_screen.display()
