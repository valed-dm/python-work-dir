class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
print(sun)

# Inheritance - why and how?
# The term inheritance is older than computer programming, and it describes the common practice
#  of passing different goods from one person to another upon that person's death. 
# The term, when related to computer programming, has an entirely different meaning.
# Let's define the term for our purposes:
# Inheritance is a common practice (in object programming) of passing attributes and methods from the superclass
#  (defined and existing) to a newly created class, called the subclass.
# In other words, inheritance is a way of building a new class, not from scratch, 
# but by using an already defined repertoire of traits. The new class inherits (and this is the key) 
# all the already existing equipment, but is able to add some new ones if needed.

# Thanks to that, it's possible to build more specialized (more concrete) classes using some sets 
# of predefined general rules and behaviors.
# The most important factor of the process is the relation between the superclass and all of its subclasses (note: if B is a subclass of A and C is a subclass of B, this also means than C is a subclass of A, as the relationship is fully transitive).

# A very simple example of two-level inheritance is presented here:

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

# We can say that:

# The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
# The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
# The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.
# The above knowledge comes from reading the code (in other words, we know it because we can see it).

# Does Python know the same? Is it possible to ask Python about it? Yes, it is.

