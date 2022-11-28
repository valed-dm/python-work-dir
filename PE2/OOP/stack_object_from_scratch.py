class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print("stack_object", stack_object.pop())
print("stack_object", stack_object.pop())
print("stack_object", stack_object.pop())

print()

stack_object_1 = Stack() # There are two stacks created from the same base class.
stack_object_2 = Stack() # They work independently. You can make more of them if you want to.

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print("stack_object_2", stack_object_2.pop())

print()

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print("funny_stack", funny_stack.pop())

print()

# Now let's go a little further. Let's add a new class for handling stacks.
# The new class should be able to evaluate the sum of all the elements currently stored on the stack.

# - we want the push method not only to push the value onto the stack 
# but also to add the value to the sum variable;

# - we want the pop function not only to pop the value off the stack 
# but also to subtract the value from the sum variable.

# Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. 
# Omitting this point will have harmful effects 
# - the object will be deprived of the __stack_list list. Such a stack will not function properly.

# Note the syntax:

# you specify the superclass's name (this is the class whose constructor you want to run)
# you put a dot (.)after it;
# you specify the name of the constructor;
# you have to point to the object (the class's instance) which has to be initialized by the constructor 
# - this is why you have to specify the argument and use the self variable here; 
# note: invoking any method (including constructors) from outside the class 
# never requires you to put the self argument at the argument's list 
# - invoking a method from within the class demands explicit usage of the self argument, 
# and it has to be put first on the list.
# Note: it's generally a recommended practice to invoke the superclass's constructor 
# before any other initializations you want to perform inside the subclass. 
# This is the rule we have followed in the snippet.

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def get_sum(self):          # We have to define a new method. We'll name it get_sum. 
        return self.__sum       # Its only task will be to return the __sum value.

    def push(self, val):        # We say that the push method has been overridden
        self.__sum += val       # - the same name as in the superclass Stack now represents a different functionality.
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object_new = AddingStack()

for i in range(10):
    stack_object_new.push(i)

print("AddingStack get_sum()", stack_object_new.get_sum())

for i in range(10):
    print("AddingStack pop(), step number: ", i, "--->",  stack_object_new.pop())
