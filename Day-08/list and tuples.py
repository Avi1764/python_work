Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
l=[10,9,5,3,6]
l
[10, 9, 5, 3, 6]
id(l)
1325471795520
l.append(37)
l
[10, 9, 5, 3, 6, 37]
l.append(28)
l
[10, 9, 5, 3, 6, 37, 28]
id(l)
1325471795520
l.insert(1,67)
l
[10, 67, 9, 5, 3, 6, 37, 28]
l.extend([89,90,57])
l
[10, 67, 9, 5, 3, 6, 37, 28, 89, 90, 57]
[10, 67, 9, 5, 3, 6, 37, 28, 89, 90, 57]
[10, 67, 9, 5, 3, 6, 37, 28, 89, 90, 57]
id(1)
140718631994488
l[3]
5
l[3]=34
l
[10, 67, 9, 34, 3, 6, 37, 28, 89, 90, 57]
l[5]=76
l
[10, 67, 9, 34, 3, 76, 37, 28, 89, 90, 57]
id(l)
1325471795520
l.pop()
57
l
[10, 67, 9, 34, 3, 76, 37, 28, 89, 90]
l.pop()
90
l
[10, 67, 9, 34, 3, 76, 37, 28, 89]
l.clear()
l
[]
del l(0)
SyntaxError: cannot delete function call
del l[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del l[0]
IndexError: list assignment index out of range
dell[0]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dell[0]
NameError: name 'dell' is not defined
l=[10, 67, 9, 34, 3, 76, 37, 28, 89, 90]
l
[10, 67, 9, 34, 3, 76, 37, 28, 89, 90]
l.pop(3)
34
l.pop(4)
76
l
[10, 67, 9, 3, 37, 28, 89, 90]
l.remove(9)
l
[10, 67, 3, 37, 28, 89, 90]
del l[1]
l
[10, 3, 37, 28, 89, 90]
id(l)
1325471668736
l
[10, 3, 37, 28, 89, 90]
max(1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    max(1)
TypeError: 'int' object is not iterable
max(l)
90
min(l)
3
sorted(2)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    sorted(2)
TypeError: 'int' object is not iterable
sorted(l)
[3, 10, 28, 37, 89, 90]
l.reverse(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    l.reverse(l)
TypeError: list.reverse() takes no arguments (1 given)
l.reverse()
l
[90, 89, 28, 37, 3, 10]
l.sort()
l
[3, 10, 28, 37, 89, 90]
l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
l.sort(reverse=True)
l
[90, 89, 37, 28, 10, 3]
sum(l)
257
l=[1,2,3]
m=[1,2,3]
n=1
n.append(2,3,4)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    n.append(2,3,4)
AttributeError: 'int' object has no attribute 'append'
n.append(4)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    n.append(4)
AttributeError: 'int' object has no attribute 'append'
n
1
l
[1, 2, 3]
id(l)==id(m)
False
i===m
SyntaxError: invalid syntax
l==m
True
n=l
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m=l.copy()
m
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
l
[1, 2, 3, 4]
all(0,'',[],(),set(),{},false)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    all(0,'',[],(),set(),{},false)
NameError: name 'false' is not defined. Did you mean: 'False'?
all(0,'',[],(),set(),{},False)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    all(0,'',[],(),set(),{},False)
TypeError: all() takes exactly one argument (7 given)
all([0,'',[],(),set(),{},false])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    all([0,'',[],(),set(),{},false])
NameError: name 'false' is not defined. Did you mean: 'False'?
all([0,'',[],(),set(),{},False])
False
all([1,'',[],(),set(),{},False])
False
any([0,'',[],(),set(),{},False])
False
any([1,'',[],(),set(),{},False])
True
l
[1, 2, 3, 4]
l.index(3)
2
l
[1, 2, 3, 4]
l.count(3)
1
l.count(5)
0
l
[1, 2, 3, 4]
l=[1,2,3,4],[5,6,7,8]
l
([1, 2, 3, 4], [5, 6, 7, 8])
l[0]
[1, 2, 3, 4]
l[1]
[5, 6, 7, 8]
l[0][3]
4
l[-1][-1]
8

#------------tuple---------------


t()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    t()
NameError: name 't' is not defined
t=()
t=tuple()
t=(1,12,11.3,3+5j,"str",[1,2],(1,2),{1,2},{1:2},True)
t
(1, 12, 11.3, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, True)
l
([1, 2, 3, 4], [5, 6, 7, 8])
l=(1,2,3)
m=(23,45,90)
l*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
45 in m
True
2 in l
True
m[1]
45
m[-1]
90
l[:2]
(1, 2)
t=(1,2,3,4,5,3)
t
(1, 2, 3, 4, 5, 3)
a,b,c,d,e,f=t
a
1
b
2
>>> f
3
>>> t(l)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    t(l)
TypeError: 'tuple' object is not callable
>>> t(1)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
>>> t=(1)
>>> t
1
>>> t=(1,)
>>> t
(1,)
>>> t=(78,4,542,556,67,767)
>>> t
(78, 4, 542, 556, 67, 767)
>>> max(t)
767
>>> 
>>> min(t)
4
>>> sorted(t)
[4, 67, 78, 542, 556, 767]
>>> sum(t)
2014
>>> t.index(556)
3
>>> t.count(542)
1
>>> t=((1,2),(3,4),(5,6),(7,8))
>>> t
((1, 2), (3, 4), (5, 6), (7, 8))
>>> t[1]
(3, 4)
>>> t[-1]
(7, 8)
>>> t[-1][-1]
8
>>> t[0][1]
2
