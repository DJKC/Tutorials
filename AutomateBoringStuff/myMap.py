#! python3
# myMap.py - Opens browser to map of address passed in or copied from the clipboard

import webbrowser, sys, pyperclip

# if the arguments passed in the command line are one or greater
if len(sys.argv) > 1:

    # Duckduckgo.com separates the address by '+', so they are added where spaces normally are
    # 1234 Jefferson Lane becomes 1234+Jefferson+Lane
    address = '+'.join(sys.argv[1:])
else:
    # address from clip board
    address = pyperclip.paste()

webbrowser.open("https://duckduckgo.com/?q=" + address + "&atb=v184-1&ia=maps&iaxm=maps")
