import re

regex = r"[\d\w]+[\d\w\-\+\.]+@[\d\w]+[\d\w-]+\.[\d\w]+"

email_answer = input('Please, type you email below\n')

check = re.sub(regex, '', email_answer)

if check != '':
    print('Sorry, this email is not valid')
else:
    print('Thank you!')
