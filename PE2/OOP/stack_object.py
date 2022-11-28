# class Stack_test:  # Defining the Stack class.
#     def __init__(self):  # Defining the constructor function.
#         print("Hi!")

# stack_object = Stack_test()  # Instantiating the object.


# class Stack:
#     def __init__(self):
#         self.stack_list = []

# stack_object = Stack()
# print(len(stack_object.stack_list))

class Stack:
    def __init__(self):
        self.__stack_list = [] # incapsulation implemented - we've added two underscores before the stack_list name 

stack_object = Stack()
print(len(stack_object.__stack_list))