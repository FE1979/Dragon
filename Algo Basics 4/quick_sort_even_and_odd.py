#Script sorts a list of numbers with quick sort

import random

def quick_sort(list, first, last):
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
        list = quick_sort(list, first, right)
    if left < last:
        list = quick_sort(list, left, last)
    return list


list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

i = 0
l_even = []
l_odd = []
n = len(l)

while i < n:
    if l[i]%2 == 0:
        l_even.append(l[i])
    else:
        l_odd.append(l[i])
    i += 1
l_even = quick_sort(l_even, 0, len(l_even) - 1)
l_odd = quick_sort(l_odd, 0, len(l_odd) - 1)

l = l_odd + l_even

print('Sorted list\n', l)
