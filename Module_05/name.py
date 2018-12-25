import re

typical_words_for_this_answer = ['hi', 'hello', 'i', 'm', 'am', 'is', 'my', 'name']
answer = input('Hello! What is your name?\n')

list_of_words = re.split(r'\W+', answer, flags=re.IGNORECASE)
list_of_words = [x.lower() for x in list_of_words]

name = [x for x in list_of_words if x not in typical_words_for_this_answer]

print(f'\nHello {name[0].capitalize()}!')
