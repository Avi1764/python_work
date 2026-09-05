Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=""
s
''
s="avinash"
s
'avinash'
'avinash' + 'paleti'
'avinashpaleti'
'avinash'*10
'avinashavinashavinashavinashavinashavinashavinashavinashavinashavinash'
>>> '_*_'25
SyntaxError: invalid syntax
>>> '_*_'*25
'_*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*_'
>>> '*'*9
'*********'
>>> s='avinash'
>>> s[4]
'a'
>>> s[-1]
'h'
>>> s-1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> s[0]
'a'
>>> names='avinash anil ganesh chintu'
>>> names[0]
'a'
>>> names[0:7]
'avinash'
>>> names[8:13]
'anil '
>>> names[14:20]
'anesh '
>>> names[-1:-8:-1]
'utnihc '
>>> names[-1:-6:-1]
'utnih'
>>> names[-1:-7:-1]
'utnihc'
>>> names[::]
'avinash anil ganesh chintu'
>>> names[::-1]
'utnihc hsenag lina hsaniva'
>>> names
'avinash anil ganesh chintu'
>>> 'avinash'in names
True
>>> 'anil'not in names
False
>>> 'ganesh'in names
True
