import random


# Генерация списка из случайных чисел
def generate_numbers(count=10, min_limit=0, max_limit=999) -> list:
    return [random.randint(min_limit, max_limit) for value in range(count)]


# Создание матрицы m*n из случайных чисел от min_limit до max_limit
def generate_matrix(m=50, n=50, min_limit=-250, max_limit=1009):
    return [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]


# Выбор случайного числа из списка
def random_value(values):
    index = random.randint(0, len(values) - 1)
    return values[index]


# Добавление элемента в список
def add_value(values, index):
    values.insert(values, index)


# Удаление элемента из списка
def delete_value(values, index):
    values.remove(values, index)


# Генерация данных
def generate_strings(variant, length):
    strings = []

    if variant == "words":
        letters = [
            "a", "a", "b", "c", "o", "o", "d", "v", "g", "u", "u", "e", "e", "e"]
        for i in range(length):
            word = ""
            for j in range(5):
                letter = random_value(letters)
                word += letter
            strings.append(word)

    elif variant == "txt_emojies":
        txt_emojies = [
            "▼・ᴥ・▼", "(O_O)", "(･ω･)", "ʕ•ᴥ•ʔ", "(´∨`)", "(ಥ‿ಥ)", "(　；∀；)", "ʕ •ₒ• ʔ", "=^._.^=", "(๑ↀᆺↀ๑)", "(*´罒`*)"]
        for i in range(length):
            txt_emoji = random_value(txt_emojies)
            strings.append(txt_emoji)

    elif variant == "emojies":
        emojies = [
            "😀", "😃", "😄", "😁", "😆", "🥹", "😅", "😂", "🤣", "🥲", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰",
            "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒",
            "😞", "😔", "😟", "😕", "🙁", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😠", "😡", "🤬", "🤯", "😳", "🥵",
            "🥶", "😶", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🫣", "🤭", "🫢", "🫡", "🤫", "🫠", "🤥", "😶", "🫥",
            "😐", "🫤", "😑", "😬", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "😪", "😮", "😵", "😵", "🤐", "🥴",
            "🤧", "😷", "🤒", "🤕", "😈", "👿", "🤡"]
        for i in range(length):
            emoji = random_value(emojies)
            strings.append(emoji)

    return strings