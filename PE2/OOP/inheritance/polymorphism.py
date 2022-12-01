# Building a hierarchy of classes isn't just art for art's sake.

# If you divide a problem among classes and decide which of them should be located at the top and which should be placed at the bottom of the hierarchy, you have to carefully analyze the issue, but before we show you how to do it (and how not to do it), we want to highlight an interesting effect. It's nothing extraordinary (it's just a consequence of the general rules presented earlier), but remembering it may be key to understanding how some codes work, and how the effect may be used to build a flexible set of classes.

# Take a look at the code in the editor. Let's analyze it:

# there are two classes, named One and Two, while Two is derived from One. Nothing special. However, one thing looks remarkable - the do_it() method.
# the do_it()method is defined twice: originally inside One and subsequently inside Two. The essence of the example lies in the fact that it is invoked just once - inside One.
# The question is - which of the two methods will be invoked by the last two lines of the code?


# The first invocation seems to be simple, and it is simple, actually - invoking doanything() from the object named one will obviously activate the first of the methods.

# The second invocation needs some attention. It's simple, too if you keep in mind how Python finds class components. The second invocation will launch do_it() in the form existing inside the Two class, regardless of the fact that the invocation takes place within the One class.

# In effect, the code produces the following output:

# do_it from One
# do_it from Two
# output

# Note: the situation in which the subclass is able to modify its superclass behavior (just like in the example) 
# is called polymorphism.
# 
# The word comes from Greek (polys: "many, much" and morphe, "form, shape"), 
# which means that one and the same class can take various forms depending on the redefinitions done by any of its subclasses.

# The method, redefined in any of the superclasses, thus changing the behavior of the superclass, is called virtual.

# In other words, no class is given once and for all. Each class's behavior may be modified at any time by any of its subclasses.

# We're going to show you how to use polymorphism to extend class flexibility.


class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()

# Look at the example in the editor.

# import time

# class TrackedVehicle:
#     def control_track(left, stop):
#         pass

#     def turn(left):
#         control_track(left, True)
#         time.sleep(0.25)
#         control_track(left, False)


# class WheeledVehicle:
#     def turn_front_wheels(left, on):
#         pass

#     def turn(left):
#         turn_front_wheels(left, True)
#         time.sleep(0.25)
#         turn_front_wheels(left, False)

# Does it resemble anything? Yes, of course it does. It refers to the example shown at the beginning of the module when we talked about the general concepts of objective programming.

# It may look weird, but we didn't use inheritance in any way - just to show you that it doesn't limit us, and we managed to get ours.

# We defined two separate classes able to produce two different kinds of land vehicles. The main difference between them is in how they turn. A wheeled vehicle just turns the front wheels (generally). A tracked vehicle has to stop one of the tracks.

# Can you follow the code?

# a tracked vehicle performs a turn by stopping and moving on one of its tracks (this is done by the control_track() method, which will be implemented later)
# a wheeled vehicle turns when its front wheels turn (this is done by the turn_front_wheels() method)
# the turn() method uses the method suitable for each particular vehicle.
# Can you see what's wrong with the code?

# The turn() methods look too similar to leave them in this form.

# Let's rebuild the code - we're going to introduce a superclass to gather all the similar aspects of the driving vehicles, moving all the specifics to the subclasses.


# Look at the code in the editor again. This is what we've done:

# import time

# class Vehicle:
#     def change_direction(left, on):
#         pass

#     def turn(left):
#         change_direction(left, True)
#         time.sleep(0.25)
#         change_direction(left, False)


# class TrackedVehicle(Vehicle):
#     def control_track(left, stop):
#         pass

#     def change_direction(left, on):
#         control_track(left, on)


# class WheeledVehicle(Vehicle):
#     def turn_front_wheels(left, on):
#         pass

#     def change_direction(left, on):
#         turn_front_wheels(left, on)


# we defined a superclass named Vehicle, which uses the turn() method to implement a general scheme of turning, 
# while the turning itself is done by a method named change_direction(); 
# note: the former method is empty, as we are going to put all the details into the subclass 
# (such a method is often called an abstract method, as it only demonstrates 
# some possibility which will be instantiated later)
# we defined a subclass named TrackedVehicle (note: it's derived from the Vehicle class) 
# which instantiated the change_direction() method by using the specific (concrete) method named control_track()
# respectively, the subclass named WheeledVehicle does the same trick, 
# but uses the turn_front_wheels() method to force the vehicle to turn.
# The most important advantage (omitting readability issues) is that this form of code 
# enables you to implement a brand new turning algorithm just by modifying the turn() method, 
# which can be done in just one place, as all the vehicles will obey it.

# This is how polymorphism helps the developer to keep the code clean and consistent.

