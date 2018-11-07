string = input('Type a sentence\n')

words = string.split(' ')

words_counted = []
words.sort()

while words:
    word = words[0]
    words_counted.append([word, words.count(word)])
    while word in words:
        words.remove(word)

print(words_counted)

words_counted.sort(key = lambda count: count[1], reverse = True)

for i in words_counted:
    print('{}: {}'.format(i[0],i[1]))
