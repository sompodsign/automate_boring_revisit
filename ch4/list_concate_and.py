
        
spam = ['apples', 'bananas', 'tofu', 'cats']


def listConcatenate(spam):
    if spam:
        s = ', '.join(spam[:-1])
        j = spam[-1]
        result = s + ' and ' + j
        print(result)
    
listConcatenate(spam)