fibo_list = [0,1]

top_number = int(input('Type a number\n'))

i = 0

while fibo_list[-1] <= top_number:
    fibo_list.append(fibo_list[-1]+fibo_list[-2])

fibo_list.pop()
print(fibo_list)
