#! python3
# mapIt.py - launches a map in the browser using an address from cmd line or clipboard

import webbrowser, sys, pyperclip


if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)