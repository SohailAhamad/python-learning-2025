Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pyperclip
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'
import pyperclip
pyperclip.copy('Hello World')
pyperclip.paste()
'Hello World'

================ RESTART: D:/Power BI/Python/function.py ===============
howdy
Hello there!!
howdy
Hello there!!
import pyperclip
pyperclip.copy('Yes This is working')
pyperclip.paste
<function init_windows_clipboard.<locals>.paste_windows at 0x00000244207014E0>
pyperclip.paste()
'Yes This is working'
'Hello has ' + str(len('hello')) + 'letters in it'
'Hello has 5letters in it'
'Hello has ' + str(len('hello')) + ' letters in it'
'Hello has 5 letters in it'

============== RESTART: D:/Power BI/Python/num_function.py =============
6
None
print('None')
None

=============== RESTART: D:/Power BI/Python/try_except.py ==============
21.0
3.5
Error: You tried to divide by zero.
None
42.0

============== RESTART: D:/Power BI/Python/try_except2.py ==============
how many cats do you have?
six
You did not enter a number

============== RESTART: D:/Power BI/Python/try_except2.py ==============
how many cats do you have?
8
That is a lot of cats

============== RESTART: D:/Power BI/Python/guess_number.py =============
hello.What is your name?
sohail
Well,sohail, I am thinking of a number between 1 to 10
Traceback (most recent call last):
  File "D:/Power BI/Python/guess_number.py", line 8, in <module>
    secretNumber = random.radint(1,10)
AttributeError: module 'random' has no attribute 'radint'. Did you mean: 'randint'?

============== RESTART: D:/Power BI/Python/guess_number.py =============
hello.What is your name?
sohail
Well,sohail, I am thinking of a number between 1 to 10
Take a guess.

Traceback (most recent call last):
  File "D:/Power BI/Python/guess_number.py", line 12, in <module>
    guess = int(input())
ValueError: invalid literal for int() with base 10: ''

============== RESTART: D:/Power BI/Python/guess_number.py =============
hello.What is your name?
sohail
Well,sohail, I am thinking of a number between 1 to 10
Take a guess.
3
Your guess is too high.
Take a guess.
1
Your guess is too low.
Take a guess.
2
GoodJob,sohail! you guessed my number in 3guesses.

spam = ['cat','rat','elephant']
spam
['cat', 'rat', 'elephant']
'the' + spam[1] + 'is afraid of' + spam[0]
'theratis afraid ofcat'
'the ' + spam[1] + ' is afraid of ' + spam[0]
'the rat is afraid of cat'
spam='hello'
spam
'hello'
spam=[10,20,30]
spam[2] = 'sohail'
spam
[10, 20, 'sohail']
[10, 20, 'sohail']
[10, 20, 'sohail']

spam = ['a','b','c']
spam
['a', 'b', 'c']
spam[3:5] = ['d','e']
spam
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd', 'e']
spam[:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
spam[:3]
['a', 'b', 'c']

del spam[3]
spam
['a', 'b', 'c', 'e']
['a', 'b', 'c', 'e']
['a', 'b', 'c', 'e']
'z' in spam
False
'c' in spam
True
'z' not in spam
True




fruits = ['apple','banana','peach','orange']
for i in range(len(fruits)):
    print('Index' + str(i) + ' in fruits is' + fruits(i))

Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print('Index' + str(i) + ' in fruits is' + fruits(i))
TypeError: 'list' object is not callable
for i in range(len(fruits)):
    print('Index' + str(i) + ' in fruits is' + fruits[i])

    
Index0 in fruits isapple
Index1 in fruits isbanana
Index2 in fruits ispeach
Index3 in fruits isorange
fruits.index('apple')
0
fruits.append('pear')
fruits
['apple', 'banana', 'peach', 'orange', 'pear']
spam.insert(3,'Guava')
spam
['a', 'b', 'c', 'Guava', 'e']
spam.remove('Guava')
spam
['a', 'b', 'c', 'e']
fruits.sort()
fruits
['apple', 'banana', 'orange', 'peach', 'pear']
fruits.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    fruits.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
fruits.sort(reverse=True)
fruits
['pear', 'peach', 'orange', 'banana', 'apple']
list('Hello')
['H', 'e', 'l', 'l', 'o']
name = 'Sohail'
name[2:5]
'hai'
name = 'leo the cat'
newname = name[0:3] + 'a' + name[9:12]
newname
'leoaat'
newname = name[0:4] + ' a ' + name[8:12]
newname
'leo  a cat'
list(123)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list(123)
TypeError: 'int' object is not iterable
list('123')
['1', '2', '3']
fruits = check
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    fruits = check
NameError: name 'check' is not defined
fruits = ['apple','banana','peach']
fruits=check
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    fruits=check
NameError: name 'check' is not defined
fruits
['apple', 'banana', 'peach']
check = fruits
check
['apple', 'banana', 'peach']
check[1] = ['mango']
fruits
['apple', ['mango'], 'peach']
check.append('Guava')
fruits
['apple', ['mango'], 'peach', 'Guava']
check[3]
'Guava'
check
['apple', ['mango'], 'peach', 'Guava']
del check[1]
check
['apple', 'peach', 'Guava']
checl.sort()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    checl.sort()
NameError: name 'checl' is not defined. Did you mean: 'check'?
check.sort()
check
['Guava', 'apple', 'peach']

================== RESTART: D:/Power BI/Python/test.py =================
Emails: ['sohail@email.com', 'backup@work.com']
Phones: ['987-654-3210']
myCat = { 'size' : 'fat' , 'color' : 'gray', 'dispotion' : 'loud' }
myCat['dispotion']
'loud'
'color' in myCat
True
list(myCat.key())
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    list(myCat.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
list(myCat.keys())
['size', 'color', 'dispotion']
list(myCat.values())
['fat', 'gray', 'loud']
list(myCat.items())
[('size', 'fat'), ('color', 'gray'), ('dispotion', 'loud')]
for k in myCat.keys():
    print(k)

size
color
dispotion
for k in myCat.values():
    print(k)

    
fat
gray
loud
for k,v in myCat.items():
    print(k,v)

    
size fat
color gray
dispotion loud
'color' in myCat.keys()
True
myCat.get('color',0)
'gray'
myCat.get('null',0)
0
myCat.setdefault('name','leo')
'leo'
myCat
{'size': 'fat', 'color': 'gray', 'dispotion': 'loud', 'name': 'leo'}

============= RESTART: D:/Power BI/Python/charactercount.py ============
Traceback (most recent call last):
  File "D:/Power BI/Python/charactercount.py", line 6, in <module>
    count[character] = cpunt[character] + 1
NameError: name 'cpunt' is not defined. Did you mean: 'count'?

============= RESTART: D:/Power BI/Python/charactercount.py ============
{' ': 14, 'I': 1, 't': 6, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}

============= RESTART: D:/Power BI/Python/charactercount.py ============
{' ': 14, 'I': 7, 'T': 6, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}

============= RESTART: D:/Power BI/Python/charactercount.py ============
{'I': 7, 'T': 6, ' ': 13, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}

============= RESTART: D:/Power BI/Python/charactercount.py ============
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 5,
 'B': 1,
 'C': 3,
 'D': 3,
 'E': 5,
 'G': 2,
 'H': 3,
 'I': 7,
 'K': 2,
 'L': 3,
 'N': 4,
 'O': 2,
 'P': 1,
 'R': 5,
 'S': 3,
 'T': 6,
 'W': 2,
 'Y': 1}
theBoard = { 'top-L': ' ','top-M': ' ','top-R': ' ','mid-L': ' ','mid-M': ' ','mid-R': ' ','mid-L': ' ','mid-M': ' ','mid-R': ' ' }
theBoard
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' '}
import pprint
pprint.pprint(theBoard)
{'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
theBoard.append('low-L': ' ', 'low-M': ' ', 'low-R': ' ')
SyntaxError: invalid syntax
theBoard.setdefault('low-L': ' ', 'low-M': ' ', 'low-R': ' ')
SyntaxError: invalid syntax
theBoard.setdefault('low-L', ' ', 'low-M',' ', 'low-R', ' ')
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    theBoard.setdefault('low-L', ' ', 'low-M',' ', 'low-R', ' ')
TypeError: setdefault expected at most 2 arguments, got 6
theBoard.setdefault('low-L', ' ')
' '
theBoard
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' '}
theBoard.setdefault('low-M', ' ')
' '
theBoard.setdefault('low-L', ' ')
' '
import pprint
pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
theBoard.setdefault('low-T', ' ')
' '
theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-T': ' ',
 'mid-L': ' ',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
def printBoard(board):
    print(board[top-L] + '|' + board[top-M] + '|' + board[top-R] + '|')
    print('-----')
    print(board[mid-L] + '|' + board[mid-M] + '|' + board[mid-R] + '|')
    print('-----')
    print
KeyboardInterrupt

=============== RESTART: D:/Power BI/Python/tictactoe.py ===============
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> def printBoard(board):
...     print(board[top-L] + '|' + board[top-M] + '|' + board[top-R] + '|')
...     print('-----')
...     print(board[mid-L] + '|' + board[mid-M] + '|' + board[mid-R] + '|')
...     print('-----')
...     print(board[low-L] + '|' + board[low-M] + '|' + board[low-R] + '|')
... 
...     
>>> 
>>> print(theBoard)
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> printBoard(theBoard)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    printBoard(theBoard)
  File "<pyshell#133>", line 2, in printBoard
    print(board[top-L] + '|' + board[top-M] + '|' + board[top-R] + '|')
NameError: name 'top' is not defined
>>> def printBoard(board):
...     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
...     print('-----')
...     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
...     print('-----')
...     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|')
... 
...     
>>> printBoard(theBoard)
 | | |
-----
 | | |
-----
 | | |
