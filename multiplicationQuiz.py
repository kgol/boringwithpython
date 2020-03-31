import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for quesionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s'%(quesionNumber, num1, num2)

    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                            blockRegexes=[('.*','Incorrect!')],
                            timeout=8, limit=3)

    except pyip.TimeoutException:
        print("out of time")
    except pyip.RetryLimitException:
        print('Out of tries!')

    else:
        print(correcr)
        correctAnswers +=1
    
    time.sleep(1)

print('Score: %s/%s' % (correctAnswers, numberOfQuestions))
