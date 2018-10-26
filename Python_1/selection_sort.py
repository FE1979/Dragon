import random

def selection_sort(list):

    n = len(list)
    min = 0
    i = 0
    j = i + 1

    while i < n-1:
        while j < n:
            if list[j] < list[j-1] and list[j] < list[min]:
                min = j
            j += 1
        list[i], list[min] = list[min], list[i]
        i += 1
        j = i + 1
        min = i
        pass

    return list


list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

print('Sorted list\n',selection_sort(l))
