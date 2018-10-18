def GCD (a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

a = 0
b = 0

print ('This script finds GCD\n')

while (a or b) != 'Q':
    print ('Enter two numbers or Q to exit\n')
    try:
        a = input('First >> ')
        x = int(a)
        b = input('Second >> ')
        y = int(b)
        print (GCD(x,y))
    except:
        if (a or b) != 'Q':
            print('Please, enter a numbers\n\n')
