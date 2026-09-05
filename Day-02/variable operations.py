Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> A=10
>>> a
10
>>> A
10
>>> a=b=c=20
>>> a
20
>>> b
20
>>> c
20
>>> a,b,c=30
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a,b,c=30
TypeError: cannot unpack non-iterable int object
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c
NameError: name 'c' is not defined
