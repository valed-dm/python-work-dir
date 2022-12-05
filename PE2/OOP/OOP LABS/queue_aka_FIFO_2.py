class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return (len(self.queue) == 0)

    def len(self):
        return len(self.queue)


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
que.put("victory")

print('stack:', que.queue)
print('length:', que.len())

print()

for i in range(100):
    if not que.isempty():
        print('length before get data:', que.len())
        print('data --> ', que.get())

    else:
        print('length before get data:', que.len())
        print("Queue empty")
        break
