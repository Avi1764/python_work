Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
datatypes(int,float,complex,str,tuple,set,dict,bool)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    datatypes(int,float,complex,str,tuple,set,dict,bool)
NameError: name 'datatypes' is not defined
a = 20
a
20
float(a)
20.0
complex(a)
(20+0j)
str(a)
'20'
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
f = 20.45
f
20.45
int(f)
20
complex(a)
(20+0j)
complex(f)
(20.45+0j)
str(f)
'20.45'
tuple(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
bool(f)
True
complex(avinash)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    complex(avinash)
NameError: name 'avinash' is not defined
c = (avinash)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c = (avinash)
NameError: name 'avinash' is not defined
c = 2+10j
c
(2+10j)
complex(c)
(2+10j)
int(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+10j)'
tuple(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s = ('avinash')
s
'avinash'
int(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'avinash'
float(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'avinash'
complex(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
str(s)
'avinash'
tuple(s)
('a', 'v', 'i', 'n', 'a', 's', 'h')
set(s)
{'v', 'n', 'h', 's', 'i', 'a'}
bool(s)
True
dict(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
f = ('chintu',9.0,1,2)
f
('chintu', 9.0, 1, 2)
int(f)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(f)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(f)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(f)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(f)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(f)
TypeError: complex() argument must be a string or a number, not tuple
str(s)
'avinash'
tuple(f)
('chintu', 9.0, 1, 2)
set(f)
{9.0, 2, 'chintu', 1}
dict(f)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(f)
ValueError: dictionary update sequence element #0 has length 6; 2 is required
bool(f)
True
l = [1,2,3,3,4]
l
[1, 2, 3, 3, 4]
int(l)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 2, 3, 3, 4]'
tuple(l)
(1, 2, 3, 3, 4)
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> d {'avinash',1,2}
SyntaxError: invalid syntax
>>> d = {'avinash',1,2}
>>> d
{1, 2, 'avinash'}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'set'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not set
>>> str(d)
"{1, 2, 'avinash'}"
>>> tuple(d)
(1, 2, 'avinash')
>>> set(d)
{1, 2, 'avinash'}
>>> list(d)
[1, 2, 'avinash']
>>> bool(d)
True
>>> int - float, complex, str, bool
... float - int, complex, str, bool
... complex - str, bool
... str - list, tuple, set, bool
... list - str, tuple, set, bool
... tuple - str, list, set, bool
... set - str, list, tuple, bool
... dict - str, list, tuple, set, bool
