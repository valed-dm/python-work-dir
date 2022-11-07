# The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.
# Analyze the example code in the editor.
# The brackets are not a part of the result - they only show the result's boundaries.

# Demonstrating the lstrip() method:
print("[" + "    tau  ".lstrip() + "]")

# The one-parameter lstrip() method does the same as its parameterless version, 
# but removes all characters enlisted in its argument (a string), not just whitespaces:
print("www.www.cisco.com.www.".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# Surprised? Leading characters, leading whitespaces.