class Queue:
    def __init__(self):
        self.queue = []

    #Add an element
    def enqueue(self, item):
        self.queue.append(item)

    #Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    #Display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(21)
q.enqueue(43)
q.enqueue(150)
q.enqueue(3)

q.display()

q.dequeue()
q.dequeue()

print("After removing 2 elements")
q.display()