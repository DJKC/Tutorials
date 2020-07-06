import math
from collections import deque


def nl(text=''):
    if (text != ''):
        {
            print('\n', "-----------", text, "--------------------------------\n")
        }

    else:
        {
            print('\n', text)
        }


def ex(text="-------"):
    print(text)


nl("LISTS!!!")  # ##########################################################

# creates empty list
jack = []

jack.append('Stella')
jack.append(3)
jack.append(True)

print(jack)

# the last element of the array
jack[-1] = 0
print(jack)

# the entire list is now empty
jack[:] = []
print(jack)

nl("FUNCTIONS")  # ##########################################################


def fib(n):
    a, b = 0, 1

    while (a < n):
        if (b > n):
            print(a, end='.')
        else:
            print(a, end=', ')

        a, b = b, b + a


nl("USER INPUT")  # ##########################################################

answer = 1000
# answer = int(input('Pick a number: '))

fib(answer)

answer = 'iery5ibyerkt7vwgrt'
# answer = input('Enter something: ')

nl("IF STATEMENTS")  # ##########################################################

if (type(answer) == int):
    print('This is an integer')
elif (type(answer) == chr):
    print('This is a char')
elif (type(answer) == str):
    print('This is a string')
else:
    print('This is not an int or string')

print('\n')

# lists can hold various types of data
varz = [1, True, 'Stella']

nl("FOR and IN STATEMENTS")  # ##########################################################

for var in varz:
    print(var, end=', ')
else:
    print("") # For can have an else as well.

nl("RANGE")  # ##########################################################

# iterates over the objects
print('0 - 4')
for i in range(5):
    print(i)

nl()
print('5 - 9')
for i in range(5, 10):
    print(i)

nl()
# starts at 0, goes until but not including 5, count by 2's
print('5 - 10 by 2\'s')
for i in range(5, 11, 2):
    print(i)

nl()

print(sum(range(0, 5, 1)))

nl()
# prints objects as a list
print(list(range(5)))

nl("PRIME NUMBER CALCULATOR")  # ##########################################################

# answer = int(input('Check primes through which number: '))
answer = 11

for i in range(2, answer):
    for j in range(2, i):
        if (i % j == 0):
            print(i, ' = ', j, ' * ', i // j)
            break

    else:
        print(i, ' is a prime number.')

l = nl

l("IF, IN and RAISE statements")  # ##########################################################


def ask(prompt='Enter some input with the number 1: ', retries=4, warn='Try again: '):
    while (True):
        # ok = input(prompt)
        ok = 1

        # if 'ok' appears in the object to the right
        if ok in ('1', 1):
            return True

        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries -= 1

        # exception handling
        if (retries <= 0):
            raise ValueError('Invalid user response')
        print(warn)


ask()
l("LISTS and APPENDING")  # ##########################################################


def f(a, L=[]):
    L.append(a)

    return L


print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):
    if (L is None):
        L = []

    L.append(a)

    return L


print(f(1))
print(f(2))
print(f(3))

l("Unpacking the * operator") # #################################################################
my_list = [1, 2, 3]
print(my_list)

my_list = [1, 2, 3]
print(*my_list) # Basically you are passing in the individual elements alone.


def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
print(my_sum(*list1, *list2, *list3)) # 45
# All three lists are unpacked. Each individual item is passed to my_sum()

my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a) # 1
print(b) # [2, 3, 4, 5]
print(c) # 6

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]
print(my_merged_list)
# [1, 2, 3, 4, 5, 6]

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}
print(my_merged_dict)
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

a = [*"RealPython"]
print(a)
# ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
l("KEYWORD, POSITIONAL(regular) and DICTIONARY arguments")  # #######################################


# keyword arg: an arg preceded by an identifier, "name ="
# or passed as a value in a dictionary preceded by **
# Keyword argument is similar to default argument, but any order is allowed
# Keyword args are in the form of def function(keywordArguments = some_value)
# The variables defined in the function must be the ones passed in
# Keyword arguments must come after regular arguments or else error
# Pos args are passed in by rvalue or in function call through var = value
# Pos arg values are plugged into first available variables without a value, they have to be first.
# The first parameter can be assigned by name as well in the function call
# *args and **args cannot be passed in by r-value in the function call.
def do_work(one, three='3', two='2'):
    print(one, two, three)


do_work(one=1, two=2)
do_work(two='3', three='33', one='55')
do_work(two='3', one='33')

l("Using *ARGS and **KWDS in function for UNLIMITED ARGUMENTOS!!!!!!!")  ##########################


# (*) After the positional args, if any, the remaining variable from the function call will
# be used as *args. There can be as many of these as you want from the function call.
# (**) There can be as many of these keywords args as you would like from the function call.
# In the above function, the kwrds are accessed like a dictionary inside the function.
# First is the var name (kw) and second the variable's value (kwds[kw]) in "for kw in kwds:"
# This differs from the do_work example above because in def cheese(), the line
# "print(kw, ':', kwds[kw])" below iterates through **kwds as they are not listed by name.
# Adding **kwds in do_work will allow the dictionary like iteration that is present in cheese()

def cheese(positional, *args, **kwds):
    print(positional)  # positional / regular

    for arg in args:
        print(arg, end='/')

    print('\n.........')

    for kw in kwds:
        print(kw, ':', kwds[kw])


def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result


def concatenate_k(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
# RealPythonIsGreat!
print(concatenate_k(a="Real", b="Python", c="Is", d="Great", e="!"))
# abcde
# If you don’t add .values(), function will iterate over the kwargs keys.

# K = 'k' marks the beginning of the keyword argument processing.
cheese('positional', 's', 'st', 'sta', 'standard', s="22", k='k', ke='ke', KEY='KEY')

cheese(1)

l("Using / and * for marking positional only and keyword only arguments")  ########################


def standard_arg(arg):
    print(arg)


# Using the / parameter marks as positional arguments only and CANNOT pass pos arg by keyword
# Ex. cannot use pos_only_arg(arg = "arg) for function call, only pos_only_arg("some value")
def pos_only_arg(arg, /):
    print("Positional only argument: ", arg)


pos_only_arg(1)


# pos_only_arg(arg = 1) is illegal in pos only mode


def kwd_only_arg(*, arg, arg1):
    for a in args:  # See [.1.] below, this won't work
        print(a)

    print(arg)
    print(arg1)
    # [.1.] Kwd_only_arg(a = 1, b = 2, c = 3) won't work
    # only ** in function definition marks the dictionary usage


# Cannot do **kwd_arg after using the * in below example. Only single args
def combined_example(pos_only, /, standard='standard', *, kwd_only='keyword'):
    print(pos_only, standard, kwd_only)


print('\nCombined example\n')

pos = 'positional'
# Will not work, as arg #3 is kwrd only. combined_example(1, 2, 3)
combined_example(1, standard='standard', kwd_only='keyword')
# Will not work, arg #1 is positional only. combined_example(pos_only=1, standard=2, kwd_only=3)

ex()

l("More Keyword dictionary stuff")  # ##########################################################


def foo(name, **kwds):
    return 'name' in kwds


print(foo(1, x=1, y=2, z=5, a=456, jayk='jake'))


def func_var_args(*args):
    print(args)


func_var_args(99, 2, '3')


def func_keyword_arg_dict(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)


def one_required_arg(req, *args, **kwrds):
    if (args):
        for arg in args:
            print(arg)

    if (kwrds):
        for kwrd in kwrds:
            print(kwrd, ': ', kwrds[kwrd])


one_required_arg(1, 2, 3, 4, q=5, r=5, s=7)

# The names of positional-only parameters can be used in **kwds without ambiguity.
# Need to specify using positional and kwrd if args have same name.
'''def foo(name, **kwds):
    return 'name' in kwds


foo(1, **{'name': 2})'''


# TypeError: foo() got multiple values for argument 'name'


def foo(name, /, **kwds):
    return 'name' in kwds


foo(1, **{'name': 2})

l("String manipulation, joining")  # ##########################################################


def joinStuff(*args, char='-'):
    return char.join(args)


print(joinStuff('2', '3', '4', '5'))

print(joinStuff('2', '3', '4', '5', char='*'))

l("Printing a dictionary passed as *args")  #########################################################
args = [3, 6]
print(list(range(*args)))

l()


def fortune(age, year=1990, yes='yes'):
    print('You are ', age, 'years and were born in ', year, end='\n')
    print('Is this correct: ', yes)


d = {'age': '22000', 'year': '199000', 'yes': 'no'}
# You are  {'age': '22000', 'year': '199000', 'yes': 'no'} years and were born in  1990
# The above line is the result of fortune(**d)
# Without the ** specifier, d is used one variable and uses the default parameters for the rest.
fortune(**d)

l("Lambdas and sorting key value pairs")  # ##########################################################


def inc(n):
    return lambda x: x + n


f = inc(100)
print(f(1))
print(f(1099))

pairs = [(1, 'z'), (2, 'd'), (30, 'r'), (4, 'z')]
pairs.sort(key=lambda pair: pair[1])
# sorted by index 1

print(pairs)

l("__doc__ aka Documentation strings")  # ##########################################################


def do_stuff():
    '''This line is viewed with f.__doc__), list brief details

    This line can only be viewed through the source code
    '''


print(do_stuff.__doc__)


# The colon after the arg name is the return type, the arrow after the the ) is the function return type
# These are used by the __annotations__ function for mark what is what.
def annotation(ham: str, eggs: str = '9') -> int:
    print('Annotations:, ', annotation.__annotations__)
    print('Arguments:, ', ham, eggs)

    return 9876


annotation('1', eggs='10')
# __annotations__ returns the type of each parameter as well as the return type.

nl('ITERATING, INSERTS AND EXTENDING LISTS')  # ##########################################################

iterable = 'ABC'
a = ['123', '456', '789']
print(a)
a[len(a):] = iterable
# a.extend(iterable) # is same as above.
# Takes every element from iterable and adds them as an a lone element to the end of a
print(a, " --->>> Length: ", len(a))

nl()

a = ['a', 'b', 'c']
a.insert(1, '90')
print(a)

# Removes first item equal to arg.
# It raises a ValueError if there is no such item.
a.remove('90')
print(a)

# Returns index of a
# Raises a ValueError if there is no such item.
print("Index of 'a': ", a.index('a'))

print("# occurences of 'x': ", a.count('x'))
# Return the number of times x appears in the list.

a.sort(key=None, reverse=True)
print(a)

a.copy()
# Returns a shallow copy, same a[:]

index = 2
print("Looking for 'a' starting at index[", index, "]\nFound at:", a.index('a', 2))
# Finds index of 'a' starting at and including # whatever
# It raises a ValueError if there is no such item.

print("a.pop(2):", a.pop(2))
# Returns value and removes index at 2 or last value if none given
print(a)

a = [None, 'james', 10]
# a.sort(), cannot sort because data type of None is not comparable to str, int etc.
print(a)

l("Nonlocal variables")
# nonlocal is used when a function nested in another function uses the outer
# function's variable. This allows the value to be used in the nested function.
# The nested function must be called to initialize the nonlocal variable
def func():
    x = 1

    def func2():
        nonlocal x
        x = 2

    func2()

    print("X = ", x)


l("Queues")  # ##########################################################

# deque can add to left and right side aka beginning and end
queue = deque(['A', 'B', 'C', 'D'])
queue.append('E')
queue.appendleft('AA')
queue.pop()
queue.popleft()
print(queue)
# Prints as "deque(['A', 'B', 'C', 'D'])" for some reason.

l()

squares = []
for x in range(10):
    squares.append(x ** 2)

# equivalent
squares = [x ** 2 for x in range(10)]

# equivalent
# Without the list below, it just says "<map object at 0x103977790>" much like a C++ memory address output.
squares = list(map(lambda x: x ** 2, range(10)))

print(squares)

l("Octal, Hex and conversions")  # ##########################################################
a = 0o10  # decimal 8 is octal 10
a = 0xa5  # decimal 165 is hex 165
hex(255)  # returns '0xff'
oct(8)  # returns '0o10
if (int('0x144', 16) == 324):  # returns int of 1st arg interpreted in base 2nd ard
    print("True")

l("Number to string conversion")  # ##########################################################
str(144)  # returns '144' string value
"{:04d}".format(144)  # returns '0144'
"{:.3f}".format(1.0 / 3.0)  # returns '0.333'

l("How do I modify a string in place? W/ Unicode")  ###############################################
import io

s = "Hello, world"
sio = io.StringIO(s)
sio.getvalue()
# 'Hello, world'
sio.seek(7)
# 7
sio.write("there!")
# 6
sio.getvalue()
# 'Hello, there!'

import array

a = array.array('u', s)
print(a)
# array('u', 'Hello, world')
a[0] = 'y'
print(a)
# array('u', 'yello, world')
a.tounicode()
# 'yello, world'

l("How do I use strings to call functions/methods?")  ##############################################
# The best is to use a dictionary that maps strings to functions.
# The primary advantage of this technique is that the strings do not
# need to match the names of the functions.
# This is also the primary technique used to emulate a case construct
# https://docs.python.org/3/faq/programming.html#how-do-i-use-strings-to-call-functions-methods
'''
def a():
    pass

def b():
    pass

dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs

dispatch[get_input()]()  # Note trailing parens to call function
'''

l("String to number conversion")  # ##########################################################
int('144')  # returns the int 144
float("144")  # returns 144.0

l("Making a list from coordinates and points")  ##################################################

var = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1]]  # if x != y]
print(var)

var = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1] if x != y]
print(var)

# same as above
var = []
for x in [1, 2, 3]:
    for y in [3, 2, 1]:
        if x != y:
            var.append((x, y))

vec = [-3, -2, -1, 0, 1, 2, 3]

print([v for v in vec if v >= 0])

print([v ** 2 for v in vec])

print(vec)

l("Removng characters from strings")  ########################################################
# doesn't work for character in middle of a string")

stuff = ['***cars', 'penci****ls', 'donkey****']
print(stuff)
print([item.strip('*') for item in stuff])

l()

print([(x, x ** 2) for x in range(0, 10, 2)])
# returns list of pairs [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64)]

l("List of lists") # ####################################################################
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l("Rounding to x number of digits in a loop")  ####################################################

pi = 3.14159265358979323
print([round(pi, i)for i in range(0, 6)])

# https://www.geeksforgeeks.org/as_integer_ratio-python-reduced-fraction-given-rational/
# function to print the fraction of
# a given rational number
def reducedfraction(d):
    # function that converts a rational number
    # to the reduced fraction
    b = d.as_integer_ratio()

    # reduced the list that contains the fraction
    return b


# driver code
b = reducedfraction(pi)
print
b[0], "/", b[1]

nl("Hexadecimal and exact decimal values, fractions")

# The float.hex() method expresses a float in hexadecimal (base 16)
# again giving the exact value stored by your computer:
x = 3.14159
x.hex() # '0x1.921f9f01b866ep+1'
# This precise hex method can be used to exactly reconstruct the float value
x == float.fromhex('0x1.921f9f01b866ep+1') # True

nl("Approximations with Numbers, Decimals and Rounding")
# Because of the way numbers are approximated, the below does not print true
if(1 + .1 + .1 == .3):
    print("True")
else:
    print("False")

# Instead, round as seen below for the answer you seek.
if(round(.1 + .1 + .1, 10) == round(.3, 10)):
    print("True")
else:
    print("False")

# math.fsum() tracks lost digits due to floating point representation
sum([0.1] * 10) == 1.0 # False

math.fsum([0.1] * 10) == 1.0 # True

from decimal import Decimal
from fractions import Fraction

Fraction.from_float(0.1)
# Fraction(3602879701896397, 36028797018963968)

(0.1).as_integer_ratio()
# (3602879701896397, 36028797018963968)

Decimal.from_float(0.1)
# Decimal('0.1000000000000000055511151231257827021181583404541015625')

format(Decimal.from_float(0.1), '.17')
# '0.10000000000000001

# https://docs.python.org/3/library/decimal.html#module-decimal
# For working more intricately with decimals

nl("Matrix made out of lists")  # ##############################################################
l("Parentheses () vs Square brackets []")
# () are for tuples and [] are for lists

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

x = matrix[0][0]

# makes a list containing the first index of each row, another with the 2nd index and so on.
print("print([[row[i] for row in matrix] for i in range(4)])")
print([[row[i] for row in matrix] for i in range(4)], "\n")

# prints the rows one at a time
print("print([row[i] for row in matrix for i in range(4)])")
print([row[i] for row in matrix for i in range(4)], "\n")

# without the [], an address is given. The [] dereferences the object and shows the data
print("print(row[i] for row in matrix for i in range(4))")
print((row[i] for row in matrix for i in range(4)), "\n")


'''
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Both the directly above and below are equivalent to the above matrix statement.

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''

l("Iterating through a tuple")
T = (10, 20, 30, 40, 50)
for var in T:
    print(T.index(var), var)

for var in range(len(T)):
  print(var, T[var])

l("Zip & Tuple lists")# ##############################################################################
# list(zipped_object) returns list of tuples
# zip() returns tuples
print(zip(*matrix))
# <zip object at 0x1028198c0>
print(zip(matrix))
# <zip object at 0x1028198c0>
print(list(matrix))
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix)
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(list(zip(*matrix)))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(list(zip(matrix)))
# [([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 10, 11, 12],)]
# print(list(*matrix))
# TypeError: list expected at most 1 argument, got 3

l("Split function")

txt = "welcome to the jungle"
x = txt.split()
print(x)

# ['welcome', 'to', 'the', 'jungle']

l("More zip practice") # ##########################################################

# https://realpython.com/python-zip-function/
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
# zip is made of two lists, so the tuples will have two elements each.
zipped = zip(numbers, letters)

print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')]

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
print(list(zip(s1, s2)))
# s1 and s2 are set objects, which don’t keep their elements in any particular order.
# This means that the tuples returned by zip() will have elements that are paired up randomly.

# A single argument zip
print(list(zip(s1)))

# use the tuple() function to display a readable version of the result:
a = (("John", "Charles", "Mike"), ("Jenny", "Christy", "Monica"), ("1", "2", "3"))

x = zip(a)
print(tuple(x))
# ((('John', 'Charles', 'Mike'),), (('Jenny', 'Christy', 'Monica'),), (('1', '2', '3'),))

x = zip(a)
print(list(x))
# [(('John', 'Charles', 'Mike'),), (('Jenny', 'Christy', 'Monica'),), (('1', '2', '3'),)]

x = zip(*a)
print(tuple(x))
# (('John', 'Jenny', '1'), ('Charles', 'Christy', '2'), ('Mike', 'Monica', '3'))

# When zipping, the shortest iterable will determine the length of the zip
list(zip(range(5), range(100)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)] because range(5) only has 5 elements

# To zip the longest instead, fills in missing values with 0
from itertools import zip_longest
print(list(zip_longest(range(5), range(100), fillvalue = 0)))

'''
Above is the same as the four below
x = zip(*a)
print(list(tuple(x)))

x = list(zip(*a))
print(tuple(x))

x = list(zip(*a))
print(list(tuple(x)))

x = list(zip(*a))
print(tuple(list(x)))
'''

l("Iterating using next()")
# iterator object can only be traversed once.

# next() retrieves the next item in the iterable.
a = ['foo', 'bar', 'baz']

itr = iter(a) #<list_iterator object at 0x031EFD10>
itr2 = iter(a)# can make multiple iterators of same object.
next(itr) # 'foo'
next(itr) # 'bar'
next(itr) # 'baz'
# StopIteration is thrown when at the end of iteration.
# itr2 can be used with next() as it is a separate object even when itr is at the end.

l("Iterating over multiple iterables/list in a zip") # ##########################################################
# This can be done with 2, 3 and more iterables.
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]

for let, num in zip(letters, numbers):
    print(f'Letter: {let}')
    print("Number:", num)

l("Add iterator behavior to a class")
# If class defines __iter__ and __next__
# If the class defines __next__(), then __iter__() can just return self


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index =  self.index - 1
        return self.data[self.index]


rev = Reverse("spam")
iter(rev)

for char in rev:
    print(char)


l("Using multiple dictionaries i a loop") # ##########################################################
dict_one = {'name': 'Khallid', 'last_name': 'Coulter', 'job': 'Mastermind'}
dict_two = {'name': 'Coulter', 'last_name': 'Khallid', 'job': 'Creator'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(f'{k1} is {v1}')
    print(k2, " | ", v2)
    print('\n')

l("Generators")
# Anything that can be done with generators can also be done with class-based iterators
# as described in the previous section. What makes generators so compact is that the
# __iter__() and __next__() methods are created automatically.
# Another key feature is that the local variables and execution state are automatically
# saved between calls. This made the function easier to write and much more clear than
# an approach using instance variables like self.index and self.data.

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


l("Generator expressions")
sum(i*i for i in range(10))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product

# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

l("Unpacking unzipping") # ##########################################################
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs) # * is the unpacking operator *.

print(numbers)
# (1, 2, 3, 4)
print(letters)
# ('a', 'b', 'c', 'd')

# Sorts by first variable type in tuple, so numbers for pair
pairs.sort()
print(pairs)
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Sorts by first variable type in tuple, so letters for opposite_pair
opposite_pair = sorted(zip(letters, numbers)) # Same as two lines below but combined
# opposite_pair = list(zip(letters, numbers))
# opposite_pair.sort()
print(opposite_pair)
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

opposite_pair = sorted(zip(letters, numbers))  # Sort by letters
    
l("Deleting elements from a list") # ##########################################################
# Like the pop function but returns nothing
a = [1, 2, 3, 4, 5]
del a[1:3]
print(a)

l("Tuples") # ##########################################################

j = 'rjk\''
tupletups = 1, True, 'dc', j
one_object_tuple = 'fff',  # needs comma afterwards
# Cannot reassign tuple variables tupletups[0] = 11
print(tupletups)
j = 'dfvfvvf'
# Tupletups will not be changed to include the new value of j
print(tupletups)

l("Checking for members in a set") # ##########################################################
# b = {}, cannot create an empty set like this. See below
b = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
# fast membership testing
if(('orange' or 'crabgrass') in basket):
    print("Yes, orange or crabgrass.")

l("Printing objects in set with logical operators") # ##########################################################
a = set('abracadabra')
b = set('alakazam')
print("Unique letters in a:", a)  # unique letters in a
print("Unique letters in b:", b)  # unique letters in b
print("Letters in a but not in b:", a - b)  # letters in a but not in b
print("Letters in a or b or both:", a | b)  # letters in a or b or both
print("Letters in both a and b:", a & b)  # letters in both a and b
print("Letters in a or b but not both:", a ^ b)  # letters in a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

l('Dictionaries') # ##########################################################
# A dictionary is a {key : value} pair

numbers = {}  # an empty dictionary
numbers = dict()  # also an empty dictionary
numbers = {'Mom': 12345, 'Dad': 1234, 'Cat': 123, 'Neighbor': 12, 'Police': 1}

# Print the data type of variable numbers.
print(type(numbers))
# Prints the value associated with the key 'Mom'
print(numbers['Mom'])
print(numbers)
# Deletes the key value pair of 'Police' : 1
del numbers['Police']
print(numbers)

# This prints the key, not the value.
print(list(numbers))
# ['Mom', 'Dad', 'Cat', 'Neighbor']
print(sorted(numbers))  # Clearly sorts the keys but on ABC order.
# Prints True if 'Jack' in numbers. False otherwise prints.
print('Jack' in numbers)

l("Creating a dictionary from values with dict()") # ##########################################################

# The square brackets are necessary below.
phonebook = dict([('Mom', 12345), ('Dad', 1234), ('Cat', 123), ('Neighbor', 12), ('Police', 1)])
print(phonebook)

green_pages = dict(Mom = 123456, Dad = 12345, Jackjack = 1234, Fido = 123)

l("Creating a dictionary with math functions, listing x and f(x)") # ##########################################################
math_dict = {x: x ** 2 for x in (1, 2, 3)}
print(math_dict)

l("Iterating through a dictionary with for") # ##########################################################
d = dict()
# Can access values array style.
for k in d:
    print(d[k])

# iterate through a dictionary’s values directly by using .values()
for v in d.values():
    print(v)
    
i, j = (1, 2)
print(i, j)
# 1 2

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
    
the_crew = {'Jake': 'funny guy', 'Jessie': 'tough girl', 'Jacob': 'Macho dude', 'James': 'the idiot',
            'Judas': 'the double agent'}
# *.items() is necessary to unpack and iterate through the dictionary pairs.
print('Name: ', 'Role:')
for k, v in the_crew.items():
    print(k, ':', v)
# Jake : funny guy...and so on.

l()
# same thing -> for i, v in enumerate(['a', 'aa', 'aaa']):
for i, v in enumerate(the_crew):
    print(i, v)
# 0 Jake...and so on.

l("Adding new / changing values in a dictionary with dict.update() ")
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']

a_list = list(zip((fields, values)))
# [(['name', 'last_name', 'age', 'job'],), (['John', 'Doe', '45', 'Python Developer'],)]
# The difference between a list and a dict.
a_dict = dict(zip(fields, values))
# {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}
# Field becomes the key and values is the value.

new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
# {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}

l("Formatting and iterating through zip objects") # #################################################

objects = {'black', 'day', 'up', 'out'}
opposites = {'white', 'night', 'down', 'in'}

for ob, op in zip(objects, opposites):
    print('What is the opposite of {0}? It is {1}'.format(ob, op))

l()


'''

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))'''

# lists all types of names: variables, modules, functions, etc.
# dir(module_name)
# list the names of built-in functions and variables.
# print(dir(__builtins__))

# import sound.effects.echo
# This loads the submodule sound.effects.echo. It must be referenced with its full name.
# sound.effects.echo.echofilter(input, output, delay=0.7, atten = 4)

# from sound.effects import echo
# echo.echofilter(input, output, delay=0.7, atten = 4)

# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten = 4)

l("File opening modes")  # ##########################################################
'''
'r' -> open for reading(default)
'w' -> open for writing, truncating the file first
'x' -> open for exclusive creation, failing if the file already exists
'a' -> open for writing, appending to the end of the file if it exists
'b' -> binary mode
't' -> text mode(default)
'+' -> open for updating(reading and writing)
'''

l("Writing JSN objects to files!!") # ##########################################################
# Files in text only mode, can only seek from beginning or end of file
f = open('test.txt', 'r+')
'''var = int(f.read())
var += 1
f.write(var)
print(var)'''
for line in f:
    print(line, end = '')

f.write("8765------\n")
f.truncate(0)

import json
jsonFile = json.dumps([1, 'simple', 2.2, True])
x = [5, 'u', True]
json.dump(x, f)
print(jsonFile)

f.close()
# Python pickles serializes python objects, aka cant be read by other languages.


l("Exceptions and base class catching") # ##########################################################
class Human(Exception):
    pass


class Baby(Human):
    pass


class Zygote(Baby):
    pass


for cls in [Human, Baby, Zygote]:
    try:
        raise cls()
    except Zygote:
        print("Zygote")
    except Baby:
        print("Baby")
    except Human:
        print("Human")
    except:
        print("Catch all")
# If except clause is the same class as the exception or the except clause
# is a base class of the exception, that clause will execute.

l('BTC STUFF')  # ##########################################################
# Leave a space after the colon as input doesn't add a space like print does.
btc = 0.5  # float(input("How much bitcoin to deposit: "))
# addresses = (int)(input("How many addresses to send to: "))

market_name = ["Cryptomixer", "Smartmixer", "Mixtum"]
market_multiplier = [0.05, 0.05, 0.05]
market_additional = [0.0005, 0.00023225, 0.00015]
markets = zip(market_name, market_multiplier, market_additional)

for n, m, a in markets:
    print(f'{n} cost: {round(m * btc + a, 6)}')
# print("{01:04d}".format(144))

l("CCXT STUFF")  # ##########################################################

import ccxt
count = 0
for ex in ccxt.exchanges:
    if(count % 10 == 0):
        spacer = '\n'
    else:
        spacer = ', '

    print(ex, end = spacer)
    count += 1

if("bitmex" in ccxt.exchanges):
    print("\n\nBitmex is here!")
else:
    print("\nBitmex is NOT here!")

nl("CLASSES")  # ##########################################################


# https://docs.python.org/3/faq/design.html#id7
class Class:
    # In python, self needs to be added to every class function
    # It is not automatically like in C++
    # __init__ is the constructor equivalent in Python
    # This function is called when the class instance is created. aka x = Class()
    def __init__(self, intz = 112):
        self.number = intz
        self.names = []
        print("Number is ", self.number)

    def add_name(self, name):
        self.names.append(name)

    # names = []
    # line above is now a var shared by all instances, bad idea usually


x = Class()

y = Class(1)


class Dog:
    # Variables who's values are shared by all members of class Dog
    kind = 'canine'

    # name is an instance variable
    def __init__(self, name):
        name = "dog"
        self.tricks = []
        # tricks is now unique to its class instance, an instance variable

    def add_tricks(self, new_trick):
        self.tricks.append(new_trick)

    def sound_off(self, tricks):
        print("I am a", self.name)
        print("My tricks are:", self.tricks)

l("Function Overridding")
# An overriding method in a derived class may in fact want to extend rather than simply
# replace the base class method of the same name. There is a simple way to call the base
# class method directly: just call BaseClassName.methodname(self, arguments)

l("Checking for instances and subclass instances")
# isinstance(object_to_check, is_instance_of_this_object)
isinstance(int, int)
#issubclass(object_to_check, is_subclass_of_this_object)
issubclass(bool, int)

l("Defining functions outside of class")

# Function defined outside the class, is strangely legal.
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

l("Naming conflicts, same name")
# If the same attribute name occurs in both an instance and in a class
# then attribute lookup prioritizes the instance:

l("Mangling, need to research further")
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)



n("OS,commands,cmd and STL")
# use the import os instead of from os import * or os.open() will shadow the built-in open()
import os
os.getcwd()      # Return the current working directory

os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell

import shutil

n("Math and Statistics")
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)

statistics.median(data)

statistics.variance(data)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
'''The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.'''

