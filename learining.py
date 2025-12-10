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
>>> list('123')
['1', '2', '3']
>>> fruits = check
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    fruits = check
NameError: name 'check' is not defined
>>> fruits = ['apple','banana','peach']
>>> fruits=check
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    fruits=check
NameError: name 'check' is not defined
>>> fruits
['apple', 'banana', 'peach']
>>> check = fruits
>>> check
['apple', 'banana', 'peach']
>>> check[1] = ['mango']
>>> fruits
['apple', ['mango'], 'peach']
>>> check.append('Guava')
>>> fruits
['apple', ['mango'], 'peach', 'Guava']
>>> check[3]
'Guava'
>>> check
['apple', ['mango'], 'peach', 'Guava']
>>> del check[1]
>>> check
['apple', 'peach', 'Guava']
>>> checl.sort()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    checl.sort()
NameError: name 'checl' is not defined. Did you mean: 'check'?
>>> check.sort()
>>> check
['Guava', 'apple', 'peach']
