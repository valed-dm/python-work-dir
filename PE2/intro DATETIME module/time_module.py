# The time module
# In addition to the time class, the Python standard library offers a module called time, 
# which provides a time-related function. 
# You already had the opportunity to learn the function called time when discussing the date class. 
# Now we'll look at another useful function available in this module.

# You must spend many hours in front of a computer while doing this course. 
# Sometimes you may feel the need to take a nap. Why not? 
# Let's write a program that simulates a student's short nap. Have a look at the code in the editor.

import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(2)


# Result:

# I'm very tired. I have to take a nap. See you later.
# I slept well! I feel great!
# output

# The most important part of the sample code is the use of the sleep function 
# (yes, you may remember it from one of the previous labs earlier in the course), 
# which suspends program execution for the given number of seconds.

# In our example it's 5 seconds. You're right, it's a very short nap.

# Extend the student's sleep by changing the number of seconds. 
# Note that the sleep function accepts only an integer or a floating point number.

print('----------------')


for name in dir(time):
    print(name, end="\t")