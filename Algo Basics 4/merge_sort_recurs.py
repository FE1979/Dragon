#Script sorts a list of numbers with recursive merge sort

import random

def merge_sort(list, step=1):
    k = 0
    while k < len(list):
        i = 0
        j = 0
        left = list[k:k+step]
        right = list[k+step: k+step*2]
        list_exchange = []

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                list_exchange.append(right[j])
                j += 1
            else:
                list_exchange.append(left[i])
                i += 1
            pass

        if i == len(left):
            while j < len(right):
                list_exchange.append(right[j])
                j += 1
                pass
        elif j == len(right):
            while i < len(left):
                list_exchange.append(left[i])
                i += 1
        i = 0
        for i in range(len(list_exchange)):
            list[k+i] = list_exchange[i]

        k = k + step*2
        pass
    if step < len(list):
        list = merge_sort(list, step*2)
    return list

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

l = merge_sort(l)
print('Sorted list\n',l)
