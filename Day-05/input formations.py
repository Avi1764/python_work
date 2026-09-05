Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=input()
dkjshiukvcihfjfku
x
'dkjshiukvcihfjfku'
name=input()
avinash
name
'avinash'
name=input("enter your name")
enter your name anil
name
' anil'
name=input("enter your name":)
SyntaxError: invalid syntax
name=input("enter your name:")
enter your name:anil
nmae
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    nmae
NameError: name 'nmae' is not defined
name
'anil'
price=int(input("enter the price:"))
enter the price:89.0
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    price=int(input("enter the price:"))
ValueError: invalid literal for int() with base 10: '89.0'
price=int(input("enter the price:"))
enter the price:12
price
12
names=input("enter the names:")
enter the names:anil avinash,ganesh
names
'anil avinash,ganesh'
names.split()
['anil', 'avinash,ganesh']
names=input("enter the names:").split()
enter the names:anil avinash ganesh
names
['anil', 'avinash', 'ganesh']
names=int(input("enter the names:"))
enter the names:1 2 3
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names=int(input("enter the names:"))
ValueError: invalid literal for int() with base 10: '1 2 3'
names=int(input("enter the names:").split())
enter the names:1,23,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names=int(input("enter the names:").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
names=input("enter the names:").split()
enter the names:1,2,3,4,5
names
['1,2,3,4,5']
map(int,names)
<map object at 0x000002B1E9AADD40>
list(map(int,names))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(map(int,names))
ValueError: invalid literal for int() with base 10: '1,2,3,4,5'
list(map(int,names))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(map(int,names))
ValueError: invalid literal for int() with base 10: '1,2,3,4,5'
values=list(map(int,input().split()))
1,2,34,5,6,9
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    values=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '1,2,34,5,6,9'
values=list(map(int,input().split()))
27290387 78 899 9 82
values
[27290387, 78, 899, 9, 82]
values=list(map(float,input().split()))
89.3 2 3 90.9
values
[89.3, 2.0, 3.0, 90.9]
names=tuple(input("enter your name").split())
enter your name anil avinash ganesh
names
('anil', 'avinash', 'ganesh')
names=set(input().split())
rwu weytr8 wew8y23
names
{'rwu', 'wew8y23', 'weytr8'}
values=set(map(int,input().split()))
7 7 9 6 5
values
{9, 5, 6, 7}
values=set(map(float,input().split()))
2 4 90.0 3 5 
values
{2.0, 3.0, 4.0, 5.0, 90.0}
a,b=(9,8)
a
9
b
8
a,b=[2,3]
a
2
b
3
email,password=input("enter the email and password:")
enter the email and password:aviansh@gmail.com 26282818
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    email,password=input("enter the email and password:")
ValueError: too many values to unpack (expected 2)
email,password=input("enter the email and password:").split()
enter the email and password:aviansh@gmail.com 26282818
email
'aviansh@gmail.com'
passwoed
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    passwoed
NameError: name 'passwoed' is not defined. Did you mean: 'password'?
password
'26282818'
a,b,c=list(map(int,input().split()))
a
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a'
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks=input().split()
avinash 99
name
'avinash'
marks
'99'
int(marks)
99
e=eval(input())
avinash
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'avinash' is not defined
>>> e=eval(input())
[1,2,3]
>>> e
[1, 2, 3]
>>> e=eval(input())
{1:1,2:1]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    {1:1,2:1]
            ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> e=eval(input())
{1:1,2:1}
>>> e
{1: 1, 2: 1}
>>> e=eval(input())
89.09
>>> e
89.09
>>> e=eval(input())
(78,892,838,09)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    (78,892,838,09)
                ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> e=eval(input())
88 7819 99
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    88 7819 99
       ^^^^
SyntaxError: invalid syntax
>>> e=eval(input())
(627,8789)
>>> e
(627, 8789)
