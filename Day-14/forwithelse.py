'''

for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print("end of the loop")
'''



'''
pin = 1234
for _ in range(5):
    epin = int(input("enter the pin: "))
    if pin == epin:
        print("Unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")
'''


'''
n = int(input("Enter the number: "))
print("Factors",end=' ')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
'''


'''
n = int(input("Enter the number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==0:
    print("prime number")
else:
    print("not a prime number")

'''


'''
n = int(input("Enter the number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")
'''






