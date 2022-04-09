# Узел бинарного дерева
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # добавление дочернего узла
    def add_branch(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add_branch(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add_branch(value)
        else:
            self.value = value

    # поиск значения от указанного узла
    def find_value(self, value):
        if value < self.value:
            if self.left is None:
                return None
            return self.left.find_value(value)

        elif value > self.value:
            if self.right is None:
                return None
            return self.right.find_value(value)

        else:
            return self