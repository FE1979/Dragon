#Script sorts a list of numbers with quick sort

import random

def quick_sort_asc(list, first, last):
    left = first
    right = last
    medium = list[round((left + right) / 2)]
    while left <= right:
        while list[left] < medium:
            left += 1
            pass
        while list[right] > medium:
            right -= 1
            pass
        if left <= right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        pass
    if first < right:
        list = quick_sort_asc(list, first, right)
    if left < last:
        list = quick_sort_asc(list, left, last)
    return list

def quick_sort_desc(list, first, last):
    left = first
    right = last
    medium = list[round((left + right) / 2)]
    while left <= right:
        while list[left] > medium:
            left += 1
            pass
        while list[right] < medium:
            right -= 1
            pass
        if left <= right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        pass
    if first < right:
        list = quick_sort_desc(list, first, right)
    if left < last:
        list = quick_sort_desc(list, left, last)
    return list

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

l_even = []
l_odd = []

for i in l:
    if i % 2 == 0:
        l_even.append(i)
    else:
        l_odd.append(i)

l_even = quick_sort_desc(l_even, 0, len(l_even) - 1)
l_odd = quick_sort_asc(l_odd, 0, len(l_odd) - 1)

l = l_even + l_odd

print('Sorted list\n', l)
