Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,565,75,675,7856,8986,8898}
s
{1, 2, 3, 675, 8898, 75, 7856, 565, 8986}
s.add(1)
s.add(12.3)
s.add(2+4j)
c.add()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c.add()
NameError: name 'c' is not defined
s.add('str')
s.add(1,2,3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.add(1,2,3)
TypeError: set.add() takes exactly one argument (3 given)
s.add(True)
s
{1, 2, 3, 675, 8898, 'str', 75, 12.3, (2+4j), 7856, 565, 8986}
s.add(False)
s
{False, 1, 2, 3, 675, 8898, 'str', 75, 12.3, (2+4j), 7856, 565, 8986}
s={1,2,3,4,5,33,2,1,2}
s
{1, 2, 3, 4, 5, 33}
l={10,1,2,3}
m={29,2,3,5}
l+m
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
l[0]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l[0]
TypeError: 'set' object is not subscriptable
l={10,1,2,3}
m={29,2,3,5}

l
{10, 1, 2, 3}
m
{29, 2, 3, 5}
a|b
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a|b
NameError: name 'a' is not defined
a | b
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a | b
NameError: name 'a' is not defined
l|m
{1, 2, 3, 5, 10, 29}
l&m
{2, 3}
l-m
{1, 10}
l^m
{1, 5, 10, 29}
{1}<=a
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    {1}<=a
NameError: name 'a' is not defined
{1}<=l
True
{1,2,3}<=l
True
{1,2,3,4,5}<=m
False
l>={2,4,5}
False
m>={2,3,5}
True
l
{10, 1, 2, 3}
m
{29, 2, 3, 5}
l.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    l.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?

l.isdisjoint(m)
False
m.isdisjoint(l)
False
l.union(m)
{1, 2, 3, 5, 10, 29}
l.intersection(m)
{2, 3}
s.difference(m)
{1, 4, 33}
l^m
{1, 5, 10, 29}
l
{10, 1, 2, 3}
m
{29, 2, 3, 5}
min(l)
1
max(m)
29
sum(l)
16
l=m
m
{29, 2, 3, 5}
sorted(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    sorted(a)
NameError: name 'a' is not defined
sorted(l)
[2, 3, 5, 29]
l.add(45)
l
{2, 3, 5, 45, 29}
l.update([46,9])
l
{2, 3, 5, 9, 45, 46, 29}
m.copy()
{2, 3, 29, 5, 9, 45, 46}
c=m.copy()
c
{2, 3, 29, 5, 9, 45, 46}
c.add(12)
c.add(7)
c
{2, 3, 5, 7, 9, 12, 29, 45, 46}
l
{2, 3, 5, 9, 45, 46, 29}
c
{2, 3, 5, 7, 9, 12, 29, 45, 46}
c.pop()
2
c.remove(12)
c
{3, 5, 7, 9, 29, 45, 46}
a.discard(12)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.discard(12)
NameError: name 'a' is not defined
c.discard(12)
c.discard(9)

c
{3, 5, 7, 29, 45, 46}
c.clear()
c
set()
a=frozenset{1,2,3,56,776,825,878}
SyntaxError: invalid syntax
a=frozenset({1,2,3,56,776,825,878})
a
frozenset({1, 2, 3, 776, 825, 56, 878})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
#.............dictionary...............................................


d={}
d=dict{}
SyntaxError: invalid syntax
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1':'k2':'v2':'k3'}
SyntaxError: invalid syntax
d={'k1':'v1':'k2':'v2':'k3':'v3'}


invalid syntaxd={'k1':'v1','k2':'v2','k3':'v3'}
SyntaxError: invalid syntax
d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2736091933760
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='flt'
d
{1: 'int', 12.3: 'flt'}
d['str']='string'
d
{1: 'int', 12.3: 'flt', 'str': 'string'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'flt', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d=[frozenset({1,2,3,4})]='frozenaet'
SyntaxError: cannot assign to function call
d=[frozenset({1,2,3,4})]='frozenset'
SyntaxError: cannot assign to function call
d=['frozenset'({1,2,3,4})]='frozenset'
SyntaxError: cannot assign to function call
d[frozenset({1,2,3,4})]='frozenset'
d
{1: 'int', 12.3: 'flt', 'str': 'string', (1, 2, 3, 4): 'tuple', frozenset({1, 2, 3, 4}): 'frozenset'}
d={}
d[1]=1
d[2]=12.3
d[3]=12+4j
d[4]='str'
d[5]=[1,2,3]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 in d
False
>>> str in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3]
>>> d[8]
{1: 1}
>>> d[9]
True
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10,'key is not present')
'key is not present'
>>> d[3]=4
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
