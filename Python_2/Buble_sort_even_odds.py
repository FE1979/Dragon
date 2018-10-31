import random

def buble_sort(list):
    i = 0
    j = 1
    n = len(list)
    while i < n-1:
        while j < n-i:
            pass
            if (list[j-1] > list[j] and (list[j-1] + list[j]) %2 == 0) or
                (list[j-1]%2 != 0 and list[j]%2 ==0):
                list[j-1], list[j] = list[j], list[j-1]
            j += 1
        pass
        i += 1
        j = 1


    return list



list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

print('Sorted list\n',buble_sort(l))
