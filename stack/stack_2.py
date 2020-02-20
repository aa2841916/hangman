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
for i in range(5):
    a_queue.enqueue(i)

for i in range(5):
    print(a_queue.dequeue())

print(a_queue.item)
