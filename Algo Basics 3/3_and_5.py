a = int(input('Enter a number >>'))

i = 3
list = []

while i <= a:
    if i%3 == 0 or i%5 == 0:
        list.append(i)
    i += 1
    pass

print(list)
