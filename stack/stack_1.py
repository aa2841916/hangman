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


# stack = Stack()
# resever = []
# for c in 'yesterday':
#     stack.push(c)
# for i in range(len(stack.item)):
#     resever += stack.pop()
# print(resever)
stack = Stack()
re = []
for i in range(1,6):
    stack.push(i)
for i in range(len(stack.item)):
    re.insert(0,stack.item[i])

print(re)