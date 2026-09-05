'''

def display(n):
    n=n+10
    print('Inside:',n)
n=10
display(n)
print('outside:',n)

'''


'''
def display(n):
    print('Inside:',n)
n=10
display(n)
print('outside:',n)

'''

'''
def display():
    n=10
    print('Inside:',n)
display()
print('outside:')

'''

'''


def display():
    global n
    n=n+10
    print('Inside:',n)
n=10
display()
print('outside:')

'''

'''
def display(n):
    n='PFS'
    print("updated course:",n)
n='JFS'
display(n)
print("final course:",n)
'''


'''
def display():
    global n
    n='PFS'
    print("updated course:",n)
n='JFS'
display()
print("final course:",n)

'''

'''
def display():
    n='JFS'
    def update():
        nonlocal n
        n='PFS'
        print("updated course:",n)
    update()
    print("final course:",n)
display()

'''

l=[1,2,3,4,5]
max=20
sum=10
print(sum)

        
