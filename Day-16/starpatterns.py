'''

n=int(input("eneter the number: "))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

'''

'''

n=int(input("enter the number: "))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

    '''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or j==n-1 or i==n//2 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or j==n-1 or i==n-1 or i==n//2 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or j==n-1 or i==n-1 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or i==n//2 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=int(input("enter the numbers: "))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n//2 ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n=int(input("enter the numbers: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or (i==n-1 and j<=mid) or (j==mid and i>=mid) or (i==mid and j>=mid) or (j==n-1 and i>=mid)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

'''
n=int(input("enter the numbers: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 or (i==m and j<=m) or (i+j==n-1 and j>=m)or (i==j and j>=m)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
'''


n=int(input("enter the numbers: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1 or (i==n//1 and i>=m) or (i+j==n-1 and i<=m) or (i==j and i<=m)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''

'''
n= int(input("enyter the number: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n//2 or (j==n-1 and i<=n//2) or (i==j and i>=n//2)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

    '''

'''
n= int(input("enyter the number: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j+i==n-1 or i==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''



