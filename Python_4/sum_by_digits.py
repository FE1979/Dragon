"""
script compounds two numbers by given array of digits
and sum of this numbers is minimum
"""
import random

"""Initial"""
list_range = int(input('Type list range >'))
random_range = 9 #only digits

l = [random.randrange(0, random_range) for i in range(list_range)]
l.sort()
print('\nInitial list\n',l,'\n')

""" if there odd quantity of digits let take first from list to make quantity even"""
if len(l) % 2 != 0:
    first_digit = l.pop(0)
    max_rank = (len(l) // 2)
else:
    max_rank = None

numbers = []
list_exchange = []
rank = 0

""" Let make a list of all possible numbers that give min sum"""
while l:
    right = l.pop()
    left = l.pop()
    if numbers:
        while numbers:
            number = numbers.pop()
            number1 = number + left * (10 ** rank)
            number2 = number + right * (10 ** rank)
            list_exchange.append(number1)
            list_exchange.append(number2)

        numbers = list_exchange[:]
        list_exchange = []
        pass
    else:
        numbers.append(left)
        numbers.append(right)

    rank += 1

"""
divide given list of numbers into two list
and add to first one max rank digit if available
"""
first_numbers = numbers[:len(numbers)//2]
second_numbers = numbers[len(numbers)//2:]
if max_rank is not None:
    first_numbers = list(map(lambda x: x + first_digit * (10 ** max_rank), first_numbers))

"""
Show all pairs of numbers and their second_numbers
"""
print('There is the pairs of numbers with minimum sum:')
i = 0
while i <= len(first_numbers) - 1:
    print("First = {}, second = {} and sum = {}".format(first_numbers[i],second_numbers[-i-1], first_numbers[i] + second_numbers[-i-1]))
    i += 1
