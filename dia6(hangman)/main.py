import random
from hangman_words import word_list

random_word = random.choice(word_list)
print(random_word)

for letter in random_word:
    print("_", end=" ")

user_letter = input("Adivinhe uma letra: ")

if user_letter in random_word:
    print (user_letter)