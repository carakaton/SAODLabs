from datetime import datetime


# Подсчет времени выполнения функции
def time_of(function, func_args, precision):
    summ = 0
    for i in range(precision):
        before = int(datetime.now().microsecond)
        function(*func_args)
        after = int(datetime.now().microsecond)
        summ += abs(after - before)

    return summ // precision


# Нахождение самой быстрой функции
def find_bestie(args_tuple, precision):
    def get_func_name(func):
        func_name_raw = str(func)

        start_index = func_name_raw.find("function")
        if start_index == -1:
            start_index = func_name_raw.find("method")
            start_index += 7
        else:
            start_index += 9

        end_index = func_name_raw.rfind(" <")
        if end_index == -1:
            end_index = func_name_raw.rfind(" at")
        else:
            end_index -= 3

        return func_name_raw[start_index:end_index]

    winner_time = 99999999999999999999999999999
    winner_name = "Your functions are too slow"

    print("Среднее время выполнения функции:")

    for args in args_tuple:
        function = args[0]
        func_args = args[1:]

        func_name = get_func_name(function)
        time = time_of(function, func_args, precision)

        print(f".\t{func_name} = {time} мкС")

        if time < winner_time:
            winner_time = time
            winner_name = func_name
        elif time == winner_time:
            winner_name += f" и {func_name}"

    print(f"\nБыстрее всех — {winner_name} 🎉 ({winner_time} мкС).")
