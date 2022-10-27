# Some useful tips
# Here are some tips which may help you to find and eliminate the bugs.
# None of them is either ultimate or definitive.
# Use them flexibly and rely on your intuition. Don't believe yourself – check everything twice.

# Try to tell someone (for example, your friend or coworker) what your code is expected to do and how it actually behaves.
# Be concrete and don't omit details.
# Answer all questions your helper asks.
# You'll likely realize the cause of the problem while telling your story,
# as speaking activates these parts of your brain which remain idle during coding.
# If no human can help you with the problem, use a yellow rubber duck instead.
# We're not kidding – consult the Wikipedia article to learn more about this commonly used technique:
# Rubber Duck Debugging.

# Try to isolate the problem.
# You can extract the part of your code that is suspected of being responsible
#  for your troubles and run it separately.
# You can comment out parts of the code that obscure the problem.
# Assign concrete values to variables instead of reading them from the input.
# Test your functions by applying predictable argument values.
# Analyze the code carefully. Read it aloud.

# If the bug has appeared recently and didn't show up earlier,
# analyze all the changes you've introduced into your code – one of them may be the reason.

# Take a break, drink a cup of coffee, take your dog and go for a walk,
# read a good book for a moment or two, make a phone call to your best friend
#  – you'll be surprised how often it helps.

# Be optimistic – you'll find the bug eventually; we promise you this.

# Unit testing – a higher level of coding
# There is also one important and widely used programming technique that you will have to adopt
# sooner or later during your developer career – it's called unit testing.
# The name may a bit confusing, as it's not only about testing the software,
# but also (and most of all) about how the code is written.

# To make a long story short – unit testing assumes that tests are inseparable
# parts of the code and preparing the test data is an inseparable part of coding.
# This means that when you write a function or a set of cooperating functions,
# you're also obliged to create a set of data for which your code's behavior is predictable and known.

# Moreover, you should equip your code with an interface that can be used
# by an automated testing environment. In this approach, any amendment made to the code
# (even the least significant) should be followed by the execution of all the unit tests
# accompanied by your source.

# To standardize this approach and make it easier to apply,
# Python provides a dedicated module named unittest.
# We're not going to discuss it here – it's a broad and complex topic.

# Therefore, we’ve prepared a separate course and certification path for this subject.
# It is called “Testing Essentials with Python”, and we invite you to participate in it.

# See you soon!
