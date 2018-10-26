# a game guess a number

import random
import sys

random.seed()

print("\nHello to the Game 'Guess a number'\n")
print("I will remember a number between 1 and 9\n")
print("and you should guess it, OKay?\n")

x = 1

while x!=0:
    print("Guess a number...\n")
    y = random.randint(1,2)
    x = int(input()) #IF YOU DO NOT PUT INTEGER IT WILL LAST ENDLESS...
    if x == 0:
        break
    elif x == y:
        print("WOW! You WIN!!!\n")
    elif x != y:
        print("No, that's wrong number. Try again...\n")
    pass

print("Bye! Bye!")
