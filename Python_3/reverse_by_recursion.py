list = [i for i in range(20)]

def reverse(list, start = 0):
    n = len(list)
    if start <= (n - 1) // 2:
        list[start], list[n - start - 1] = list[n - start - 1], list[start]
        start += 1
        reverse(list, start)

    return list

print('Initial list\n{}'.format(list))
print('Reversed list\n{}'.format(reverse(list)))
