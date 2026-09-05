Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='string.py'
c.startwith('str')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
c.startswith('str')
True
c.startswith('python')
False
isalpha('hello')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    isalpha('hello')
NameError: name 'isalpha' is not defined
c.isalpha('hello')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c.isalpha('hello')
TypeError: str.isalpha() takes no arguments (1 given)
'hello'.isalpha()
True
c.endseith('python')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c.endseith('python')
AttributeError: 'str' object has no attribute 'endseith'. Did you mean: 'endswith'?
c.endsweith('python')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c.endsweith('python')
AttributeError: 'str' object has no attribute 'endsweith'. Did you mean: 'endswith'?
>>> c.endswith('python')
False
>>> c.endswith('py')
True
>>> c.islower()
True
>>> c.isupper()
False
>>> 'AVINASH'.isupper()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> 'HELLO WORLD'istitle()
SyntaxError: invalid syntax
>>> 'HELLO WORLD'.istitle()
False
>>> 'Hello World'.istitle()
True
>>> 'variable1'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> #list
>>> #list............
>>> l=[1,2,3,4,3,2,1]
>>> l
[1, 2, 3, 4, 3, 2, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[3,4,5]
>>> l+m
[1, 2, 3, 4, 3, 4, 5]
>>> m*3
[3, 4, 5, 3, 4, 5, 3, 4, 5]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
