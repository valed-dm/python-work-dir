from dataclasses import dataclass, field

# print(dir(dataclass))

# creating a employee class
# Let us see the traditional approach without using DataClass:


class employee:

    # init method or constructor
    def __init__(self, name, emp_id, age, city):

        # Instance Variable
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.city = city

    # magic function to return class object
    def __repr__(self):
        return ("employee (name={}, emp_id={}, age={}, city={} )"
                .format(self.name, self.emp_id, self.age, self.city))

    # magic function to return boolean
    def __eq__(self, check):
        return ((self.name, self.emp_id, self.age, self.city) ==
                ((check.name, check.emp_id, check.age, check.city)))


# initialization the object
emp1 = employee("Satyam", "ksatyam858", 21, 'Patna')
emp2 = employee("Anurag", "au23", 28, 'Delhi')
emp3 = employee("Satyam", "ksatyam858", 21, 'Patna')

print("employee object are :")
print(emp1)
print(emp2)
print(emp3)

# printing new line
print()

# referring two object to check equality
print("Data in emp1 and emp2 are same? ", emp1 == emp2)
print("Data in emp1 and emp3 are same? ", emp1 == emp3)

print("--------------------------------------")

# In the above code the biggest problem in passing the argumentin __init__, __repr__, and __eq__.

# Each time it has to copy its properties and return the object.
# It is a good way of dealing with a small amount of data but supposes we have work with large data.
# It makes your code more complicated.
# So, that why DataClass will implement to make your code easier and handy.

# Here are the same example, implemented in Python DataClasses:

# A basic Data Class
# importing dataclass module

# A class for holding an employees content


@dataclass
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    emp_id: str
    age: int
    city: str


emp1 = employee("Satyam", "ksatyam858", 21, 'Patna')
emp2 = employee("Anurag", "au23", 28, 'Delhi')
emp3 = employee("Satyam", "ksatyam858", 21, 'Patna')

print("employee object are :")
print(emp1)
print(emp2)
print(emp3)

# printing new line
print()

# referring two object to check equality
print("Data in emp1 and emp2 are same? ", emp1 == emp2)
print("Data in emp1 and emp3 are same? ", emp1 == emp3)

# In the above code, we don’t need to write a code for __init__, __repr__, and __eq__ function !!!!
print("--------------------------------------")


# dataclasses.Field()

# The field() objects describe each defined field.

# Example: Demonstration of how to view the fields of a dataclass object.


# A class for holding an employees content

@dataclass
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    emp_id: str
    age: int
    city: str


# object of the class
emp = employee("Satyam", "ksatyam858", 21, 'Patna')

print(emp.__dataclass_fields__)
print("--------------------------------------")

# Explanation of the parameters:

# default: This field is used to specify default values for this field.

# default field example:
# A class for holding an employees content


@dataclass
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    emp_id: str
    age: int

    # default field set
    # city : str = "patna"
    city: str = field(default="patna")


emp = employee("Satyam", "ksatyam858", 21)
print(emp)
print("--------------------------------------")

# default_factory:

# This field accepts a function and returns the initial value of the field, it must be a zero-argument.

# default factory example


def get_emp_id():
    id = 2345
    return id

# A class for holding an employees content


@dataclass
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    age: int

    # default factory field
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="patna")


# object of dataclass
emp = employee("Satyam", 21)
print(emp)
print("--------------------------------------")

# init : If true this field is included as a parameter to the generated __init__() method.

# init field example

# A class for holding an employees content


@dataclass
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    age: int

    # init field
    emp_id: str
    city: str = field(init=False, default="patna")


# object of dataclass
emp = employee("Satyam", "ksatyam858", 21)
print(emp)
print("--------------------------------------")

# repr: If true (the default), this field is included in the string
# returned by the generated __repr__() method.

# repr field

# A class for holding an employees content


@dataclass
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    age: int
    emp_id: str
    city: str = field(init=False, default="patna", repr=False)


emp = employee("Satyam", 21, "ksatyam858"),
print(emp)
print("--------------------------------------")

# hash: If true, this field is included in the generated __hash__() method.

# hash

# A class for holding an employees content


@dataclass(unsafe_hash=True)
class employee:

    # Attributes Declaration
    # using Type Hints
    name: str
    age: int
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(init=False, default="patna", repr=True, hash=True)


emp = employee("Satyam", "ksatyam858", 21)
print(hash(emp))
print("--------------------------------------")

# DataClass Inheritance
# Inheritance enables us to define a class that takes all the functionality from a parent class.

# Example: Child class inherits the properties of the parent class.

# A basic Data Class
# importing dataclass module


# parent class


@dataclass
class Staff:
    name: str
    emp_id: str
    age: int

# child class


@dataclass
class employee(Staff):
    salary: int


emp = employee("Satyam", "ksatyam858", 21, 60000)
print(emp)
