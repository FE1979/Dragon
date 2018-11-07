import random

def split(list, start, end):
    splitter = list[end]
    i = start - 1

    for j in range(start,end):
        if list[j] <= splitter:
            i += 1
            list[j], list[i] = list[i], list[j]

    list[i+1], list[end] = list[end], list[i+1]

    return i + 1

list_range = int(input('Type list range >'))
random_range = int(input('Type random range >'))

l = [random.randrange(random_range) for i in range(list_range)]
print('\nInitial list\n',l,'\n')

stack = []
stack.append(0)
stack.append(len(l)-1)

end = 0
start = 0

while stack:
    end = stack.pop()
    start = stack.pop()
    s = split(l, start, end)

    if s - 1 > start:
        stack.append(start)
        stack.append(s-1)

    if s + 1 < end:
        stack.append(s+1)
        stack.append(end)

    pass

print('Sorted list\n{}'.format(l))
