class Stack:
    def __init__(self):
        self.items = list()

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        del_item = self.items.pop()
        return del_item

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

