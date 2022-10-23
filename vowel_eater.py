# # Prompt the user to enter a word
# # and assign it to the user_word variable.
# user_word = input("please, enter a word: ")
# user_word = user_word.upper()

# for letter in user_word:
#     # Complete the body of the for loop.
#     if letter in ["A", "E", "I", "O", "U"]:
#         continue
#     print(letter)


word_without_vowels = ""
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("please, enter a word: ")
user_word = user_word.upper()


for letter in user_word:
    # Complete the body of the loop.
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)