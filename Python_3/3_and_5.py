import random

list_range = int(input('Type list range >'))

list = [i for i in range(list_range) if (i % 2 == 0 and i % 3 == 0) or (i % 2 != 0 and i % 5 == 0)]

print(list)
