myPets = ['Zophie', 'Pooka', 'simi']
print('enter you cat name: ')
name = input()
if name not in myPets:
    print('I do not have pet named ' + name)
else:
    print(name + ' is my pet.')