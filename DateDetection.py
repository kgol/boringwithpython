import pyperclip, re

dateRegex = re.compile(r'''(
    ([0-3]\d|\d)\/([0-1]\d|\d)\/(\d{4})
    )''',re.VERBOSE)

text = str(pyperclip.paste())
match =[]
months30days =['04','06','09','11']

def LeapYear(year):
    if (int(year)%4==0):
        if (int(year)%100==0):
            if (int(year)%400==0):
                LYear = 'True'
            else:
                LYear = 'False'
        else:
            LYear = 'True'
    else:
        LYear = 'False'
    return LYear




for groups in dateRegex.findall(text):
    day = ''.join(groups[1])
    month = ''.join(groups[2])
    year = ''.join(groups[3])
    if LeapYear(int(year))=='True' and month =='02':
        if 0 < int(day) <= 29:
            date = '/'.join([groups[1],groups[2],groups[3]])
            match.append(date)
        else:
            print('incorrect date')
    else:
        if month in months30days:
            if int(day) in range(0,31):
                date = '/'.join([groups[1],groups[2],groups[3]])
                match.append(date)
            else:
                print('incorrect date')
        else:
            if int(day) in range(0,32):
                date = '/'.join([groups[1],groups[2],groups[3]])
                match.append(date)
            else:
                print('incorrect date')

'''
    date = '/'.join([groups[1],groups[2],groups[3]])
    match.append(date)'''


print(match)





