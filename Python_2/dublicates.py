import random

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

list = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',list,'\n')

list_nondublicates = []

for i in list[:]:
    if i in list_nondublicates:
        pass
    else:
        list_nondublicates.append(i)

print('List without dublicates\n', list_nondublicates)
