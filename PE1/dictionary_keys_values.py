dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for english, french in dictionary.items():
    print(english, "->", french)
    print(french, "->", english)

for french in dictionary.values():
    print(french)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.update({"duck": "canard"})
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
del dictionary['dog']
print(dictionary)

# To remove the last item in a dictionary, you can use the popitem() method:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}
