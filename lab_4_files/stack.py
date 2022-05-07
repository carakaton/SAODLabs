class Stack:
    def __init__(self):
        self.data = [""] * 0

    def is_empty(self) -> bool:
        return True if len(self.data) == 0 else False

    def push(self, element):
        length = len(self.data)
        data = [""] * (length + 1)
        for i in range(length):
            data[i] = self.data[i]
        data[-1] = element
        self.data = data

    def pop(self):
        length = len(self.data) - 1
        data = [""] * length
        popped = self.data[-1]
        for i in range(length):
            data[i] = self.data[i]
        self.data = data
        return popped

    def display(self):
        print(self.data)

    def __len__(self) -> int:
        return len(self.data)