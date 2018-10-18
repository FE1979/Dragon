import random

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]

print(l,'\n')

i = 0
j = i + 1
count = 0

while i <= len(l) - 1:
    while j <= len(l) - 1:
        if l[i] > l[j]:
            count += 1
            j += 1
        else:
            j += 1
    i += 1
    j = i + 1

print(count)

print('Bye-bye!')
