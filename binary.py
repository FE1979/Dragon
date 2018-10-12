import random

def BinaryFirstPosition(list, value):
    high = len(list)
    low = -1

    while (high - low) > 1:
        mid = round((high + low)/2)
        if list[mid] >= value:
            high = mid
        else:
            low = mid

    if list[high] > value:
        return None
    else:
        return high

def BinaryLastPosition(list,value):
    high = len(list)
    low = -1
    mid = 0

    while (high-low) > 1:
        mid = round((high + low)/2)
        if list[mid] <= value:
            low = mid
        else:
            high = mid
    return low

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
l = sorted(l)

print(l,'\n')
value = int(input('Type number to search >>'))

if BinaryFirstPosition(l,value) is not None:
    print('First position of searched item' +
            ' is {} and last position is {}'.format(BinaryFirstPosition(l,value), BinaryLastPosition(l,value)))
else:
    print('Not found')
