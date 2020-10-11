fileObj = open('mad.txt', 'r')

text = fileObj.read()
x = text.split()
fileObj.close()

for i in range(len(x)):
    if x[i][-1] != '.':
        if x[i].lower() == 'adjective':
            userInput = input('Enter an adjective: ')
            x[i] = userInput
        elif x[i].lower() == 'noun':
            userInput = input('Enter a noun: ')
            x[i] = userInput
        elif x[i].lower() == 'verb':
            userInput = input('Enter a verb: ')
            x[i] = userInput
    else:
        x[i] = x[i][:-1]
        if x[i].lower() == 'adjective':
            userInput = input('Enter an adjective: ')
            x[i] = userInput
        elif x[i].lower() == 'noun':
            userInput = input('Enter a noun: ')
            x[i] = userInput
        elif x[i].lower() == 'verb':
            userInput = input('Enter a verb: ')
            x[i] = userInput
        x[i] = x[i] + '.'
        

print(' '.join(x))