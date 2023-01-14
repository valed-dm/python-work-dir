# Описание

# В основе SOLID — пять универсальных и применимых к любому ООП-языку принципов.
# Все они направлены на то, чтобы привести ваш код к слабой связанности и сильной связности.

# Single Responsibility — принцип единственной ответственности.
# Open-Closed — принцип открытости/закрытости.
# Liskov Substitution — принцип подстановки Барбары Лисков.
# Interface Segregation — принцип разделения интерфейса.
# Dependency Inversion — принцип инверсии зависимостей.

# Слабая связанность означает, что модуль должен иметь как можно меньше зависимостей от других.
# Такой модуль легко переиспользовать и удобно тестировать.

# Сильная связность означает, что все классы и методы, отвечающие за близкую функциональность,
# должны быть сгруппированы друг с другом. Размазанная по проекту логика или, наоборот,
# слишком близко соседствующие методы для разных задач, превратят ваш проект в запутанный клубок.


# SRP (Single Responsibility): Принцип единственной ответственности.


# Классы должны иметь одну и только одну причину для изменений.
# или
# Каждый класс должен отвечать только за одну операцию.

# Допустим, перед вами стоит задача: написать код, который будет готовить еду.
# Если структурировать код, отталкиваясь только от задания,
# у вас, скорее всего, получится примерно такой класс:

import inspect
from abc import ABC, abstractmethod


class KitchenRobot:
    def choose_food(self): pass
    def buy_food(self): pass
    def carry_food(self): pass

    def choose_dish(self): pass
    def prepare_ingredients(self): pass
    def cook_dish(self): pass

    def set_the_table(self): pass
    def wash_tableware(self): pass
    def clear_kitchen(self): pass

    def start(self): pass


# У этого класса много ответственных задач:
    # он должен уметь:
    # покупать, готовить еду, накрывать на стол, а также убирать после себя.
    # При этом код ещё должен выполнять действия в правильном порядке.

# Но если любой из этих процессов изменится, вам придётся править этот код:
# например, вместо многоразовой посуды, вы начнёте пользоваться одноразовой,
# тогда её мыть не надо или купите полуфабрикаты, тогда подготавливать ингредиенты не надо.

# Чтобы проверить, нарушен ли принцип SRP, попробуйте описать то, чем занимается этот класс,
# в одном предложении. Получится что-то вроде: «Он стирает, сушит и гладит одежду».
# Наличие перечисления и союзов «и» — один из признаков возможного нарушения принципа единой ответственности.

# Давайте избавимся от перечисления, разбив код на несколько отдельных классов.


class FoodSupply:
    def choose_food(self): pass
    def buy_food(self): pass
    def carry_food(self): pass
    def start(self): pass


class DishCook:
    def choose_dish(self): pass
    def prepare_ingredients(self): pass
    def cook_dish(self): pass
    def start(self): pass


class Waiter:
    def set_the_table(self): pass
    def start(self): pass


class Cleaning:
    def wash_tableware(self): pass
    def clear_kitchen(self): pass
    def start(self): pass


class KitchenRobot:
    def start(self): pass


# Теперь закупкой еды занимается класс FoodSupply, готовкой — класс DishCook,
# накрыванием на стол — класс Waiter, уборку — класс Cleaning, а за запуск процесса отвечает KitchenRobot.
# Если в классе FoodSupply найдётся ошибка, ваши исправления не затронут работающий код, потому что он находится в другом классе.


# OCP (Open-Closed): Принцип открытости/закрытости.


# Программные сущности должны быть открыты для расширения, но закрыты для изменения.

# Идея в том, что однажды написанный класс не должен никаким образом изменяться.
# Если вам требуются изменения, создайте класс-наследник и пишите код в нём.

# Представим у нас есть класс, который описывает работу очереди.
# Там есть методы получения элемента из очереди и добавление элемента в очередь.
# Спустя некоторое время, у нас появилась необходимость очищать очередь.
# Чтобы следовать принципу Open-Closed, нам надо наследовать свойства от существующего класса
# и добавить туда наши новые методы поведения.


class PrimalQueue:
    def get_from_queue(self): pass
    def set_in_queue(self): pass


class MutateQueue(PrimalQueue):
    def reset_queue(self): pass


# LSP (Liskov Substitution): Принцип подстановки Барбары Лисков.


# Функции, которые используют базовый тип, должны иметь возможность
# использовать подтипы базового типа,не зная об этом.
    # или
# Если П является подтипом Т, то любые объекты типа Т, присутствующие в программе,
# могут заменяться объектами типа П без негативных последствий для функциональности программы.


# Этот принцип указывает, что наследники должны уметь всё то, что умеют их родители.
# Вы можете быть уверены, что код, который успешно работает с классом File,
# будет корректно работать с его «ребёнком» PdfFile и «внуком» EncryptedPdfFile.

# Пример такой реализаций, можно посмотреть в примере к принципу Open-Closed.


# ISP (Interface Segregation): Принцип разделения интерфейса.


# Программные сущности не должны зависеть от методов, которые они не используют.

# Когда ваш класс реализует интерфейс, ему могут достаться методы, которые совсем не нужны для его работы.
# Несмотря на это, их всё равно придётся реализовывать, иначе интерфейс будет считаться не соблюдённым.
# Если интерфейс по какой-то причине изменит сигнатуру этих методов или добавит новый,
# вам придётся вносить изменения в класс.

# Для примера рассмотрим абстрактный класс Bird,
# который обязывает реализовать методы fly(), eat() и build_nest().
# Создадим на его основе несколько птиц:

# note
# Abstract Base Class

# The main goal of the abstract base class is to provide a standardized way to test
# whether an object adheres to a given specification.

# It can also prevent any attempt to instantiate a subclass
# that doesn’t override a particular method in the superclass.

# And finally, using an abstract class, a class can derive identity from another class
# without any object inheritance.


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def build_nest(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Eagle(Bird):
    def fly(self):
        """ Лететь быстро и высоко """

    def build_nest(self):
        """ Затаскивание веток на скалу """

    def eat(self):
        """ Поедание вкусных мясных кусочков """


class Colibri(Bird):
    def fly(self):
        """ Лететь, выписывая «восьмёрки» """

    def build_nest(self):
        """ построить гнездо из травинок и пуха """

    def eat(self):
        """ Пить нектар """


# Пока всё идёт хорошо. Теперь попробуем добавить Пингвина, который не умеет летать.


class Pinguin(Bird):
    def build_nest(self):
        """ Строить гнездо из камней """

    def eat(self):
        """ Ловить рыбу """


# При создании экземпляра Pinguin вы получите ошибку
# TypeError: Can't instantiate abstract class Pinguin with abstract methods fly.
# Абстрактный класс заставляет вас реализовывать ненужный пингвину метод.
# Чтобы избавиться от этой проблемы, разбейте класс на Bird, FlyingBird и NestingBird,
# распределив методы между ними. Теперь реализация пингвина может выглядеть так:

class NestingBird:
    pass


class Pinguin(NestingBird, Bird):
    ...


# DIP (Dependency Inversion): Принцип инверсии зависимостей.


# Модули верхних уровней не должны зависеть от модулей нижних уровней.
# Оба типа модулей должны зависеть от абстракций.

# Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

# Принцип инверсии зависимостей предлагает избавиться от использования конструкторов явно заданных классов.
# Вместо этого высокоуровневый модуль должен объявить интерфейс, в котором он нуждается.
# Это даст ему возможность пользоваться любым из низкоуровневых модулей, реализовавших его требования.


class Endpoint:
    def __init__(self):
        self.value = Cache().get_value(key="key")


class Cache:
    def __init__(self):
        ...

    def get_value(self, key: str):
        return ...


# Высокоуровневый класс Endpoint создаёт экземпляр класса Cache. У такого кода есть несколько проблем:

# Вы не можете заменить Cache на DummyCache или другую реализацию, не изменив класс.
# Вы не сможете протестировать свой код, не выполнив код из связанных классов.
# Теперь применим к этому коду принцип инверсии зависимостей, добавив абстрактные классы между связями.


class AbstractCache(ABC):
    @abstractmethod
    def get_value(self, key: str):
        ...


class Endpoint:
    def __init__(self, specific_cache: AbstractCache):
        self.value = specific_cache.get_value(key="key")


class Cache(AbstractCache):
    def __init__(self):
        ...

    def get_value(self, key: str):
        return ...


# Let’s understand one of the key principles of SOLID principles group namely, Dependency inversion principle.

# Dependency inversion principle is one of the principles on which most of the design patterns
# are build upon. Dependency inversion talks about the coupling between the different classes or modules.
# It focuses on the approach where the higher classes are not dependent on the lower classes
# instead depend upon the abstraction of the lower classes.
# The main motto of the dependency inversion is:
# Any higher classes should always depend upon the abstraction of the class rather than the detail.

# This aims to reduce the coupling between the classes is achieved by introducing abstraction
# between the layer, thus doesn’t care about the real implementation.

# Let’s understand the dependency inversion principle with an example.
# Say you are a manager having some persons as an employee of which some are developers
# and some are graphic designers and rest are testers.

# Now let’s see how a naive design would look without any dependency inversion
# and what are the loopholes in that design:

class Manager:
    def __init__(self):
        self.developers = []
        self.designers = []
        self.testers = []

    def addDeveloper(self, dev):
        self.developers.append(dev)

    def addDesigners(self, design):
        self.designers.append(design)

    def addTesters(self, testers):
        self.testers.append(testers)


class Developer:
    def __init__(self):
        print("developer added")


class Designer:
    def __init__(self):
        print("designer added")


class Testers:
    def __init__(self):
        print("tester added")


if __name__ == "__main__":
    a = Manager()
    a.addDeveloper(Developer())
    a.addDesigners(Designer())


print("------------------------")

# Now, let’s look at the design loop holes in the source code :
# First, you have exposed everything about the lower layer to the upper layer,
# thus abstraction is not mentioned.
# That means Manager must already know about the type of the workers that he can supervise.

# Now if another type of worker comes under the manager lets say, QA (quality assurance),
# then the whole class needs to be rejigged. This is where dependency inversion principle pitch in.

# Let’s see how to solve the problem to the better extent using Dependency Inversion Principle:


class Employee:
    def Work():
        pass


class Manager:
    def __init__(self):
        self.employees = []

    def addEmployee(self, a):
        self.employees.append(a)


class Developer:
    def __init__(self):
        print("developer added")

    def Work():
        print("turning coffee into code")


class Designer:
    def __init__(self):
        print("designer added")

    def Work():
        print("turning lines to wireframes")


class Testers:
    def __init__(self):
        print("tester added")

    def Work():
        print("testing everything out there")


if __name__ == "__main__":
    a = Manager()
    a.addEmployee(Developer())
    a.addEmployee(Designer())

print([m for m in dir(a) if not m.startswith('__')])
for emp in a.employees:
    print([method for method in dir(emp) if not method.startswith('__')])
    print(emp.__class__.__name__, "<<main task>>", end=" = ")
    emp.__class__.Work()
print("---------------------")
for emp in a.employees:
    emp.__class__.Work()

members = inspect.getmembers(a)
print(members)
