import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += groups[8]
    matches.append(phoneNum)
    print(groups)
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# Copied to clipboard:
# 800-420-7240
# 415-863-9900
# 415-863-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# info@nostarch.com