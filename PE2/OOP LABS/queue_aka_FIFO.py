# Follow the hints:

# use a list as your storage (just like we did in stack)
# put() should append elements to the beginning of the list,
# while get() should remove the elements from the list's end;
# define a new exception named QueueError (choose an exception to derive it from)
# and raise it when get() tries to operate on an empty list.


# class QueueError(IndexError):  # Choose base class for the new exception.
#     def __init__(self, message='QueueError: stack is empty'):
#         self.message = message
#         super().__init__(self.message)


# class Queue:
#     def __init__(self):
#         self.__stack = []

#     def put(self, elem):
#         self.__stack.insert(0, elem)

#     def get(self):
#         val = self.__stack[-1]
#         del self.__stack[-1]
#         return val


# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)

# try:
#     for i in range(10):
#         print(que.get())
# except:
#     print('queue stack is empty')


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            elem = self.__queue[-1]
            del self.__queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
que.put("Test")
que.put("ABCDEFG")

try:
    for i in range(100):
        print(que.get())
except:
    print('queue stack is empty')
