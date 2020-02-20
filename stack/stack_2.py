class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def enqueue(self,item):
        self.item.insert(0,item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

a_queue = Queue()
for c in range(1,6):
    a_queue.enqueue(c)

print(a_queue.item)