import random

def quick_sort(list, start, end):
    splitter = list[end]
    i = start - 1

    for j in range(start,end):
        if list[j] >= splitter:
            i += 1
            list[j], list[i] = list[i], list[j]

    list[i+1], list[end] = list[end], list[i+1]

    if i > start:
        list = quick_sort(list, start, i)

    if i + 2 < end:
        list = quick_sort(list, i + 2, end)

    return list


list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

l = quick_sort(l, 0, len(l) - 1)
print('Sorted list\n{}'.format(l))
