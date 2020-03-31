import re, requests, sys, os, pyperclip, bs4, matplotlib
import pandas as pd


os.makedirs('coviddata', exist_ok=True)
url = 'https://www.google.com/covid19-map/'
print('Dwonloading data %s' %(url))

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
name=[]
value=[]
nameRegex=re.compile(r'''(
    (\D*)(\d)?
)''', re.VERBOSE)
#sa jakies ograniczenia i mozna tylko 15 wartosci pobrac ??
#pobieranie danych

for i in range(1,16):
    classElement = soup.select('tr.A5V3jc')[i]
    str(classElement)
    x=classElement.getText()
    name.append(x)

print(name)
name2=[]

for k in range(15):
    for groups in nameRegex.findall(name[k]):
        name2.append(groups[1])


print(name2)




#datazip = zip(name, value)
#dataDictionary = dict(datazip)

#pData=pd.DataFrame(dataDictionary)

#print(dataDictionary)

'''print(name)
print(value)'''


