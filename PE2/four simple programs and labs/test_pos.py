# two dogs in a flat
# The cat sat on the mat

sentence = input("Please input a sentence\n").lower().split() 
# Assigns a sentence to a variable, puts it into lower case and then splits the string into words

print(sentence)

word_positions = input("Please input a word\n") 
# Assigns a word for the program to print its positions 

end = [pos for pos, word in enumerate(sentence, start=1) if word == word_positions]

print (end)
# prints the positions of the word