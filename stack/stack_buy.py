import time
import random

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

    def simulate_line(self,till_show,max_time):
        pq = Queue()
        tix_sold = []


        for i in range(10):
            pq.enqueue("person" + str(i))

        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randit(0,max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold

