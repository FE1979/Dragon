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

#look for lowest difference in pairs
i = 1
j = 0
while i <= len(pairs) - 1:
    if pairs[i][0] < pairs[i-1][0] and pairs[i][0] < pairs[j][0]:
        j = i
        i += 1
    else:
        i += 1

print(pairs[j][1])

print('Bye-bye!')
