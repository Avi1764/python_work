Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {'name':'avinash','batch':63,'course':,'PFS'}
SyntaxError: expression expected after dictionary key and ':'
data = {'name':'avinash','batch':63,'course':'PFS'}
data['name']
'avinash'
data['batch']
63
data['course']
'PFS'
63 in data
False
data.get('age''key is not present')
data['age']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']
63
data
{'name': 'avinash', 'batch': 63, 'course': 'PFS'}
data['skills']=['python','mysql','flask']
data
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
data
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phon':8106686988,'email,:avinashpaleti@gmail.com})
             
SyntaxError: unterminated string literal (detected at line 1)
data.update({'phon':8106686988,'email':avinashpaleti@gmail.com})
             
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data.update({'phon':8106686988,'email':avinashpaleti@gmail.com})
NameError: name 'avinashpaleti' is not defined
data.update({'phno':8106686988,'email':'avinashpaleti@gmail.com'})
             
data
             
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com'}
data.pop('age')
             
21
data.pop('phno')
             
8106686988
data
             
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'avinashpaleti@gmail.com'}
data.popitem()
             
('email', 'avinashpaleti@gmail.com')
data
             
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.popitem()
             
('skills', ['python', 'mysql', 'flask'])
data
             
{'name': 'avinash', 'batch': 63, 'course': 'PFS'}
data.clear()
             
data
             
{}
data={'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com'}
             
data
             
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com'}
data.keys()
             
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
data.values()
             
dict_values(['avinash', 63, 'PFS', ['python', 'mysql', 'flask'], 21, 8106686988, 'avinashpaleti@gmail.com'])
data.items()
             
dict_items([('name', 'avinash'), ('batch', 63), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('age', 21), ('phno', 8106686988), ('email', 'avinashpaleti@gmail.com')])
sorted(data)
             
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
             
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
max(data)
             
'skills'
min(dat)
             
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    min(dat)
NameError: name 'dat' is not defined. Did you mean: 'data'?
min(data)
             
'age'
data
             
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com'}
>>> data.get('age')
...              
21
>>> data.pop('age')
...              
21
>>> data
...              
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com'}
>>> data.setdefault('age',0)
...              
0
>>> data
...              
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com', 'age': 0}
>>> len(data)
...              
7
>>> all(data)
...              
True
>>> any(data)
...              
True
>>> data
...              
{'name': 'avinash', 'batch': 63, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 8106686988, 'email': 'avinashpaleti@gmail.com', 'age': 0}
>>> c=a.copy()
...              
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c=a.copy()
NameError: name 'a' is not defined
>>> c= a.copy()
...              
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c= a.copy()
NameError: name 'a' is not defined
>>> d=data.fromkeys(["a","b"],0)
...              
>>> d
...              
{'a': 0, 'b': 0}
