#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add starts.

pyperclip.copy(text)

# Separate lines and add starts.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexs in "lines" list
    lines[i] = '* ' + lines[i] # add start to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)