tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    newTable = {0:[], 1:[], 2:[], 3:[]}
    for li in tableData:
        for i in range(len(li)):
            newTable[i].append(li[i])
    
    longest = 0
    
    
    for k, v in newTable.items():
        length = len(''.join(v))
        if length > longest:
            longest = length
    print(f'longest {longest}')
    
    for k, v in newTable.items():
        print(len(''.join(v)))
        print(' ' * (longest - len(''.join(v))) + ' '.join(v))
            
printTable(tableData)