from pathlib import Path
import os
import sys
import shelve
import pyperclip
import re


toFolder = Path.home() / Path('pythonData')
os.chdir(toFolder)

myShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1] == 'save':
    myShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2 and sys.argv[1] == 'list':
    # toCopy = ' '.join(list(myShelf.keys()))
    toCopy = '\n'.join(list(myShelf.keys()))
    pyperclip.copy(toCopy)

elif len(sys.argv) == 3 and sys.argv[1] == 'del':
    del myShelf[sys.argv[2]]

elif len(sys.argv) == 3 and sys.argv[1] == 'last':
    try:
        num = int('-' + sys.argv[2])
        toCopy = ' '.join(list(myShelf.keys())[num:])

        if len(list(myShelf.keys())[num:]) == 1:
            pyperclip.copy(myShelf[toCopy])
        else:
            pyperclip.copy(toCopy)
    except:
        pass

elif len(sys.argv) == 2 and sys.argv[1] == 'howmany':
    try:
        toCopy = str(len(myShelf))
        pyperclip.copy(toCopy)
    except:
        pass

elif len(sys.argv) == 3 and sys.argv[1] == 'search':
    try:
        freshDict = {}
        for item in myShelf.keys():
            freshDict[(item).upper()] = item

        theInput = (str(sys.argv[2])).upper()

        anySnip = r"(.*?)"
        regexTerm = f"^{anySnip}{theInput}{anySnip}$"
        regex = re.compile(regexTerm)
        allMatchesForKeys = list(filter(regex.match, freshDict.keys()))

        allMatches = []
        for item in allMatchesForKeys:
            allMatches.append(freshDict[item])

        toCopy = ' '.join(allMatches)
        pyperclip.copy(toCopy)
    except:
        pass

else:
    try:
        pyperclip.copy(myShelf[sys.argv[1]])
    except:
        pass

myShelf.close()
