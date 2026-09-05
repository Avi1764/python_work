'''

def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)

'''


'''
def display(n):
    if n>10:
        return
    display(n+1)
    print(n,end=' ')
display(1)
'''
'''
def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(18))

'''


'''
def displaypro(n):
    if n==1:
        return 1
    return n*displaypro(n-1)
print(displaypro(5))

'''

'''
s='python programming'
def display(n):
    if n==len(s):
        return
    print(s[n],end=' ')
    display(n+1)
display(0)

'''


'''
s='python programming'
def display(n):
    if n==len(s):
        return
    display(n+1)
    print(s[n],end=' ')
display(0)

'''
'''
s='python'
def display(n):
    if n==len(s):
        return
    print(s[:n+1])
    display(n+1)
display(0)
'''

'''
s='python programming'
def display(n):
    if n==len(s):
        return
    print(s[:n+1])
    display(n+1)
display(0)

'''

'''
def display(ind,w):
    if ind > len(s) - w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)
s='python programming'
display(0,10)
'''


'''
def display(n):
    if n<=0:
        return
    display(n//10)
    print(n%10,end='')
display(987654)

'''


a=0
b=1
n=10
for i in range(n-1):
    a,b=b,a+b
    print(b,end=' ')

