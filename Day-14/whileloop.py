'''

i=1
while i<=10:
    print(i)
    i+=1

'''

'''
i=10
while i>=0:
    print(i)
    i-=1

'''


'''
i=2
while i<=100:
    print(i,end=' ')
    i+=2

'''


'''

....reverse of string...

s="Avinash"
i = len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
'''


'''
...removing zeros....

l=[1,0,0,0,2,3,4,5,67,0,9,78,45,0,0,1,0]
while 0 in l:
    l.remove(0)
print(l)

'''

'''
d={}
total_bill=0
while True:
    name=input("Enter the name: ")
    if name == 'exit':
        break
    price=eval(input("Enter the price: "))
    total_bill+=price
    d[name]=[price]
print(d)
print("total bill:",total_bill)

'''



i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i,end=' ')
else:
    print("end of the loop")