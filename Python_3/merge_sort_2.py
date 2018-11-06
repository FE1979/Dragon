#Script sorts a list of numbers with merge sort
#but uses additional list

import random

def merge(list1,list2):
    i = 0
    j = 0
    list = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            list.append(list2[j])
            j += 1
        else:
            list.append(list1[i])
            i += 1
        pass

    if i == len(list1):
        while j < len(list2):
            list.append(list2[j])
            j += 1
            pass
    elif j == len(list2):
        while i < len(list1):
            list.append(list1[i])
            i += 1

    return list

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

#divide origin list into list of lists with size 1
l = [l[i:i+1] for i in range(len(l))]


k = 0
temp_list = []

a = []
b = []

#merge consequent lists, add merged into temp_list and then replace origin with temp
#do it until there will be one list in a list
while len(l) > 1:
    while k < len(l):
        if k+1 > len(l)-1: # in case of out of index error
            a = l[k]
            b = []
        else:
            a = l[k]
            b = l[k+1]

        temp_list.append(merge(a, b))
        k += 2

    l = temp_list[:]
    temp_list = []
    k = 0


l = l[0]
#print sorted list
print('Sorted list\n',l)
