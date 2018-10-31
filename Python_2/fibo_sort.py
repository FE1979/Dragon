import random

def insertion_sort(list):

    k = 0
    i = 0
    l = list[:]

    while i <= len(l) - 1:
        k = l[i]
        j = i - 1
        while j >= 0 and k < l[j]:
            l[j+1], l[j] = l[j], k
            j -= 1
        i += 1

    return l

fibo_list = [0,1]
list_lenght = int(input('Type a lenght of a list\n'))

i = 0
while i < list_lenght:
    fibo_list.append(fibo_list[-1]+fibo_list[-2])
    i += 1
fibo_list.pop()

fibo_list__to_sort = [fibo_list[random.randrange(len(fibo_list) - 1)] for i in range(list_lenght)]

print('Initial fibonacci list\n', fibo_list__to_sort)

fibo_list_sorted = insertion_sort(fibo_list__to_sort)

print('Sorted fibonacci list\n', fibo_list_sorted)
