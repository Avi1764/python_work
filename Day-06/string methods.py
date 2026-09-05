Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='avinash paleti'
len(c)
14
ord('a')
97
ord('p')
112
chr(98)
'b'
chr(67)
'C'
chhr(23)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    chhr(23)
NameError: name 'chhr' is not defined. Did you mean: 'chr'?
chr(23)
'\x17'
min(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    min(a)
NameError: name 'a' is not defined
min(c)
' '
sorted(c)
[' ', 'a', 'a', 'a', 'e', 'h', 'i', 'i', 'l', 'n', 'p', 's', 't', 'v']
max(c)
'v'
c='avinash programming'
c.upper()
'AVINASH PROGRAMMING'
c.lower()
'avinash programming'
c.captalize()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize()
'Avinash programming'
c.title()
'Avinash Programming'
c.swapcase()
'AVINASH PROGRAMMING'
c.casefold()
'avinash programming'
'ige8rwehjfuhhe8rujfrg'.casefold()
'ige8rwehjfuhhe8rujfrg'
c
'avinash programming'
c.center(50'-')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
c.center(60'-')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
KeyboardInterrupt
c.center(50,'-')
'---------------avinash programming----------------'
c.center(50'0')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
c.center(50,'0')
'000000000000000avinash programming0000000000000000'
c.rjust(50,'-')
'-------------------------------avinash programming'
'12'.zfill(10)
'0000000012'
c.ljust(50,'-')
'avinash programming-------------------------------'
c
'avinash programming'
c.find('a')
0
c.find('s')
5
c.find('l')
-1
c.rfind('m')
15
c.index('m')
14
c.rindex('m')
15
c.index('m')
14
c.index('z')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c
'avinash programming'
c.count('a')
3
c.count('m')
2
c.count('p')
1
c
'avinash programming'
c.replace('a','l')
'lvinlsh progrlmming'
c.replace('string','float')
'avinash programming'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'1v3n1sh pr4gr1mm3ng'
c.translate(c.maketrans('aeiou','*****'))
'*v*n*sh pr*gr*mm*ng'
s='string is immutable'
s
'string is immutable'
s.split()
['string', 'is', 'immutable']
'string is immutable'.split()
['string', 'is', 'immutable']
KeyboardInterrupt
'string is immutable'.split('-')
['string is immutable']
'string is immutable'.rsplit()
['string', 'is', 'immutable']
'string is immutable'.rsplit(' ',1)
['string is', 'immutable']
p='''
python
programming
language'''
p
'\npython\nprogramming\nlanguage'
>>> s.splitlines()
['string is immutable']
>>> p.splitlines()
['', 'python', 'programming', 'language']
>>> ''.join(['', 'python', 'programming', 'language'])
'pythonprogramminglanguage'
>>> '-'.join(['', 'python', 'programming', 'language'])
'-python-programming-language'
>>> ' '.join(['', 'python', 'programming', 'language'])
' python programming language'
>>> 'python.py.partition('.')
SyntaxError: unterminated string literal (detected at line 1)
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> ('python', '.', 'py')
('python', '.', 'py')
>>> s='java',',','python','c,c++'
>>> s
('java', ',', 'python', 'c,c++')
>>> c= '                  hello    world               '
>>> c
'                  hello    world               '
>>> c.strip()
'hello    world'
>>> c.lstrip()
'hello    world               '
>>> c.rstrip()
'                  hello    world'
>>> text=>>>'Hello नमस्ते你好 café 🙂'
SyntaxError: invalid syntax
>>> text='Hello नमस्ते你好 café 🙂'
>>> text
'Hello नमस्ते你好 café 🙂'
>>> text.encode
<built-in method encode of str object at 0x0000023D6FD12790>
>>> >>>'Hello नमस्ते你好 café 🙂'
SyntaxError: invalid syntax
>>> <built-in method encode of str object at 0x0000023D6FD12790>.decode()
SyntaxError: invalid syntax
>>> built-in method encode of str object at 0x0000023D6FD12790.decode()
SyntaxError: invalid syntax
>>> text="hello 🙂"
>>> text.encode()
b'hello \xf0\x9f\x99\x82'
>>> b'hello \xf0\x9f\x99\x82'.decode()
'hello 🙂'
