#Script sorts a list of numbers by frequency of appearing
#w/out using pop, insert and other methods of lists
#but using try/ecxept


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

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]

print('\nInitial list\n',l,'\n')
l_sorted = insertion_sort(l)

count = 0
i = 0

freq = [] # [[freq1, item1], [freq2, item2] ...]
          #item of a list corresponds with its frequency

#count a frequency
try:
    while i <= len(l_sorted):
        count = 1
        while l_sorted[i] == l_sorted[i+1] and i < len(l_sorted):
            count += 1
            i += 1
        freq.append([count, l_sorted[i]])
        i += 1
except:
    pass

freq = insertion_sort(freq) # sort by frequency

#create sorted list by value
l_sorted = []
i = len(freq) - 1
j = 0
while i >= 0:
    for j in range(freq[i][0]):
        l_sorted.append(freq[i][1])
    i -= 1
    pass

print('Sorted by frequency\n',l_sorted)

print('Bye-bye!')
