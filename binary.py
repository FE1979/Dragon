import random

l = [random.randrange(10) for i in range(10)]
l = sorted(l)

print(l,'\n')
value = int(input('type number to search >>'))


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

a = BinaryFirstPosition(l,value)
b = BinaryLastPosition(l,value)


if BinaryFirstPosition(l,value) is not None:
    print('First position of searched item is {} and last position is {}'.format(a, b))
else:
    print('Not found')
