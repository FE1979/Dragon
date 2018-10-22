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

def merge_sort(list):
    l = list[:]
    k = 0
    step = 1
    n = len(l)
    a = []
    b = []
    d = []

    while step < n:
        while k < n:
            #take left and right parts and merge them
            if k+step>n:
                a = l[k:n]
                b = []
            else:
                a = l[k: k+step]
                b = l[k+step: k+step*2] #it's cheating, because didn't rise Index out of range error
                                        #so I added IF statement above to be correct

            d = merge(a, b)
            #replace parts with merged (and sorted) list in origin
            s = 0
            j = k
            for i in d:
                l[j] = i
                j+=1
            #let's move to next parts
            k = k + step*2
        #double size of parts and start from the beginning
        step = step * 2
        k = 0
    return l

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

l_even = merge_sort(l_even)
l_odd = merge_sort(l_odd)

l = []
l = l_odd + l_even

print(l)
