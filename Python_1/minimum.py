words = ['hi', 'my', 'name', 'is', 'i', 'am']
punct_symbols = ['!', ',', '.', '?']

def input_int(request):
    while True:
        try:
            answer = int(input(request+'\n'))
            break
        except ValueError:
            print('It is not a number. Please, try again')
    return answer

answer = input("Hello! What's your name?\n")

while answer != 'quit':

    answer_lower = answer.lower()

    for i in punct_symbols:
        answer_lower = answer_lower.replace(i, ' ')

    answer_words = answer_lower.rsplit()

    name = None
    for i in answer_words:
        if i in words:
            pass
        else:
            name = i.capitalize()

    if name is None or answer[-1] == '?':
        answer = input("I don't understand you. Please try again. Or type 'quit' to exit\n")
    else:
        print("Nice to meet you, " + name + '!')
        break

answer = input_int('How old are you?')

age_100 = 2018 - answer + 100
print('You will be 100 years old in {}'.format(age_100))

answer = input_int('Type a number')

if answer%2 == 0:
    print('It is odd number')
else:
    print('It is even number')

answer = input('Please, type a word\n')
answer_lower = answer.lower()

n = round((len(answer_lower)-1)/2)

palindrome = True
i = 0
while i<=n:
    if answer_lower[i] != answer_lower[-i-1]:
        palindrome = False
    i += 1
    pass

if palindrome == True:
    print('This word is palindrome')
else:
    print('This word is not palindrome')
