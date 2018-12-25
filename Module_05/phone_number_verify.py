import re

regex = r"\(\d{3}\) *\d{3}-\d{4}"

phone_answer = input('Please, type you phone number below\n')

check = re.sub(regex, '', phone_answer)

if check != '':
    print('Sorry, this phone number is not valid')
else:
    print('Thank you!')
