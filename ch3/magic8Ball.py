import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'


randomNumber = random.randint(1,3)
fortune = getAnswer(randomNumber)
print(fortune)