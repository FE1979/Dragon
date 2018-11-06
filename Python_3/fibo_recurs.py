fibo_top = int(input('Type top of Fibonacci list>'))

list = [0,1]

def fibonacci(list, top):
    if list[-1] < top:
        list.append(list[-1] + list[-2])
        list = fibonacci(list, top)
    if list[-1] > top:
        list.pop()
    return list

print('Fibonacci list\n{}'.format(fibonacci(list,fibo_top)))
