import pyinputplus as pyip 
import random, time

numberOfQuestions = 10
correctAnswer = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f"{questionNumber+1}: {num1} X {num2} = "
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)], 
        blockRegexes=[('.*', 'Incorrect')],timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswer += 1
    time.sleep(0.2)
print('Score %s / %s' % (correctAnswer, numberOfQuestions))