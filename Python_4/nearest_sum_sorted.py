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
l = insertion_sort(l)
print(l,'\n')

a = int(input('Type a number '))

i = 0
j = i + 1
pairs = []

#create a list with difference and pair of numbers
while i <= len(l) - 1:
    while j <= len(l) - 1:
        pairs.append((abs(l[i] + l[j] - a), (l[i], l[j])))
        j += 1
    i += 1
    j = i + 1

#sort a pairs and print the first pairs with similar difference
pairs_sorted = insertion_sort(pairs)
print('\nThe pairs are')

i = 0
while pairs_sorted[i][0] == pairs_sorted[0][0]:
    print(pairs_sorted[i][1])
    i +=1

print('Bye-bye!')
