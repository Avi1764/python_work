Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 20
b = 10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**b
10240000000000
a=20
b=30
a>b
False
a<b
True
a<=b
True
a>=b
False
a==b
False
a!=b
True
#assignment operators
c=20
c=c+10
c
30
c=c+10
c
40
c += 10
c
50
c-=10
c
40
c*=2
c
80
c//=2
c
40
c**=2
c
1600
c%=2
c
0
c%=3
c
0
#Relational or logical operators
c=20
c/=2
c
10.0
True and True
True
n=20
n%2
0
n=20
n%=2
n
0
n=10
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%8==0 or n%3==0
False
n
10
n<5
False
not n<5
True
#collection of elements(str,list,tuple,set,dict)
s='avinash'
v in s
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    v in s
NameError: name 'v' is not defined
'v' in s
True
'p' in s
False
'i' not in s
False
'k not in s
SyntaxError: unterminated string literal (detected at line 1)
'k' not in s
True
a=[1,2,3,4]
'1' in a
False
'1' not in a
True
1 in a
True
1 not in a
False
#tuple
t=(2,3,4,6)
7 not in t
True
6 in t
True
3 in t
True
# set
s={9,8,0,6}
5 in s
False
0 in s
True
# dict
d={'name':'avinash','batch:63,'course':'python'}
   
SyntaxError: unterminated string literal (detected at line 1)
d={'name':'avinash','batch':63,'course':'python'}
   
'name' in d
   
True
'avinash' in d
   
False
'python' not in a
   
True
'python' not in d
   
True
'python' in d
   
False
#identity operators
   
l=[1,2,3]
   
m=[1,2,3]
   
id(l)
   
1487130396928
id(m)
   
1487130241792
i is m
   
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    i is m
NameError: name 'i' is not defined. Did you mean: 'id'?
l is m
   
False
n=1
   
id(n)
   
140719275558008
n=1
   
id(l)
   
1487130396928
l is n
   
False
n=l
   
id(l)
   
1487130396928
l is n
   
True
#difference b/w mutable and immutable
   
# "mutable" means we can change the elements with in the element
   
# "immutable"means we cannot change the elements with in the elements
   
a=20
   
id(a)
   
140719275558616
s={1,2,3,4}
   
id(s)
   
1487130011104
s.add(5)
   
s
   
{1, 2, 3, 4, 5}
id(s)
   
1487130011104
#bitwise operators
   
9&10
   
8
9|10
   
11
a^10
   
30
9^10
   
3
8>>2
   
2
8<<2
   
32
~8
   
-9
-9
   
-9
~13
   
-14
-13
   
-13
~45
   
-46
#output statements
   
a=10
   
b=20
   
c='avinash'
   
print(a,b,c)
   
10 20 avinash
print("a value is",a)
   
a value is 10
print("a value is",a "| b value is",b "| c value is",c)
   
SyntaxError: invalid syntax
print("a value is",a,"| b value is",b,"| c value is",c)
   
a value is 10 | b value is 20 | c value is avinash
print(a,b,c)
   
10 20 avinash
print(a,b,c,sep='')
   
1020avinash
print(a,b,c,sep='\n')
   
10
20
avinash
print(a,b,c,sep='\t')
   
10	20	avinash
print(a,b,c,sep'\t',end='@')
   
SyntaxError: invalid syntax
print(a,b,c,sep='\t',end='@')
   
10	20	avinash@
print(a,b,c,sep='\t',end='\n\n')
   
10	20	avinash

>>> print(f'a={a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c}')
...       
a=10 b=20 c=avinash
>>> print('a={a} b={b} c={c})
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('a={a} b={b} c={c}')
...       
a={a} b={b} c={c}
>>> print(f'a value is {a} | b value is {b} | c value is {c}')
...       
a value is 10 | b value is 20 | c value is avinash
>>> print('a=%d b=%f c=%s'%(a,b,c))
...       
a=10 b=20.000000 c=avinash
>>> print('a=%d b=2.f c=%s'%(a,b,c))
...       
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    print('a=%d b=2.f c=%s'%(a,b,c))
TypeError: not all arguments converted during string formatting
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...       
a=10 b=20.00 c=avinash
>>> print('a={} | b={}
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('a={} | b={} | c={} .format(c,b,a))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('a={} | b={} | c={} .format(c,b,a)')
...       
a={} | b={} | c={} .format(c,b,a)
>>> print('a={} | b={} | c={}' .format(c,b,a))
...       
a=avinash | b=20 | c=10
>>> print('a={} | b={} | c={}' .format(a,b,c))
...       
a=10 | b=20 | c=avinash
>>> print('a={1} | b={2} | c={0}' .format(c,b,a))
...       
a=20 | b=10 | c=avinash
