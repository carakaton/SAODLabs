from time import sleep, perf_counter


# pass
def wait(sec: int = 1) -> None:
    sleep(sec)


# Подсчёт времени выполнения функции
def time_of(func: (), *args: tuple) -> (float, any):
    time = perf_counter()
    results = func(*args)
    time = abs(perf_counter() - time) * 1000
    return time, results


# Нахождение самого быстрого времени
def find_bestie(funcs: any, args: any) -> (list[float], float, list[tuple]):
    results, times = [], []
    best_time = float('Inf')

    for func, arg in zip(funcs, args):
        try:
            time, result = time_of(func, *arg)
        except:
            time, result = time_of(func, arg)
        times.append(time)
        results.append(result)
        best_time = min(time, best_time)

    return times, best_time, results


# Вывод списка времен
def display_times(names: list[str], times: list[int], best_time: float = None) -> None:
    print('\nВремя выполнения функции (мс):')
    for name, time in zip(names, times):
        line = '🎉' if time == best_time else '. '
        print(line + f'  {time:.4f}\t{name}')


# Получение короткого имени из результата str(функция)
def func_name(func: ()) -> str:
    func_name_raw = str(func)
    start_index = func_name_raw.find('function')
    if start_index == -1:
        start_index = func_name_raw.find('method') + 7
    else:
        start_index += 9
    end_index = func_name_raw.rfind(' <')
    if end_index == -1:
        end_index = func_name_raw.rfind(' at')
    else:
        end_index -= 3
    return func_name_raw[start_index:end_index]
