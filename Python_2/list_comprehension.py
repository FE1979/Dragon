import random

list1_range = int(input('Type list 1 range >'))
list2_range = int(input('Type list 2 range >'))
random_range = 10


list1 = [random.randrange(random_range) for i in range(list1_range)]
list2 = [random.randrange(random_range) for i in range(list2_range)]
print('\nInitial lists\n',list1,'\n',list2,'\n')

list_output = []
for i in list1:
    if i in list2:
        list_output.append(i)

print(list_output)
