Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> count = 20
>>> count
20
>>> tyoe(count)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tyoe(count)
NameError: name 'tyoe' is not defined. Did you mean: 'type'?
>>> type(count)
<class 'int'>
>>> price = 79.90
>>> price
79.9
>>> type(price)
<class 'float'>
>>> c = 10+8j
>>> c
(10+8j)
>>> type(c)
<class 'complex'>
>>> a = "codegnan"
>>> a
'codegnan'
>>> type(a)
<class 'str'>
>>> s = [1,2,5,6,6]
>>> s
[1, 2, 5, 6, 6]
>>> type(s)
<class 'list'>
>>> r = [avinash,lokesh,vikas,bharath,2,5,]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    r = [avinash,lokesh,vikas,bharath,2,5,]
NameError: name 'avinash' is not defined
>>> r = [avinash,ganesh,vikas,bharath]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    r = [avinash,ganesh,vikas,bharath]
NameError: name 'avinash' is not defined
>>> r = ['avinash','vikas','ganesh','bharath']
>>> r
['avinash', 'vikas', 'ganesh', 'bharath']
>>> type(r)
<class 'list'>
a = {'japan','china','india',2,5,9,0}
a
{0, 2, 'japan', 5, 'india', 9, 'china'}
type(a)
<class 'set'>
t = ('avinash','sowmya','ganesh',9.0,5,6)
t
('avinash', 'sowmya', 'ganesh', 9.0, 5, 6)
type(t)
<class 'tuple'>
s = {}
s
{}
type(s)
<class 'dict'>
s = {'chintu','bobby',[1,2,2],9,0}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s = {'chintu','bobby',[1,2,2],9,0}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s = {'name','age','gender'}
s
{'name', 'gender', 'age'}
type(s)
<class 'set'>
t = None
t
status = None
status
type(status)
<class 'NoneType'>
s = frozenset({1,8,9,0})
s
frozenset({0, 1, 8, 9})
type(s)
<class 'frozenset'>
