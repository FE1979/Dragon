username = input('Type your name\n')

out_string = ' '.join(format(ord(i)) for i in username)
print('Unicode string: ', out_string)

out_string = ' '.join(format(ord(i), 'b') for i in username)
print('Binary string: ', out_string)
