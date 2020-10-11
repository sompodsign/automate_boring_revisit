import re

text_file = open('madtext.txt', 'r')
text = text_file.read()
text_file.close()

madLibsRegex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
while madLibsRegex.search(text) != None:
    word = input(f"Enter a(n) {madLibsRegex.search(text).group().lower()}: ")
    text = madLibsRegex.sub(word, text, 1)

madLibsFile = open(f"madlib_s.txt", "w")
madLibsFile.write(text)
madLibsFile.close()

print(text)