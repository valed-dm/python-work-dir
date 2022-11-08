# In general, Python offers two different ways to sort lists.
# The first is implemented as a function named sorted().
# The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements. (Note: this description is a bit simplified compared to the actual implementation - we'll discuss it later.)
# The original list remains untouched.

greek = ['omega', 'alpha', 'pi', 'gamma']

print(sorted(greek))
print(greek)
print()

# The second method affects the list itself - no new list is created. 
# Ordering is performed in situ by the method named sort().
greek.sort()
print(greek)
