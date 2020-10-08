# sandwichMaker.py
import pyinputplus as pyip 
prices = {'wheat': 2, 'white': 3, 'sourdough': 1.5,
            'chicken': 5, 'turkey': 2, 'ham': 1, 
            'tofu': 0.5}
def sandWichePrefs():
    breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
    proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
    wantCheese = pyip.inputYesNo(prompt='Do you want cheese?')
    if wantCheese:
        cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'Mozarella'],prompt='Enter cheese type: ')
    wantMayo = pyip.inputYesNo(prompt='Do you want mayo, musturd, lettuce, or tomato? ')    
    quantity = pyip.inputInt(prompt='How many sandwiches do you want? ')

    perPieceCost = prices[breadType] + prices[proteinType]
    totalCost = perPieceCost * quantity

    print('price per sandwiches is $%s' %(perPieceCost))
    print('For %s sandwiches your cost is: $%s.' % (quantity, totalCost))

sandWichePrefs()