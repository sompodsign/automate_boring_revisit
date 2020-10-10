# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

# import shelve, pyperclip, sys
# mcbShelf = shelve.open('mcb')

# # Save clipboard content.
# if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
#     print(sys.argv[1], sys.argv[2])
#     mcbShelf[sys.argv[2]] = pyperclip.paste()
#     print('pasted!')

# elif len(sys.argv) == 2:
#     # List keywords and load content
#     if sys.argv[1].lower == 'list':
#         pyperclip.copy(str(list(mcbShelf.keys())))
#         print('keys: appeared')
#     elif sys.argv[1] in mcbShelf:
#         pyperclip.copy(mcbShelf[sys.argv[1]])
#         print('items showing.', mcbShelf[sys.argv[1]])
# mcbShelf.close()

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
	print("Text copied to clipboard" , sys.argv[2])


elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	if sys.argv[2].lower() == 'all':
		mcbShelf.clear()
		print("Deleted all saved clipboards!")
		
	elif sys.argv[2] in mcbShelf:
		del mcbShelf[sys.argv[2]]
		print ("\"%s\" clipboard deleted." % (sys.argv[2]))

elif len(sys.argv) == 2:

	if sys.argv[1].lower() == 'list':
	#	pyperclip.copy(str(list(mcbShelf.keys())))		-- uncomment to make list copy to real clipboard
		print (list(mcbShelf.keys()))

	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		print ("\"%s\" clipboard has copied to your original clipboard, press Ctrl+v to paste!" % (sys.argv[1]))


mcbShelf.close()