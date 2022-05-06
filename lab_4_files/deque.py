class Deque:
    def __init__(self):
        self.data = [""] * 0

    def is_empty(self):
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
        getted = self.data[-1]
        for i in range(length):
            data[i] = self.data[i]
        self.data = data
        return getted

    def push_left(self, element):
        length = len(self.data)
        data = [""] * (length + 1)
        for i in range(length):
            data[i+1] = self.data[i]
        data[0] = element
        self.data = data

    def pop_left(self):
        length = len(self.data) - 1
        data = [""] * length
        popped = self.data[0]
        for i in range(0, length):
            data[i] = self.data[i+1]
        self.data = data
        return popped

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return ""

    def peek_left(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return ""

    def display(self):
        print(self.data)
