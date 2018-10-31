i = 1500
list = []
while i <= 3000:
    if i%7 == 0 and i%3 != 0:
        list.append(i)
    i += 1

print(list)
