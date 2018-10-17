import random

def insertion_sort(list):

    k = 0
    i = 0
    l = list[:]

    while i <= len(l) - 1:
        k = l[i]
        j = i - 1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            l[j] = k
            j -= 1
        i += 1

    return l

while True:
    try:

        list_range = int(input('Type list range >'))
        random_range = int(input('Type random range >'))

        l = [random.randrange(random_range) for i in range(list_range)]
        l_sorted = insertion_sort(l)

        print('Initial list\n',l)
        print('\nSorted list:\n', l_sorted)

    except:
        break

print('Bye-bye!')
