# Inheritance: isinstance()
# As you already know, an object is an incarnation of a class. This means that the object is like a cake baked using a recipe which is included inside the class.

# This can generate some important issues.

# Let's assume that you've got a cake (e.g., as an argument passed to your function). You want to know what recipe has been used to make it. Why? Because you want to know what to expect from it, e.g., whether it contains nuts or not, which is crucial information to some people.

# Similarly, it can be crucial if the object does have (or doesn't have) certain characteristics. In other words, whether it is an object of a certain class or not.

# Such a fact could be detected by the function named isinstance():

# isinstance(objectName, ClassName)


# The functions returns True if the object is an instance of the class, or False otherwise.

# Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either the class or one of its superclasses.

# Don't forget: if a subclass contains at least the same equipment as any of its superclasses, it means that objects of the subclass can do the same as objects derived from the superclass, ergo, it's an instance of its home class and any of its superclasses.

# Let's test it. Analyze the code in the editor.

# We've created three objects, one for each of the classes. Next, using two nested loops, we check all possible object-class pairs to find out if the objects are instances of the classes.

# Run the code.

# This is what we get:

# True	False	False
# True	True	False
# True	True	True
# output

# Let's make the result more readable once again:

# ↓ is an instance of →	Vehicle	LandVehicle	TrackedVehicle
# my_vehicle	True	False	False
# my_land_vehicle	True	True	False
# my_tracked_vehicle	True	True	True
# Does the table confirm our expectations?


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
