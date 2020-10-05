import pyperclip

text = pyperclip.paste()

# separate lines and add star
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # added start and space before each lines.
text = '\n'.join(lines)
pyperclip.copy(text)

