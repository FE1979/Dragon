n = int(input('Enter top of a list > '))

i = 1
list = []
Odd = False

while i < n:
    if Odd == False and i%3 == 0:
        list.append(i)
        Odd = True
    elif Odd == True and i%7 ==0:
        list.append(i)
        Odd = False
    i += 1

print(list)
