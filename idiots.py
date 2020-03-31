import pyinputplus as pyip
i = 0
while True:
    prompt = 'Czy chcesz miec zajecie na cala kwarantanne? \n'
    response = pyip.inputYesNo(prompt, yesVal='Tak', noVal='Nie')
    if response != 'Nie':
        i+=1
    if response == 'Nie':
        break
print('Dziekuje, Milego dnia.')
print('Wynik: '+ str(i))
