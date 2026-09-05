'''

os.getcwd()  Returns the current working directory
os.chdir(path)  Changes the current working directory
os.listdir(path)  Returns a list of files and folders in a directory
os.mkdir(name)  Creates a new directory
os.remove(file)  Deletes a specified file
os.rmdir(dir)  Removes an empty directory
os.path.exists(path)  Checks if a path exists

'''
'''
import os
#os.mkdir("demo")
#os.rmdir('demo')
#print(os.getcwd())

'''

'''
import sys
#print(sys.path)
#print(sys.version)
print("startS")
sys.exit()
print("end")

'''


'''
import platform
print(platform.system())
print(platform.release())
print(platform.processor())

'''

'''
import math
print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(2,3))

print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.99999999))

print(math.floor(12.00001))
print(math.floor(12.3))
print(math.floor(12.6))
print(math.ceil(12.99999999))

print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))

'''

'''

import random
random.seed(10)

print(random.randint(1,10))
print(random.randint(10000,99999))
print(random.random())
print(random.uniform(1,6))

l=['R','P','S']
print(random.choice(l))
print(random.choices(l,k=2))
random.shuffle(l)
print(l)

'''

'''
from collections import Counter,defaultdict
s='python programming'
m='this is that that is this'.split()
l=[1,1,1,1,2,3,4,56,6,6,63,3,8,8,9,6,8,8,]

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
#print(Counter(s))
#print(Counter(l))
#print(Counter(m))

'''


'''
from collections import Counter,defaultdict,deque

l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()

print(l)


'''

'''
from collections import Counter,defaultdict,deque

l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()

print(l)

'''

from itertools import combinations,permutations

res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print([''.join(i)for i in res1])
print([''.join(i)for i in res2])
