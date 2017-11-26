#! /usr/bin/env python3
# toUppercase.py - converts clipboard text or argument to uppercase

import sys, pyperclip
if len(sys.argv) > 2:
	print('''Usage: python toUppercase.py - converts clipboard text to uppercase OR
       python toUppercase.py [string] - converts string to uppercase and prints to console''')
	sys.exit()

if len(sys.argv) == 2:
	inputString = sys.argv[1]
	print(inputString.upper())
	print('Would you like to copy this to the clipboard? (Type \'yes\' to copy)')
	if input().lower() == 'yes':
		pyperclip.copy(inputString.upper())
		print('Copied to clipboard succesfully.')
else:
	print('Converting string from clipboard to uppercase.')
	clipboardString = pyperclip.paste()
	pyperclip.copy(clipboardString.upper())
	print('Conversion successful.') 
