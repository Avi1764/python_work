
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
n= int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if(i==0 or j+i==n-1 or i==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n= int(input("enyter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or (j+i==n-1 and j<=m) or (i==j and i>=m)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

