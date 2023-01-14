# Кратко

# Описанный в PEP557 и добавленный в версий 3.7 модуль dataclasses,
# упрощают создание классов, в которых в последующем хранятся некие данные.
# С помощью декоратора @dataclass, у нас автоматически генерируются
# магические методы __init__ и __repr__.

# Практика

# Допустим мы хотим создать класс Person, для этого нам понадобится написать следующий код:

from dataclasses import dataclass, make_dataclass
from dataclasses import asdict, astuple


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'


# В случае с dataclasses, мы можем написать:

# (очень важна аннотация типов, т.к. атрибуты без аннотаций будут проигнорированы и
# приведет к exception NameError):


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int = 1


# А магические методы __init__ и __repr__ как и было сказано ранее, сгенерируются автоматически.
# Обратите внимание, мы также можем задавать значения по умолчанию для атрибутов.
# Однако мы можем еще упростить этот код:


Person = make_dataclass("Person", ["first_name", "last_name", "age"])


# Из полезного в модуле есть дополнительно методы, которые позволяют вернуть атрибуты класса
# в виде кортежа или словаря.

person = Person("Dmitrii", "Val", 35)
print(person)
print("repr(Person) -->", repr(person))
print("print astuple -->", astuple(person))
print("print asdict -->", asdict(person))
print(asdict(Person("John", "Doe", 20)))
print("---------------------------------------------------")
# {'full_name': 'John Doe', 'age': 20}


# С помощью параметра frozen можно закрыть изменение экземпляров dataclass-а:


@dataclass(frozen=True)
class Person:
    full_name: str
    age: int = 1


person = Person("John Doe", 20)
person.email = "Doe@gmail.com"
# raise dataclasses.FrozenInstanceError: cannot assign to field 'email'


# Напоследок, dataclasses - исходя из названия классы, которые можно наследовать и производить любые действия,
# как и с обычными классами в питоне.

# Ссылка для лучшего ознакомления:

# https://docs.python.org/3/library/dataclasses.html

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


person = Person('John', 'Doe', 25)
# use str()
print("use str() -->", person)

# use repr()
print("use repr() -->", repr(person))


# (John,Doe,25)
# Person("John","Doe",25)

# __str__ vs __repr__

# The main difference between __str__ and __repr__ method is intended audiences.

# The __str__ method returns a string representation of an object that is human-readable
# while the __repr__ method returns a string representation of an object that is machine-readable.

# Summary

# Implement the __repr__ method to customize the string representation of an object
# when repr() is called on it.
# The __str__ calls __repr__ internally by default.
