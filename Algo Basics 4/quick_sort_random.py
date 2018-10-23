#Script sorts a list of numbers with quick sort

import random

def quick_sort(list, first, last):
    left = first
    right = last
    medium = list[random.randrange(left, right)]
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
        list = quick_sort(list, first, right)
    if left < last:
        list = quick_sort(list, left, last)
    return list


list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

l = quick_sort(l, 0, len(l)-1)

print('Sorted list\n', l)
