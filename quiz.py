import pyinputplus as pyip 
import random, time

prompt1='Jaka jest predkosc przeciagniecia szybowca "bocian"'
Q1=['65','70','80']
prompt2='jaka jest czestotliwos ratunkowa w lotnictwie ?'
Q2=['111,500','121,500','118,500']
prompt3='jaka jest dopuszczalna minimalna waga pilota na przednim fotelu ?'
Q3=['50','70','60']
prompt4='szybowiec obraca sie w korkociagu w prawo, co nalzy zrobic ?'
Q4=['prawa noga, drazek do siebie', 'lewa noga, drazek od siebie', 'lewa noga, drozek do siebie']
prompt5='minimalna predkosc ladowania dla szybowca "puchacz"'
Q5=['100','80','110']
prompt=[prompt1,prompt2,prompt3,prompt4,prompt5]
Q=[Q1,Q2,Q3,Q4,Q5]
print(Q)

numberOfQuestion = 2
correctAnswers = 0


for question in range(numberOfQuestion):
    print(prompt[question])
    try:
        q1answer=pyip.inputMenu(Q[question],timeout=8,limit=3,lettered=True)
        if q1answer == '65' and question == 1:
            print('Dobrze!')
            time.sleep(1)
            correctAnswers+=1
            break
        elif q1answer == '121,500' and question == 2:
            print('Dobrze!')
            time.sleep(1)
            correctAnswers+=1
            break
 
    except pyip.TimeoutException:
        print('czas minal')
    except pyip.RetryLimitException:
        print('limit prob wykorzystany')

'''      
    print(prompt2)
    try:
        for attempts in range(3):
            q2answer=pyip.inputMenu(Q2,timeout=8,limit=3,lettered=True)
            if q2answer == '121,500':
                print('Dobrze!')
                time.sleep(1)
                correctAnswers+=1
                break
    except pyip.TimeoutException:
        print('czas minal')
    except pyip.RetryLimitException:
        print('limit prob wykorzystany')'''

print('Poprawnych odpwiedzic %s/%s' %(correctAnswers, numberOfQuestion))
time.sleep(2)