import pyperclip, re

MobilephoneRegex = re.compile(r'''(
    (00\d{2}|\(00\d{2}\)|\(+\d{2}\)|\+\d{2})?    #prefix
    (\s|-|\.|)?                                 #separator
    (\d{9}|(\d{3}(\s|-|\.|)){3})                #mobile phone number
    )''', re.VERBOSE)

HomephoneRegex = re.compile(r'''(
    (00\d{2}|\(00\d{2}\)|\(+\d{2}\)|\+\d{2})?    #prefix
    (\s|-|\.|)?                                 #separator
    (\d{9}|(\d{2}(\s|-|\.|)\d{7}|\d{2}(\s|-|\.|)\d{3}(\s|-|\.|)\d{2}(\s|-|\.|)\d{2}))                #home phone number
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                           #username
    @
    [a-zA-Z0-9.-]+                              #domain name
    (\.[a-zA-Z]{2,4})                           #dot - something
    )''',re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in MobilephoneRegex.findall(text):
    phoneNum = ''.join([groups[1],groups[3]])
    matches.append(phoneNum)
for groups in HomephoneRegex.findall(text):
    HomephoneNum = ''.join([groups[1],groups[3]])
    matches.append(HomephoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails')

