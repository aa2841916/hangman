class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        last = len(self.item)-1
        return self.item[last]

    def size(self):
        return len(self.item)

stak = Stack()
for c in 'Hello':
    stak.push(c)
resver = ""
for i in range(5):
    resver += stak.pop()


print()