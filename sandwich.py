import pyinputplus as pyip

breadType = {'wheat':5, 'white':3, 'sourdough':10 }
breadList=['wheat','white','sourdough']
proteinType = {'chicken':5, 'turkey':7, 'ham':6, 'tofu':10}
proteinList =['chicken','turkey','ham','tofu']
chessType = {'cheddar':10, 'Swiss': 8, 'mozzarella': 7}
chessList = ['cheddar','Swiss','mozzarella']
addonsType = {'mayo': 2, 'mustard': 2, 'lettuce': 3, 'tomato': 4 }
addonsList = ['mayo','mustard','lettuce','tomato']

quantity = 0

while True:
    bread = pyip.inputMenu(breadList)
    protein = pyip.inputMenu(proteinList)


    chess1 = pyip.inputYesNo(prompt='Do you want chess? ')
    if chess1 == 'yes':
        chess = pyip.inputMenu(chessList)
    else:
        chess ='0'

    addons1 = pyip.inputYesNo(prompt = 'Any extras ? yes/no ')

    if addons1 == 'yes':
        addons = pyip.inputMenu(addonsList)
    else:
        addons = '0'

    quantity = pyip.inputInt(prompt='How many times ?')
    break

breadPrice = breadType.get(bread,0)
proteinPrice = proteinType.get(protein,0)
chessPrice = chessType.get(chess, 0)
addonPrice = addonsType.get(addons,0)

sandwichPrice = quantity*(breadPrice+proteinPrice+chessPrice+addonPrice)
print('Total price: '+ str(sandwichPrice))








