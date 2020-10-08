catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) + 
    ' (Or enter nothing to stop).')
    name = input()
    if name == '':
        break
    catNames += [name]

print('The catnames are: ')
for catname in catNames:
    print('     ' + catname)

