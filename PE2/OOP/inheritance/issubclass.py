# Python offers a function which is able to identify a relationship between two classes, and although its diagnosis isn't complex, it can check if a particular class is a subclass of any other class.

# This is how it looks:

# issubclass(ClassOne, ClassTwo)


# The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.

# Let's see it in action - it may surprise you. Look at the code in the editor. Read it carefully.

# There are two nested loops. Their purpose is to check all possible ordered pairs of classes, and to print the results of the check to determine whether the pair matches the subclass-superclass relationship.

# Run the code. The program produces the following output:

# True	False	False	
# True	True	False	
# True	True	True	
# output

# Let's make the result more readable:

# ↓ is a subclass of →	Vehicle	LandVehicle	TrackedVehicle
# Vehicle	                True	False	False
# LandVehicle	            True	True	False
# TrackedVehicle	        True	True	True
# There is one important observation to make: each class is considered to be a subclass of itself.

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
