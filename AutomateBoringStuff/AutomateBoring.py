

def ln():
    print('\n')


def nl():
    print("#########################################")

####################################################################

import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

# There are quite a few inputs that I want to skip, they are skipped if the if is false
# skip = input("Run all code?: ")
# if(str(skip).isalpha() == False):
if 1 == 2:
    if input("Run moving line program?\nY or N: ") == 'y':
        # noinspection PyUnreachableCode
        try:
            while True: # The main program loop.
                print(' ' * indent, end='')
                print('********')
                time.sleep(0.1) # Pause for 1/10 of a second.

                if indentIncreasing:
                    # Increase the number of spaces:
                    indent = indent + 1
                    if indent == 20:
                        # Change direction:
                        indentIncreasing = False

                else:
                    # Decrease the number of spaces:
                    indent = indent - 1
                    if indent == 0:
                        # Change direction:
                        indentIncreasing = True
        except KeyboardInterrupt:
            sys.exit()

    ####################################################################

    def divide42ByX(x):
        try:
            return 42 / x

        except ZeroDivisionError: # Only catches dividing by Zero
            print("You divided by zero, don't try that anymore.")

    nl()
    print("Divide 42 by what number: ")
    x = int(input())
    print(divide42ByX(x))

    ####################################################################

    def catPrint():
        print("How many cats do you have: ", end = "")
        numCats = input()
        try:
            if(int(numCats) >= 4):
                print("That is a lot of cats!")
            elif int(numCats) > 0:
                print("That is not that many cats.")
            else:
                print("Please explain how that makes sense?!")
        # Type error is getting a number and expecting a letter etc.
        except ValueError: # Entering a value that is not a number
            print("That is clearly not a number.")

    nl()
    catPrint()

    ####################################################################
    # Guess the number game
    def guessNumber():
        import random
        print("Hello, what is your name?")
        name = input()

        print("Well, " + name + " I am thinking of a number between 1 and 20")

        secretNumber = random.randint(1, 20)

        for guess in range(1, 7):
            print("[" + str(secretNumber) + "]Take a guess: ")
            guess = int(input())

            if guess > secretNumber:
                print("Your guess is too high")
            elif guess < secretNumber:
                print("Your guess is too low.")
            else:
                break

        if guess == secretNumber:
            print(name + ", you guessed it!!")
        else:
            print(name + ", you did not guess it. The number was " + secretNumber)

    guessNumber()
    nl()

    ####################################################################
    # More list practice
    # https://automatetheboringstuff.com/2e/chapter4/
    spam = [['a', 'b', 'c'], [1, 2, 3]]
    mushabi = [1, 2, 3, 45]
    rice = ['r', 'i', 'c', 'e']
    milk = ['m', 'i', 'l', 'k']

    nl()
    print(spam[1][2], spam[-1])

    # slice is a subsection of a list
    print(mushabi[1:3])

    print(rice + milk)

    print([1, 2, 3] + [11, 22, 33])
    print([1] * 12)
    print(list("Hello"))

    if 1 in mushabi:
        print("ye!!")

    cat = ['a', 'b', 'c']
    first = cat[0]
    second = cat[1]
    third = cat[2]

    first, second, third = cat

    print(first, second, third)

    print("Found at: " + str(cat.index(third)))

    cat.insert(0, "0")

    print(cat)

    # del cat[0]
    cat.remove('0') # Remves first instance of '.'
    # Sort sorts in Ascii order
    print(cat.sort(key = str.lower)) # Can only sort single type, no mixing alpha and numeric

    name = "Elmotina"

    if "motin" in name:
        print("yes motinahgffjcy.")

    import copy

    spam = [1, 2, 3, 4]
    cheese = spam # cheese is a reference and data is shared
    cheese[0] = 'x'
    print(spam)
    print(cheese)
    cheese = copy.deepcopy(spam)
    spam[0] = 1
    print(spam)
    print(cheese)

    ####################################################################
    # Dictionaries, order of vars doesn't matter
    nl()

    food = {'breakfast': "eggs", "lunch": "grass", "dinner": "cereal"}

    print("~~For breakfast, we will be eating " + food['breakfast'] + ".")

    # checks for key
    if 'lunch' in food:
        print("~~Lunch in food dict.")

    # Creates a list of the keys used in food dictionary
    print("~~Keys in dict food:", list(food.keys()))

    # Creates a list of the values used in food dictionary
    print("~~Values in dict food: ", list(food.values()))

    print("~~Key Value")
    for k, v in food.items(): # .items() returns a tuple
        print(k, v)

    print("~~Dict food tuple")
    for i in food.items():
        print(i)

    # return "breakfast" value or return 99 if it doesn't exist
    print(food.get("breakfast", 99))
    print(food.get("fv", 99))

    # Adds a key if it doesnt exist
    if "snack" not in food:
        food["snack"] = "dinosaurs"

    # Same as above but clearly shorter
    # Only works if it doesnt exist already.
    food.setdefault("snack", "vehicles")

    print(food,  "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    import pprint
    def characterCount(message):
        count = {}

        for char in message.upper():
            count.setdefault(char, 0)
            count[char] += 1

        # print(count)

        #for k, v in count.items():
            #print(k, ": ", v)

        # The output is organized vertically, one pair per line
        pprint.pprint(count)

    characterCount("dvbkhlsbbrwfbuabvhabfivbasubauyrbfiyuaghryih947hgriuyaebiufb489hgp79hep7rg")

    ####################################################################
    # Data structures
    nl()

    animal = {"kind": "lizard", "name": "zebbewr"}

    myZoo = []
    myZoo.append({"kind": "giraffe", "name": "kiwi"})
    myZoo.append({"kind": "moose", "name": "buckz"})

    print(myZoo)

    print(type("100"))

    ####################################################################
    # Strings
    nl()
    # raw string, prints exactly what you pass into
    print(r'Jake\'s bird')

    # Will print just as it is typed, new lines and all.
    print("""nkjrnvrvrvr
    
    vjrnrerionr""")

    string = "jkhjgvj"
    string.isalnum()
    string.isalnum()
    string.isdecimal()
    string.isspace() # true if consists of spaces, tabs or newlines
    string.istitle() # True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
    string.startswith("jh") # true if starts with "jh"
    string.title() # returns title style text
    string.endswith("vj")

    numbers = ['0', '1', '2', '3', '4', '5']

    print("*".join(numbers)) # joins elements with *

    print("\n\n".join(numbers)) # joins elements with two new lines

    # a list split by whitespace
    print("True if the string consists only of words".split())

    # a list split by 't'
    print("True if the string consists only of words".split('t'))

    print("tyy".rjust(10)) # text is shifted to the right, also is ljust()

    string = "j hygkggtvjh gy    "
    print(string.strip()) # removes whitespace from left and right sides
    # lstrip and rstrip exist too

    spam = 'SpamSpamBaconSpamEggsSpamSpam'
    spam.strip('ampS') # 'BaconSpamEggs'
    # removes passed characters and stops when it meets an unpassed

    spam = "Hello there"
    print(spam.replace('e', "h77gf656cex$#¢xe"))

    import pyperclip
    pyperclip.copy("vcjf!!!fhg")
    print("Pasted: " + pyperclip.paste())

    monkey = "nanas"
    print("%s, %s" % ("AS", monkey))
# End skip code
####################################################################
# Regular expression

nl()

# Checks for a phone number without regular expression
def isPhoneNumber(text): # 806-234-2217
    count = 0
    for char in text:
        if len(text) != 12:
            print("Not a phone number!!")
            return False

        if(count == 3 or count == 7) and char != '-':
                print(text, " is not a number.")
                return False
        else:
            if str(char).isdecimal() == False:
                print(text, " is not a number.")

                return False

        print(text, " is a number.")
        count += 1
        return True


def checkForPhone(message):
    count = -1

    if (len(message) != 12):
        return -1

    for char in message:
        count += 1

        if(str(char).isdigit()):
            chunk = message[count:count + 12]

            if (isPhoneNumber(chunk)):
                print("Phone number found: ", chunk)
                return count

            else:
                print("Not a phone number!!!!!!!")
                return -1

# text = ''
# while text != 'z':
#     text = input("Enter a number, enter z to exit: ")
#     isPhoneNumber(text)

checkForPhone("123-123-1234")

# Checks for a phone number with regular expression
import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message = "Call me at 123-128-1234, (231) 122-6854 or 231-122-6854 by tomorrow"
print("Message: ", message)

# When using findall, [] can be used to access results like an array
print(phoneNumberRegex.findall(message)[1])

print("-----")

# Finds the first match
mo = phoneNumberRegex.search(message)
print("First match: ", mo.group())
#group() returns a tuple

# Regex groups, grouped by parentheses. Can be isolated by .group(1).
# Begins at 1 not 0, Can look for first group in () or the second group
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(message)
print("Search for number in message: ", mo.group())
print("Search for group 1, aread code: ", mo.group(1))
print("Search for group 2, phone 7 digits: ", mo.group(2))

# Includes searches for the area code parentheses
phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print("Number with grouped area code: ", mo.group())
# The following characters have special meanings
# You need to escape them with a backslash to find them in the text
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

# Searches for words beginning with Bat
batRegex = re.compile(r'Bat(man|mobile|copter|bat|woman|cycle)')
mo = batRegex.search("Batmobile lost a wheel")
print("Searched [Bat(man|mobile|copter|bat|woman|cycle]: ", mo.group(1), end = '\n\n') # returns matched option

# (x)? x can appear one or zero times in search match
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("SPider aND Batwoman")
print("SPider aND Batwoman: ", mo.group())

phoneRegex = re.compile(r'\(\d\d\d\)?-\d\d\d-\d\d\d\d')

try:
    mo = phoneRegex.search("234-111-5965")
    print(mo.group())

except:
    print("Except catch, no matches found")

# (x)?, x can appear zero or one times
phoneRegex = re.compile(r'\(?\d\d\d\)?-\d\d\d-\d\d\d\d')
mo = phoneRegex.search("234-111-5965")
print("Question mark ? search: ", mo.group())

# (x)*, x can appear zero to infinite times
phoneRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d(\w)*')
mo = phoneRegex.search("(234)-111-5965jftkdtfftyftf")
print("Asterisk * search: ", mo.group())

# (x)+, x must appear at least once and as many times after that
phoneRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d(\w)+')
mo = phoneRegex.search("(234)-111-5965jftkdtfftyftf(234)-111-2223-")
print("Plus + search: ", mo.group())

# Matches Ha 3 - 5 times, both do the same thing. Will match the longest string by default
haRegex = re.compile(r'(Ha){3,5}')
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

# Using findall with no group returns a list, with groups then a tuple is returned
numberRegex = re.compile(r'(\(?\d\d\d\)?)?-?(\d\d\d(-|\s)?\d\d\d\d)+')
mo = numberRegex.findall("(931)-231-2883c9312312884")
print("Findall List Tuple: ", mo)

# Anything in the brackets and negation
abc = "abcdefghijklmonpqrstuvwxyz"
abdregex = re.compile(r'[^aeiouy]') # skips vowels
abdregex = re.compile(r'[aeiouy]') # only vowels
mo = abdregex.findall(abc)
print("ABC search: ", mo)
# Character in brackets do not need to be escaped
# [0-5\.], no. --> [0-5.] aka 0 to 5 and then followed by a period
# Begins with ^ and ends with $
beginsWithHello = re.compile(r'^Hello') # ^ in fromt means string starts with Hello
endWithHello = re.compile(r'Hello$') # $ at the end means ends with Hello
mo = beginsWithHello.search("Helloqwerfg")
print("Begins with hello: ", mo.group())
mo = endWithHello.search("kjbhbhahvHello")
print("Ends with Hello: ", mo.group())

text = '''Chorus.


  Escalus, Prince of Verona.

  Paris, a young Count, kinsman to the Prince.

  Montague, heads of two houses at variance with each other.

  Capulet, heads of two houses at variance with each other.

  An old Man, of the Capulet family.

  Romeo, son to Montague.

  Tybalt, nephew to Lady Capulet.

  Mercutio, kinsman to the Prince and friend to Romeo.

  Benvolio, nephew to Montague, and friend to Romeo

  Tybalt, nephew to Lady Capulet.

  Friar Laurence, Franciscan.

  Friar John, Franciscan.

  Balthasar, servant to Romeo.

  Abram, servant to Montague.

  Sampson, servant to Capulet.

  Gregory, servant to Capulet.

  Peter, servant to Juliet's nurse.

  An Apothecary.

  Three Musicians.

  An Officer.


  Lady Montague, wife to Montague.

  Lady Capulet, wife to Capulet.

  Juliet, daughter to Capulet.

  Nurse to Juliet.


  Citizens of Verona; Gentlemen and Gentlewomen of both houses;
    Maskers, Torchbearers, Pages, Guards, Watchmen, Servants, and
    Attendants.
'''

# dot aka any character except new line
atRegex = re.compile(r'[^\n\s]\w*ar') # character chunks that end with ar
print("RJ search *ar: ", atRegex.findall(text))

# greedy matching. Regex by default matches the longest string over shorter ones
# {n,m}? or *? or +? performs a non-greedy match of the preceding group.
# The default seems to be the non greedy right here, reasons currently unknown
greedyRegex = re.compile(r'(ha){3,4}?')
mo = greedyRegex.search("hahahaah_hahahaha")
print("Greedy search: ", mo.group())

# Matching newline with re.DOTALL
# re.compile(''), note r for raw string was not used here. I need to find out why
nonewlineRegex = re.compile('.*')
mo = nonewlineRegex.search("Bay\n123 and Dock #4.")
print("Before newline dotall: ", mo.group())
newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search("Bay\n123 and Dock #4.")
print("After newline dotall: ", mo.group())

# Case insensitive
robocop = re.compile(r'robocop', re.I)
mo = robocop.findall("robocop_ROBOCOP")
print("Robocop case insensitive: ", mo)

namesRegex = re.compile(r'Student #\d+')
mo = namesRegex.sub("???", "Student #123 gave the message to Student #222")
print("Sub replacement regex: ", mo)

# Replacing or censoring part of the message text
# \1 is group number, only one group here.
# Number of asterisks in \1**** will be the number of * that appear in the text
agentNameRegex = re.compile(r'Student #(\d)\d*')
mo = agentNameRegex.sub(r'\1***', "Student #123 told Student #234 that Student #345 was a teacher")
print("Censred partial student number: ", mo)

# Cleaning up complicated looking expressions
# Go from this:
# Phone number regex
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# To this:
# The ''' along with verbose mode ignores comments and white spaces, making it more quickly readable
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Use pipe to use multiple flags since only one secondary argument can be taken
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

####################################################################
# Input validation, in the book only https://automatetheboringstuff.com/2e/chapter8/

# currently having issues with installing pyinputplus


####################################################################
# Reading and writing files
# Forward slashes (\) are Windows, Back slashes (/) are Unix - Mac, Linux etc.
nl()
from pathlib import Path
# creates path with each
print("Path here: ", Path("spam", "bacon", "eggs"))
# Creates a str out of path
print("Path here: ", str(Path("spam", "bacon", "eggs")))

nl()

# List files in a list
myFiles = ["foo.txt", "bar.txt", "bar.fuuu"]
for filename in myFiles:
    print("File and path: ", Path('/Home/videos/family/', filename))

for filename in myFiles:
    print("File and path: ", Path(r'\Home\videos\family', filename))

homefolder = "/this/is/a/folder"
subfolder = "spam"

nl()

# Create a new path from two folders
newPath = '/'.join([homefolder, subfolder])
print("The new path: ", newPath)

homefolder = Path("/home/user/pictures")
subfolder = Path("newCar_pics")

# Path objects will will / operator to join folder strings
print(str(homefolder / subfolder))

import os

# Prints current working directory
Path.cwd()

try:
    # Changes the current folder
    os.chdir("/home/secret")
except FileNotFoundError:
    print("No such folder exists.")

nl()

# User's home folder
print(Path.home())

# Make a new folder
print("Creating a folder, does it exist:\n")
try:
    os.makedirs("MadeInTheConsole")
except FileExistsError:
    print("File already exists")

# Creates the folder specified before th mkdir call
try:
    Path.home().mkdir()
except FileExistsError:
    print("File already exists again")
# Path(/folder/folder).mkdir()

# Relative folders assume the current directory and choose a file in the cwd
#   cd Folder__16a
# Absolute path list the entire path
#   cd /home/user/homework/week16/Folder__16a

# Checks if folder is absolute or relative
Path("someFolderHere").is_absolute()
os.path.isabs(r'\someFile')

# Returns the absolute path of cwd
os.path.abspath(Path.cwd())

# Gets absolute path of string location
#   os.path.abspath(r'.\fileInCWD')

# More absolutes
os.path.isabs(os.path.abspath('.'))

# This I do not fullly understand, yet.
# https://www.codespeedy.com/os-path-relpath-method-in-python/
# https://www.geeksforgeeks.org/python-os-path-relpath-method/
# os.path.relpath()

# Unix doesn't have a drive attribute
#   print(print(p.drive()))

# Anchor is drive letter in windows or / in Unix
p = Path(r"/Users/X/F2A/file.txt")
print("Anchor:", p.anchor)

# Parent is folder containing the stem
print("Parent: ", p.parent)

print("Name: ", p.name)

# Stem is the file or folder at the end of the path
print("Stem: ", p.stem)

# Suffix is the file type, folders returns None
print("File suffix: ", p.suffix)

nl()

# Splitting a path apart
Path.cwd()
# /Users/X/F2A

p = Path.cwd()
p.parents[0]
# /Users/X/
# ...
p.parents[2]
# /

# File operations
# Returns a tuple of path name and file
os.path.split(p)
# ('/Users/X/F2A/', 'file.txt')
# Same as above

# os.chdir(Path(os.getcwd()) / 'F2B')
# Can use os and Path to change current directory

print("Tuple of base url and file: ", (os.path.dirname(p), os.path.basename(p)))

# Separate path into folder components
"/Users/X/F2A/file.txt".split(os.sep)
# ['', 'Users', 'newxsc', 'Documents', 'Coding', 'Python']

# File size
print("File size: ", os.path.getsize("/Users/X/F2A/file.txt"), " bytes")

# List contents of directory
print("Listdir: ", os.listdir("/Users/X/F2A"), end = '\n\n')


# Total size of files in folder
totalSize = 0
for filename in os.listdir("/Users/X/F2A"):
    totalSize = totalSize + os.path.getsize(os.path.join("/Users/X/F2A"))

print("Total size of /Users/X/F2A: ", totalSize)

####################################################################
# Path.glob method

path = Path('/Users/X/F2A')

# Find and makes a list of the files located in the directory
files = list(path.glob('*'))
print("Files: ", files)

# * is wild card and stand for any number of any character
# Find and makes a list of all text files in directory
files = list(path.glob('*.txt'))
print("Text files: ", files)

# ? stands for any single character
print(": ", list(path.glob("*.?s")))

nl()

# List all files in path
path = Path("/Users/X/F2A")
for file in path.glob('*'):
    print("File name: ", file)

nl()

# Check if file exists
if path.exists() == True:
    print(path, "exists!")
else:
    print(path, " does not exist!")

if path.is_file() == True:
    print(path, " is a file!")
else:
    print(path, " is not a file!")

if path.is_dir() == True:
    print(path, " is a folder!")
else:
    print(path, " is not a folder!")

# On windows, check for dvd drive
# Path("D:/").exists()

####################################################################
# File Reading! And writing.

nl()

# Creates a file and overwrites if file already exists
path = Path("/Users/X/F2A/spamLite.txt")
path.write_text("Hola Mundo!!!!!")
print("Text from file: ", path.read_text())

nl()

# More file exercise
# python 3.6 only accepted Path objects, string available 3.7+
# This is now a file object with the specified file open
helloFile = open("/Users/X/F2A/file.txt")
helloWords = helloFile.read()
print("File contents: ", helloWords)
helloFile.close()

# Read multiple lines from file
anotherFile = open("/Users/X/F2A/2drags.txt")
for line in anotherFile.readlines():
    print("Line: ", line)
anotherFile.close()

# Write plain text data to file
# open is not a function of writer!
writer = open("/Users/X/F2A/file00.txt", 'w') # 'w' for write mode
writer.write("Hello, world!!\n") # Add in the new line, it is not automatically added
writer.close()

writer = open("/Users/X/F2A/file00.txt", 'a') # 'a' for append mode
writer.write("Is this the first or second line?")
writer.close()

reader = open("/Users/X/F2A/file00.txt")
fileData = reader.read()
reader.close()
print("File content: ", fileData)
####################################################################
# Shelves allow you to store data as binary

nl()

import shelve

# if file exists and is not a previous opened shelf file, an error will be thrown
shelfFile = shelve.open('/Users/X/F2A/shelfData.txt') # open file for storage
cars = ["Maro", "Stang", "Gur"] # Cars will hold the data to store
shelfFile['carList'] = cars # call it carList and store it with the data from cars
shelfFile.close() # close file until needed again.

cats = 1 # Reset value
print("Cats: ", cats)

shelfFile = shelve.open("/Users/X/F2A/shelfData.txt") # opened the storage file for access
cats = shelfFile['carList'] # Cats now equal to shelf data
print("Cats: ", cats)

# Shelves are like dictionaries with a key and value pair
# They are like list but not exactly, so pass it to a list() first
shelfKeyList = list(shelfFile.keys())
print("Shelf keys: ", shelfKeyList)

shelfValueList = list(shelfFile.values())
print("Shelf value: ", shelfValueList)
numValues = len(shelfFile['carList'])
print("Number of values: ", numValues)

# Print individual items in 'carlist' shelf
count = 1
for k in shelfFile['carList']:
    print(count, " of ", numValues, " items: ", k)
    count += 1

shelfFile.close()

####################################################################
# Pretty print aka pprint

nl()

import pprint

# created a list of dicts
cars = [{'name': 'Tesla', 'desc': 'my tesla'}, {'name': 'buggy', 'desc': 'my horse cart'}]
carsPprint = pprint.pformat(cars)
print("Cars pprint:\n", carsPprint)

# Stored pprint string into a file with pprint formatting
fileObject = open("/Users/X/F2A/myCars.py", 'w')
fileObject.write("cars = " + carsPprint + '\n')
fileObject.close

import myCars

print("My cars from file: ", myCars.cars)
print(myCars.cars[0]['name'])

####################################################################
# Organizing files

nl()

# shutil aka shell utilities allows for copy, move, rename and delete
import shutil, os

from pathlib import Path

p = Path("/Users/X/F2A/")
os.chdir("/Users/X/F2A/")

# copies a single file, file.txt to F2B
# if filename is specified, it is copied using the new name
if(Path.exists(p / "F2B/file.txt")):
    print("File " + "file.txt" + " already exists!")
else:
    print("File " + "file.txt" + " has been copied!")
    shutil.copy(p / 'file.txt', p / 'F2B')

os.chdir("/Users/X/")
if Path.exists(os.getcwd() / Path("F2AA/spamLite.txt")):
    print("File tree for F2AA has already been copied")
else:
    # Destintion can't exist
    shutil.copytree('F2A', 'F2AA')
    print("F2A has been copied to F2AA.")

os.chdir("/Users/X/F2A/")
# Moves files
if(Path.exists(p / "F2B/file00.txt")):
    print("File " + "file00.txt" + " has already been moved!")
else:
    shutil.move(p / 'file00.txt', p / 'F2B') # Can also specify absolute path
    print("File " + "file00.txt" + " has been moved!")

# Rename, it is just a move operation specifying a new name
# Can rename a file in the sme directory, just specify a new name
if Path.exists(Path("00077.ts")):
    print("File " + "00066.ts" + " has already been renamed to " + "00077.ts")
else:
    print("00066.ts" + " renamed to " + "00077.ts")
    shutil.move("00066.ts", "00077.ts")

# Deleting single file
# FileNotFoundError will be thrown if doesn't exist
try:
    os.unlink(Path("F2AA/00066.ts"))
except OSError:
    print("File " + "00066.ts" + " doesnt exist.")

# Remove directory, must be empty
# FileNotFoundError will be thrown if doesn't exist
# OSError will be thrown if directory isn't empty
try:
    os.rmdir(Path("F2AA"))
except OSError:
    print("Directory " + "F2AA" + " not empty.")

# Remove folder and files
# FileNotFoundError will be thrown if doesn't exist
try:
    shutil.rmtree(Path("F2AA"))
except FileNotFoundError:
    print("Directory F2AA doesnt exist.")

os.chdir("/Users/X/")
if Path.exists(os.getcwd() / Path("F2AA/spamLite.txt")):
    print("File tree for F2AA has already been copied")
else:
    # Destintion can't exist
    shutil.copytree('F2A', 'F2AA')
    print("F2A has been copied to F2AA.")

for fileName in Path(os.getcwd() / Path("F2AA/F2B")).glob('*'):
    print(fileName, " will be deleted.")
    os.unlink(fileName)

# Sends file to recycle bin vs permanent deletion
os.chdir("/Users/X/F2A/")
import send2trash
newFile = open('abc.txt', 'w')
if Path.exists(Path("abc.txt")):
    print("File " + "abc.txt" + " has been created")
    newFile.write("This text is it!!!")
    newFile.close()
    send2trash.send2trash("abc.txt")
    if not Path.exists(Path("abc.txt")):
        print("File " + "abc.txt" + " has successfully been sent to the Trash Bin.")

else:
    print("Nothing to see folks.")
    newFile.close()

####################################################################
# os.walk() goes through a folder and returns the subfolders and files inside

for folderName, subfolders, fileNames in os.walk("/Users/X/"):
    print("\n\tCurrent folder:", folderName)
    # Current folder: /Users/X/F2AA

    for subfolder in subfolders:
        print('\t' + folderName + subfolder)
        # /Users/X/F2AAF2B

    for fileName in fileNames:
        print('\t' + folderName + fileName)
        # /Users/X/F2A/file00.txt

####################################################################
# Zip files

import zipfile

# Info about compressed file and list of its contents
p = Path("/Users/X/F2AA/")
exampleZip = zipfile.ZipFile(p / "PythonArchive.zip")
print("Files inside: ", exampleZip.namelist())
appJSinfo = exampleZip.getinfo("app.js")
print("File size: ", appJSinfo.file_size)
print("Compressed size: ", appJSinfo.compress_size)
# Math seems very questionable, 14 / 14 is 1, so 1x smaller?
print("Compressed file is " + str(round(appJSinfo.file_size / appJSinfo.compress_size, 5)) + " x smaller!")

# Extract contents into new folder, will create if needed, or CWD.
exampleZip = zipfile.ZipFile(p / "PythonArchive.zip")
exampleZip.extractall("/Users/X/F2AA/extracted")
exampleZip.close()

# Creating a new zip and adding files to it
moreZip = zipfile.ZipFile("another.zip", 'w')
moreZip.write("file.txt", compress_type=zipfile.ZIP_DEFLATED)
moreZip.close()
moreZip = zipfile.ZipFile("another.zip", 'a') # Append new files
moreZip.write("file00.txt", compress_type=zipfile.ZIP_DEFLATED)
print("Files in current archive: ", moreZip.namelist())
moreZip.close()

####################################################################
# Debugging

try:
    raise Exception("This is an error message, get down!")
except Exception as err:
    print(str(err))

print("CWD: ", os.getcwd())

# Log an exception and keep the program running
import traceback
try:
    raise Exception("An error message!!!")
except:
    errorFile = open("errorInfo.txt", 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()

print(type(traceback.format_exc()))

# Throws AssertionError is assert is false
# Asserts are for finding errors during programming
#   and are different from exceptions which users can cause.
numbers = [12, 34,654, 76, 234, 0, 22, -1]
numbers.sort()
print("Numbers: ", numbers)
# assert(numbers[2] <= numbers[0])
# Message in assert is optional but also very helpful
# Only prints assert if statement is false
assert(numbers[2] <= numbers[4]), "Numbers are not in order!"

import logging
# When events are logged, a logRecord object holds event info. Below is configuring how log info is shown.

# The line below goes at the top file
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# %s%% appears to be stand in for variable value of n
# This is how logging is done
d = "dd"
logging.debug('Start of factorial(%s%%)' % (d))
logging.debug('Start of program') # Log start of program

# Log types and recommendations for use
logging.debug("Log debug: show details of variables.")
logging.info("Log info: records general information.")
logging.warning("Log warning: maybe a potential problem.")
logging.error("Log error: records issues.")
logging.critical("Logging critical: highest error level, fatal errors.")

# logging.disable(logging.CRITICAL) # disables logging for that level and below

# Logging to a file
file = open("errorLogging.txt", 'w')
file.close()

# https://stackoverflow.com/questions/12158048/changing-loggings-basicconfig-which-is-already-set
# Remove current logging basicConfig to set a new one
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Logs DEBUG and higher, or which ever level is specified
logging.basicConfig(filename="errorLogging.txt", level=logging.DEBUG, format = '%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug("Does this get written to file?")

'''
Debugging Functions

Continue - program executes until it reaches a breakpoint
Step in - execute the next line of code and wait
Step over - executes the next line of code. If next line is a function, it executes then resumes pause
Step out - Executes remaining lines of current function and pauses after it executes
Breakpoints - debugger will pause on user set breakpoints , usually for variable value inspection
'''

####################################################################
# Web scraping

nl()

# Web scraper program is available at the below link:
# myMap.py - Opens browser to map of address passed in by terminal or from the clipboard
# https://github.com/DJKC/AutomateBoringStuff/blob/master/myMap.py

import requests

print("CWD: ", os.getcwd())

reqUrl = ("https://automatetheboringstuff.com/files/rj.txt")
fileName = Path(reqUrl).name
fileSuffix = Path(reqUrl).suffix
# Downloads the url file passed in by string
req = requests.get(reqUrl)

# I am assuming the open function knows which stream data belings to the file
# 'wb' must be passed becuase file must be written in binary data
saveFile = open("DownloadedFile" + fileSuffix, 'wb')

# iter_content takes x amount of data and writes it to the file
# Saves in cwd
for chunk in req.iter_content(100000): # 100 Kb
    saveFile.write((chunk))

saveFile.close()

# Will thrown exception if there was an error downloading.
# Downloading file may or may not be crucial for your program.
# Exit program if downloads are necessary.
try:
    req.raise_for_status()
except Exception as err:
    print("There was a problem: %s" % (err))
    # Use %s and add variable to the end, very handy!

# checks status of the most recent request, report status
if req.status_code == requests.codes.ok: # 200, 404 is "Not Found"
    print("File " + fileName + " was downloaded successfully.")
else:
    print("File " + fileName + " was not downloaded successfully.")

print("Type of req: ", type(req))
print("Req.url: ", req.url)
print("Size of file: " + str(len(req.text)) + " characters.")
print("Text of file: ", req.text[0:250])# The plain text of the page source
print("\nRaw contents of file: ", req.content[0:250])# The raw bytes for the page source

nl()
'''
Thiss works but I didn't want to crowd the console screen witht html source.

# Pulls text from a webpage and writes it to a file
fetchedSiteUrl = "https://docs.wxwidgets.org/stable/pages.html"
# "exampleFetched.html"
req = requests.get("https://docs.wxwidgets.org/stable/pages.html")
fetchedSiteFile = open("exampleFetched.html", 'wb+')

for chunk in req.iter_content(100000):
    fetchedSiteFile.write(chunk)

fetchedSiteFile.seek(0)

if Path("exampleFetched.html").exists():
    print("exampleFetched.html" + " has been downloaded")

    for line in fetchedSiteFile.readlines():
        print(line)

    fetchedSiteFile.close()
'''

import pyperclip
# Creates html file and copies source code copied to the clipboard
fileName = "example.html"
pyperclip.copy(r'''<!-- This is the example.html example file. -->

<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="https://
inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>''')

if Path.exists(Path(fileName)):
    print(fileName + " already exists")
else:
    createFile = open("example.html", 'w+')
    createFile.write(pyperclip.paste())

    if Path.exists(Path(fileName)):
        print(fileName + " has been created")

        # Seeks to the beginning of the file because read marker is at the end after writing to file.
        # https://stackoverflow.com/questions/3266180/can-iterators-be-reset-in-python
        createFile.seek(0)
        fileText = createFile.read()
        print(fileText)
        createFile.close()
    else:
        assert str(fileName + " was not created")

import bs4
req = requests.get("https://duckduckgo.com")

try:
    req = requests.get("http://www.duckduckgo.com")
except Exception as err:
    print("There was a problem: ", err)

# The text version of the request is passed to bs4
# The bs4 object is stored in duckSoup
# The second argument is necessary
# Once the bs4 object is made, html can be parsed
# Instead of req.text, a local file can be specified
duckSoup = bs4.BeautifulSoup(req.text, 'html.parser')
print("Type: ", type(duckSoup))

# Can also use a file to open soup object
# with open("index.html") as fp:
#    soup = BeautifulSoup(fp)

duckSoup.select('div')
# duckSoup.select('#author) # selects id element with author attribute / tag
# duckSoup.select('.notice') # selects CSS class attributes named .notice
# duckSoup.select("p #author") # matches author tag inside a p element
# duckSoup.select("div > span") # matches span elements right under a div element
# duckSoup.select("div span") # matches span elements in a div tag
# duckSoup.select("input[name]") # matches element named input that has a name atttribute assigned to it
# duckSoup.select("input[type="button"]") # matches input elements with type element assigned "button

# Here I find the selected elements (author) from the web site and display them

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elementSoupSelect = exampleSoup.select("#author")
# Can also do select("#author")[0] to just store the first element
print("Number of author tags: ", len(elements))
print("Type of elements object: ", type(elements))
print("Type of elements[0]: ", type(elements[0]))
print("Whole elements[0] tag  str(elements[0]): ", str(elements[0]))
print("Text inside elements[0] elements[0].getText(): ", elements[0].getText())
print("Attribute / tag of elements[0] elements[0].attrs: ", elements[0].attrs)

# There are many other html elements accessible by bs4 variables
print("resultSoup.title: ", exampleSoup.title) # The title tag and text
print("resultSoup.title.name: ", exampleSoup.title.name) # name of the tag
print("resultSoup.title.string: ", exampleSoup.title.string) # text of the tag without the tag
# Can also do resultsSoup.p to print paragraph tags

# Prints all the paragraph in soup object
for paragraph in resultsSoup.find_all("p"):
    print(paragraph.string)

# https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search
# soup.findAll("div", {"id" : re.compile('date.*')}) # Regex can be used here

# https://icetutor.com/question/python-beautifulsoup-how-to-get-href-attribute-of-a-element/
# The ‘a’ tag in your html does not have any text directly,
# but it contains a ‘h3’ tag that has text. This means that
# text is None, and .find_all() fails to select the tag.
# Generally do not use the text parameter if a tag contains
# any other html elements except text content.

# https://stackoverflow.com/questions/38136424/python-beautifulsoup-request-to-scrape-search-engines
# Most of the results are dynamically loaded with JavaScript code.
# Requests only download the initial static HTML page.

# http://akul.me/blog/2016/beautifulsoup-cheatsheet/
# attribute value
# soup.select('a[href="http://example.com/elsie"]') # exact attribute
# soup.select('a[href^="http://example.com/"]') # negative match
# soup.select('a[href$="tillie"]') # end match
# soup.select('a[href*=".com/el"]') # middle match

# soup.find_all(["a", "b"]) # match by tag in list

# function (complex condition)
# def has_class_but_no_id(tag):
#   return tag.has_attr('class') and not tag.has_attr('id')
# soup.find_all(has_class_but_no_id)
#
# yanSoupResults = yanSoup.find_all("a")
# for item in yanSoupResults:
#     print(item.get("href"))

# helpful to do p = soupObject.p