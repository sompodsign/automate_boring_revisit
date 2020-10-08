def stripp(text, leftright = None):
    import re
    if leftright == None:
        stripRegex = re.compile(r'^\s*|\s*$')
        text = stripRegex.sub('', text)
        print(text)
    else:
        stripRegex = re.compile(r'^.|.$')
        margins = stripRegex.findall(text)
        print(margins)
        while margins[0] in leftright:
            text = text[1:]
            margins = stripRegex.findall(text)
        while margins[-1] in leftright:
            text = text[:-2]
            margins = stripRegex.findall(text)
        print(text) 


mo = '    @@@@@@     '
mow = '@&&@#$texttexttext&&^&&&&%%'
bla = '@&#$^%+'

stripp(mo)
stripp(mow, bla)
