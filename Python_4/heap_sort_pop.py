import random

"""Initial"""
list_range = int(input('Type list range >'))
random_range = 9 #only digits

l = [random.randrange(0, random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

''' Build a heap'''
def heap(lst):
    i = len(lst)//2 - 1
    while i >= 0:
        if i * 2 + 2 <= len(lst) - 1 and lst[i] < lst[i * 2 + 2]:
            lst[i], lst[i * 2 + 2] = lst[i * 2 + 2], lst[i]
        if lst[i] < lst [i * 2 + 1]:
            lst[i], lst[i * 2 + 1] = lst[i * 2 + 1], lst[i]
        i -= 1
    lst[0], lst[-1] = lst[-1], lst[0]

    return lst

''' Let's sort'''
lst_sorted = []
while l:
    l = heap(l)
    max = l.pop()
    lst_sorted.insert(0,max)
    pass

print('Sorted list\n', lst_sorted)
