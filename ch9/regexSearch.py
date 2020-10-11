import pyinputplus, re
from pathlib import Path

all_text = ''
files = Path.cwd().glob('*.txt')
for file in files:
    all_text += open(file, 'r').read()

userInputRegexPattern = pyinputplus.inputStr(prompt='Enter your regex pattern: ')
userRegex = re.compile(f"{userInputRegexPattern}", re.IGNORECASE)

matchedText = userRegex.findall(all_text)

for match in matchedText:
    if match != '':
        print(match)