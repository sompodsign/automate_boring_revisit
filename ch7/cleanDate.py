import re


dateRegex = re.compile(r'''(
    (\d{,2})    # day
    (-|/|\.)     # separator
    (\d{,2})  
    (-|/|\.)     # month/day
    (\d{2,4})   # year
)''', re.VERBOSE)


adate = dateRegex.search('the date was 05-12-2011')

newDate = '/'.join([adate.groups()[1], adate.groups()[3], adate.groups()[5]])

print(newDate)
