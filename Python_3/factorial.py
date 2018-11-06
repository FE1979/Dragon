number = int(input('Type a number>'))

def fact(n, counter = 1):
    if n == 0:
        factorial = 0
    else:
        factorial = 1
    if counter <= n:
        counter += 1
        factorial = fact(n, counter) * (counter - 1)
    return factorial

print(fact(number))
