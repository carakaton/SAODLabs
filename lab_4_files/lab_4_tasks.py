from lab_4_files.stack import Stack
from lab_4_files.deque import Deque


def task_1():
    with open("lab_4_files/books.data") as books:
        q1, q2 = Deque(), Deque()
        for book in books:
            q1.push(book.rstrip())

        while not q1.is_empty():
            x = q1.pop()
            while not q2.is_empty() and q2.peek() < x:
                q1.push_left(q2.pop())
            q2.push(x)

        while not q2.is_empty():
            print(q2.pop())


def task_2():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    coding = Deque()
    for char in alphabet:
        coding.push(char)

    def encode(char):
        if alphabet.find(char) != -1:
            while True:
                if coding.peek_left() == char:
                    coding.push(coding.pop_left())
                    coding.push(coding.pop_left())
                    return coding.peek_left()
                coding.push(coding.pop_left())
        return char

    def decode(char):
        if alphabet.find(char) != -1:
            while True:
                if coding.peek() == char:
                    coding.push_left(coding.pop())
                    coding.push_left(coding.pop())
                    return coding.peek()
                coding.push_left(coding.pop())
        return char

    with open("lab_4_files/encoded_text.data") as text:
        for char in text.read():
            print(decode(char), end="")
    print()


def task_3():
    A = Stack()
    B = Stack()
    C = Stack()

    disks = 4


def task_4():
    with open("lab_4_files/code.data") as code:
        stack = Stack()
        for char in code.read():
            if char == '(':
                stack.push('')
            elif char == ')':
                if stack.is_empty():
                    print(False)
                    return
                stack.pop()
        print(stack.is_empty())


def task_5():
    with open("lab_4_files/code.data") as code:
        deque = Deque()
        for char in code.read():
            if char == '[':
                deque.push('')
            elif char == ']':
                if deque.is_empty():
                    print(False)
                    return
                deque.pop()
        print(deque.is_empty())


def task_6():
    letters = Stack()
    digits = Stack()
    others = Stack()

    with open("lab_4_files/code.data") as code:
        for char in code.read():
            if char.isalpha():
                letters.push(char.rstrip())
            elif char.isdigit():
                digits.push(char.rstrip())
            elif char.rstrip() != '':
                others.push(char.rstrip())

    def print_stack(stack):
        output = ""
        while not stack.is_empty():
            output = stack.pop() + output
        print(output)

    print_stack(digits)
    print()
    print_stack(letters)
    print()
    print_stack(others)


def task_7():
    deque = Deque()

    with open("lab_4_files/numbers.data") as numbers:
        for number in numbers:
            if int(number) < 0:
                deque.push_left(number.rstrip())
            else:
                deque.push(number.rstrip())

    while not int(deque.peek()) < 0:
        deque.push_left(deque.pop())

    while int(deque.peek()) < 0:
        print(deque.pop())

    while not deque.is_empty():
        print(deque.pop_left())


def task_8():
    with open("lab_4_files/books.data") as books:
        stack = Stack()

        for book in books:
            print(book.rstrip())
            stack.push(book.rstrip())

        print("🔄")

        while not stack.is_empty():
            print(stack.pop())