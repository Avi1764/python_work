#int float str list tuple set dict bool
#int float str tuple bool-(immutable items)
#list set dict----we are passing object refernce(mutable items)

'''int----
def display(n):
    n+=10
    print("inside:",n)
n=10
display(n)
print("outside:",n)

'''

'''float----
def display(n):
    n+=10.9
    print("inside:",n)
n=10.4
display(n)
print("outside:",n)

'''

'''dict---
def display(n):
    n[5]=6
    print("inside:",n)
n={1:2,2:4}
display(n)
print("outside:",n)

'''
'''str----
def display(n):
     n += ' Krishna'
     print("Inside: ",n)

n = 'Hare'
display(n)
print("Outside: ",n)
'''

'''tuple----
def display(n):
     n += (1, 2, 3, 4)
     print("Inside: ",n)

n = (1, 2, 3)
display(n)
print("Outside: ",n)
'''


'''bool----
def display(n):
     n = False
     print("Inside: ",n)

n = True
display(n)
print("Outside: ",n)
'''
'''list----
def display(n):
     n.append(10)
     print("Inside: ",n)

n = [1, 2, 3, 4, 5]
display(n)
print("Outside: ",n)

'''

'''set----
def display(n):
     n.add(10)
     print("Inside: ",n)

n = {1, 2, 3}
display(n)
print("Outside: ",n)
'''
