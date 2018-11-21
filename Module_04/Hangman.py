import random
import json

words = []
word = ''
guessed_letters = []
words_count = 0
out_string= ['_']

with open("countries.json") as f:
    words = json.load(f)

words_count = len(words)
word = words[random.randrange(0,words_count-1)]
word = word.upper()
#print(word)

print('Welcome Hangman')
print('Guess a country')

while True:
    letter = input('type a letter\n')
    letter = letter.upper()
    if letter in word:
        guessed_letters.append(letter)
        out_string = [i if i in guessed_letters else '_' for i in word]
        for i in out_string:
            print(i, end="")
        print('\n')
    else:
        print('Incorrect')

    if '_' not in out_string:
        break
    pass

print('Wow! You win!')
